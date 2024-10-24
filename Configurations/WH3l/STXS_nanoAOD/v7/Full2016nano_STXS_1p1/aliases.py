import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP = 'mva_90p_Iso2016'
muWP = 'cut_Tight80x'

aliases['WH3l_pTW'] = {
    'expr' : 'Lepton_pt[0]*(WH3l_drOSll[2]==MinIf$(WH3l_drOSll,WH3l_drOSll>0))+Lepton_pt[1]*(WH3l_drOSll[1]==MinIf$(WH3l_drOSll,WH3l_drOSll>0))+Lepton_pt[2]*(WH3l_drOSll[0]==MinIf$(WH3l_drOSll,WH3l_drOSll>0))'
}

aliases['LepWPCut'] = {
    # 'expr': 'LepCut3l__ele_'+eleWP+'__mu_'+muWP,
    'expr': 'LepCut3l__ele_'+eleWP+'__mu_'+muWP+'*(((abs(Lepton_pdgId[0])==13 && Muon_mvaTTH[Lepton_muonIdx[0]]>0.8) || (abs(Lepton_pdgId[0])==11 && Electron_mvaTTH[Lepton_electronIdx[0]]>0.7)) && ((abs(Lepton_pdgId[1])==13 && Muon_mvaTTH[Lepton_muonIdx[1]]>0.8) ||  (abs(Lepton_pdgId[1])==11 && Electron_mvaTTH[Lepton_electronIdx[1]]>0.7)) && ((abs(Lepton_pdgId[2])==13 && Muon_mvaTTH[Lepton_muonIdx[2]]>0.8) || (abs(Lepton_pdgId[2])==11 && Electron_mvaTTH[Lepton_electronIdx[2]]>0.7)))',

    'samples': mc + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

eleFWP = 'mva_90p_Iso2016_tthmva_70'
muFWP = 'cut_Tight80x_tthmva_80'

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}

# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lElUp/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lElDown/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lMuUp/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lMuDown/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lstatElUp/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lstatElDown/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lstatMuUp/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3lstatMuDown/fakeW_ele_'+eleFWP+'_mu_'+muFWP+'_3l',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch3l matches to *any* gen lepton)
aliases['PromptGenLepMatch3l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]*Lepton_promptgenmatched[2], 0)',
    'samples': mc
}

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

# B tagging

aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}
aliases['bVeto'] = {
    'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.6321) == 0'
}

aliases['bReq'] = {
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.6321) >= 1'
}
aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    #'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
    'expr': 'bVeto*bVetoSF',
    'samples': mc
}

for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:


    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'CountGenJet',
    'samples': mc
}


# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF3l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF3l__mu_'+muWP+'__Do',
    'samples': mc
}
aliases['nllWOTF'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/nllW.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'WWNLLW',
    'args': ('central',),
    'samples': ['WW']
}

aliases['ttHMVA_SF_3l'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/patches/compute_SF_BETA.C+' % os.getenv('CMSSW_BASE')],
    'class': 'compute_SF',
    'args' : ('2016', 3, 'total_SF'),
    'samples': mc
}

aliases['ttHMVA_SF_Up_0'] = {
    'class': 'compute_SF',
    'args' : ('2016', 3, 'single_SF_up', 0),
    'nominalOnly' : True,
    'samples': mc
}

aliases['ttHMVA_SF_Up_1'] = {
    'class': 'compute_SF',
    'args' : ('2016', 3, 'single_SF_up', 1),
    'nominalOnly' : True,
    'samples': mc
}

aliases['ttHMVA_SF_Up_2'] = {
    'class': 'compute_SF',
    'args' : ('2016', 3, 'single_SF_up', 2),
    'nominalOnly' : True,
    'samples': mc
}

aliases['ttHMVA_SF_Down_0'] = {
    'class': 'compute_SF',
    'args' : ('2016', 3, 'single_SF_down', 0),
    'nominalOnly' : True,
    'samples': mc
}

aliases['ttHMVA_SF_Down_1'] = {
    'class': 'compute_SF',
    'args' : ('2016', 3, 'single_SF_down', 1),
    'nominalOnly' : True,
    'samples': mc
}

aliases['ttHMVA_SF_Down_2'] = {
    'class': 'compute_SF',
    'args' : ('2016', 3, 'single_SF_down', 2),
    'nominalOnly' : True,
    'samples': mc
}

aliases['ttHMVA_3l_ele_SF_Up'] = {
    'expr' : '(ttHMVA_SF_Up_0[0]*(abs(Lepton_pdgId[0]) == 11) + (abs(Lepton_pdgId[0]) == 13)) *\
              (ttHMVA_SF_Up_1[0]*(abs(Lepton_pdgId[1]) == 11) + (abs(Lepton_pdgId[1]) == 13)) *\
              (ttHMVA_SF_Up_2[0]*(abs(Lepton_pdgId[2]) == 11) + (abs(Lepton_pdgId[2]) == 13))',
    'nominalOnly' : True,
    'samples' : mc
}

