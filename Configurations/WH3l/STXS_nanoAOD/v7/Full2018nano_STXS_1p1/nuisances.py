# nuisances
# name of samples here must match keys in samples.py 
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()



################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity
#### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['Zg','ZgS','WZ'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['Zg','ZgS','WZ'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['Zg','ZgS','WZ'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['Zg','ZgS','WZ'])
}

### FAKES
nuisances['fake_syst']  = {
               'name'  : 'CMS_fake_syst',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake' : '1.30',
                             },
               }

nuisances['fake_ele']  = {
                'name'  : 'CMS_fake_e_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                            'Fake': ['fakeWEleUp', 'fakeWEleDown'],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_stat_e_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                            'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'CMS_fake_m_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                            'Fake': ['fakeWMuUp', 'fakeWMuDown'],
                             },
}

nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_stat_m_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                            'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
                             },
}


##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency


trig_syst = ['((TriggerEffWeight_3l_u)/(TriggerEffWeight_3l))*(TriggerEffWeight_3l>0.02) + (TriggerEffWeight_3l<=0.02)', '(TriggerEffWeight_3l_d)/(TriggerEffWeight_3l)']

nuisances['trigg']  = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

id_syst_ele = [ 'ttHMVA_3l_ele_SF_Up', 'ttHMVA_3l_ele_SF_Down']

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples'  : dict((skey, id_syst_ele) for skey in mc),
    # 'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}

##### Muon Efficiency and energy scale

id_syst_mu = [ 'ttHMVA_3l_mu_SF_Up', 'ttHMVA_3l_mu_SF_Down']

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples'  : dict((skey, id_syst_mu) for skey in mc),
    # 'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']
folderup = ""
folderdo = ""

for js in jes_systs:
  if 'Absolute' in js:
    folderup = makeMCDirectory('JESAbsoluteup_suffix')
    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
  elif 'BBEC1' in js:
    folderup = makeMCDirectory('JESBBEC1up_suffix')
    folderdo = makeMCDirectory('JESBBEC1do_suffix')
  elif 'EC2' in js:
    folderup = makeMCDirectory('JESEC2up_suffix')
    folderdo = makeMCDirectory('JESEC2do_suffix')
  elif 'HF' in js:
    folderup = makeMCDirectory('JESHFup_suffix')
    folderdo = makeMCDirectory('JESHFdo_suffix')
  elif 'Relative' in js:
    folderup = makeMCDirectory('JESRelativeup_suffix')
    folderdo = makeMCDirectory('JESRelativedo_suffix')
  elif 'FlavorQCD' in js:
    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')

  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc),
      'folderUp': folderup,
      'folderDown': folderdo,
      'AsLnN': '1'
  }
# for js in jes_systs:
  # nuisances[js] = {
      # 'name': 'CMS_scale_'+js,
      # 'kind': 'suffix',
      # 'type': 'shape',
      # 'mapUp': js+'up',
      # 'mapDown': js+'do',
      # 'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['VZ','Vg','VgS']),
      # 'folderUp': makeMCDirectory('JESup_suffix'),
      # 'folderDown': makeMCDirectory('JESdo_suffix'),
      # 'AsLnN': '1'
  # }

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}


# nuisances['PS_whss']  = {
                # 'name'  : 'PS_whss',
                # 'skipCMS' : 1,
                # 'type'  : 'lnN',
                # 'samples': dict((skey, '1.037') for skey in mc),
# }

