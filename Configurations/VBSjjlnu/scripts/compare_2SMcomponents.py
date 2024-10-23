import ROOT
import math
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", help="components", type=str, )
args = parser.parse_args()



ROOT.gROOT.SetBatch(True)  # Enable batch mode
ROOT.objs = []

Hin = dict()


year=2018
file = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_Aug2024_allOperators_SMsplit/plots_fit_v4.5_2018_split_aQGC_Aug2024_allOperators_SMsplit.root' #FIXME

outputPath='/eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/EFTplots/Aug2024/'+str(year)+'/components/' #IRENEchanged
component=args.c
print " component ",component
operators = ['cT0', 'cT2', 'cT1', 'cT3', 'cT4', 'cT5', 'cS0', 'cS1', 'cM0', 'cM1', 'cM2', 'cM3', 'cM4']

# operators = ['cT0', 'cT2', 'cT1', 'cT3', 'cT4', 'cT5', 'cT6', 'cT7', 'cS0', 'cS1', 'cM0', 'cM1', 'cM2', 'cM3', 'cM4', 'cM5', 'cM7']
# full_operators_name = ['sm_'+component+'_'+op for op in operators] ## this is the name for the histogram for SM prediction coming fom reweighting cM3 operator weights IRENEsame

 
#colors = ['kGreen+1','kRed+1']

variables = [ 'Mww_binzv'] ## update mame of variable IRENEchanged

def Getting_histograms(cut, variable):
    """Routine to get the histogram to plot from the .root files"""
    try:
        Fin = ROOT.TFile.Open(file)
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
        for operator in operators:
            print('operator:', operator)
            print(cut+'/'+variable+'/histo_sm_'+component+'_'+operator)
            Hin[operator] = Fin.Get(cut+'/'+variable+'/histo_sm_'+component+'_'+operator).Clone()
        
            Hin[operator].SetBinErrorOption(ROOT.TH1.kPoisson)
            print('TRY 1:', Hin[operator])
    except:
            print('Could not get the histogram')
            raise


    canvas = ROOT.TCanvas("plot_"+component+"_"+variable, "Plot_"+component+"_"+variable, 500, 600)
    # canvas.Divide(1, 2)
    # canvas.cd(1)
    # canvas.cd(1).SetPad(0, 0.3, 1, 1)
    # canvas.cd(1).SetBottomMargin(0.02)
    # canvas.cd(1).SetTopMargin(0.1)
    # canvas.cd(1).SetRightMargin(0.04)
    
    legend = ROOT.TLegend(0.1, 0.5, 0.7, .9)
    legend.SetTextSize(0.039)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetNColumns(3)
    
    color=1
    # Plot main histogram
    for operator in operators:
        Hin[operator].SetTitle(component)
        Hin[operator].SetLineColor(color)
        color+=1
        Hin[operator].SetLineWidth(2)
        print ("drawing")
        Hin[operator].Draw("Ehistsame")
    

        yaxis = Hin[operator].GetYaxis()
        yaxis.SetRangeUser(-1, 10)

    
        # Calculate the integral of the histograms
        integral = Hin[operator].Integral()

        # Add the integral to the labels
        legend.AddEntry(Hin[operator], operator+", {:.2f}".format(integral), "l")
    
    legend.Draw("same")
    canvas.Update()

    # canvas.cd(2)
    # canvas.cd(2).SetPad(0, 0, 1, 0.3)
    # canvas.cd(2).SetTopMargin(0.02)
    # canvas.cd(2).SetBottomMargin(0.3)
    # canvas.cd(2).SetRightMargin(0.04)

    # # Calculate and plot relative percentage ratios
    # Rat_down[sample_Hin_up] = Hin_down[sample_Hin_down].Clone()
    # Rat_down[sample_Hin_up].Add(Hin_up[sample_Hin_up], -1.0)
    # Rat_down[sample_Hin_up].Divide(Hin_down[sample_Hin_down])
    # Rat_down[sample_Hin_up].Scale(100.0)
    # Rat_down[sample_Hin_up].SetLineColor(ROOT.kRed+1)
    # Rat_down[sample_Hin_up].SetLineWidth(2)
    # Rat_down[sample_Hin_up].GetYaxis().SetTitle("(Up - Nom)/Nom [%]")
    # Rat_down[sample_Hin_up].GetYaxis().SetTitleOffset(0.5)
    # Rat_down[sample_Hin_up].GetYaxis().SetRangeUser(-50, 50)
    # Rat_down[sample_Hin_up].Draw("hist")


    # Calculate and print the integral ratios in the legend
    # histoUpIntegral = Hin_up[sample_Hin_up].Integral()
    # histoDownIntegral = Hin_down[sample_Hin_down].Integral()

    # canvas.Update()

    # ROOT.objs.append([canvas, Hin_up[sample_Hin_up], Hin_down[sample_Hin_down], Rat_up[sample_Hin], Rat_down[sample_Hin], legend, legend_ratio])
    canvas.SaveAs(outputPath+cut+'_'+component+'_'+variable+'.png')  ## IRENEsame
    canvas.SaveAs(outputPath+cut+'_'+component+'_'+variable+'.pdf')   ## IRENEsame

if __name__ == '__main__':
    import sys
    cuts = [ 'boost_sig_ele','boost_sig_mu']                      ### update here the name of your regions IRENE

    
    for cut in cuts:
        for variable in variables:
            Getting_histograms(cut, variable)

    print("Plots saved in batch mode.")


