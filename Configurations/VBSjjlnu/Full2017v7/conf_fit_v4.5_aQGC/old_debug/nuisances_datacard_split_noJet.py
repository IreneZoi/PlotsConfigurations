# nuisances
# # # name of samples here must match keys in samples.py 
VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VBS_WV_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj"]
VBS_ZV_samples = ["VBS_WZll", "VBS_ZZ"]
VV_WV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj"]
VV_ZV_samples = ["VV_WZll", "VV_ZZ"]
VV_samples = VV_WV_samples + VV_ZV_samples
VBS_aQGC_samples = ["quad_cT0","sm_lin_quad_cT0","sm_dipole"]
signals = ['quad_cT0','sm_lin_quad_cT0']
mc =["DY", "top", "VV", "VVV", "VBF-V_dipole", "Vg", "VgS","VBS_dipoleRecoil","ggWW", "Wjets_boost"] + wjets_res_bins + VV_samples + VBS_aQGC_samples
# "VBS", "VBF-V",

phasespaces = ["res_wjetcr_ele","res_wjetcr_mu" ,"boost_wjetcr_ele" ,"boost_wjetcr_mu",
        "res_topcr_ele","res_topcr_mu" ,"boost_topcr_ele" ,"boost_topcr_mu",
        "res_sig_ele","res_sig_mu" ,"boost_sig_ele" ,"boost_sig_mu" ]

def getSamplesWithout(samples, samples_to_remove):
    return [m for m in samples if m not in samples_to_remove]


phase_spaces_boost = [ c for c in phasespaces if 'boost' in c]
phase_spaces_res = [ c for c in phasespaces if 'res' in c]

phase_spaces_res_ele = [ c for c in phase_spaces_res if 'ele' in c]
phase_spaces_res_mu = [ c for c in phase_spaces_res if 'mu' in c]
phase_spaces_boost_ele = [ c for c in phase_spaces_boost if 'ele' in c]
phase_spaces_boost_mu =  [ c for c in phase_spaces_boost if 'mu' in c]

phase_spaces_tot_ele = phase_spaces_res_ele + phase_spaces_boost_ele
phase_spaces_tot_mu = phase_spaces_res_mu + phase_spaces_boost_mu
phase_spaces_tot_res = phase_spaces_res_ele + phase_spaces_res_mu
phase_spaces_tot_boost = phase_spaces_boost_ele + phase_spaces_boost_mu

phase_spaces_dict = {"boost": phase_spaces_boost, "res": phase_spaces_res}
phase_spaces_tot = phase_spaces_tot_ele + phase_spaces_tot_mu

# Function to split a nuisance on different folders for different group of samples
# keeping the same nuisance name
# groups = [ (list of samples, folder), ...  ]
# def split_nuisance_samples_dir(nuisance_name, nuisance_options, variation, groups):
#     for ig, (samples_list, folder) in enumerate(groups):
#         n = {}
#         n.update(nuisance_options)
#         n["samples"] = dict((skey, ['1.','1.']) for skey in samples_list)
#         n["folderUp"] = folder +'_'+variation + 'up'
#         n["folderDown"] = folder +'_'+variation + 'do'
#         nuisances['{}_{}'.format(nuisance_name, ig)] = n

# # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # #### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['top', "Wjets_boost"]+wjets_res_bins)
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc if skey not in ['top', "Wjets_boost"]+wjets_res_bins)
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc if skey not in ['top', "Wjets_boost"]+wjets_res_bins)
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['top', "Wjets_boost"]+wjets_res_bins)
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in ['top', "Wjets_boost"]+wjets_res_bins)
}


nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc if skey not in ['top', "Wjets_boost"]+wjets_res_bins)
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc if skey not in ['top', "Wjets_boost"]+wjets_res_bins)
}


##########Fakes
fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
fakeW_statUp        =  '( fakeWeight_35_statUp / fakeWeight_35  )'
fakeW_statDown      =  '( fakeWeight_35_statDo / fakeWeight_35  )'