nuisances['PS_ISR'] = {
              'name': 'PS_ISR',
              'kind': 'weight',
              'type': 'shape',
              'samples': {
#                   'ggZH_hww': ['1.066107*(nCleanGenJet==0) + 1.047857*(nCleanGenJet==1) + 1.030005*(nCleanGenJet==2) + 1.005028*(nCleanGenJet>=3)', '0.921874*(nCleanGenJet==0) + 0.941939*(nCleanGenJet==1) + 0.962282*(nCleanGenJet==2) + 0.991580*(nCleanGenJet>=3)'],
#                   'ZH_hww': ['1.000684*(nCleanGenJet==0) + 1.000924*(nCleanGenJet==1) + 1.001683*(nCleanGenJet==2) + 1.002104*(nCleanGenJet>=3)', '0.999150*(nCleanGenJet==0) + 0.998821*(nCleanGenJet==1) + 0.997859*(nCleanGenJet==2) + 0.997316*(nCleanGenJet>=3)'],
                   'WZ': ['1.002552*(nCleanGenJet==0) + 1.010286*(nCleanGenJet==1) + 1.014420*(nCleanGenJet==2) + 1.006226*(nCleanGenJet>=3)', '0.996802*(nCleanGenJet==0) + 0.987227*(nCleanGenJet==1) + 0.982005*(nCleanGenJet==2) + 0.992030*(nCleanGenJet>=3)'],
                   'ZZ': ['1.003210*(nCleanGenJet==0) + 1.005480*(nCleanGenJet==1) + 1.004674*(nCleanGenJet==2) + 0.987845*(nCleanGenJet>=3)', '0.995997*(nCleanGenJet==0) + 0.993056*(nCleanGenJet==1) + 0.993659*(nCleanGenJet==2) + 1.014695*(nCleanGenJet>=3)'],
                   },
}

nuisances['PS_FSR'] = {
             'name': 'PS_FSR',
             'kind': 'weight',
             'type': 'shape',
             'samples': {
#                 'ggZH_hww': ['0.987316*(nCleanGenJet==0) + 0.986764*(nCleanGenJet==1) + 0.996498*(nCleanGenJet==2) + 1.004161*(nCleanGenJet>=3)', '1.019871*(nCleanGenJet==0) + 1.013853*(nCleanGenJet==1) + 1.005229*(nCleanGenJet==2) + 0.998573*(nCleanGenJet>=3)'],
#                 'ZH_hww': ['0.992867*(nCleanGenJet==0) + 0.992845*(nCleanGenJet==1) + 0.999470*(nCleanGenJet==2) + 1.007245*(nCleanGenJet>=3)', '1.012465*(nCleanGenJet==0) + 1.012743*(nCleanGenJet==1) + 1.003215*(nCleanGenJet==2) + 0.991286*(nCleanGenJet>=3)'],
                 'WZ': ['0.992987*(nCleanGenJet==0) + 0.993725*(nCleanGenJet==1) + 1.000617*(nCleanGenJet==2) + 1.010869*(nCleanGenJet>=3)', '1.011267*(nCleanGenJet==0) + 1.010097*(nCleanGenJet==1) + 0.999445*(nCleanGenJet==2) + 0.983609*(nCleanGenJet>=3)'],
                 'ZZ': ['0.997245*(nCleanGenJet==0) + 0.998689*(nCleanGenJet==1) + 1.004475*(nCleanGenJet==2) + 1.011440*(nCleanGenJet>=3)', '1.004482*(nCleanGenJet==0) + 1.002081*(nCleanGenJet==1) + 0.992617*(nCleanGenJet==2) + 0.981314*(nCleanGenJet>=3)'],
             },
}


nuisances['UE_CP5']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples': dict((skey, '1.010') for skey in mc if skey not in ['WH_hww','ZH_hww','ggZH_hww','WH_htt','ZH_htt']),
}

###### pdf uncertainties

valuesggh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','pdf','sm')
valuesggzh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm')
valuesbbh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH','125.09','pdf','sm')

nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        'ggH_hww': valuesggh,
        'ggH_htt': valuesggh,
        #'ggZH_hww': valuesggzh,
        'bbH_hww': valuesbbh
    },
    'type': 'lnN',
}

#values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')

#nuisances['pdf_Higgs_ttH'] = {
#    'name': 'pdf_Higgs_ttH',
#    'samples': {
#        'ttH_hww': values
#    },
#    'type': 'lnN',
#}

valuesqqh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm')
valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','pdf','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','pdf','sm')

nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        'qqH_hww': valuesqqh,
        'qqH_htt': valuesqqh,
        #'WH_hww': valueswh,
        #'WH_htt': valueswh,
        #'ZH_hww': valueszh,
        #'ZH_htt': valueszh
    },
}

nuisances['pdf_qqbar'] = {
    'name': 'pdf_qqbar',
    'type': 'lnN',
    'samples': {
        'Wg': '1.04',
        'Zg': '1.04',
        'ZZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'WZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'WgS': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
        'ZgS': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
    },
}

nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        'ggH_hww': '1.006',
        'ggH_htt': '1.006',
        #'ggZH_hww': '1.006',
        'bbH_hww': '1.006'
    },
    'type': 'lnN',
}
nuisances['pdf_gg_ACCEPT'] = {
    'name': 'pdf_gg_ACCEPT',
    'samples': {
        'ggWW': '1.006',
    },
    'type': 'lnN',
}

nuisances['pdf_Higgs_qqbar_ACCEPT'] = {
    'name': 'pdf_Higgs_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_hww': '1.002',
        'qqH_htt': '1.002',
        #'WH_hww': '1.003',
        #'WH_htt': '1.003',
        #'ZH_hww': '1.002',
        #'ZH_htt': '1.002',
    },
}

nuisances['pdf_qqbar_ACCEPT'] = {
    'name': 'pdf_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'ZZ': '1.001',
        'WZ': '1.001',
    },
}

##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

nuisances['QCDscale_V'] = {
    'name': 'QCDscale_V',
    'skipCMS': 1,
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {'DY': variations},
    'AsLnN': '1'
}

nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'WW':variations,
        'Zg': variations,
        'Wg': variations,
        'ZZ': variations,
        'WZ': variations,
        'WgS': variations,
        'ZgS': variations
    }
}

nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    },
}

#### QCD scale uncertainties for Higgs signals other than ggH

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm')

nuisances['QCDscale_qqH'] = {
    'name': 'QCDscale_qqH',
    'samples': {
        'qqH_hww': values,
        'qqH_htt': values
    },
    'type': 'lnN'
}

#valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm')
#valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm')

#nuisances['QCDscale_VH'] = {
#    'name': 'QCDscale_VH',
#    'samples': {
#        'WH_hww': valueswh,
#        'WH_htt': valueswh,
#        'ZH_hww': valueszh,
#        'ZH_htt': valueszh
#    },
#    'type': 'lnN',
#}

#values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm')

#nuisances['QCDscale_ggZH'] = {
#    'name': 'QCDscale_ggZH',
#    'samples': {
#        'ggZH_hww': values
#    },
#    'type': 'lnN',
#}

#values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm')

#nuisances['QCDscale_ttH'] = {
#    'name': 'QCDscale_ttH',
#    'samples': {
#        'ttH_hww': values
#    },
#    'type': 'lnN',
#}

nuisances['QCDscale_WWewk'] = {
    'name': 'QCDscale_WWewk',
    'samples': {
        'WWewk': '1.11',
    },
    'type': 'lnN'
}

nuisances['QCDscale_qqbar_ACCEPT'] = {
    'name': 'QCDscale_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'qqH_hww': '1.003',
        'qqH_htt': '1.003',
        #'WH_hww': '1.010',
        #'WH_htt': '1.010',
        #'ZH_hww': '1.015',
        #'ZH_htt': '1.015',
    }
}

#FIXME: these come from HIG-16-042, maybe should be recomputed?
nuisances['QCDscale_gg_ACCEPT'] = {
    'name': 'QCDscale_gg_ACCEPT',
    'samples': {
        'ggH_htt': '1.012',
        'ggH_hww': '1.012',
        #'ggZH_hww': '1.012',
        'ggWW': '1.012',
    },
    'type': 'lnN',
}

###### pdf uncertainties

# nuisances['pdf_Higgs_qqbar_wh3l']  = {
               # 'name'  : 'pdf_Higgs_qqbar',
               # 'type'  : 'lnN',
               # 'samples'  : {
                   # 'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   # 'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   # },
              # }


# nuisances['pdf_Higgs_qqbar_ACCEPT_wh3l']  = {
               # 'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               # 'type'  : 'lnN',
               # 'samples'  : {
                   # #
                   # 'WH_htt'  : '1.007',
                   # 'WH_hww'  : '1.007',
                   # 'WZ'      : '1.005'
                   # },
              # }

##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)
# [0] is muR=0.50000E+00 muF=0.50000E+00
# [8] is muR=0.20000E+01 muF=0.20000E+01

# nuisances['QCDscale_VH']  = {
               # 'name'  : 'QCDscale_VH',
               # 'samples'  : {
                   # 'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   # 'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
                   # },
               # 'type'  : 'lnN',
              # }


