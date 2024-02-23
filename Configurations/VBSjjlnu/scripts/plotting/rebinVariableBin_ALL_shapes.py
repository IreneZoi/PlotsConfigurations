import ROOT as R
import sys
import argparse
import array

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-s","--sample", help="Sample", type=str, default="*")
parser.add_argument("-n","--nuisances", help="Nuisances", type=str, nargs="+")
parser.add_argument("-vars","--vars", help="Vars", type=str, nargs="+")
parser.add_argument("-l","--label", help="identify the rebinning", type=str, default="GiacomoTest2")
#parser.add_argument("-nbins",help="Number of bins for rebinning", type=int)
args = parser.parse_args()

#nbins = args.nbins
f = R.TFile(args.input, "READ")
fout = R.TFile((args.input).replace(".root","_"+args.label+".root"), "RECREATE")

# samples = ['VBS','top','DATA','Fake','Wjets_HT','VVV','VV','VgS','Vg','DY','VBF-V','ggWW']
# samples = []
# for ir in range(1,22):
#     samples.append("Wjets_res_"+str(ir))
# for ir in range(1,8):
#     samples.append("Wjets_boost_"+str(ir))
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]
VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VBS_signals = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj"]
#samples = ['VBF-V_dipole']
VBS_aQGC_samples = ["quad_cT0","sm_lin_quad_cT0"] #,'sm']
#samples = VV_samples + VBS_samples + VBS_aQGC_samples #args.sample
samples = VBS_aQGC_samples
    #f.ls()
f.cd()
for k in f.GetListOfKeys():
    #if "sig" not in k.GetName(): continue
    print(k)
    fout.cd()
    R.gDirectory.mkdir(str(k.GetName()))
    f.cd()
    R.gDirectory.Cd(k.GetName())
    for z in R.gDirectory.GetListOfKeys():

        if args.vars and z.GetName() not in args.vars:
            continue
        #print(z)
        print ">>> ", k.GetName(), z.GetName()
        fout.cd()
        R.gDirectory.mkdir(str(k.GetName()+"/"+z.GetName())+"_rebinned_"+args.label)
        f.cd()
        R.gDirectory.Cd(k.GetName()+"/"+z.GetName())
        # R.gDirectory.Cd(z.GetName())
        

        #for nuisance_name in args.nuisances:
        #Delete boh up and down
        for histname in R.gDirectory.GetListOfKeys():
            print ("histname ",histname.GetName())
            # if  "histo_Wjets_res_4_CMS_btag_cferr1Down" not in histname.GetName(): continue 
                
            hist=f.Get(str(k.GetName())+"/"+str(z.GetName())+"/"+str(histname.GetName()))
            hist.SetDirectory(0)
            width = hist.GetBinWidth(1)
            print("hist ",hist, " bin width ",width )
            nbins=[]
            binedge = 0
            nbins.append(binedge)
            multiply = [2,2,2,2,2,2,4,6,36]
            for i in range(0,len(multiply)):
                binedge = binedge + width*multiply[i]
                nbins.append(binedge)
            print( " nbins ", nbins)
            xbins = array.array('d',nbins)
            # if hist.GetNbinsX()%nbins != 0:
            #     print("Cannot go form {} bins to {} bins!!!!\n".format(hist.GetNbinsX(), nbins))
            #     sys.exit()
            print("Rebinning variable {} from {} bins to {} bins\n".format(args.vars, hist.GetNbinsX(), nbins))
            
            #from original script but I think it is not working as expected
            # theCall=[False]*nbins

            # # divide the range in n intervals
            # theInterval=[False]*nbins
            # for i in range(nbins):
            #     theInterval[i] = (i+1.)/nbins
            # print(theInterval)
            # theInterval[nbins-1] = 1.001; #why?
            # s=0
            # toKeep=[0]*nbins
            # #for each bin in the original distribution, sum until one interval is reached
            # print (" hist.GetSumOfWeights() ", hist.GetSumOfWeights())
            # for b in range(hist.GetNbinsX()):
            #     # print(" b ",b," hist.GetBinContent(b) ",hist.GetBinContent(b))
            #     s=s + hist.GetBinContent(b)/hist.GetSumOfWeights()
            #     for i in range(nbins):
            #         if ((theCall[i] == False ) & (s > theInterval[i])): #check if the interval edge has already bin reached and if we are over it
            #             binHighedge= hist.GetBinLowEdge(b)+2*(hist.GetBinCenter(b)-hist.GetBinLowEdge(b)) #compute bin high edge
            #             print(b, binHighedge,s,i)
            #             theCall[i]=True #memory that the edge has already been reached
            #             toKeep[i]=binHighedge #record edge value. 
            #             break

            # print(" hist.GetBinCenter(hist.GetNbinsX()) ",hist.GetBinCenter(hist.GetNbinsX()), " hist.GetBinLowEdge(hist.GetNbinsX()) ",hist.GetBinLowEdge(hist.GetNbinsX()))
            # toKeep[-1]=hist.GetBinLowEdge(hist.GetNbinsX())+2*(hist.GetBinCenter(hist.GetNbinsX())-hist.GetBinLowEdge(hist.GetNbinsX()))
            # toKeep=[0]+toKeep
            # print("toKeep: ", toKeep)
            # print("New binning = ", toKeep)
            # newbins=array.array('d',toKeep)
            # print("newbins ",newbins)
            # print ("rebinning")
            # print("nbins ",nbins," newbins ",newbins)
            # R.gDirectory.Cd("../")
            # R.gDirectory.mkdir(str(z.GetName())+"_rebinned_"+args.label)
            # R.gDirectory.Cd(str(z.GetName()))
            #rebinned_hist.SetName()
            fout.cd()
            R.gDirectory.Cd(str(k.GetName()+"/"+z.GetName())+"_rebinned_"+args.label)

            savehistname = histname.GetName()
            hist.SetName(savehistname+"_old")
            print( " hist.GetName() ",hist.GetName())
            # rebinned_hist = hist.Clone()
            print( "after clone rebinned_hist.GetName() ",hist.GetName())
            # myhistname = histname.GetName()
            # rebinned_hist.SetName("hnew")
            # hist.SetDirectory(0)
                        
            
            rebinned_hist = hist.Rebin(len(multiply),savehistname,xbins)
            print( "after rebin rebinned_hist.GetName() ",rebinned_hist.GetName(), " savehistname ", savehistname)
            # R.gDirectory.Delete(savehistname)
            # rebinned_hist.SetName(savehistname)
            del hist
            
            R.gDirectory.pwd()
            # rebinned_hist.Write()
            # print("wrote rebinned hist ")
            f.cd()
            R.gDirectory.Cd(k.GetName()+"/"+z.GetName())
            #R.gDirectory.Delete("histo_" + sample + "_*;*")
                   
        R.gDirectory.Cd("../")

    R.gDirectory.Cd("../")

fout.Write()
f.Close()
fout.Close()
