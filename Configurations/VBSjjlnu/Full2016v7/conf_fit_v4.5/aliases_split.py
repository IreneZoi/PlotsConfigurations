import os
import copy
import inspect

configurations = os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/"
conf_folder = configurations +"/VBSjjlnu/Full2016v7"

VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]
#aliases = {}

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

wjets_res_bins = [ ]
for i in range(1, 22):
    wjets_res_bins.append("Wjets_res_{}".format(i))
# for i in range(1, 8):
#     Wjets_bins.append("Wjets_boost_{}".format(i))


aliases['nJets30']= {
    'expr' : 'Sum$(CleanJet_pt[CleanJetNotFat_jetIdx] >= 30)'
}

aliases['fit_bin_res'] = {
    'expr': '(VBS_category==1)*( \
            1*( (w_lep_pt < 100) && (vbs_1_pt < 55) ) +\
            2*( (w_lep_pt < 100) && (vbs_1_pt >= 55 && vbs_1_pt < 75) ) +\
            3*( (w_lep_pt < 100) && (vbs_1_pt >= 75 && vbs_1_pt < 100) ) +\
            4*( (w_lep_pt < 100) && (vbs_1_pt >= 100 && vbs_1_pt < 135) ) +\
            5*( (w_lep_pt < 100) && (vbs_1_pt >= 135 && vbs_1_pt < 170) ) +\
            6*( (w_lep_pt < 100) && (vbs_1_pt >= 170) ) +\
            7*( (w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt < 55) ) +\
            8*( (w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 55 && vbs_1_pt < 75) ) +\
            9*( (w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 75 && vbs_1_pt < 100) ) +\
            10*( (w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 100 && vbs_1_pt < 135) ) +\
            11*( (w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 135 && vbs_1_pt < 170) ) +\
            12*( (w_lep_pt >= 100 && w_lep_pt < 200) && (vbs_1_pt >= 170) ) +\
            13*( (w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt < 90) ) +\
            14*( (w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt >= 90 && vbs_1_pt < 125) ) +\
            15*( (w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt >= 125 && vbs_1_pt < 160) ) +\
            16*( (w_lep_pt >= 200 && w_lep_pt < 300) && (vbs_1_pt >= 160) ) +\
            17*( (w_lep_pt >= 300 && w_lep_pt < 400) && (vbs_1_pt < 90) ) +\
            18*( (w_lep_pt >= 300 && w_lep_pt < 400) && (vbs_1_pt >= 90) ) +\
            19*( (w_lep_pt >= 400 && w_lep_pt < 500) && (vbs_1_pt < 85) ) +\
            20*( (w_lep_pt >= 400 && w_lep_pt < 500) && (vbs_1_pt >= 85) ) +\
            21*( w_lep_pt >= 500) \
            ) + (VBS_category==0)*(-1)'
}

###################3
# trigger eff

aliases['ele_trig_eff'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/src/PlotsConfigurations/Configurations/patches/triggerEff_1lep.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'TrigEff_1lep',
    'args': ('/afs/cern.ch/user/a/arun/public/fixedTextfiles/2016/mvaid/Ele25_pt_eta_efficiency_withSys_Run2016.txt'),
    'samples': mc
}

aliases['SingleLepton_trigEff_corrected'] = {
    'expr': '(abs(Lepton_pdgId[0])==11)*ele_trig_eff[0] +  (abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l',
    'samples': mc
}

aliases['SingleLepton_trigEff_corrected_up'] = {
    'expr': '(abs(Lepton_pdgId[0])==11)*ele_trig_eff[1] +  (abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l_u',
    'samples': mc
}


aliases['SingleLepton_trigEff_corrected_down'] = {
    'expr': '(abs(Lepton_pdgId[0])==11)*ele_trig_eff[2] +  (abs(Lepton_pdgId[0])==13)*TriggerEffWeight_1l_d',
    'samples': mc
}


###### W EWK nlo ######

aliases['EWKnloW'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L %s/src/PlotsConfigurations/Configurations/VBSjjlnu/macros/EWKnloW_otf.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'EWKnloW_otf',
    'args': ('%s/src/LatinoAnalysis/Gardener/python/data/ewk/kewk_w_for_python.txt' % os.getenv('CMSSW_BASE')),
    'samples': wjets_res_bins + ['Wjets_boost']
}

##################################
# BTag

bAlgo = 'DeepB'
bWP = ' 0.2217 '
bWPtight = '0.8953'

aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] >  0.2217 ) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] >  0.2217 ) >= 1)'
}


aliases['bReqTight'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] >  0.8953 ) >= 1)'
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': 'bVeto*bVetoSF + bReqTight *bReqSF',
    'samples': mc
}

systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
  aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReqTight*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReqTight) ))', 'samples':mc  }
  aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReqTight*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReqTight) ))', 'samples':mc }


aliases['nJetsBtag']= {
    'expr' : 'Sum$(CleanJet_pt > 20 && abs(CleanJet_eta)<2.5)'
}


