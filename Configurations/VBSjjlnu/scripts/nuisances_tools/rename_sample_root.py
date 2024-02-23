from __future__ import print_function
import ROOT as R
import sys
import argparse

'''
This script can be used to rename a systematic shape including the name
of the samples or a custom name. 

The original shape is not removed
'''

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("--rename", help="Rename",type=str)
parser.add_argument("--sample","-s", help="Sample", type=str)
parser.add_argument("-ev","--exclude-vars", help="Exclude vars", type=str, nargs="+")
parser.add_argument("-ec","--exclude-cuts", help="Exclude cuts", type=str, nargs="+")
args = parser.parse_args()


if args.sample and len(args.sample) > 0:
    sample = args.sample
else:
    print("Please provide a sample")
    exit(1)


f = R.TFile(args.input, "UPDATE")
rename_sample = args.rename

for k in f.GetListOfKeys():
    if args.exclude_cuts and k.GetName() in args.exclude_cuts: continue
    R.gDirectory.Cd(k.GetName())
    for z in R.gDirectory.GetListOfKeys():
        if args.exclude_vars and z.GetName() in args.exclude_vars: continue
        R.gDirectory.Cd(z.GetName())
        print(k.GetName(), z.GetName())
        for l in R.gDirectory.GetListOfKeys():
            histoname = l.GetName()
            print(histoname)
            if sample in histoname:
                histoname = histoname.replace(sample,rename_sample) 
                print(" replace with ",histoname)
                obj = R.gDirectory.Get(l.GetName())
                obj.SetName(histoname)
                obj.Write()
                # obj.SetDirectory(0)
        R.gDirectory.Cd("../")

    R.gDirectory.Cd("../")


print (" end loops ")
# Already writter
print ( " going to write file")
f.Write()
print ( " going to close file")
f.Close()
print ("file close ")
