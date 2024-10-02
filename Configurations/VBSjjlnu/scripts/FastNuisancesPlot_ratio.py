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

# directory = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_25May2023_2018/'
#directory = '/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/2018_Dec22/resolved/'
#file = directory + 'plots_VBS_ZV_25May2023_2018_resolved.root'
# file = '/eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_eboliv2_official/plots_fit_v4.5_2017_split_aQGC_cT0_eboliv2_official_withBKG_GiacomoTest2_addingNuis.root'
#file = directory + 'plots_VBS_ZV_25May2023_2018_resolved.root'
# file = '/eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_DYonly/plots_fit_v4.5_2017_split_aQGC_DYonly.root' #split_aQGC_DYonly.root'
# file = '/eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_sm_1file_each_batch/plots_fit_v4.5_2016_split_sm_1file_each_batch.root' #split_aQGC_DYonly.root'
file = '/eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0sm_eboliv2_official/plots_fit_v4.5_2017_split_aQGC_cT0sm_eboliv2_official.root' #split_aQGC_DYonly.root'

year="2017"
VV_WV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj"]
VV_ZV_samples = ["VV_WZll", "VV_ZZ"]
VV_samples = VV_WV_samples + VV_ZV_samples
VBS_aQGC_samples = ["quad_cT0","sm_lin_quad_cT0","sm"]
samples =["DY", "top", "VVV", "VBF-V_dipole"] + VV_samples + VBS_aQGC_samples
for ir in range(1,8):
        sname = "Wjets_boost_"+str(ir)
        samples.append(sname)
        
samples = ["sm"]        
print(samples)
# samples = ["Wjets_boost"] + VV_samples + VBS_aQGC_samples

#samples = ['DY_Boosted_Z_1', 'DY_Boosted_Z_2', 'DY_Boosted_Z_3', 'DY_Boosted_Z_4', 'DY_Boosted_Z_5']
colors = ['kBlue+1', 'kGreen+1', 'kRed+1']

variations = ['Up', 'Down']

# 2016
# jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2',
#             'JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal',
#             'JESRelativeSample_2016']
# QCDscale_uncertainties = []

# for js in jes_systs:
#     QCDscale_uncertainties.append('CMS_j_scale_'+js)
#     QCDscale_uncertainties.append('CMS_fj_scale_'+js)
# QCDscale_uncertainties += ["CMS_jetpuid_2016","CMS_scale_met_2016","QCDscale_EWK_WV","CMS_PS_ISR","CMS_PS_FSR","CMS_PU_2016"]



# 2017
jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2',
            'JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal',
            'JESRelativeSample_2017']
QCDscale_uncertainties = ['CMS_res_j_2017','CMS_fatjet_res_2017','fatjetJMR','fatjetJMS']
for js in jes_systs:
    QCDscale_uncertainties.append('CMS_j_scale_'+js)
    QCDscale_uncertainties.append('CMS_fj_scale_'+js)
QCDscale_uncertainties += ["CMS_jetpuid_2017","CMS_scale_met_2017","singleTopToTTbar","CMS_topPtRew","QCDscale_EWK_WV","QCD_scale_QCD_VV","CMS_PS_ISR","CMS_PS_FSR","CMS_PU_2017","pdf_1718"]
# # 2018
# QCDscale_uncertainties = ['CMS_res_j_2018','CMS_fatjet_res_2018','fatjetJMR','fatjetJMS']
# jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2',
#             'JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal',
#             'JESRelativeSample_2018']
# for js in jes_systs:
#     QCDscale_uncertainties.append('CMS_j_scale_'+js)
#     QCDscale_uncertainties.append('CMS_fj_scale_'+js)
# QCDscale_uncertainties +=["CMS_scale_e_2017"]
print (QCDscale_uncertainties)
# QCDscale_uncertainties.append('CMS_res_j_2017')
# QCDscale_uncertainties.append('CMS_fatjet_res_2017')
# QCDscale_uncertainties.append('fatjetJMR')
# QCDscale_uncertainties.append('fatjetJMS')
#,'PS_FSR', 'PS_ISR']
#PS_uncertainties = ['PS_FSR', 'PS_ISR']

#variables = [ 'DYfit_Z_bin_Boosted','mjj','DNNoutput_pruned_bReq_morebins','DNNoutput_pruned_bVeto_morebins']#
variables = [ "fit_bins_boost", "events", "Mww", "Mww_binzv", "deltaeta_vbs"]#