btagSF_corr_samples_groups = {
    'VBS': ['VBS', 'VBS_dipoleRecoil'] + VBS_samples ,
    'Wjets_HT': ['Wjets_boost']+wjets_res_bins,
    'Vg_VgS_VBFV':['Vg','VgS','VBF-V', 'VBF-V_dipole'],
    'VV_VVV_ggWW':['VVV','VV','ggWW'] + VV_samples,
    'top':['top'],
    'DY': ['DY']
}

for sgroup_name, sgroup in btagSF_corr_samples_groups.items():
    aliases['btagSF_corr_'+sgroup_name] = {
        'class': 'BtagSFNormCorrection',
        'args': ('{}/VBSjjlnu/weights_files/btagsf_correction/btagsf_corr_2016.root'.format(configurations), sgroup_name),
        'linesToAdd' : [
            'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
            '.L {}/VBSjjlnu/macros/btagsf_norm_correction.cc+'.format(configurations)
        ],     
        'samples' : sgroup
    }

################################################################################################


aliases['PUJetIdSF'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2 && ( (Jet_electronIdx1 != Lepton_electronIdx[0]) || Jet_electronIdx1 < 0 )  \
                                          && ( (Jet_muonIdx1 != Lepton_muonIdx[0] ) || Jet_muonIdx1 < 0 ) \
                            )*TMath::Log(Jet_PUIDSF_loose)))',
  'samples': mc
}

aliases['PUJetIdSF_up'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2 && ( (Jet_electronIdx1 != Lepton_electronIdx[0]) || Jet_electronIdx1 < 0 )  \
                                          && ( (Jet_muonIdx1 != Lepton_muonIdx[0] ) || Jet_muonIdx1 < 0 ) \
                            )*TMath::Log(Jet_PUIDSF_loose_up)))',
  'samples': mc
}

aliases['PUJetIdSF_down'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2 && ( (Jet_electronIdx1 != Lepton_electronIdx[0]) || Jet_electronIdx1 < 0 )  \
                                          && ( (Jet_muonIdx1 != Lepton_muonIdx[0] ) || Jet_muonIdx1 < 0 ) \
                            )*TMath::Log(Jet_PUIDSF_loose_down)))',
  'samples': mc
}

##########################################

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'CountGenJet',
    'samples': mc
}

##### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'getGenZpt',
    'samples': ['DY']
}
handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2016']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2016']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

#######################################################

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}

aliases['topGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

##### Top pT reweighting
aliases['Top_pTrw'] = {
    # Mine:
    #'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(-2.02274e-01 + 1.09734e-04*topGenPt - 1.30088e-07*topGenPt*topGenPt + 5.83494e+01/(topGenPt+1.96252e+02)) * TMath::Exp(-2.02274e-01 + 1.09734e-04*antitopGenPt - 1.30088e-07*antitopGenPt*antitopGenPt + 5.83494e+01/(antitopGenPt+1.96252e+02)))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPt - 8.90557e-08*topGenPt*topGenPt) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPt - 8.90557e-08*antitopGenPt*antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5

    # New Top PAG
    'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPtOTF - 8.90557e-08*topGenPtOTF*topGenPtOTF) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPtOTF - 8.90557e-08*antitopGenPtOTF*antitopGenPtOTF))) + (topGenPtOTF * antitopGenPtOTF <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5
    'samples': ['top']
}


##############################################

basedir_fakes = configurations + "/VBSjjlnu/weights_files/fake_rates/2016"

ets = ["25", "35", "45"]
el_pr_file = configurations + "/VBSjjlnu/weights_files/prompt_rates/2016/plot_ElCh_l1_etaVpt_ptel_2D_pr.root"
mu_pr_file = configurations + "/VBSjjlnu/weights_files/prompt_rates/2016/plot_MuCh_l1_etaVpt_ptmu_2D_pr.root"

for et in ets:
    el_fr_file = basedir_fakes + "/plot_ElCh_JetEt"+et+"_l1_etaVpt_ptel_aseta_fw_ewk_2D.root" #No absolute value for fakes
    mu_fr_file = basedir_fakes + "/plot_MuCh_JetEt"+et+"_l1_etaVpt_ptmu_fw_ewk_2D.root"
    aliases['fakeWeight_'+et] = { 
        'class': 'newFakeWeightOTFall',
        'args': (eleWP, muWP, copy.deepcopy(el_fr_file), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file), copy.deepcopy(mu_pr_file), False, False, False),  #doabsEta=False, no stat variations
        'linesToAdd' : [
            'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
            '.L {}/VBSjjlnu/macros/newfakeweight_OTFall.cc+'.format(configurations)
        ],     
        'samples': ["Fake"]
    }

# stat variations
el_fr_file35 = basedir_fakes + "/plot_ElCh_JetEt35_l1_etaVpt_ptel_aseta_fw_ewk_2D.root" #No absolute value for fakes
mu_fr_file35 = basedir_fakes + "/plot_MuCh_JetEt35_l1_etaVpt_ptmu_fw_ewk_2D.root"

