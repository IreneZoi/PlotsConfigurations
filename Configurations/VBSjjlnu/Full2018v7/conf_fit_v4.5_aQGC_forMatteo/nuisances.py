from pprint import pprint
# # # name of samples here must match keys in samples.py 

mc =["DY", "top", "VV", "VVV", "VBF-V", "VBF-V_dipole", "Vg", "VgS", "VBS", "ggWW","VBS_dipoleRecoil"] + wjets_all_bins + VBS_samples + VV_samples + VBS_aQGC_samples



def getSamplesWithout(samples, samples_to_remove):
    return [m for m in samples if m not in samples_to_remove]



# # ################################ EXPERIMENTAL UNCERTAINTIES  #################################

# # #### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['top']+wjets_all_bins)
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['top']+wjets_all_bins)
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['top']+wjets_all_bins)
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['top']+wjets_all_bins)
}


##########Fakes
fakeW_jetUp       = '( fakeWeight_45 / fakeWeight_35  )'
fakeW_jetDown     =  '( fakeWeight_25 / fakeWeight_35  )'
fakeW_statUp        =  '( fakeWeight_35_statUp / fakeWeight_35  )'
fakeW_statDown      =  '( fakeWeight_35_statDo / fakeWeight_35  )'

nuisances['fake_syst']  = {
               'name'  : 'CMS_fake_syst_em',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
               }


nuisances['fake_emu']  = {
                'name'  : 'CMS_fake_emu_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_jetUp , fakeW_jetDown ],
                             },
}

nuisances['fake_emu_stat']  = {
                'name'  : 'CMS_fake_emu_stat_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statUp , fakeW_statDown ],
                             },
}



# ##### Btag nuisances

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

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
                'name'  : 'CMS_eff_trigger_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples' :  dict((skey, trig_syst) for skey in mc)
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
                'name'  : 'CMS_eff_e_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :   dict((skey, id_syst_ele) for skey in mc ),
}

nuisances['electronpt']  = {
                'name'  : 'CMS_scale_e_2018',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'ElepTup',
                'mapDown': 'ElepTdo',
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]+ wjets_all_bins),
                'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_ElepTup',
                'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_ElepTdo',
}


for wjbin in wjets_all_bins:
    nuisances['electronpt_'+wjbin]  = {
                    'name'  : 'CMS_scale_e_2018',
                    'kind'  : 'suffix',
                    'type'  : 'shape',
                    'mapUp': 'ElepTup',
                    'mapDown': 'ElepTdo',
                    'samples':{ wjbin:  ['1.','1.']},
                    'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbin]+'_ElepTup',
                    'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbin]+'_ElepTdo',
    }


# # ##### Muon Efficiency and energy scale


nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc ),
}

nuisances['muonpt']  = {
                'name'  : 'CMS_scale_m_2018',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'MupTup',
                'mapDown': 'MupTdo',
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]+wjets_all_bins),
                'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_MupTup',
                'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_MupTdo',
}

for wjbin in wjets_all_bins:
    nuisances['muonpt_'+wjbin]  = {
                'name'  : 'CMS_scale_m_2018',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp': 'MupTup',
                'mapDown': 'MupTdo',
                'samples': { wjbin:  ['1.','1.']},
                'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbin]+'_MupTup',
                'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbin]+'_MupTdo',
}

##################
# PU jet id

nuisances['JetPUID_sf']  = {
                'name'  : 'CMS_jetpuid_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc ),
}


# ##### Jet energy scale

##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2',
            'JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal',
            'JESRelativeSample_2018']

for js in jes_systs:
    nuisances[js]  = {
                    'name': 'CMS_j_scale_'+js,
                    'kind': 'suffix',
                    'type': 'shape',
                    'mapUp': js+'up',
                    'mapDown': js+'do',
                    'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]+wjets_all_bins),
                    'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_JESup',
                    'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_JESdo',
                    'AsLnN'      : '1',
                    
    }

    ### Only total variation for fatjetJES
    nuisances['fatjet' +js]  = {
                    'name': 'CMS_fj_scale_'+js,
                        'kind': 'suffix',
                        'type': 'shape',
                        'mapUp': 'fatjet' + js+'up',
                        'mapDown': 'fatjet' + js+'do',
                        'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]+wjets_all_bins),
                        'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJESup',
                        'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJESdo',
                        'AsLnN'      : '1',
    }


