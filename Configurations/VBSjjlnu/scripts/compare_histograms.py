import ROOT
import math
import os

ROOT.gROOT.SetBatch(True)  # Enable batch mode
ROOT.objs = []

Hin = dict()
Hin_up = dict()
Hin_down = dict()
Rat_up = dict()
Rat_down = dict()

# year=2018
# file_Hin = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_oldbasis_allOperators_smDipole/plots_fit_v4.5_2018_split_aQGC_oldbasis_allOperators_smDipole_ALL_INPUTS.root' #IRENEchanged
# file_Hin_up = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_eboliv2_official_allOperators_smDipole/plots_fit_v4.5_2018_split_aQGC_eboliv2_official_ALL_INPUTS.root' #IRENEchanged
# file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_eboliv2_allOperators_smDipole/plots_fit_v4.5_2018_split_aQGC_eboliv2_allOperators_smDipole_ALL_INPUTS.root' #IRENEchanged

year=2017
file_Hin = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_oldbasis_allOperators_smDipole/plots_fit_v4.5_2017_split_aQGC_oldbasis_allOperators_smDipole.root' #IRENEchanged
file_Hin_up = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_eboliv2_official_allOperators_smDipole/plots_fit_v4.5_2017_split_aQGC_eboliv2_official_allOperators_smDipole.root' #IRENEchanged
file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_eboliv2_allOperators_smDipole/plots_fit_v4.5_2017_split_aQGC_eboliv2_allOperators_smDipole.root' #IRENEchanged

# year=2016
# file_Hin = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_cT0_eboliv2_official/plots_fit_v4.5_2016_split_aQGC_cT0_eboliv2_official_withBKG_GiacomoTest2_addingNuis.root' #IRENEchanged
# file_Hin_up = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_eboliv2_official_allOperators/plots_fit_v4.5_2016_split_aQGC_eboliv2_official_allOperators.root' #IRENEchanged
# file_Hin_down = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_eboliv2_official_allOperators/plots_fit_v4.5_2016_split_aQGC_eboliv2_official_allOperators.root' #IRENEchanged


outputPath='/eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/EFTplots/compare_sm_lin_quad/'+str(year)+'/' #IRENEchanged
 
#suffixUp = '_QCDscale_ZVUp'
#samples_Hin_up = [s + suffixUp for s in samples_HinUp]
#suffixDown = '_QCDscale_ZVDown'
#samples_Hin_down = [s + suffixDown for s in samples_HinDown]

colors = ['kBlue+1', 'kGreen+1', 'kRed+1']

variables = [ 'Mww_binzv'] ## update mame of variable IRENEchanged

def Getting_histograms(sample_Hin, sample_Hin_up, sample_Hin_down, cut, variable):
    """Routine to get the histogram to plot from the .root files"""
    try:
        Fin_Hin = ROOT.TFile.Open(file_Hin)
        Fin_Hin_up = ROOT.TFile.Open(file_Hin_up)
        Fin_Hin_down = ROOT.TFile.Open(file_Hin_down)
    except:
        print('Could not open file')
        raise
    try:
        print('Taking histogram from sample', sample_Hin)
        print('sample:', sample_Hin)
        print(cut+'/'+variable+'/histo_'+sample_Hin)
        Hin[sample_Hin] = Fin_Hin.Get(cut+'/'+variable+'/histo_'+sample_Hin).Clone()
        # Subtracting the histogram
        #Hin[sample_Hin].Add(Fin_Hin.Get(cut+'/'+variable+'/histo_sm').Clone(), -1)
        #
        Hin[sample_Hin].SetBinErrorOption(ROOT.TH1.kPoisson)
        Hin_up[sample_Hin_up] = Fin_Hin_up.Get(cut+'/'+variable+'/histo_'+sample_Hin_up).Clone()
        # Subtracting the histogram
        #Hin_up[sample_Hin_up].Add(Fin_Hin_up.Get(cut+'/'+variable+'/histo_p_sm').Clone(), -1)
        #
        Hin_up[sample_Hin_up].SetBinErrorOption(ROOT.TH1.kPoisson)
        Hin_down[sample_Hin_down] = Fin_Hin_down.Get(cut+'/'+variable+'/histo_'+sample_Hin_down).Clone()
        Hin_down[sample_Hin_down].SetBinErrorOption(ROOT.TH1.kPoisson)
        print('TRY 1:', Hin[sample_Hin])
    except:
        print('Could not get the histogram', sample_Hin)
        raise


    print('TRY 2:', Hin[sample_Hin])
    print('TRY 3:', Hin_up[sample_Hin_up])
    print('TRY 4:', Hin_down[sample_Hin_down])

    canvas = ROOT.TCanvas("plot_"+sample_Hin+"_"+variable, "Plot_"+sample_Hin+"_"+variable, 500, 600)
    canvas.Divide(1, 2)
    canvas.cd(1)
    canvas.cd(1).SetPad(0, 0.3, 1, 1)
    canvas.cd(1).SetBottomMargin(0.02)
    canvas.cd(1).SetTopMargin(0.1)
    canvas.cd(1).SetRightMargin(0.04)
