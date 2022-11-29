import os
import ROOT as R
import shutil
from matplotlib import pyplot as plt
import pandas as pd
import array

#Run with python -m rebinning, should be place in cofniguration folder
FILE ='/eos/home-a/ahakimi/www/ZV_analysis/rootFile_03Nov22_2018_testbinning/plots_VBS_ZV_03Nov22_2018_testbinning.root' #mkshape root output to rebin
CUT="Resolved_SR_bVeto" # cut to rebin
VARIABLE="DNNoutput_pruned_bVeto_fine_binning" # variable to rebin
SAMPLE="VBS_ZV" #Sample taht should have equal yields in new bins (usually signal)
NEWFILE='rebin.root' # name of the rebinned file
PLOT_ORIGINAL=False #if you want to plot the original histogram (might be buggy)
PLOT_REBIN=False # if you want to plot the rebinned histo (might be buggy)
MAX=20 # max number of bins to test
OUTPUT='out'#no extansion
DATACARDDIR='datacard_rebin' #name of repertory for saving rebinned datacards
CONFIGFILE='configuration_test.py'# config file used to produce FILE

def rebin(FILE, CUT, VARIABLE, SAMPLE, NEWFILE, nbins, PLOT_ORIGINAL, PLOT_REBIN):
    #rebin FILE and save content in NEWFILE
    print("Making a copy of the original root file\n")
    shutil.copyfile(FILE, NEWFILE)
    f= R.TFile.Open(NEWFILE, "UPDATE")
    tree=f.Get(CUT+'/'+VARIABLE)
    hist_names=[]
    for k in tree.GetListOfKeys(): # get all SAMPLE related histos
        if SAMPLE in k.GetName():
            hist_names.append(k.GetName())
    hist=tree.Get("histo_"+SAMPLE)
    print("Rebinning variable {} from {} bins to {} bins\n".format(VARIABLE, hist.GetNbinsX(), nbins))
    if PLOT_ORIGINAL:
        bins=[]
        centers=[]
        left=[]
        width=[]
        for b in range(hist.GetNbinsX()):
            bins.append(hist.GetBinContent(b))
            centers.append(hist.GetBinCenter(b))
            left.append(hist.GetBinLowEdge(b))
            width.append(hist.GetBinWidth(b))

        plt.bar(x=centers, height=bins,width=width)
    theCall=[False]*nbins

    # divide the range in n intervals
    theInterval=[False]*nbins
    for i in range(nbins):
        theInterval[i] = (i+1.)/nbins;
    #print(theInterval)
    theInterval[nbins-1] = 1.001; #why?
    s=0
    toKeep=[0]*nbins
    #for each bin in the original distribution, sum until one interval is reached
    for b in range(hist.GetNbinsX()):
        s=s + hist.GetBinContent(b)/hist.GetSumOfWeights()
        for i in range(nbins):
            if ((theCall[i] == False ) & (s > theInterval[i])): #check if the interval edge has already bin reached and if we are over it
                binHighedge= hist.GetBinLowEdge(b)+2*(hist.GetBinCenter(b)-hist.GetBinLowEdge(b)) #compute bin high edge
                #print(b, binHighedge,s,i)
                theCall[i]=True #memory that the edge has already been reached
                toKeep[i]=binHighedge #record edge value. 
                break


    toKeep[-1]=1
    toKeep=[0]+toKeep
    #print("toKeep: ", toKeep)
    print("New binning = ", toKeep)
    newbins=array.array('d',toKeep)
    if PLOT_REBIN:
        test=hist.Rebin(nbins, "new2",newbins)
        binsh=[]
        centers=[]
        width=[]
        left=[]

        for b in range(test.GetNbinsX()):
            binsh.append(test.GetBinContent(b+1))
            centers.append(test.GetBinCenter(b+1))
            width.append(test.GetBinWidth(b+1))
            left.append(test.GetBinLowEdge(b+1))
        plt.figure()
        plt.bar(x=centers, height=binsh, width=width, edgecolor='red')

    # rebin all nuisances

    for h in hist_names:
        thisHist=tree.Get(h)
        rebinnedHist=thisHist.Rebin(nbins, h,newbins)
    return toKeep


#write optimization loop

#create the output file
if os.path.isfile(OUTPUT):
    print('ERROR, output file {} already exists'.format(OUTPUT))
else:
    results=pd.DataFrame(columns=['nbins', 'bins', 'sig'])
    for n in range(1,MAX):
        bins=rebin(FILE, CUT, VARIABLE, SAMPLE, NEWFILE, n, False, False)
        #run makedatacards
        os.system("mkDatacards.py --pycfg={} --inputFile={} --outputDirDatacard={}".format(CONFIGFILE,FILE, DATACARDDIR)) #makedatacards
        #this writes to OUTPUT/CUT/VARIABLE/datacard.txt
        #extract significance only from SR, should switch to simultaneous fit?
        os.system('combine -M Significance {}/{}/{}/datacard.txt -t -1 --expectSignal=1 >significance.txt'.format(DATACARDDIR, CUT, VARIABLE))
        #read the output
        sigfile= 'significance.txt'
        if not os.path.isfile('significance.txt'):
            print("Could not find significance.txt\n")
            break
        with open(sigfile, 'r') as f:
	    read = False
            for line in f:
                if "Significance:" in line:
                    sig=float(line[14:])
		    read=True
	if read == False:
		sig='error'
        print("Significance= ",sig)
        #write the output to txt
        
        results.loc[len(results.index)]=[n,bins,sig]
        with open(OUTPUT+'.txt', 'a') as f:
            f.write("Binning with {} bins with edges {} yields a significance of {}\n".format(n,bins, sig))
    #find optimum
    results.to_csv(OUTPUT + '.csv')
    bestrow=results.iloc[results['sig'].idxmax()]
    with open(OUTPUT+'.txt', 'a') as f:
        f.write("Best signficance of {} obtained with {} bins : {} ".format(bestrow['sig'], bestrow['nbins'], bestrow['bins']))