def Getting_histograms(sample, cut, variable):
    """Routine to get the histogram to plot from the .root files"""
    print(" file ",file)
    try:
        Fin = ROOT.TFile.Open(file)
    except:
        print('Could not open file')
        raise
    try:
        print('Taking histogram from sample', sample)
        print('sample:', sample)
        print(cut+'/'+variable+'/histo_'+sample)
        Hin[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample).Clone()
        print('TRY 1:', Hin[sample])
    except:
        print('Could not get the histogram', sample)
        raise

    for uncertainty in QCDscale_uncertainties:
        print (" unc ",uncertainty)
        if Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Up'):
            Hin_up[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Up').Clone()
        if Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Down'):
            Hin_down[sample] = Fin.Get(cut+'/'+variable+'/histo_'+sample+'_'+ uncertainty + 'Down').Clone()

        print('TRY 2:', Hin[sample])
        print('TRY 3:', Hin_up[sample])
        print('TRY 4:', Hin_down[sample])
    
        canvas = ROOT.TCanvas("plot_"+sample+"_"+variable, "Plot_"+sample+"_"+variable, 500, 600)
        canvas.Divide(1, 2)
        canvas.cd(1)
        canvas.cd(1).SetPad(0, 0.3, 1, 1)
        canvas.cd(1).SetBottomMargin(0.02)
        canvas.cd(1).SetTopMargin(0.1)
        canvas.cd(1).SetRightMargin(0.04)
    
        # Plot main histogram
        Hin[sample].SetLineColor(ROOT.kBlue+1)
        Hin_up[sample].SetLineColor(ROOT.kGreen+1)
        Hin_down[sample].SetLineColor(ROOT.kRed+1)
        Hin[sample].SetLineWidth(2)
        Hin_up[sample].SetLineWidth(2)
        Hin_down[sample].SetLineWidth(2)
        Hin[sample].Draw("hist")
        Hin_up[sample].Draw("hist sames")
        Hin_down[sample].Draw("hist sames")
    
        # Create and draw legend
        legend = ROOT.TLegend(0.55, 0.7, 0.88, .9)
        legend.SetTextSize(0.039)
        legend.SetFillStyle(0)
        legend.SetBorderSize(0)
        legend.AddEntry(Hin_up[sample], "Up", "l")
        legend.AddEntry(Hin[sample], "Nominal", "l")
        legend.AddEntry(Hin_down[sample], "Down", "l")
        legend.Draw("same")
        canvas.Update()
    
        canvas.cd(2)
        canvas.cd(2).SetPad(0, 0, 1, 0.3)
        canvas.cd(2).SetTopMargin(0.02)
        canvas.cd(2).SetBottomMargin(0.3)
        canvas.cd(2).SetRightMargin(0.04)
    
        # Calculate and plot relative percentage ratios
        Rat_up[sample] = Hin_up[sample].Clone()
        Rat_down[sample] = Hin_down[sample].Clone()
        Rat_up[sample].Add(Hin[sample], -1.0)
        Rat_up[sample].Divide(Hin[sample])
        Rat_up[sample].Scale(100.0)
        Rat_down[sample].Add(Hin[sample], -1.0)
        Rat_down[sample].Divide(Hin[sample])
        Rat_down[sample].Scale(100.0)
        Rat_up[sample].SetLineColor(ROOT.kGreen+1)
        Rat_down[sample].SetLineColor(ROOT.kRed+1)
        Rat_up[sample].SetLineWidth(2)
        Rat_down[sample].SetLineWidth(2)
        Rat_up[sample].GetYaxis().SetTitle("(Up - Nom)/Nom [%]")
        Rat_up[sample].GetYaxis().SetTitleOffset(0.5)
        Rat_up[sample].GetYaxis().SetRangeUser(-50, 50)
        Rat_up[sample].Draw("hist")
        Rat_down[sample].Draw("hist sames")
    
        # Calculate and print the integral ratios in the legend
        histoIntegral = Hin[sample].Integral()
        histoUpIntegral = Hin_up[sample].Integral()
        histoDownIntegral = Hin_down[sample].Integral()
    
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
        legend_ratio.AddEntry(Rat_up[sample], "Diff Up: {:.4f}".format(diffUp), "l")
        legend_ratio.AddEntry(Rat_down[sample], "Diff Down: {:.4f}".format(diffDo), "l")
        legend_ratio.Draw("same")   
        
        f = open("Large uncertainty"+year+".txt", "a")
        f.write("cut \t sample \t uncertainty \t up \t down \t variable \n") 
        if abs(diffUp)> 0.01 or abs(diffDo)> 0.01:
            f.write(cut+" \t "+sample+" \t "+uncertainty+" \t "+str(diffUp)+" \t "+str(diffDo)+" \t "+variable+"\n") 
        f.close()

        canvas.Update()
    
        ROOT.objs.append([canvas, Hin_up[sample], Hin[sample], Hin_down[sample], Rat_up[sample], Rat_down[sample], legend, legend_ratio])
        try:
            os.system('mkdir /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/')
            os.system('cp /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/')
        except:
            print('directory /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/ exists')
        try:
            os.system('mkdir /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/'+cut)
            os.system('cp /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/'+cut+'/')            
        except:
            print('directory /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/'+cut+' exists')
        canvas.SaveAs('/eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/'+cut+'/'+uncertainty+'_'+cut+'_'+sample+'_'+variable+'.pdf')
        canvas.SaveAs('/eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/'+year+'/cT0sm/'+sample+'/'+cut+'/'+uncertainty+'_'+cut+'_'+sample+'_'+variable+'.png')

if __name__ == '__main__':
    import sys
    cuts = [ "boost_wjetcr_ele" ,"boost_wjetcr_mu",
        "boost_topcr_ele" ,"boost_topcr_mu",
        "boost_sig_ele" ,"boost_sig_mu"]
    # cuts = [ "boost_wjetcr_ele", #"boost_wjetcr_mu",
    #     "boost_topcr_ele", #"boost_topcr_mu",
    #     "boost_sig_ele"] #,"boost_sig_mu"]
    for sample in samples:
        for cut in cuts:
            for variable in variables:
                Getting_histograms(sample, cut, variable)

#    input("Press ENTER to exit... ")    
    print("Plots saved in batch mode.")