# nuisances['QCDscale_qqbar_ACCEPT']  = {
               # 'name'  : 'QCDscale_qqbar_ACCEPT',
               # 'type'  : 'lnN',
               # 'samples'  : {
                   # 'WH_htt'  : '1.05',
                   # 'WH_hww'  : '1.05',
                   # 'WZ'      : '1.029'
                   # },
              # }

### QCD STXS accept                                                                                                                           

STXS_QCDUnc = {
    'VH_scale_0jet'           : ['QQ2HQQ_0J'], 
    'VH_scale_1jet'           : ['QQ2HQQ_1J'],
    'VH_scale_lowmjj'         : ['QQ2HQQ_GE2J_MJJ_0_60', 'QQ2HQQ_GE2J_MJJ_60_120', 'QQ2HQQ_GE2J_MJJ_120_350'],
    'VH_scale_highmjj_lowpt'  : ['QQ2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25', 'QQ2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25', 'QQ2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25', 'QQ2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    'VH_scale_highmjj_highpt' : ['QQ2HQQ_GE2J_MJJ_GT350_PTH_GT200'],
    'WH_scale_lowpt'          : ['QQ2HLNU_PTV_0_75', 'QQ2HLNU_PTV_75_150', 'QQ2HLNU_PTV_150_250_0J', 'QQ2HLNU_PTV_150_250_GE1J'],
    'WH_scale_highpt'         : ['QQ2HLNU_PTV_GT250'],
    'ZH_scale_lowpt'          : ['QQ2HLL_PTV_0_75', 'QQ2HLL_PTV_75_150', 'QQ2HLL_PTV_150_250_0J', 'QQ2HLL_PTV_150_250_GE1J', 'GG2HLL_PTV_0_75', 'GG2HLL_PTV_75_150', 'GG2HLL_PTV_150_250_0J', 'GG2HLL_PTV_150_250_GE1J'],
    'ZH_scale_highpt'         : ['QQ2HLL_PTV_GT250', 'GG2HLL_PTV_GT250']
}

# Norm factors -- note norm factors in QCDScaleFactors are [LHEScaleWeight[0]/nom, LHEScaleWeight[8]/nom]
if os.path.exists('%s/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/QCDScaleFactors.py'%os.getenv('CMSSW_BASE')) :
  handle = open('%s/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/QCDScaleFactors.py'%os.getenv('CMSSW_BASE'),'r')
  exec(handle)
  handle.close()

for unc in STXS_QCDUnc.keys():
    nuisances[unc] = {
        'name' : unc,
        'kind' : 'weight',
        'type' : 'shape'
        'samples' : {}
    }

    for signal in QCDScaleFactors:
        bins_applied = list(set(QCDScaleFactors[signal].keys()),set(STXS_QCDUnc[unc]))
        if len(bins_applied) > 0:
            norm_QCD = ['+'.join(['(HTXS_stage1_2_cat_pTjet30GeV == {})*({})'.format(HTXSStage1_2Categories[binname],QCDScaleFactors[signal][binname][0])]) for binname in bins_applied]),
                        '+'.join(['(HTXS_stage1_2_cat_pTjet30GeV == {})*({})'.format(HTXSStage1_2Categories[binname],QCDScaleFactors[signal][binname][1])]) for binname in bins_applied])]
            nuisances[unc]['samples'][signal] = ['Alt$(LHEScaleWeight[0],1)/('+norm_QCD[0]+')','Alt$(LHEScaleWeight[8],1)/('+norm_QCD[1]+')']

