import ROOT as R
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-s","--sample", help="Sample", type=str, default="*")
parser.add_argument("-n","--nuisances", help="Nuisances", type=str, nargs="+")
parser.add_argument("-vars","--vars", help="Vars", type=str, nargs="+")
args = parser.parse_args()


f = R.TFile(args.input, "UPDATE")

# samples = ['VBS','top','DATA','Fake','Wjets_HT','VVV','VV','VgS','Vg','DY','VBF-V','ggWW']
# samples = []
# for ir in range(1,22):
#     samples.append("Wjets_res_"+str(ir))
# for ir in range(1,8):
#     samples.append("Wjets_boost_"+str(ir))
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]
VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
#samples = ['VBF-V_dipole']
VBS_aQGC_samples = ["quad_cT0","sm_lin_quad_cT0",'sm']
samples = VV_samples + VBS_samples + VBS_aQGC_samples #args.sample
    #f.ls()
for k in f.GetListOfKeys():
    #print(k)
    R.gDirectory.Cd(k.GetName())
    for z in R.gDirectory.GetListOfKeys():
        if args.vars and z.GetName() not in args.vars:
            continue
        #print(z)
        print ">>> ", k.GetName(), z.GetName()
        R.gDirectory.Cd(z.GetName())

        for nuisance_name in args.nuisances:
            #Delete boh up and down
            for sample in samples:
                print (sample)
                R.gDirectory.Delete("histo_" + sample + "_"+nuisance_name+"*;*")
                   
        R.gDirectory.Cd("../")

    R.gDirectory.Cd("../")

f.Write()
f.Close()