##### Jet energy resolution
nuisances['JER'] = {
                'name': 'CMS_res_j_2018',
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': 'JERup',
                'mapDown': 'JERdo',
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]+wjets_all_bins),
                'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_JERup',
                'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_JERdo',
                'AsLnN'      : '1',
}

nuisances['fatjetJER'] = {
                'name': 'CMS_fatjet_res_2018',
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': 'fatjetJERup',
                'mapDown': 'fatjetJERdo',
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ["Vg","VgS", "ggWW"]+wjets_all_bins),
                'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJERup',
                'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJERdo',
                'AsLnN'      : '1',
}

######################
for wjbinres in wjets_res_bins:
    for js in jes_systs:\
        # Only ak4 jets for resolved bins
        nuisances[js+"_"+wjbinres]  = {
                        'name': 'CMS_j_scale_'+js,
                        'kind': 'suffix',
                        'type': 'shape',
                        'mapUp': js+'up',
                        'mapDown': js+'do',
                        'samples': { wjbinres:  ['1.','1.']},
                        'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinres]+'_JESup',
                        'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinres]+'_JESdo',
                        'AsLnN'      : '1',          
        }
    nuisances['JER_'+wjbinres] = {
            'name': 'CMS_res_j_2018',
            'kind': 'suffix',
            'type': 'shape',
            'mapUp': 'JERup',
            'mapDown': 'JERdo',
            'samples': { wjbinres:  ['1.','1.']},
            'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinres]+'_JERup',
            'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinres]+'_JERdo',
            'AsLnN'      : '1',
    }

############################3
#### Boosted bins
for wjbinboost in wjets_boost_bins:
    for js in jes_systs:
        nuisances[js+"_"+wjbinboost]  = {
                        'name': 'CMS_j_scale_'+js,
                        'kind': 'suffix',
                        'type': 'shape',
                        'mapUp': js+'up',
                        'mapDown': js+'do',
                        'samples': { wjbinboost:  ['1.','1.']},
                        'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_JESup',
                        'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_JESdo',
                        'AsLnN'      : '1',
                        
        }
        ### Only total variation for fatjetJES
        nuisances['fatjet' +js +"_"+wjbinboost ]  = {
                        'name': 'CMS_fj_scale_'+js,
                            'kind': 'suffix',
                            'type': 'shape',
                            'mapUp': 'fatjet' + js+'up',
                            'mapDown': 'fatjet' + js+'do',
                            'samples': { wjbinboost:  ['1.','1.']},
                            'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJESup',
                            'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJESdo',
                            'AsLnN'      : '1',
        }
    nuisances['JER_'+wjbinboost] = {
            'name': 'CMS_res_j_2018',
            'kind': 'suffix',
            'type': 'shape',
            'mapUp': 'JERup',
            'mapDown': 'JERdo',
            'samples': { wjbinboost:  ['1.','1.']},
            'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_JERup',
            'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_JERdo',
            'AsLnN'      : '1',
    }   
    nuisances['fatjetJER_'+wjbinboost] = {
            'name': 'CMS_fatjet_res_2018',
            'kind': 'suffix',
            'type': 'shape',
            'mapUp': 'fatjetJERup',
            'mapDown': 'fatjetJERdo',
            'samples': { wjbinboost:  ['1.','1.']},
            'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJERup',
            'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJERdo',
            'AsLnN'      : '1',
    }

# # ##### MET energy scale
nuisances['MET']  = {
                'name'  : 'CMS_scale_met_2018',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp':   'METup',
                'mapDown': 'METdo', 
                'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ['Vg', 'VgS', "ggWW"]+wjets_all_bins),
                'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_METup',
                'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_METdo',
                'AsLnN'      : '1',
}

for wjbin in wjets_all_bins:
    nuisances['MET_'+wjbin]  = {
                'name'  : 'CMS_scale_met_2018',
                'kind'  : 'suffix',
                'type'  : 'shape',
                'mapUp':   'METup',
                'mapDown': 'METdo', 
                'samples': { wjbin:  ['1.','1.']},
                'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbin]+'_METup',
                'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbin]+'_METdo',
                'AsLnN'      : '1',
    }

##################################
######## Fatjet uncertainties