#STXS VHlep migration uncertainties
STXS_migUnc = {
    'THU_WH_inc'      : {'PTV_0_75' : '0.993/1.005', 'PTV_75_150' : '0.993/1.005', 'PTV_150_250_0J' : '0.993/1.005', 'PTV_150_250_GE1J' : '0.993/1.005', 'PTV_GT250' : '0.993/1.005'},
    'THU_WH_mig75'    : {'PTV_0_75' : '0.965',       'PTV_75_150' : '1.039',       'PTV_150_250_0J' : '1.039',       'PTV_150_250_GE1J' : '1.039',       'PTV_GT250' : '1.039'},
    'THU_WH_mig150'   : {                            'PTV_75_150' : '0.995',       'PTV_150_250_0J' : '1.013',       'PTV_150_250_GE1J' : '1.013',       'PTV_GT250' : '1.013'},
    'THU_WH_mig250'   : {                                                          'PTV_150_250_0J' : '0.9958',      'PTV_150_250_GE1J' : '0.9958',      'PTV_GT250' : '1.014'},
    'THU_WH_mig01'    : {                                                          'PTV_150_250_0J' : '0.961',       'PTV_150_250_GE1J' : '1.050'},
    'THU_ZH_inc'      : {'PTV_0_75' : '0.994/1.005', 'PTV_75_150' : '0.994/1.005', 'PTV_150_250_0J' : '0.994/1.005', 'PTV_150_250_GE1J' : '0.994/1.005', 'PTV_GT250' : '0.994/1.005'},
    'THU_ZH_mig75'    : {'PTV_0_75' : '0.963',       'PTV_75_150' : '1.040',       'PTV_150_250_0J' : '1.04',        'PTV_150_250_GE1J' : '1.04',        'PTV_GT250' : '1.04'},
    'THU_ZH_mig150'   : {                            'PTV_75_150' : '0.995',       'PTV_150_250_0J' : '1.013',       'PTV_150_250_GE1J' : '1.013',       'PTV_GT250' : '1.013'},
    'THU_ZH_mig250'   : {                                                          'PTV_150_250_0J' : '1.9958',      'PTV_150_250_GE1J' : '0.9958',      'PTV_GT250' : '1.014'},
    'THU_ZH_mig01'    : {                                                          'PTV_150_250_0J' : '0.956',       'PTV_150_250_GE1J' : '1.053'},
    'THU_ggZH_inc'    : {'PTV_0_75' : '0.811/1.251', 'PTV_75_150' : '0.811/1.251', 'PTV_150_250_0J' : '0.811/1.251', 'PTV_150_250_GE1J' : '0.811/1.251', 'PTV_GT250' : '0.811/1.251'},
    'THU_ggZH_mig75'  : {'PTV_0_75' : '1.9/0.1',     'PTV_75_150' : '1.27',        'PTV_150_250_0J' : '1.27',        'PTV_150_250_GE1J' : '1.27',        'PTV_GT250' : '1.27'},
    'THU_ggZH_mig150' : {                            'PTV_75_150' : '0.882',       'PTV_150_250_0J' : '1.142',       'PTV_150_250_GE1J' : '1.142',       'PTV_GT250' : '1.142'},
    'THU_ggZH_mig250' : {                                                          'PTV_150_250_0J' : '0.963',       'PTV_150_250_GE1J' : '0.963',       'PTV_GE250' : '1.154'},
    'THU_ggZH_mig01'  : {                                                          'PTV_150_250_0J' : '1.6/0.393',   'PTV_150_250_GE1J' : '1.277'} 
}

prefix = {'WH' : 'QQ2HLNU', 'ZH' : 'QQ2HLL', 'ggZH' : 'GG2HLL'}

for unc in STXS_migUnc.keys():
    prod = unc.split('_')[1]
    samples = [skey for skey in mc if skey.split('_')[0] == prod]
    nuisances[unc] = {
        'name' : unc,
        'type' : 'lnN',
        'samples': dict((skey+'_'+prefix[prod]+'_'+binname, STXS_migUnc[unc][binname]) for binname in STXS_migUnc[unc] for skey in samples)
    }

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '1',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}


nuisances['Zg3lnorm']  = {
               'name'  : 'CMS_hww_Zg3lnorm',
               'samples'  : {
                   'Zg' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'wh3l_zg_13TeV',
                   'wh3l_13TeV_ossf_ptv_lt150',
                   'wh3l_13TeV_sssf_ptv_lt150',
                   #'wh3l_13TeV_ossf_ptv_gt150',
                   #'wh3l_13TeV_sssf_ptv_gt150',
                   'wh3l_13TeV_merged',
                   'wh3l_wz_13TeV',
                ]
              }

nuisances['WZ3lnorm']  = {
               'name'  : 'CMS_hww_WZ3lnorm',
               'samples'  : {
                   'WZ' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'wh3l_zg_13TeV',
                   'wh3l_13TeV_ossf_ptv_lt150',
                   'wh3l_13TeV_sssf_ptv_lt150',
                   #'wh3l_13TeV_ossf_ptv_gt150',
                   #'wh3l_13TeV_sssf_ptv_gt150',
                   'wh3l_13TeV_merged',
                   'wh3l_wz_13TeV',
                ]
              }



for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))