nuisances['fake_syst_ele']  = {
               'name'  : 'CMS_fake_syst_ele',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
                'cuts': phase_spaces_tot_ele
               }

nuisances['fake_syst_mu']  = {
               'name'  : 'CMS_fake_syst_mu',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
                'cuts': phase_spaces_tot_mu
               }

nuisances['fake_ele']  = {
                'name'  : 'CMS_fake_ele_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                            'Fake'     : [ fakeW_jetUp , fakeW_jetDown ],
                              'Fake_ele'     : [ fakeW_jetUp , fakeW_jetDown ],
                              'Fake_mu'      : [ fakeW_jetUp , fakeW_jetDown ],
                             },
                'cuts':  phase_spaces_tot_ele
}

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_ele_stat_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                            'Fake'      : [ fakeW_statUp , fakeW_statDown ],
                              'Fake_ele'      : [ fakeW_statUp , fakeW_statDown ],
                              'Fake_mu'      : [ fakeW_statUp , fakeW_statDown ],
                             },
                'cuts':  phase_spaces_tot_ele
}

nuisances['fake_mu']  = {
                'name'  : 'CMS_fake_mu_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                                'Fake'     : [ fakeW_jetUp , fakeW_jetDown ],
                              'Fake_ele'     : [ fakeW_jetUp , fakeW_jetDown ],
                              'Fake_mu'     : [ fakeW_jetUp , fakeW_jetDown ],
                             },
                'cuts':  phase_spaces_tot_mu
}


nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_mu_stat_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                            'Fake'     :[ fakeW_statUp , fakeW_statDown ],
                              'Fake_ele'     :[ fakeW_statUp , fakeW_statDown ],
                              'Fake_mu'     :[ fakeW_statUp , fakeW_statDown ]
                             },
                'cuts':  phase_spaces_tot_mu
}

# ##### Btag nuisances

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc)
    }

# # ##### Trigger Efficiency

trig_syst = ['( SingleLepton_trigEff_corrected_up / SingleLepton_trigEff_corrected )*(SingleLepton_trigEff_corrected>0.02) + (SingleLepton_trigEff_corrected<=0.02)', 
            '(SingleLepton_trigEff_corrected_down/SingleLepton_trigEff_corrected)']

nuisances['trigg']  = {
                'name'  : 'CMS_eff_trigger_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' :  dict((skey, trig_syst) for skey in mc)
}

# # Prefire correction
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire']  = {
                'name'  : 'CMS_eff_prefiring_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, trig_syst) for skey in mc)
}

# # ##### Electron Efficiency and energy scale

ele_id_syst_up = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Up[0])/\
                    (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
ele_id_syst_do = '(abs(Lepton_pdgId[0]) == 11)*(Lepton_tightElectron_'+eleWP+'_TotSF'+'_Down[0])/\
                    (Lepton_tightElectron_'+eleWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 13)'
mu_id_syst_up = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Up[0])/\
                    (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'
mu_id_syst_do = '(abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_'+muWP+'_TotSF'+'_Down[0])/\
                    (Lepton_tightMuon_'+muWP+'_TotSF[0]) + (abs(Lepton_pdgId[0]) == 11)'

id_syst_ele = [ ele_id_syst_up, ele_id_syst_do ]
id_syst_mu = [ mu_id_syst_up, mu_id_syst_do ]

nuisances['eff_e']  = {
                'name'  : 'CMS_eff_e_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :   dict((skey, id_syst_ele) for skey in mc ),
                'cuts': phase_spaces_tot_ele
}

nuisances['electronpt']  = {
                'name'  : 'CMS_scale_e_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'ElepTup',
                'mapDown': 'ElepTdo',
                'cuts': phase_spaces_tot_ele,
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
                'folderUp' : directory_mc+'_ElepTup',
                'folderDown' : directory_mc+'_ElepTdo',
}

# for wjbin in wjets_res_bins:
#     nuisances['electronpt_'+wjbin]  = {
#                     'name'  : 'CMS_scale_e_2017',
#                     'kind'  : 'suffix',
#                     'type'  : 'shape',
#                     'mapUp': 'ElepTup',
#                     'mapDown': 'ElepTdo',
#                     'cuts': phase_spaces_tot_ele, 
#                     'samples': { wjbin:  ['1.','1.']},
#                     'folderUp' : directory_wjets_res_bins[wjbin]+'_ElepTup',
#                     'folderDown' : directory_wjets_res_bins[wjbin]+'_ElepTdo',
#     }


# # ##### Muon Efficiency and energy scale


nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc  ),
                'cuts': phase_spaces_tot_mu
}