aliases['ttHMVA_3l_ele_SF_Down'] = {
    'expr' : '(ttHMVA_SF_Down_0[0]*(abs(Lepton_pdgId[0]) == 11) + (abs(Lepton_pdgId[0]) == 13)) *\
              (ttHMVA_SF_Down_1[0]*(abs(Lepton_pdgId[1]) == 11) + (abs(Lepton_pdgId[1]) == 13)) *\
              (ttHMVA_SF_Down_2[0]*(abs(Lepton_pdgId[2]) == 11) + (abs(Lepton_pdgId[2]) == 13))',
    'nominalOnly' : True,
    'samples' : mc
}

aliases['ttHMVA_3l_mu_SF_Up'] = {
    'expr' : '(ttHMVA_SF_Up_0[0]*(abs(Lepton_pdgId[0]) == 13) + (abs(Lepton_pdgId[0]) == 11)) *\
              (ttHMVA_SF_Up_1[0]*(abs(Lepton_pdgId[1]) == 13) + (abs(Lepton_pdgId[1]) == 11)) *\
              (ttHMVA_SF_Up_2[0]*(abs(Lepton_pdgId[2]) == 13) + (abs(Lepton_pdgId[2]) == 11))',
    'nominalOnly' : True,
    'samples' : mc
}

aliases['ttHMVA_3l_mu_SF_Down'] = {
    'expr' : '(ttHMVA_SF_Down_0[0]*(abs(Lepton_pdgId[0]) == 13) + (abs(Lepton_pdgId[0]) == 11)) *\
              (ttHMVA_SF_Down_1[0]*(abs(Lepton_pdgId[1]) == 13) + (abs(Lepton_pdgId[1]) == 11)) *\
              (ttHMVA_SF_Down_2[0]*(abs(Lepton_pdgId[2]) == 13) + (abs(Lepton_pdgId[2]) == 11))',
    'nominalOnly' : True,
    'samples' : mc
}


# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight3l', 'ttHMVA_SF_3l', 'LepWPCut', 'btagSF', 'PrefireWeight']),
    'samples': mc
}


aliases['WH3l_dphilllmet_test'] = {
    'linesToAdd': [
        '.L %s/src/PlotsConfigurations/Configurations/WH3l/scripts/WH3l_patch_BDT1718.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'WH3l_patch_BDT1718',
    'args': ("dphilllmet")
}

aliases['WH3l_mOSll_min_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("mOSllmin")
}

aliases['WH3l_ptOSll_min_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("ptOSllmin")
}

aliases['WH3l_drOSll_min_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("drOSllmin")
}

aliases['WH3l_ZVeto_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("ZVeto")
}

aliases['WH3l_ptlll_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("ptlll")
}

aliases['WH3l_mtlmet0_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("mtlmet0")
}

aliases['WH3l_mtlmet1_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("mtlmet1")
}

aliases['WH3l_mtlmet2_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("mtlmet2")
}

aliases['WH3l_dphilmet0_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("dphilmet0")
}

aliases['WH3l_dphilmet1_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("dphilmet1")
}

aliases['WH3l_dphilmet2_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("dphilmet2")
}

aliases['WH3l_ptWWW_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("ptWWW")
}

aliases['WH3l_mtWWW_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("mtWWW")
}

aliases['WH3l_mlll_test'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("mlll")
}

aliases['BDT_SSSF2016'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016")
}
aliases['BDT_SSSF2016_v1'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016_v1")
}
aliases['BDT_SSSF2016_v2'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016_v2")
}
aliases['BDT_SSSF2016_v3'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016_v3")
}
aliases['BDT_SSSF2016_v4'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016_v4")
}
aliases['BDT_SSSF2016_v5'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016_v5")
}
aliases['BDT_SSSF2016_v6'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016_v6")
}
aliases['BDT_SSSF2016_v7'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_SSSF2016_v7")
}
#aliases['BDT_SSSFcombin'] = {
#    'class': 'WH3l_patch_BDT1718',
#    'args': ("BDT_SSSFcombin")
#}
aliases['BDT_OSSF2016'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016")
}
aliases['BDT_OSSF2016_v1'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v1")
}
aliases['BDT_OSSF2016_v2'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v2")
}
aliases['BDT_OSSF2016_v3'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v3")
}
aliases['BDT_OSSF2016_v4'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v4")
}
aliases['BDT_OSSF2016_v5'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v5")
}
aliases['BDT_OSSF2016_v6'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v6")
}
aliases['BDT_OSSF2016_v7'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v7")
}
aliases['BDT_OSSF2016_v8'] = {
    'class': 'WH3l_patch_BDT1718',
    'args': ("BDT_OSSF2016_v8")
}
#aliases['BDT_OSSFcombin'] = {
#    'class': 'WH3l_patch_BDT1718',
#    'args': ("BDT_OSSFcombin")
#}