#    canvas.cd(1).SetLogy() 


    # Plot main histogram
    Hin[sample_Hin].SetLineColor(ROOT.kBlue+1)
    Hin_up[sample_Hin_up].SetLineColor(ROOT.kGreen+1)
    Hin_down[sample_Hin_down].SetLineColor(ROOT.kRed+1)
    Hin[sample_Hin].SetLineWidth(2)
    Hin_up[sample_Hin_up].SetLineWidth(2)
    Hin_down[sample_Hin_down].SetLineWidth(2)
    Hin[sample_Hin].Draw("Ehist")
    Hin_up[sample_Hin_up].Draw("Ehist same")
    Hin_down[sample_Hin_down].Draw("Ehist same")

    ymax = Hin[sample_Hin].GetBinContent(Hin[sample_Hin].GetMaximumBin())
    if (Hin_up[sample_Hin_up].GetBinContent(Hin_up[sample_Hin_up].GetMaximumBin())>ymax):
        ymax = Hin_up[sample_Hin_up].GetBinContent(Hin_up[sample_Hin_up].GetMaximumBin())
    if (Hin_down[sample_Hin_down].GetBinContent(Hin_down[sample_Hin_down].GetMaximumBin())>ymax):
        ymax = Hin_down[sample_Hin_down].GetBinContent(Hin_down[sample_Hin_down].GetMaximumBin())
    yaxis = Hin[sample_Hin].GetYaxis()
    yaxis.SetRangeUser(0, ymax*1.2)

    # Create and draw legend
    legend = ROOT.TLegend(0.1, 0.7, 0.38, .9)
    legend.SetTextSize(0.039)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    # Calculate the integral of the histograms
    integral_Hin_up = Hin_up[sample_Hin_up].Integral()
    integral_Hin = Hin[sample_Hin].Integral()
    integral_Hin_down = Hin_down[sample_Hin_down].Integral()

    # Add the integral to the labels
    legend.AddEntry(Hin[sample_Hin],sample_Hin, "") 
    legend.AddEntry(Hin[sample_Hin], "old, Int.: {:.2f}".format(integral_Hin), "l")                      ### if you wish, update legend IRENEsame
    legend.AddEntry(Hin_up[sample_Hin_up],"central, Int.: {:.2f}".format(integral_Hin_up), "l")                ### if you wish, update legend IRENEsame
    legend.AddEntry(Hin_down[sample_Hin_down],"private, Int.: {:.2f}".format(integral_Hin_down), "l")          ### if you wish, update legend IRENEsame

    legend.Draw("same")
    canvas.Update()

    canvas.cd(2)
    canvas.cd(2).SetPad(0, 0, 1, 0.3)
    canvas.cd(2).SetTopMargin(0.02)
    canvas.cd(2).SetBottomMargin(0.3)
    canvas.cd(2).SetRightMargin(0.04)

    # Calculate and plot relative percentage ratios
    Rat_up[sample_Hin] = Hin_up[sample_Hin_up].Clone()
    Rat_down[sample_Hin] = Hin_down[sample_Hin_down].Clone()
    Rat_up[sample_Hin].Add(Hin[sample_Hin], -1.0)
    Rat_up[sample_Hin].Divide(Hin[sample_Hin])
    Rat_up[sample_Hin].Scale(100.0)
    Rat_down[sample_Hin].Add(Hin[sample_Hin], -1.0)
    Rat_down[sample_Hin].Divide(Hin[sample_Hin])
    Rat_down[sample_Hin].Scale(100.0)
    Rat_up[sample_Hin].SetLineColor(ROOT.kGreen+1)
    Rat_down[sample_Hin].SetLineColor(ROOT.kRed+1)
    Rat_up[sample_Hin].SetLineWidth(2)
    Rat_down[sample_Hin].SetLineWidth(2)
    Rat_up[sample_Hin].GetYaxis().SetTitle("(Up - Nom)/Nom [%]")
    Rat_up[sample_Hin].GetYaxis().SetTitleOffset(0.5)
    Rat_up[sample_Hin].GetYaxis().SetRangeUser(-50, 50)
    Rat_up[sample_Hin].Draw("hist")
    Rat_down[sample_Hin].Draw("hist same")

    # Calculate and print the integral ratios in the legend
    histoIntegral = Hin[sample_Hin].Integral()
    histoUpIntegral = Hin_up[sample_Hin_up].Integral()
    histoDownIntegral = Hin_down[sample_Hin_down].Integral()

    diffUp = 0.
    if histoIntegral > 0. and histoUpIntegral > 0.:
        diffUp = (histoUpIntegral - histoIntegral) / histoIntegral

    diffDo = 0.
    if histoIntegral > 0. and histoDownIntegral > 0.:
        diffDo = (histoDownIntegral - histoIntegral) / histoIntegral

    legend_ratio = ROOT.TLegend(0.55, 0.1, 0.88, 0.3)
    legend_ratio.SetTextSize(0.039)
    legend_ratio.SetFillStyle(0)
    legend_ratio.SetBorderSize(0)
    legend_ratio.AddEntry(Rat_up[sample_Hin], "Diff Up: {:.4f}".format(diffUp), "l")
    legend_ratio.AddEntry(Rat_down[sample_Hin], "Diff Down: {:.4f}".format(diffDo), "l")
    legend_ratio.Draw("same")

    canvas.Update()

    ROOT.objs.append([canvas, Hin_up[sample_Hin_up], Hin[sample_Hin], Hin_down[sample_Hin_down], Rat_up[sample_Hin], Rat_down[sample_Hin], legend, legend_ratio])
    canvas.SaveAs(outputPath+cut+'_'+sample_Hin+'_'+variable+'.png')  ## IRENEsame
    canvas.SaveAs(outputPath+cut+'_'+sample_Hin+'_'+variable+'.pdf')   ## IRENEsame

