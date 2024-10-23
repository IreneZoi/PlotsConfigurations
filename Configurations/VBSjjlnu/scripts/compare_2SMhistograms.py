import ROOT
import math
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", help="operator", type=str, )
args = parser.parse_args()



ROOT.gROOT.SetBatch(True)  # Enable batch mode
ROOT.objs = []

Hin_up = dict()
Hin_down = dict()
Rat_up = dict()
Rat_down = dict()

year=2018
file_Hin_up = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_oldbasis_allOperators_smDipole/plots_fit_v4.5_2018_split_aQGC_oldbasis_allOperators_smDipole_ALL_INPUTS.root' #IRENEchanged
file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_Aug2024_allOperators/plots_fit_v4.5_2018_split_aQGC_Aug2024_allOperators.root' #IRENEchanged
# file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_eboliv2_official_allOperators_smDipole/plots_fit_v4.5_2018_split_aQGC_eboliv2_official_ALL_INPUTS.root' #IRENEchanged

# year=2017
# # # file_Hin = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_oldbasis_allOperators_smDipole/plots_fit_v4.5_2017_split_aQGC_oldbasis_allOperators_smDipole.root' #IRENEchanged
# file_Hin_up = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_oldbasis_allOperators_smDipole/plots_fit_v4.5_2017_split_aQGC_oldbasis_allOperators_smDipole.root' #IRENEchanged
# # file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_Aug2024_allOperators/plots_fit_v4.5_2017_split_aQGC_Aug2024_allOperators.root' #IRENEchanged
# file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_eboliv2_official_allOperators_smDipole/plots_fit_v4.5_2017_split_aQGC_eboliv2_official_allOperators_smDipole.root' #IRENEchanged

# year=2016
# # # file_Hin = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_cT0_eboliv2_official/plots_fit_v4.5_2016_split_aQGC_cT0_eboliv2_official_withBKG_GiacomoTest2_addingNuis.root' #IRENEchanged
# file_Hin_up = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_oldbasis_allOperators_smDipole/plots_fit_v4.5_2016_split_aQGC_oldbasis_allOperators_smDipole_ALL_INPUTS.root' #IRENEchanged
# # file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_Aug2024_allOperators/plots_fit_v4.5_2016_split_aQGC_Aug2024_allOperators.root' #IRENEchanged
# file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_eboliv2_official_allOperators_smDipole/plots_fit_v4.5_2016_split_aQGC_eboliv2_official_allOperators_smDipole_ALL_INPUTS.root' #IRENEchanged



outputPath='/eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/EFTplots/Aug2024/'+str(year)+'/' #IRENEchanged
# outputPath='/eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/EFTplots/eboliv2_official/'+str(year)+'/' #IRENEchanged

operator1=args.o
print " operator1 ",operator1
samples_Hin_up = ['sm'] ## this is the name for the histogram for SM prediction coming fom reweighting cT8 operator weights IRENEsame
samples_Hin_down = ['sm_'+operator1] ## this is the name for the histogram for SM prediction coming fom reweighting cM3 operator weights IRENEsame
label_up = "EWK"
label_down = "Aug2024"
 
#suffixUp = '_QCDscale_ZVUp'
#samples_Hin_up = [s + suffixUp for s in samples_HinUp]
#suffixDown = '_QCDscale_ZVDown'
#samples_Hin_down = [s + suffixDown for s in samples_HinDown]

colors = ['kGreen+1','kRed+1']

variables = [ 'Mww_binzv'] ## update mame of variable IRENEchanged

def Getting_histograms(sample_Hin_up, sample_Hin_down, cut, variable):
    """Routine to get the histogram to plot from the .root files"""
    try:
        Fin_Hin_up = ROOT.TFile.Open(file_Hin_up)
        Fin_Hin_down = ROOT.TFile.Open(file_Hin_down)
    except:
        print('Could not open file')
        raise
    try:
        # print('Taking histogram from sample', sample_Hin)
        # print('sample:', sample_Hin)
        # print(cut+'/'+variable+'/histo_'+sample_Hin)
        # Hin[sample_Hin] = Fin_Hin.Get(cut+'/'+variable+'/histo_'+sample_Hin).Clone()
        # Hin[sample_Hin].SetBinErrorOption(ROOT.TH1.kPoisson)
        #
        print('sample:', sample_Hin_up)
        print(cut+'/'+variable+'/histo_'+sample_Hin_up)
        Hin_up[sample_Hin_up] = Fin_Hin_up.Get(cut+'/'+variable+'/histo_'+sample_Hin_up).Clone()
        Hin_up[sample_Hin_up].SetBinErrorOption(ROOT.TH1.kPoisson)
        # Subtracting the histogram
        #Hin_up[sample_Hin_up].Add(Fin_Hin_up.Get(cut+'/'+variable+'/histo_p_sm').Clone(), -1)
        #
        print('sample:', sample_Hin_down)
        print(cut+'/'+variable+'/histo_'+sample_Hin_down)
        Hin_down[sample_Hin_down] = Fin_Hin_down.Get(cut+'/'+variable+'/histo_'+sample_Hin_down).Clone()
        Hin_down[sample_Hin_down].SetBinErrorOption(ROOT.TH1.kPoisson)
        print('TRY 1:', Hin_up[sample_Hin_up])
    except:
        print('Could not get the histogram')
        raise


    print('TRY 3:', Hin_up[sample_Hin_up])
    print('TRY 4:', Hin_down[sample_Hin_down])

    canvas = ROOT.TCanvas("plot_"+sample_Hin_up+"_"+variable, "Plot_"+sample_Hin_up+"_"+variable, 500, 600)
    canvas.Divide(1, 2)
    canvas.cd(1)
    canvas.cd(1).SetPad(0, 0.3, 1, 1)
    canvas.cd(1).SetBottomMargin(0.02)
    canvas.cd(1).SetTopMargin(0.1)
    canvas.cd(1).SetRightMargin(0.04)