nuisances['muonpt']  = {
                'name'  : 'CMS_scale_m_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'MupTup',
                'mapDown': 'MupTdo',
                'cuts': phase_spaces_tot_mu,
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
                'folderUp' : directory_mc+'_MupTup',
                'folderDown' : directory_mc+'_MupTdo',
}

# for wjbin in wjets_res_bins:
#     nuisances['muonpt_'+wjbin]  = {
#                     'name'  : 'CMS_scale_m_2017',
#                     'kind'  : 'suffix',
#                     'type'  : 'shape',
#                     'mapUp': 'MupTup',
#                     'mapDown': 'MupTdo',
#                     'cuts': phase_spaces_tot_mu, 
#                     'samples': { wjbin:  ['1.','1.']},
#                     'folderUp' : directory_wjets_res_bins[wjbin]+'_MupTup',
#                     'folderDown' : directory_wjets_res_bins[wjbin]+'_MupTdo',
#     } 
# for wjbin in wjets_res_bins:
#     nuisances['JER_'+wjbin]  = {
#                     'name': 'CMS_res_j_2017',
#                     'kind': 'suffix',
#                     'type': 'shape',
#                     'mapUp': 'JERup',
#                     'mapDown': 'JERdo',
#                     'samples': { wjbin:  ['1.','1.']},
#                     'folderUp' : directory_wjets_res_bins[wjbin]+'_JERup',
#                     'folderDown' : directory_wjets_res_bins[wjbin]+'_JERdo',
#                     'AsLnN'      : '1',
#     }
##################
# PU jet id

nuisances['JetPUID_sf']  = {
                'name'  : 'CMS_jetpuid_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc ),
}


# ##### Jet energy scale - Irene test

##### Jet energy scale
# jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2',
#             'JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal',
#             'JESRelativeSample_2017']

# for js in jes_systs:
#     nuisances[js]  = {
#                     'name': 'CMS_j_scale_'+js,
#                     'kind': 'suffix',
#                     'type': 'shape',
#                     'mapUp': js+'up',
#                     'mapDown': js+'do',
#                     'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
#                     'folderUp' : directory_mc+'_JESup',
#                     'folderDown' : directory_mc+'_JESdo',
#                     # 'AsLnN'      : '1',
                    
#     }

    ### Only total variation for fatjetJES
    # nuisances['fatjet' +js]  = {
    #                 'name': 'CMS_fj_scale_'+js,
    #                     'kind': 'suffix',
    #                     'type': 'shape',
    #                     'mapUp': 'fatjet' + js+'up',
    #                     'mapDown': 'fatjet' + js+'do',
    #                     'cuts': phase_spaces_boost, #because we are vetoing fatjets anyway in resolved category 
    #                     'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
    #                     'folderUp' : directory_mc+'_fatjetJESup',
    #                     'folderDown' : directory_mc+'_fatjetJESdo',
    #                     # 'AsLnN'      : '1',
    # }