# Wtagging uncertainties enters also resolved region
fatjet_eff = ['BoostedWtagSF_up/BoostedWtagSF_nominal', 'BoostedWtagSF_down/BoostedWtagSF_nominal']
nuisances['Wtagging_eff'] = {
                'name': 'CMS_fatjet_tau21eff_2018',
                'kind' : 'weight', 
                'type' : 'shape',
                'samples': dict( (skey, fatjet_eff) for skey in mc)
}

fatjet_eff_ptextr = ['BoostedWtagSF_ptextr[0]', 'BoostedWtagSF_ptextr[1]']
nuisances['Wtagging_ptextr'] = {
                'name': 'CMS_fj_tau21ptextr_2018',
                'kind' : 'weight', 
                'type' : 'shape',
                'samples': dict( (skey, fatjet_eff_ptextr) for skey in mc)
}

#FatJet mass scale and resolution
nuisances['fatjetJMR']  = {
    'name': 'CMS_fatjet_jmr_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'fatjetJMRup',
    'mapDown': 'fatjetJMRdo',
    'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ["Vg","VgS", "ggWW"]+wjets_all_bins),
    'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJMRup',
    'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJMRdo',
    'AsLnN'      : '1',

}

nuisances['fatjetJMS']  = {
    'name': 'CMS_fatjet_jms_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'fatjetJMSup',
    'mapDown': 'fatjetJMSdo',
    'samples': dict((skey, ['1.','1.']) for skey in mc if skey not in ["Vg","VgS", "VV", "ggWW"]+wjets_all_bins + VV_samples),
    'folderUp' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJMSup',
    'folderDown' : 'root://eoscms.cern.ch/'+directory_mc+'_fatjetJMSdo',
    'AsLnN'      : '1',
}

for wjbinboost in wjets_boost_bins:
    #FatJet mass scale and resolution
    nuisances['fatjetJMR_'+wjbinboost]  = {
        'name': 'CMS_fatjet_jmr_2018',
        'kind': 'suffix',
        'type': 'shape',
        'mapUp': 'fatjetJMRup',
        'mapDown': 'fatjetJMRdo',
        'samples': { wjbinboost:  ['1.','1.']},
        'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJMRup',
        'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJMRdo',
        'AsLnN'      : '1',
    }
    nuisances['fatjetJMS_'+wjbinboost]  = {
        'name': 'CMS_fatjet_jms_2018',
        'kind': 'suffix',
        'type': 'shape',
        'mapUp': 'fatjetJMSup',
        'mapDown': 'fatjetJMSdo',
        'samples': { wjbinboost:  ['1.','1.']},
        'folderUp' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJMSup',
        'folderDown' : 'root://eoscms.cern.ch/'+directory_wjets_bins[wjbinboost]+'_fatjetJMSdo',
        'AsLnN'      : '1',
    }

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


# ######################
# # Theory nuisance


#import json, os
#VBS_pdf_factors = json.load(open("/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4" + "/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2018v7/conf_fit_v4.3/pdf_normcorr_VBS.json"))
#nuis_factors = json.load(open("/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4" + "/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2018v7/conf_fit_v4.5_aQGC/nuisance_incl_norm_factors_2018.json"))

for sample in mc :
    if sample in ["ggWW"] + wjets_all_bins +  VV_samples: continue
    nuisances['QCD_scale_'+sample] = {
        'name'  : 'QCDscale_'+sample,
        'kind'  : 'weight',
        'type'  : 'shape',
        'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
    }


nuisances['QCD_scale_VV'] = {
            'name'  : 'QCDscale_VV',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in VV_samples }
        }

nuisances['QCD_scale_Wjets'] = {
            'name'  : 'QCDscale_Wjets',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for sample in wjets_all_bins }
        }


# #
# # PS and UE
# # #
# #### USE this for producing shapes
nuisances['PS_ISR']  = {
                'name'  : 'CMS_PS_ISR',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :    dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc ),
            }
nuisances['PS_FSR']  = {
                'name'  : 'CMS_PS_FSR',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  :  dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc ),
            }


##############

nuisances['PU_wjets']  = {
                'name'  : 'CMS_PU_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    s : ['(puWeightUp/puWeight)',
                         '(puWeightDown/puWeight)'] for s in mc},
                'AsLnN'      : '1',
}

######## PDF uncertainty
nuisances['pdf_weight'] = {
    'name'  : 'pdf_1718',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["VBS", "top"]+wjets_all_bins+VBS_samples},
    'AsLnN':  '1'
}


# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ["top"]+wjets_all_bins), 
}


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