#    canvas.cd(1).SetLogy() 


    # Plot main histogram
    Hin_up[sample_Hin_up].SetLineColor(ROOT.kGreen+1)
    Hin_down[sample_Hin_down].SetLineColor(ROOT.kRed+1)
    Hin_up[sample_Hin_up].SetLineWidth(2)
    Hin_down[sample_Hin_down].SetLineWidth(2)
    Hin_up[sample_Hin_up].Draw("Ehist")
    Hin_down[sample_Hin_down].Draw("Ehist same")

    yaxis = Hin_up[sample_Hin_up].GetYaxis()
    yaxis.SetRangeUser(-1, 10)

    # Create and draw legend
    legend = ROOT.TLegend(0.1, 0.7, 0.38, .9)
    legend.SetTextSize(0.039)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    # Calculate the integral of the histograms
    integral_Hin_up = Hin_up[sample_Hin_up].Integral()
    integral_Hin_down = Hin_down[sample_Hin_down].Integral()

    # Add the integral to the labels
    # ### if you wish, update legend IRENEsame
    legend.AddEntry(Hin_up[sample_Hin_up], label_up+", Int.: {:.2f}".format(integral_Hin_up), "l")                ### if you wish, update legend IRENEsame
    legend.AddEntry(Hin_down[sample_Hin_down], operator1+" "+label_down+", Int.: {:.2f}".format(integral_Hin_down), "l")          ### if you wish, update legend IRENEsame

    legend.Draw("same")
    canvas.Update()

    canvas.cd(2)
    canvas.cd(2).SetPad(0, 0, 1, 0.3)
    canvas.cd(2).SetTopMargin(0.02)
    canvas.cd(2).SetBottomMargin(0.3)
    canvas.cd(2).SetRightMargin(0.04)

    # Calculate and plot relative percentage ratios
    Rat_down[sample_Hin_up] = Hin_down[sample_Hin_down].Clone()
    Rat_down[sample_Hin_up].Add(Hin_up[sample_Hin_up], -1.0)
    Rat_down[sample_Hin_up].Divide(Hin_down[sample_Hin_down])
    Rat_down[sample_Hin_up].Scale(100.0)
    Rat_down[sample_Hin_up].SetLineColor(ROOT.kRed+1)
    Rat_down[sample_Hin_up].SetLineWidth(2)
    Rat_down[sample_Hin_up].GetYaxis().SetTitle("(Up - Nom)/Nom [%]")
    Rat_down[sample_Hin_up].GetYaxis().SetTitleOffset(0.5)
    Rat_down[sample_Hin_up].GetYaxis().SetRangeUser(-50, 50)
    Rat_down[sample_Hin_up].Draw("hist")


    # Calculate and print the integral ratios in the legend
    histoUpIntegral = Hin_up[sample_Hin_up].Integral()
    histoDownIntegral = Hin_down[sample_Hin_down].Integral()

    canvas.Update()

    # ROOT.objs.append([canvas, Hin_up[sample_Hin_up], Hin_down[sample_Hin_down], Rat_up[sample_Hin], Rat_down[sample_Hin], legend, legend_ratio])
    canvas.SaveAs(outputPath+cut+'_'+operator1+'_'+label_up+'_'+label_down+'_'+variable+'.png')  ## IRENEsame
    canvas.SaveAs(outputPath+cut+'_'+operator1+'_'+label_up+'_'+label_down+'_'+variable+'.pdf')   ## IRENEsame

if __name__ == '__main__':
    import sys
    cuts = [ 'boost_sig_ele','boost_sig_mu']                      ### update here the name of your regions IRENE

    for sample_Hin_up, sample_Hin_down in zip( samples_Hin_up, samples_Hin_down):
        for cut in cuts:
            for variable in variables:
                Getting_histograms(sample_Hin_up, sample_Hin_down, cut, variable)

    print("Plots saved in batch mode.")