# for wjbin in wjets_res_bins:
#     for js in jes_systs:
#         nuisances[js + "_" +wjbin]  = {
#                         'name': 'CMS_j_scale_'+js,
#                         'kind': 'suffix',
#                         'type': 'shape',
#                         'mapUp':   js+'up',
#                         'mapDown': js+'do',
#                         'samples': { wjbin:  ['1.','1.']},
#                         'folderUp' : directory_wjets_res_bins[wjbin]+'_JESup',
#                         'folderDown' : directory_wjets_res_bins[wjbin]+'_JESdo',
#                         'AsLnN'      : '1',               
        # }

##### Jet energy resolution - Irene test
# nuisances['JER'] = {
#                 'name': 'CMS_res_j_2017',
#                 'kind': 'suffix',
#                 'type': 'shape',
#                 'mapUp': 'JERup',
#                 'mapDown': 'JERdo',
#                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
#                 'folderUp' : directory_mc+'_JERup',
#                 'folderDown' : directory_mc+'_JERdo',
#                 # 'AsLnN'      : '1',
# }



# nuisances['fatjetJER']  = {
#                 'name': 'CMS_fatjet_res_2017',
#                 'kind': 'suffix',
#                 'type': 'shape',
#                 'mapUp': 'fatjetJERup',
#                 'mapDown': 'fatjetJERdo',
#                 'cuts': phase_spaces_boost, #because we are vetoing fatjets anyway in resolved category
#                 'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ["Vg","VgS", 'ggWW']),
#                 'folderUp' : directory_mc+'_fatjetJERup',
#                 'folderDown' : directory_mc+'_fatjetJERdo',
#                 # 'AsLnN'      : '1',
# }


# # ##### MET energy scale
nuisances['MET']  = {
                'name'  : 'CMS_scale_met_2017',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp':   'METup',
                'mapDown': 'METdo', 
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', 'ggWW']),
                'folderUp' : directory_mc+'_METup',
                'folderDown' : directory_mc+'_METdo',
                'AsLnN'      : '1',
}

# for wjbin in wjets_res_bins:
#     nuisances['MET_'+wjbin]  = {
#                 'name'  : 'CMS_scale_met_2017',
#                 'kind'  : 'suffix',
#                 'type'  : 'shape',
#                 'mapUp':   'METup',
#                 'mapDown': 'METdo', 
#                 'samples': { wjbin:  ['1.','1.']},
#                 'folderUp' : directory_wjets_res_bins[wjbin]+'_METup',
#                 'folderDown' : directory_wjets_res_bins[wjbin]+'_METdo',
#                 'AsLnN'      : '1',
#     }

##################################
######## Fatjet uncertainties - Irene test

# Wtagging uncertainties enters also resolved region
# fatjet_eff = ['BoostedWtagSF_up/BoostedWtagSF_nominal', 'BoostedWtagSF_down/BoostedWtagSF_nominal']
# nuisances['Wtagging_eff'] = {
#                 'name': 'CMS_fatjet_tau21eff_2017',
#                 'kind' : 'weight', 
#                 'type' : 'shape',
#                 'samples': dict( (skey, fatjet_eff) for skey in mc)
# }

# fatjet_eff_ptextr = ['BoostedWtagSF_ptextr[0]', 'BoostedWtagSF_ptextr[1]']
# nuisances['Wtagging_ptextr'] = {
#                 'name': 'CMS_fj_tau21ptextr_2017',
#                 'kind' : 'weight', 
#                 'type' : 'shape',
#                 'samples': dict( (skey, fatjet_eff_ptextr) for skey in mc)
# }

#FatJet mass scale and resolution
# nuisances['fatjetJMR']  = {
#     'name': 'CMS_fatjet_jmr_2017',
#     'kind': 'suffix',
#     'type': 'shape',
#     'mapUp': 'fatjetJMRup',
#     'mapDown': 'fatjetJMRdo',
#     'cuts': phase_spaces_boost, #because we are vetoing fatjets anyway in resolved category
#     'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ["Vg","VgS", 'ggWW']),
#     'folderUp' : directory_mc+'_fatjetJMRup',
#     'folderDown' : directory_mc+'_fatjetJMRdo',
#     # 'AsLnN'      : '1',