aliases['fakeWeight_35_statUp'] = { 
        'class': 'newFakeWeightOTFall',
        'args': (eleWP, muWP, copy.deepcopy(el_fr_file35), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file35), copy.deepcopy(mu_pr_file), False, True, False),   
        'samples': ["Fake"]
    }
aliases['fakeWeight_35_statDo'] = { 
        'class': 'newFakeWeightOTFall',
        'args': (eleWP, muWP, copy.deepcopy(el_fr_file35), copy.deepcopy(el_pr_file), copy.deepcopy(mu_fr_file35), copy.deepcopy(mu_pr_file), False, False, True), 
        'samples': ["Fake"]
    }

################################################
# For VgS
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

##############################################
# 
aliases['veto_fatjet_180'] = {
            'class': 'VetoFatJetResolved',
            'args': (180.),
            'linesToAdd' : [
                'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                '.L {}/VBSjjlnu/macros/veto_fatjet_resolved.cc+'.format(configurations)
            ]           
}

#######################################

aliases['QCDscale_normalized'] = {
            'class': 'QCDScaleNormalized',
            'args': (),
            'linesToAdd' : [
                # 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
                '.L {}/VBSjjlnu/macros/QCDscale_normalize.cc+'.format(configurations)
            ] ,
            'samples':['VBS', 'VBS_dipoleRecoil', 'VV'] + VBS_samples + VV_samples          
}

# aliases['PDFweight_normalized'] = {
#             'class': 'PDFWeightNormalized',
#             'args': (),
#             'linesToAdd' : [
#                 # 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#                 '.L {}/VBSjjlnu/macros/PDFweight_normalize.cc+'.format(configurations)
#             ] ,
#             'samples':['VBS', 'VBS_dipoleRecoil']          
# }

###################################3
# QGL variables

morphing_file = configurations + "/VBSjjlnu/weights_files/qgl_morphing/morphing_functions_withvars_2016.root"


aliases["CleanJet_qgl_morphed"]  = {
    'class': 'QGL_morphing',
    'args' : (morphing_file, "nom", "0000"),
    'linesToAdd' : [
        # 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}/macros/qgl_morphing.cc+'.format(configurations)
        ] 
}


##########################



aliases['vbs_0_qgl_res'] = {
   'expr': 'Alt$(CleanJet_qgl_morphed[VBS_jets_maxmjj_massWZ[0]],-1)'
} 

aliases['vbs_1_qgl_res'] = {
   'expr': 'Alt$(CleanJet_qgl_morphed[VBS_jets_maxmjj_massWZ[1]],-1)'
} 

aliases['vjet_0_qgl_res'] = {
    'expr': 'Alt$(CleanJet_qgl_morphed[V_jets_maxmjj_massWZ[0]],-1)'
} 

aliases['vjet_1_qgl_res'] = {
    'expr': 'Alt$(CleanJet_qgl_morphed[V_jets_maxmjj_massWZ[1]],-1)'
} 

aliases['vbs_0_qgl_boost'] = {
    'expr': 'Alt$(CleanJet_qgl_morphed[VBS_jets_maxmjj[0]],-1)'
} 

aliases['vbs_1_qgl_boost'] = {
    'expr': 'Alt$(CleanJet_qgl_morphed[VBS_jets_maxmjj[1]],-1)'
} 

##########################
# additional uncertainties for Wtagging from pt extrapolation
aliases['BoostedWtagSF_ptextr'] = {
    'class': 'Wtagging_SF_ptExtrap',
    'args': ('2016'),
    'linesToAdd' : [
        # 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        '.L {}/VBSjjlnu/macros/Wtagging_SF_ptExtrap.cc+'.format(configurations)
    ]   
}


#########################

mva_reader_path = os.getenv('CMSSW_BASE') + '/src/PlotsConfigurations/Configurations/VBSjjlnu/macros/'
models_path = '/eos/home-d/dvalsecc/www/VBSPlots/DNN_archive/FullRun2_v7/FullRun2_v7/'

aliases['DNNoutput_boosted'] = {
     'class': 'MVAReaderBoosted_mVauto',
     'args': ( models_path +'boost_sig/models/v3_d/',  models_path +'boost_sig/models/v3_d/cumulative_signal_2016.root', False, 0),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mva_reader_boosted_v3d_mVauto.cc+',
    ],
}

aliases['DNNoutput_resolved_v1'] = {
    'class': 'MVAReaderResolved_mVauto',
    'args': ( models_path+ 'res_sig/models/v4_d/',models_path+ 'res_sig/models/v4_d/cumulative_signal_2016.root', False, 1),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mva_reader_resolved_v4d_mVauto.cc+',
    ],
}


# aliases['dipole_weight'] = {
#     'class': 'ReweightDNN',
#     'args': (configurations + "/VBSjjlnu/weights_files/DNN_reweight_VBS_dipole.root", False),
#     'linesToAdd': [
#         # 'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
#             '.L {}/VBSjjlnu/macros/reweight_dnn.cc+'.format(configurations)
#     ],
#     'samples': ["VBS", "VBS_dipoleRecoil"]
# }