if __name__ == '__main__':
    import sys
    cuts = [ 'boost_sig_ele','boost_sig_mu']                      ### update here the name of your regions IRENE

    # operator1="cT0"

    # samples_Hin = ['quad_'+operator1]  ## this is the name of the histogram for SM_DIPOLE IRENEchanged
    # samples_Hin_up = ['quad_'+operator1] ## this is the name for the histogram for SM prediction coming fom reweighting cT8 operator weights IRENEsame
    # samples_Hin_down = ['quad_'+operator1] ## this is the name for the histogram for SM prediction coming fom reweighting cM3 operator weights IRENEsame
    theOperators = ["cT0", "cT2", "cT1", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM7"]
    quad_name = []
    sm_name = []
    sm_lin_quad_name = []
    for op in theOperators:   
        quad_name.append("quad_"+op)
        sm_name.append("sm_"+op)
        sm_lin_quad_name.append("sm_lin_quad_"+op)
    
    samples_Hin      = sm_lin_quad_name
    samples_Hin_up   = sm_lin_quad_name 
    samples_Hin_down = sm_lin_quad_name
    
    for sample_Hin, sample_Hin_up, sample_Hin_down in zip(samples_Hin, samples_Hin_up, samples_Hin_down):
        for cut in cuts:
            for variable in variables:
                Getting_histograms(sample_Hin, sample_Hin_up, sample_Hin_down, cut, variable)

    print("Plots saved in batch mode.")