# }

# nuisances['fatjetJMS']  = {
#     'name': 'CMS_fatjet_jms_2017',
#     'kind': 'suffix',
#     'type': 'shape',
#     'mapUp': 'fatjetJMSup',
#     'mapDown': 'fatjetJMSdo',
#     'cuts': phase_spaces_boost, #because we are vetoing fatjets anyway in resolved category
#     'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ["Vg","VgS", 'ggWW']),
#     'folderUp' : directory_mc+'_fatjetJMSup',
#     'folderDown' : directory_mc+'_fatjetJMSdo',
#     # 'AsLnN'      : '1',
# }


## Top pT reweighting uncertainty

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
       'top': [
        'isSingleTop * 1.0816 + isTTbar',
        'isSingleTop * 0.9184 + isTTbar']
      }
}

## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
   'name': 'CMS_topPtRew',   # Theory uncertainty
   'kind': 'weight',
   'type': 'shape',
   'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
   'symmetrize': True
}

###########################################

# for jtype in ["quark", "gluon"]:
#       for  jeta in ["higheta", "loweta"]:
#         nuisances['QGLmorphing_{}_{}'.format(jtype, jeta)]  = {
#             'name': 'QGLmorph_{}_{}_1718'.format(jtype, jeta),
#             'kind': 'suffix',
#             'type': 'shape',
#             'samples': dict((skey, ['1.','1.']) for skey in mc),
#         }


# ######################
# # Theory nuisance


## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
# qcdscale_variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
import json, os

wjets_bins = []
for ir in range(1,22):
    wjets_bins.append("Wjets_res_"+str(ir))
for ir in range(1,8):
    wjets_bins.append("Wjets_boost_"+str(ir))

# VBS_pdf_factors = json.load(open(os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2017v7/conf_fit_v4.3/pdf_normcorr_VBS.json"))
nuis_factors = json.load(open(os.getenv("CMSSW_BASE") + "/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2017v7/conf_fit_v4.5_aQGC/nuisance_incl_norm_factors_2017.json"))

for sample in mc :
    if sample in ["ggWW","VBS","VBS_dipoleRecoil","Wjets_boost"] + wjets_res_bins + VBS_samples + VV_samples + VBS_aQGC_samples: continue
    # irene tring to remove QCD unc for minor bkg
    # if sample in ["ggWW","VBS","VBS_dipoleRecoil","Wjets_boost", "VVV", "VBF-V_dipole", "Vg", "VgS","VBS_dipoleRecoil"] + wjets_res_bins + VBS_samples + VV_samples + VBS_aQGC_samples: continue
    nuisances['QCD_scale_'+sample] = {
        'name'  : 'QCDscale_'+sample,
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
    }

# for sample in VBS_aQGC_samples:
#     nuisances['QCD_scale_EWK_WV'] = {
#             'name'  : 'QCDscale_EWK_WV',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { sample:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
#         }
#works for datacard
nuisances['QCDscale_EWK_WV'] = {
            'name'  : 'QCDscale_EWK_WV',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples': { sample:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for sample in VBS_aQGC_samples}
        }

#Correlate all signal samples
# nuisances['QCD_scale_VBS_WV_accept'] = {
#             'name'  : 'QCDscale_VBS_WV_accept',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             # 'samples'  :  { "VBS": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"],
#             #                 "VBS_dipoleRecoil": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"], }
#             'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in VBS_WV_samples }
#         }

# nuisances['QCD_scale_VBS_ZV_accept'] = {
#             'name'  : 'QCDscale_VBS_ZV_accept',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             # 'samples'  :  { "VBS": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"],
#             #                 "VBS_dipoleRecoil": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"], }
#             'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in VBS_ZV_samples }
#         }

