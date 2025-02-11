import ROOT as R
import sys
import argparse
import array

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
# parser.add_argument("-s","--sample", help="Sample", type=str, default="*")
parser.add_argument("-n","--nuisances", help="Nuisances", type=str, nargs="+")
parser.add_argument("-vars","--vars", help="Vars", type=str, nargs="+")
parser.add_argument("-l","--label", help="identify the rebinning", type=str, default="SplitLastTwo")
#parser.add_argument("-nbins",help="Number of bins for rebinning", type=int)
args = parser.parse_args()

#nbins = args.nbins
f = R.TFile(args.input, "UPDATE")
# fout = R.TFile((args.input).replace(".root","_"+args.label+".root"), "RECREATE")


# # create the directory structure in the output file
# f.cd()
# for k in f.GetListOfKeys():
#     #if "sig" not in k.GetName(): continue
#     print(k)
#     fout.cd()
#     R.gDirectory.mkdir(str(k.GetName()))
#     f.cd()
#     R.gDirectory.Cd(k.GetName())
#     for z in R.gDirectory.GetListOfKeys():

#         if args.vars and z.GetName() not in args.vars:
#             continue
#         #print(z)
#         print ">>> ", k.GetName(), z.GetName()
#         fout.cd()
#         R.gDirectory.mkdir(str(k.GetName()+"/"+z.GetName())+"_rebinned_"+args.label)
#         f.cd()
#         R.gDirectory.Cd(k.GetName()+"/"+z.GetName())
#         # R.gDirectory.Cd(z.GetName())
                   
#         R.gDirectory.Cd("../")

#     R.gDirectory.Cd("../")





# rebin
f.cd()
for k in f.GetListOfKeys():
    #if "sig" not in k.GetName(): continue
    print(" first key ",k)
    # fout.cd()
    # R.gDirectory.mkdir(str(k.GetName()))
    # f.cd()
    R.gDirectory.Cd(k.GetName())
    for z in R.gDirectory.GetListOfKeys():

        if args.vars and z.GetName() not in args.vars:
            continue
        #print(z)
        print ">>> ", k.GetName(), z.GetName()
        # fout.cd()
        print(" in directory ",R.gDirectory.pwd())
        # R.gDirectory.mkdir(str(k.GetName()+"/"+z.GetName())+"_rebinned_"+args.label)
        R.gDirectory.mkdir(str(z.GetName())+"_rebinned_"+args.label)
        R.gDirectory.Cd(str(z.GetName())+"_rebinned_"+args.label)
        print(" am I in the new directory? ",R.gDirectory.pwd())
        # f.cd()
        R.gDirector
        y.Cd(k.GetName()+"/"+z.GetName())
        R.gDirectory.Cd("../"+z.GetName())
        #print(" am I in the directory with the hist to be rebinned? ",R.gDirectory.pwd())

        for histname in R.gDirectory.GetListOfKeys():
            print("directory: ",str(k.GetName())+"/"+str(z.GetName()))
            print ("histname ",histname.GetName())
                
            hist=f.Get(str(k.GetName())+"/"+str(z.GetName())+"/"+str(histname.GetName()))
            hist.SetDirectory(0)
            width = hist.GetBinWidth(1)
            print("hist ",hist, " bin width ",width )
            nbins=[]
            binedge = 0
            nbins.append(binedge)
            multiply = [3,1,1,1,1,1,1,1,1,1,3,3,3,3,3,60] # need to understand the last bin
            for i in range(0,len(multiply)):
                # print ("bin ", i ," binedge low ",binedge, "binedge high ",binedge + width*multiply[i])
                if (i < len(multiply) - 1 ):
                    # print ("len bin ", i ," binedge low ",binedge, "binedge high ",binedge + width*multiply[i])
                    binedge = binedge + width*multiply[i]
                else:
                    # print ("bin ", i ," binedge low ",binedge, "binedge high ",hist.GetXaxis().GetXmax())
                    binedge = hist.GetXaxis().GetXmax()
                    
                nbins.append(binedge)
                
                    
            print( " nbins ", nbins)
            xbins = array.array('d',nbins)
            # if hist.GetNbinsX()%nbins != 0:
            #     print("Cannot go form {} bins to {} bins!!!!\n".format(hist.GetNbinsX(), nbins))
            #     sys.exit()
            print("Rebinning variable {} from {} bins to {} bins\n".format(args.vars, hist.GetNbinsX(), nbins))
            

            # fout.cd()
            R.gDirectory.Cd("../"+str(z.GetName())+"_rebinned_"+args.label)

            # savehistname = histname.GetName()
            # hist.SetName(savehistname+"_old")
            # print( " hist.GetName() ",hist.GetName())
            # # rebinned_hist = hist.Clone()
            # print( "after clone rebinned_hist.GetName() ",hist.GetName())
            # myhistname = histname.GetName()
            # rebinned_hist.SetName("hnew")
            # hist.SetDirectory(0)
                        
            
            rebinned_hist = hist.Rebin(len(multiply),histname.GetName(),xbins)
            print( "after rebin rebinned_hist.GetName() ",rebinned_hist.GetName()) #, " savehistname ", savehistname)
            rebinned_hist.Write()
            # R.gDirectory.Delete(savehistname)
            # rebinned_hist.SetName(savehistname)
            del hist
            print (" pwd dir ")
            #R.gDirectory.pwd()
            # rebinned_hist.Write()
            # print("wrote rebinned hist ")
            # f.cd()
            # R.gDirectory.Cd(k.GetName()+"/"+z.GetName())
            #R.gDirectory.Delete("histo_" + sample + "_*;*")
                   
        R.gDirectory.Cd("../")

    R.gDirectory.Cd("../")

# fout.Write()
f.Close()
# fout.Close()
