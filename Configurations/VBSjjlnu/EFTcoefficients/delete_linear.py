# -*- coding: utf-8 -*-
import ROOT as R
import sys
import argparse
import shutil

#         RUN IT IN SINGULARITY, AFTER cmsenv, with Python2
#   e.g.: python2 EFTcoefficients/delete_linear.py -i=/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_Aug2024_AllOperators_withNuis/plots_fit_v4.5_2016_split_aQGC_Aug2024_AllOperators_withNuis_withBKG_noStat.root -vars=Mww_binzv+events+fit_bin_boost

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Input file", type=str, required=True)
    parser.add_argument("-s", "--sample", help="Sample", type=str, default="*")
    parser.add_argument("-vars", "--vars", help="Vars", type=str, required=True)
    args = parser.parse_args()

    vars_to_process = args.vars.split("+")

    # Definisco il nome del file output aggiungendo '_noStat' al nome del file originale
    output_file = args.input.replace('.root', '_noLin.root')

    # Clonare il file ROOT
    shutil.copyfile(args.input, output_file)

    # Aprire il file clonato in modalità UPDATE per le modifiche
    f = R.TFile(output_file, "UPDATE")

    all_operators = ['cT0', 'cT1', 'cT2', 'cT3', 'cT4', 'cT5', 'cT6', 'cT7', 
                    'cS0', 'cS1', 'cS2', 'cM0', 'cM1', 'cM2', 'cM3', 'cM4', 'cM5', 'cM7']
                 
    samples = ['sm_lin_quad_' + op for op in all_operators]

    for k in f.GetListOfKeys():
        print(k)
        R.gDirectory.Cd(k.GetName())
        for z in R.gDirectory.GetListOfKeys():
            if z.GetName() not in vars_to_process:
                continue
            print(z)
            print(">>> ", k.GetName(), z.GetName())
            R.gDirectory.Cd(z.GetName())

            for sample in samples:
                hist_name = "histo_{}".format(sample)
                hist = R.gDirectory.Get(hist_name)
                if hist:
                    print("Processing {}".format(hist_name))
                    for bin in range(1, hist.GetNbinsX() + 1):
                        hist.SetBinError(bin, 0)
                        hist.SetBinContent(bin, 0)
                    hist.Write("", R.TObject.kOverwrite)

            R.gDirectory.Cd("../")

        R.gDirectory.Cd("../")

    f.Write()
    f.Close()

if __name__ == "__main__":
    main()