### Adding also normalization effect for ZV component
# nuisances['QCD_scale_VBS_ZV_norm'] = {
#             'name'  : 'QCDscale_VBS_ZV',
#             'kind'  : 'weight',
#             'type'  : 'lnN',
#             # 'samples'  :  { "VBS": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"],
#             #                 "VBS_dipoleRecoil": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"], }
#             'samples': { k: "1.007/0.986" for k in VBS_ZV_samples }
#         }

# irene tring to remove QCD unc for minor bkg
# Adding also the non-normalized 
# nuisances['QCD_scale_VBS_WV_full'] = {
#             'name'  : 'QCDscale_VBS_WV',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VBS_WV_samples }
#         }

# nuisances['QCD_scale_VBS_ZV_full'] = {
#             'name'  : 'QCDscale_VBS_ZV',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VBS_ZV_samples }
#         }

nuisances['QCD_scale_QCD_VV'] = {
            'name'  : 'QCDscale_QCD_VV',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VV_samples }
        }

# nuisances['QCD_scale_QCD_WV_accept'] = {
#             'name'  : 'QCDscale_QCD_WV_accept',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             # 'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VV_WV_samples } --> It was wrong in 4.5.3
#             'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in VV_WV_samples }
#         }

# nuisances['QCD_scale_QCD_WV_full'] = {
#             'name'  : 'QCDscale_QCD_WV',
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VV_WV_samples }
#         }

# nuisances['QCD_scale_QCD_ZV'] = {
#             'name'  : 'QCDscale_QCD_ZV', #==> needs to become QCDscale_QCD_ZV
#             'kind'  : 'weight',
#             'type'  : 'shape',
#             'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VV_ZV_samples }
#         }



nuisances['QCD_scale_Wjets'] = {
            'name'  : 'QCDscale_Wjets',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for sample in wjets_res_bins + ["Wjets_boost"] }
        }


# ### Propagated from 2018 effect, split by sample
samples_PS = ['top','DY','VVV','Vg','VgS','VBF-V_dipole','ggWW'] + wjets_bins + VBS_aQGC_samples + VV_samples #VBS_dipoleRecoil
# irene tring to remove PS unc for minor bkg
# samples_PS = ['top','DY'] + wjets_bins + VBS_aQGC_samples #VBS_dipoleRecoil


for sample in samples_PS:
    nuisances['PS_ISR_'+sample]  = {
                    'name'  : 'CMS_PS_ISR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample : ['PSWeight[2]', 'PSWeight[0]'],
                    },
                    'cuts_samples':{'Vg': [ f for f in phasespaces if "boost_topcr" not in f  ]} # necessary only for postfit in the cr
                }
    nuisances['PS_FSR_'+sample]  = {
                    'name'  : 'CMS_PS_FSR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample :  ['PSWeight[3]', 'PSWeight[1]'],
                    },
                    'cuts_samples':{'Vg': [ f for f in phasespaces if "boost_topcr" not in f  ]}  # necessary only for postfit in the cr
                }



# nuisances['PS_ISR_VBS_WV']  = {
#                     'name'  : 'CMS_PS_ISR_VBS_WV',
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {
#                         sample : ['PSWeight[2]', 'PSWeight[0]'] for sample in VBS_WV_samples
#                     }
#                 }
# nuisances['PS_FSR_VBS_WV']  = {
#                 'name'  : 'CMS_PS_FSR_VBS_WV',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     sample :  ['PSWeight[3]', 'PSWeight[1]'] for sample in VBS_WV_samples
#                 }
#             }

# nuisances['PS_ISR_VBS_ZV']  = {
#                     'name'  : 'CMS_PS_ISR_VBS_ZV',
#                     'kind'  : 'weight',
#                     'type'  : 'shape',
#                     'samples'  : {
#                         sample : ['PSWeight[2]', 'PSWeight[0]'] for sample in VBS_ZV_samples
#                     }
#                 }
# nuisances['PS_FSR_VBS_ZV']  = {
#                 'name'  : 'CMS_PS_FSR_VBS_ZV',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     sample :  ['PSWeight[3]', 'PSWeight[1]'] for sample in VBS_ZV_samples
#                 }
#             }

# When VV is a background all the PS is correlated
# irene tring to remove PS unc for minor bkg
nuisances['PS_ISR_QCD_VV']  = {
                    'name'  : 'CMS_PS_ISR_QCD_VV',
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample : ['PSWeight[2]', 'PSWeight[0]'] for sample in VV_samples
                    }
                }
