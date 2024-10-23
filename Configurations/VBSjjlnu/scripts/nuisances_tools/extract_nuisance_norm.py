import argparse
import json
'''
This script saves in a TFile the effect of the selected nuisance for the 
given samples and variables. 

The effect is saved as the ratio of variationn/nominal.
'''
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("-o","--output", help="Output file", type=str)
# parser.add_argument("-s","--samples", help="Samples", type=str, nargs="+")
parser.add_argument("-c","--cut", help="Cut", type=str)
parser.add_argument("-n","--nuisances", help="Nuisances", type=str, nargs="+")
args = parser.parse_args()

import ROOT as R 
R.gROOT.SetBatch(True)
R.TH1.SetDefaultSumw2()


iF = R.TFile.Open(args.input, "READ")
output = {}

cut = args.cut
print "Cut: ", cut
theOperators = ["cT0", "cT2", "cT1", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cS2", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
full_operators_name = []
for op in theOperators:
     full_operators_name.append("quad_"+op)
     full_operators_name.append("sm_lin_quad_"+op)
full_operators_name.append("sm")

for s in full_operators_name:
    output[s] = {}
    print ">> Sample: ", s 
    h_nom = iF.Get("{}/events/histo_{}".format(cut, s ))

    for n in args.nuisances:
        try:
            h_up = iF.Get("{}/events/histo_{}_{}Up".format(cut, s, n))
            h_do = iF.Get("{}/events/histo_{}_{}Down".format(cut, s, n))
            corr_up = h_nom.Integral()/h_up.Integral()
            corr_do = h_nom.Integral()/h_do.Integral()
            print s, " | ", n, " | nom: ",h_nom.Integral(), " | up: ", h_up.Integral(), " (", corr_up , \
                                        ") | do: ", h_do.Integral(), " (" , corr_do, ") |"
            output[s][n] = (corr_up, corr_do)
        except:
            print " nuisance ",n," not found!"
            continue
         
print "------------------------------"

with open(args.output,'w') as out:
    out.write(json.dumps(output, indent=2))