nuisances['PS_FSR_QCD_VV']  = {
                'name'  : 'CMS_PS_FSR_QCD_VV',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    sample :  ['PSWeight[3]', 'PSWeight[1]'] for sample in VV_samples
                }
            }
##############
### testing for official production!!!
# #
# # PS and UE
# # #
# #### USE this for producing shapes
# nuisances['PS_ISR']  = {
#                 'name'  : 'CMS_PS_ISR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {   
#                     s : ['PSWeight[2] * {}'.format(nuis_factors[s]["PS_ISR"][0]),
#                          'PSWeight[0] * {}'.format(nuis_factors[s]["PS_ISR"][1]) ] for s in signals }
#             }

# nuisances['PS_FSR']  = {
#                 'name'  : 'CMS_PS_FSR',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {   
#                     s : ['PSWeight[3] * {}'.format(nuis_factors[s]["PS_FSR"][0]),
#                          'PSWeight[1] * {}'.format(nuis_factors[s]["PS_FSR"][1]) ] for s in signals}
#             }


##############

nuisances['PU']  = {
                'name'  : 'CMS_PU_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    # s : ['(puWeight_noeras[1]/puWeight_noeras[0]) * {}'.format(nuis_factors[s]["CMS_PU_2017"][0]),
                    #      '(puWeight_noeras[2]/puWeight_noeras[0])* {}'.format(nuis_factors[s]["CMS_PU_2017"][1])] for s in mc },
                    s : ["",""] for s in mc }, # only for dataset and plotting 
                'AsLnN'      : '1',
}

# nuisances['PU_wjets']  = {
#                 'name'  : 'CMS_PU_2017',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'samples'  : {
#                     s : ['(puWeight_noeras[1]/puWeight_noeras[0]) * {}'.format(nuis_factors["Wjets_res"]["CMS_PU_2017"][0]),
#                          '(puWeight_noeras[2]/puWeight_noeras[0]) * {}'.format(nuis_factors["Wjets_res"]["CMS_PU_2017"][1])] for s in wjets_res_bins },
#                 'AsLnN'      : '1',
# }

######## PDF uncertainty
# --> How it was in fit 4.5.3
# nuisances['pdf_weight'] = {
#     'name'  : 'pdf_1718',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["VBS", "VBS_dipoleRecoil", "top"]+wjets_all_bins+VBS_samples},
#     'AsLnN':  '1'
# }

nuisances['pdf_weight'] = { # --> Now save also the normalization one for the signal
    'name'  : 'pdf_1718',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["top","Wjets_boost"]+wjets_res_bins},
    'AsLnN':  '1'
}
# irene tring to remove pdf unc for minor bkg
# nuisances['pdf_weight'] = { # --> Now save also the normalization one for the signal
#     'name'  : 'pdf_1718',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["top","Wjets_boost","VVV", "VBF-V_dipole", "Vg", "VgS","VBS_dipoleRecoil","ggWW"]+wjets_res_bins+VV_samples},
#     'AsLnN':  '1'
# }

# nuisances['pdf_weight_accept'] = {
#     'name'  : 'pdf_1718_accept',
#     'kind'  : 'weight_envelope',
#     'type'  : 'shape',
#     # 'samples' :  { "VBS": [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ],
#     #                "VBS_dipoleRecoil": [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ]}
#     'samples': { k : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] for k in VBS_samples}
# }


# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ["Wjets_boost","top"]+wjets_res_bins), 
}

############################

# nuisances['dipole']  = {
#                 'name'  : 'dipole',
#                 'kind'  : 'weight',
#                 'type'  : 'shape',
#                 'OneSided': True,
#                 'samples'  : { 'VBS': ['dipole_weight']}
# }


###############
# Normalization factors

#############
##Samples normalizations
for fl in ['ele','mu']:
    nuisances['Top_norm_boost_'+fl]  = {
                'name'  : 'CMS_Top_norm_{}_boost_2017'.format(fl),
                'samples'  : {
                    'top' : '1.00',
                    },
                'type'  : 'rateParam',
                'cuts'  : [f for f in phase_spaces_dict["boost"] if fl in f ]
                }

    nuisances['Top_norm_res_'+fl]  = {
                'name'  : 'CMS_Top_norm_{}_res_2017'.format(fl),
                'samples'  : {
                    'top' : '1.00',
                    },
                'type'  : 'rateParam',
                'cuts'  : [f for f in phase_spaces_dict["res"] if fl in f ]
                }


regrouped_Wjets = False
for wjbin in wjets_bins:
    for fl in ["ele", "mu"]:
        if "boost" in wjbin:
            nuisances["{}_norm_{}_boost_2017".format(wjbin, fl)]  = {
                'name'  : 'CMS_{}_norm_{}_boost_2017'.format(wjbin, fl),
                'samples'  : {wjbin: '1.00'},
                'type'  : 'rateParam',
                'cuts'  : [f for f in phase_spaces_dict["boost"] if fl in f ]
            }
            if regrouped_Wjets: 
                nuisances["{}_norm_{}_boost_2017".format(wjbin, fl)]['name'] = 'CMS_Wjets_norm_{}_boost_2017'.format(fl)
        else:
            nuisances["{}_norm_{}_res_2017".format(wjbin, fl)] = {
                'name'  : 'CMS_{}_norm_{}_res_2017'.format(wjbin, fl),
                'samples'  : { wjbin: '1.00' },
                'type'  : 'rateParam',
                'cuts'  : [f for f in phase_spaces_dict["res"] if fl in f]
            }
            if regrouped_Wjets: 
                nuisances["{}_norm_{}_res_2017".format(wjbin, fl)]['name'] = 'CMS_Wjets_norm_{}_res_2017'.format(fl)



# ## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }


for n in nuisances.values():
    n['skipCMS'] = 1

   

# nuisances = {k:v for k,v in nuisances.items() if k in ["JetPUID_sf"] } #if 'PS' in k or 'QCD' in k
################################
## Customizations

# Customization to redo the QCDscales
#nuisances = {k:v for k,v in nuisances.items() if 'QCD_scale' in k or k == "pdf_weight" or 'PS' in k} # or 'QCD' in k
#nuisances = {k:v for k,v in nuisances.items() if 'PS' in k} # or 'QCD' in k
#nuisances = {k:v for k,v in nuisances.items() if 'QCDscale' in k}
# Customization for mu fit with QCDscale normalization included
#exclude = ["QCD_scale_VBS_WV_accept","QCD_scale_VBS_ZV_accept", "QCD_scale_QCD_WV_accept", "pdf_weight_accept"]
#nuisances = {k:v for k,v in nuisances.items() if k not in exclude}

# Customization for mu fit with QCDscale normalization excluded
# exclude = ["QCD_scale_VBS_WV_full","QCD_scale_VBS_ZV_accept", "QCD_scale_QCD_WV_accept", "pdf_weight"]
# nuisances = {k:v for k,v in nuisances.items() if k not in exclude}

nuisances = {k:v for k,v in nuisances.items() if "QGLmorph" not in k}
# print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))
# print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))