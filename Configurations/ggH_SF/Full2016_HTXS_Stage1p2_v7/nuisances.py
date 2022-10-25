# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

import os

if os.path.exists('HTXS_stage1_categories.py') :
  handle = open('HTXS_stage1_categories.py','r')
  exec(handle)
  handle.close()

#if os.path.exists('UEnormfactors.py') :
#  handle = open('UEnormfactors.py','r')
#  exec(handle)
#  handle.close()

if os.path.exists('thuNormFactors.py') :
  handle = open('thuNormFactors.py','r')
  exec(handle)
  handle.close()

if os.path.exists('thuVBFNormFactors.py') :                                  
  handle = open('thuVBFNormFactors.py','r')                                  
  exec(handle)                                                            
  handle.close() 



sampleNames = []

for cat in HTXSStage1_1Categories:
  if 'GG2H_' in cat:
    sampleNames.append(cat.replace('GG2H','ggH_hww'))
    sampleNames.append(cat.replace('GG2H','ggH_htt'))
  elif 'QQ2HQQ_' in cat:
    sampleNames.append(cat.replace('QQ2HQQ','qqH_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','qqH_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_htt'))
  elif 'QQ2HLNU_' in cat:
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_htt'))
  elif 'QQ2HLL_' in cat:
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_htt'))
  elif 'GG2HLL_' in cat:
    sampleNames.append(cat.replace('GG2HLL','ggZH_lep_hww'))
  elif 'TTH' in cat:
    sampleNames.append(cat.replace('TTH','ttH_hww'))
  elif 'BBH' in cat:
    sampleNames.append(cat.replace('BBH','bbH_hww'))

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


cuts0j  = []
cuts1j  = []
cuts2j  = []
cutshpt = []

for k in cuts:
  for cat in cuts[k]['categories']:
    if   '0j'  in cat or '0j'  in k:  cuts0j.append(k+'_'+cat)
    elif '1j'  in cat or '1j'  in k:  cuts1j.append(k+'_'+cat)
    elif '2j'  in cat or '2j'  in k:  cuts2j.append(k+'_'+cat)
    elif 'hpt' in cat or 'hpt' in k: cutshpt.append(k+'_'+cat)
    else: print 'WARNING: name of category does not contain on either 0j,1j,2j,hpt'

print("cuts0j  = {}".format(cuts0j))
print("cuts1j  = {}".format(cuts1j))
print("cuts2j  = {}".format(cuts2j))
print("cutshpt = {}".format(cutshpt))

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2016',
#    'type': 'lnN',
#    'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES

nuisances['fake_syst_ee'] = {
    'name': 'CMS_fake_syst_ee',
    'type': 'lnN',
    'samples': {
        'Fake_ee': '1.3'
    },
    'cutspost': lambda self, cuts: [cut for cut in cuts if 'ee' in cut],
}

nuisances['fake_syst_mm'] = {
    'name': 'CMS_fake_syst_mm',
    'type': 'lnN',
    'samples': {
        'Fake_mm': '1.3'
    },
    'cutspost': lambda self, cuts: [cut for cut in cuts if 'mm' in cut],
}

nuisances['fake_syst_df'] = {
    'name': 'CMS_fake_syst_df',
    'type': 'lnN',
    'samples': {
        'Fake_df': '1.3'
    },
    'cutspost': lambda self, cuts: [cut for cut in cuts if 'df' in cut],
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc if skey not in ['DY']),
    }

##### Trigger Efficiency

trig_drll_rw_syst = ['1.', '1./trig_drll_rw']

nuisances['trigg_drll_rw_unc'] = {
    'name': 'CMS_eff_hwwtrigger_drllrw_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_drll_rw_syst) for skey in mc if skey not in ['DY']),
    'symmetrize' : True,
}

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc if skey not in ['DY']),
}

prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc if skey not in ['DY']),
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc if skey not in ['DY']),
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp' : 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['DY']),
    'folderUp': makeMCDirectory('trigFix__ElepTup_suffix'),
    'folderDown': makeMCDirectory('trigFix__ElepTdo_suffix'),
    'AsLnN': '1'
}

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
   'name': 'CMS_eff_m_2016',
   'kind': 'weight',
   'type': 'shape',
   'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc if skey not in ['DY']),
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['DY']),
    'folderUp': makeMCDirectory('trigFix__MupTup_suffix'),
    'folderDown': makeMCDirectory('trigFix__MupTdo_suffix'),
    'AsLnN': '1'
}


##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']
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
      'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['DY','Vg','VgS']),
      'folderUp': folderup,
      'folderDown': folderdo,
      'AsLnN': '1'
  }

##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['DY']),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}

### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc if skey not in ['DY'])
}

##### Pileup

nuisances['PU'] = {  ## need to update acceptance for each region
    'name': 'CMS_PU_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        #'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
        'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
        'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
}

##### PS
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
        'ggWW'   : ['1.040233912070831*(nCleanGenJet==0) + 0.9611236379290876*(nCleanGenJet==1) + 0.9014289294088699*(nCleanGenJet==2) + 0.864310738090035*(nCleanGenJet>=3)', '0.9510305474211223*(nCleanGenJet==0) + 1.0433432942960381*(nCleanGenJet==1) + 1.1271383507266095*(nCleanGenJet==2) + 1.1885756983901514*(nCleanGenJet>=3)'],
        'WW'     : ['1.0005237869294796*(nCleanGenJet==0) + 1.0157425373134328*(nCleanGenJet==1) + 0.9644598124510606*(nCleanGenJet==2) + 0.9271488926223369*(nCleanGenJet>=3)', '0.9993553300024391*(nCleanGenJet==0) + 0.9806102300995024*(nCleanGenJet==1) + 1.042603303739856*(nCleanGenJet==2) + 1.0950369125887705*(nCleanGenJet>=3)'],
        'top'    : ['1.0020618369910668*(nCleanGenJet==0) + 1.0063081530771556*(nCleanGenJet==1) + 1.0094298425968304*(nCleanGenJet==2) + 0.9854207999040726*(nCleanGenJet>=3)', '0.9974340279269026*(nCleanGenJet==0) + 0.9920634820709106*(nCleanGenJet==1) + 0.988226385054923*(nCleanGenJet==2) + 1.017968568319235*(nCleanGenJet>=3)'],
        #'DY'     : ['0.9998177685645392*(nCleanGenJet==0) + 1.0080838149428026*(nCleanGenJet==1) + 1.0057948912950987*(nCleanGenJet==2) + 0.9721358221196619*(nCleanGenJet>=3)', '1.0003244155266309*(nCleanGenJet==0) + 0.9897992135367016*(nCleanGenJet==1) + 0.9928782069009531*(nCleanGenJet==2) + 1.0348902921423981*(nCleanGenJet>=3)'],
        'VVV'    : ['1.0270826786253018*(nCleanGenJet==0) + 1.0198703447307862*(nCleanGenJet==1) + 1.0109191915514344*(nCleanGenJet==2) + 0.9838184220287978*(nCleanGenJet>=3)', '0.9661665482954546*(nCleanGenJet==0) + 0.9751744967838527*(nCleanGenJet==1) + 0.9859624782745712*(nCleanGenJet==2) + 1.0202995039288625*(nCleanGenJet>=3)'],
        'ggH_hww': ['1.0007510488273352*(nCleanGenJet==0) + 1.0152476349471342*(nCleanGenJet==1) + 0.9645590929269297*(nCleanGenJet==2) + 0.9189171704206691*(nCleanGenJet>=3)', '0.9989909143752528*(nCleanGenJet==0) + 0.9814978813068076*(nCleanGenJet==1) + 1.0416554335980368*(nCleanGenJet==2) + 1.1060543963750413*(nCleanGenJet>=3)'],
        'qqH_hww': ['1.0008858084852863*(nCleanGenJet==0) + 1.001293920824975*(nCleanGenJet==1) + 1.0013304143711548*(nCleanGenJet==2) + 0.9875473532521144*(nCleanGenJet>=3)', '0.9987483211480337*(nCleanGenJet==0) + 0.9982952329209852*(nCleanGenJet==1) + 0.9983076740658964*(nCleanGenJet==2) + 1.016023412328836*(nCleanGenJet>=3)'],
        'WH_hww' : ['1.0006979353025824*(nCleanGenJet==0) + 1.0014529360558138*(nCleanGenJet==1) + 1.0007920644457673*(nCleanGenJet==2) + 0.996814275350521*(nCleanGenJet>=3)', '0.9990367459746422*(nCleanGenJet==0) + 0.9980712824836634*(nCleanGenJet==1) + 0.9989875513096169*(nCleanGenJet==2) + 1.0039628146069568*(nCleanGenJet>=3)'],
        'ZH_hww' : ['1.0008198940532742*(nCleanGenJet==0) + 1.001574300159756*(nCleanGenJet==1) + 1.0014892423703352*(nCleanGenJet==2) + 0.9982835923429388*(nCleanGenJet>=3)', '0.9991322211949244*(nCleanGenJet==0) + 0.9979828392772856*(nCleanGenJet==1) + 0.9980190791034156*(nCleanGenJet==2) + 1.0021025907582017*(nCleanGenJet>=3)'],
    },
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
        'ggWW'   : ['0.9910563426395067*(nCleanGenJet==0) + 1.0069894351287263*(nCleanGenJet==1) + 1.016616376034912*(nCleanGenJet==2) + 1.015902717074592*(nCleanGenJet>=3)', '1.0147395976461193*(nCleanGenJet==0) + 0.9860219489006646*(nCleanGenJet==1) + 0.9694680606617647*(nCleanGenJet==2) + 0.9489845115821678*(nCleanGenJet>=3)'],
        'WW'     : ['0.995462478372054*(nCleanGenJet==0) + 1.0052129975124378*(nCleanGenJet==1) + 1.008836750560578*(nCleanGenJet==2) + 0.9984120564941189*(nCleanGenJet>=3)', '1.008927720738437*(nCleanGenJet==0) + 0.995163868159204*(nCleanGenJet==1) + 0.9911024228315418*(nCleanGenJet==2) + 0.9763787172658678*(nCleanGenJet>=3)'],
        'top'    : ['0.9910899786333963*(nCleanGenJet==0) + 0.9990635702054794*(nCleanGenJet==1) + 1.002141744200183*(nCleanGenJet==2) + 1.0129742776372779*(nCleanGenJet>=3)', '1.0068843378231833*(nCleanGenJet==0) + 0.998988498438759*(nCleanGenJet==1) + 0.9952696584115224*(nCleanGenJet==2) + 0.9790955840673237*(nCleanGenJet>=3)'],
        #'DY'     : ['0.9958763409773141*(nCleanGenJet==0) + 1.0041335498093422*(nCleanGenJet==1) + 1.0163363150953029*(nCleanGenJet==2) + 1.0296733670670226*(nCleanGenJet>=3)', '1.0066775262249232*(nCleanGenJet==0) + 0.9945601465681602*(nCleanGenJet==1) + 0.9662459619335311*(nCleanGenJet==2) + 0.9479423453563661*(nCleanGenJet>=3)'],
        'VVV'    : ['0.9809047855490748*(nCleanGenJet==0) + 0.9823641498350338*(nCleanGenJet==1) + 0.9976414629808243*(nCleanGenJet==2) + 1.0077953569413387*(nCleanGenJet>=3)', '1.035388723727876*(nCleanGenJet==0) + 1.0347339790465233*(nCleanGenJet==1) + 1.0017058788771533*(nCleanGenJet==2) + 0.9829344116371653*(nCleanGenJet>=3)'],
        'ggH_hww': ['0.9936588910230489*(nCleanGenJet==0) + 1.0087564198432573*(nCleanGenJet==1) + 1.014636529653396*(nCleanGenJet==2) + 1.00399261707105*(nCleanGenJet>=3)','1.0125063182369591*(nCleanGenJet==0) + 0.9846168672324244*(nCleanGenJet==1) + 0.9778204449152542*(nCleanGenJet==2) + 1.0014057292097962*(nCleanGenJet>=3)'],
        'qqH_hww': ['0.9902864012471768*(nCleanGenJet==0) + 0.9950165165635796*(nCleanGenJet==1) + 1.0024778632714528*(nCleanGenJet==2) + 1.0132965690130387*(nCleanGenJet>=3)', '1.0171041801597582*(nCleanGenJet==0) + 1.0088822239287307*(nCleanGenJet==1) + 0.9946938338710369*(nCleanGenJet==2) + 0.9782409053438381*(nCleanGenJet>=3)'],
        'WH_hww' : ['0.9864466858859676*(nCleanGenJet==0) + 0.9911412676207558*(nCleanGenJet==1) + 1.0047988929561447*(nCleanGenJet==2) + 1.0135375714689319*(nCleanGenJet>=3)', '1.022768308571873*(nCleanGenJet==0) + 1.0147067259919833*(nCleanGenJet==1) + 0.9932121652658327*(nCleanGenJet==2) + 0.9807301742549035*(nCleanGenJet>=3)'],
        'ZH_hww' : ['0.98702584755388*(nCleanGenJet==0) + 0.9881328970299905*(nCleanGenJet==1) + 1.0046199525397077*(nCleanGenJet==2) + 1.0091561054313662*(nCleanGenJet>=3)', '1.0236225630459734*(nCleanGenJet==0) + 1.0213677207764504*(nCleanGenJet==1) + 0.9933149152918336*(nCleanGenJet==2) + 0.978832627595614*(nCleanGenJet>=3)'],
    },
}

for name in sampleNames:
  if 'ggH_hww' in name:
    nuisances['PS_ISR']['samples'].update({name: ['1.0007510488273352*(nCleanGenJet==0) + 1.0152476349471342*(nCleanGenJet==1) + 0.9645590929269297*(nCleanGenJet==2) + 0.9189171704206691*(nCleanGenJet>=3)', '0.9989909143752528*(nCleanGenJet==0) + 0.9814978813068076*(nCleanGenJet==1) + 1.0416554335980368*(nCleanGenJet==2) + 1.1060543963750413*(nCleanGenJet>=3)']})
    nuisances['PS_FSR']['samples'].update({name: ['0.9936588910230489*(nCleanGenJet==0) + 1.0087564198432573*(nCleanGenJet==1) + 1.014636529653396*(nCleanGenJet==2) + 1.00399261707105*(nCleanGenJet>=3)','1.0125063182369591*(nCleanGenJet==0) + 0.9846168672324244*(nCleanGenJet==1) + 0.9778204449152542*(nCleanGenJet==2) + 1.0014057292097962*(nCleanGenJet>=3)']})
  if 'qqH_hww' in name:
    nuisances['PS_ISR']['samples'].update({name: ['1.0008858084852863*(nCleanGenJet==0) + 1.001293920824975*(nCleanGenJet==1) + 1.0013304143711548*(nCleanGenJet==2) + 0.9875473532521144*(nCleanGenJet>=3)', '0.9987483211480337*(nCleanGenJet==0) + 0.9982952329209852*(nCleanGenJet==1) + 0.9983076740658964*(nCleanGenJet==2) + 1.016023412328836*(nCleanGenJet>=3)']})
    nuisances['PS_FSR']['samples'].update({name: ['0.9902864012471768*(nCleanGenJet==0) + 0.9950165165635796*(nCleanGenJet==1) + 1.0024778632714528*(nCleanGenJet==2) + 1.0132965690130387*(nCleanGenJet>=3)', '1.0171041801597582*(nCleanGenJet==0) + 1.0088822239287307*(nCleanGenJet==1) + 0.9946938338710369*(nCleanGenJet==2) + 0.9782409053438381*(nCleanGenJet>=3)']})
  if 'WH_lep_hww' in name or 'WH_had_hww' in name:
    nuisances['PS_ISR']['samples'].update({name: ['1.0006979353025824*(nCleanGenJet==0) + 1.0014529360558138*(nCleanGenJet==1) + 1.0007920644457673*(nCleanGenJet==2) + 0.996814275350521*(nCleanGenJet>=3)', '0.9990367459746422*(nCleanGenJet==0) + 0.9980712824836634*(nCleanGenJet==1) + 0.9989875513096169*(nCleanGenJet==2) + 1.0039628146069568*(nCleanGenJet>=3)']})
    nuisances['PS_FSR']['samples'].update({name: ['0.9864466858859676*(nCleanGenJet==0) + 0.9911412676207558*(nCleanGenJet==1) + 1.0047988929561447*(nCleanGenJet==2) + 1.0135375714689319*(nCleanGenJet>=3)', '1.022768308571873*(nCleanGenJet==0) + 1.0147067259919833*(nCleanGenJet==1) + 0.9932121652658327*(nCleanGenJet==2) + 0.9807301742549035*(nCleanGenJet>=3)']})
  if 'ZH_lep_hww' in name or 'ZH_had_hww' in name:
    nuisances['PS_ISR']['samples'].update({name: ['1.0008198940532742*(nCleanGenJet==0) + 1.001574300159756*(nCleanGenJet==1) + 1.0014892423703352*(nCleanGenJet==2) + 0.9982835923429388*(nCleanGenJet>=3)', '0.9991322211949244*(nCleanGenJet==0) + 0.9979828392772856*(nCleanGenJet==1) + 0.9980190791034156*(nCleanGenJet==2) + 1.0021025907582017*(nCleanGenJet>=3)']})
    nuisances['PS_FSR']['samples'].update({name: ['0.98702584755388*(nCleanGenJet==0) + 0.9881328970299905*(nCleanGenJet==1) + 1.0046199525397077*(nCleanGenJet==2) + 1.0091561054313662*(nCleanGenJet>=3)', '1.0236225630459734*(nCleanGenJet==0) + 1.0213677207764504*(nCleanGenJet==1) + 0.9933149152918336*(nCleanGenJet==2) + 0.978832627595614*(nCleanGenJet>=3)']})

# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CUET',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if not skey in ['WW', 'top', 'DY']),
}

####### Generic "cross section uncertainties"

apply_on = {
    'top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

## Top pT reweighting uncertainty

# nuisances['TopPtRew'] = {
#     'name': 'CMS_topPtRew',   # Theory uncertainty
#     'kind': 'weight',
#     'type': 'shape',
#     'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
#     'symmetrize': True
# }

nuisances['VgStar'] = {
    'name': 'CMS_hww_VgStarScale',
    'type': 'lnN',
    'samples': {
        'VgS_L': '1.25'
    }
}

if useWgFXFX:
  nuisances['VgScale'] = {
      'name': 'CMS_hww_VgScale',
      'type': 'lnN',
      'samples': {
          'Vg': '1.06'
      }
  }

nuisances['VZ'] = {
    'name': 'CMS_hww_VZScale',
    'type': 'lnN',
    'samples': {
        'VgS_H': '1.16'
    }
}

###### pdf uncertainties

valuesggh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','pdf','sm')
valuesggzh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm')
valuesbbh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH','125.09','pdf','sm')

nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        #'ggH_hww': valuesggh,
        'ggH_htt': valuesggh,
        #'ggZH_hww': valuesggzh,
        'bbH_hww': valuesbbh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')

nuisances['pdf_Higgs_ttH'] = {
    'name': 'pdf_Higgs_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

valuesqqh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm')
valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','pdf','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','pdf','sm')

nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        #'qqH_hww': valuesqqh,
        'qqH_htt': valuesqqh,
        #'WH_hww': valueswh,
        'WH_htt': valueswh,
        #'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
}

nuisances['pdf_qqbar'] = {
    'name': 'pdf_qqbar',
    'type': 'lnN',
    'samples': {
        'Vg': '1.04',
        'VZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'VgS': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
    },
}

nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        #'ggH_hww': '1.006',
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
        #'qqH_hww': '1.002',
        'qqH_htt': '1.002',
        #'WH_hww': '1.003',
        'WH_htt': '1.003',
        #'ZH_hww': '1.002',
        'ZH_htt': '1.002',
    },
}

nuisances['pdf_qqbar_ACCEPT'] = {
    'name': 'pdf_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'VZ': '1.001',
    },
}

##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for top
## LHE scale variation weights (w_var / w_nominal)
## Different approach in this case because LHEScaleWeight is missing in single top samples
topvariations = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[5],1)','Alt$(LHEScaleWeight[7],1)','Alt$(LHEScaleWeight[8],1)']

topvars0j = []
topvars1j = []
topvars2j = []

## Factors computed to renormalize the top scale variations such that the integral is not changed in each RECO jet bin (we have rateParams for that)
topScaleNormFactors0j = {'Alt$(LHEScaleWeight[3],1)': 1.0127481603212656, 'Alt$(LHEScaleWeight[0],1)': 1.0781331279433415, 'Alt$(LHEScaleWeight[1],1)': 1.0690928216708382, 'Alt$(LHEScaleWeight[7],1)': 0.9345571161077737, 'Alt$(LHEScaleWeight[8],1)': 0.9227838225449528, 'Alt$(LHEScaleWeight[5],1)': 0.9907270914731349}
topScaleNormFactors1j = {'Alt$(LHEScaleWeight[3],1)': 1.0153655578503986, 'Alt$(LHEScaleWeight[0],1)': 1.0907798004584341, 'Alt$(LHEScaleWeight[1],1)': 1.0798026063785011, 'Alt$(LHEScaleWeight[7],1)': 0.92428116499208, 'Alt$(LHEScaleWeight[8],1)': 0.9101690580310614, 'Alt$(LHEScaleWeight[5],1)': 0.9888177133975222}
topScaleNormFactors2j = {'Alt$(LHEScaleWeight[3],1)': 1.0239541358390016, 'Alt$(LHEScaleWeight[0],1)': 1.125869020564376, 'Alt$(LHEScaleWeight[1],1)': 1.105896547188302, 'Alt$(LHEScaleWeight[7],1)': 0.9037581174447249, 'Alt$(LHEScaleWeight[8],1)': 0.8828417179568193, 'Alt$(LHEScaleWeight[5],1)': 0.981806136304384}

topvars0j.append('Alt$(LHEScaleWeight[0],1)/'+str(topScaleNormFactors0j['Alt$(LHEScaleWeight[0],1)']))
topvars0j.append('Alt$(LHEScaleWeight[7],1)/'+str(topScaleNormFactors0j['Alt$(LHEScaleWeight[7],1)']))

topvars1j.append('Alt$(LHEScaleWeight[0],1)/'+str(topScaleNormFactors1j['Alt$(LHEScaleWeight[0],1)']))
topvars1j.append('Alt$(LHEScaleWeight[7],1)/'+str(topScaleNormFactors1j['Alt$(LHEScaleWeight[7],1)']))

topvars2j.append('Alt$(LHEScaleWeight[0],1)/'+str(topScaleNormFactors2j['Alt$(LHEScaleWeight[0],1)']))
topvars2j.append('Alt$(LHEScaleWeight[7],1)/'+str(topScaleNormFactors2j['Alt$(LHEScaleWeight[7],1)']))

'''
for var in topvariations:
  topvars0j.append(var+'/'+str(topScaleNormFactors0j[var]))
  topvars1j.append(var+'/'+str(topScaleNormFactors1j[var]))
  topvars2j.append(var+'/'+str(topScaleNormFactors2j[var]))
'''

## QCD scale nuisances for top are decorrelated for each RECO jet bin: the QCD scale is different for different jet multiplicities so it doesn't make sense to correlate them
nuisances['QCDscale_top_0j']  = {
    'name'  : 'QCDscale_top_0j',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'cutspost' : lambda self, cuts: [cut for cut in cuts if '0j' in cut],
    'samples'  : {
       'top' : topvars0j,
    }
}

nuisances['QCDscale_top_1j']  = {
    'name'  : 'QCDscale_top_1j',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'cutspost' : lambda self, cuts: [cut for cut in cuts if '1j' in cut],
    'samples'  : {
       'top' : topvars1j,
    }
}

nuisances['QCDscale_top_2j']  = {
    'name'  : 'QCDscale_top_2j',
    'skipCMS' : 1,
    'kind'  : 'weight',
    'type'  : 'shape',
    'cutspost' : lambda self, cuts: [cut for cut in cuts if '2j' in cut],
    'samples'  : {
       'top' : topvars2j,
    }
}

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

#nuisances['QCDscale_V'] = {
#    'name': 'QCDscale_V',
#    'skipCMS': 1,
#    'kind': 'weight_envelope',
#    'type': 'shape',
#    'samples': {'DY': variations},  #is finally included in the DY systematics? 
#    'AsLnN': '1'
#}

if useWgFXFX:
  nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
      'VZ': variations,
    }
  }
else:
  nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
      'Vg': variations,
      'VZ': variations,
      'VgS': variations
    }
  }
  
# ggww and interference
nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    },
}

# NLL resummation variations
nuisances['WWresum0j']  = {
  'name'  : 'CMS_hww_WWresum_0j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
}

nuisances['WWqscale0j']  = {
   'name'  : 'CMS_hww_WWqscale_0j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
}

nuisances['WWresum1j']  = {
  'name'  : 'CMS_hww_WWresum_1j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
}

nuisances['WWqscale1j']  = {
   'name'  : 'CMS_hww_WWqscale_1j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
}

nuisances['WWresum2j']  = {
  'name'  : 'CMS_hww_WWresum_2j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
}

nuisances['WWqscale2j']  = {
   'name'  : 'CMS_hww_WWqscale_2j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
}

nuisances['EWKcorr_WW'] = {
    'name': 'CMS_hww_EWKcorr_WW',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WW': ['1.', '1./ewknloW']
    },
    'symmetrize' : True,
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_WW'] = {
    'name': 'CMS_hww_CRSR_accept_WW',
    'type': 'lnN',
    'samples': {'WW': '1.01'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_WW_' in cut]),
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_top'] = {
    'name': 'CMS_hww_CRSR_accept_top',
    'type': 'lnN',
    'samples': {'top': '1.01'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_top_' in cut]),
}

# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop

#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools

thus = [
    ('THU_ggH_Mu', 'ggH_mu_2'),
    ('THU_ggH_Res', 'ggH_res_2'),
    ('THU_ggH_Mig01', 'ggH_mig01_2'),
    ('THU_ggH_Mig12', 'ggH_mig12_2'),
    ('THU_ggH_VBF2j', 'ggH_VBF2j_2'),
    ('THU_ggH_VBF3j', 'ggH_VBF3j_2'),
    ('THU_ggH_PT60', 'ggH_pT60_2'),
    ('THU_ggH_PT120', 'ggH_pT120_2'),
    ('THU_ggH_qmtop', 'ggH_qmtop_2')
]

for name, vname in thus:
    updown = [vname, '2.-%s' % vname]
    
    nuisances[name] = {
        'name': name,
        'skipCMS': 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
          'ggH_hww': updown,
          #'ggH_htt': updown
        }
    }
    for sname in sampleNames:
        if 'ggH_hww' in sname:
            if 'GT200' not in sname:
              #print globals()                                                                                                                 
              normthu = globals()[name.replace("THU_","thuNormFactors_")][sname.replace('ggH_hww','GG2H')][0]
              nuisances[name]['samples'].update({sname : [vname+'/'+normthu,'2.-'+vname+'/'+normthu]})
            else:
              nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_200_300'][0]
              ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_200_300'][0]]})
              nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_300_450'][0]
              ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_300_450'][0]]})
              nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_450_650'][0]
              ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_450_650'][0]]})
              nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_GT650'][0]
              ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_GT650'][0]]})

# Theory uncertainty for qqH 
#
#
#   see https://gitlab.cern.ch/LHCHIGGSXS/LHCHXSWG2/STXS/VBF-Uncertainties/-/blob/master/qq2Hqq_uncert_scheme.cpp

thusQQH = [
  ("THU_qqH_YIELD","qqH_YIELD"),
  ("THU_qqH_PTH200","qqH_PTH200"),
  ("THU_qqH_Mjj60","qqH_Mjj60"),
  ("THU_qqH_Mjj120","qqH_Mjj120"),
  ("THU_qqH_Mjj350","qqH_Mjj350"),
  ("THU_qqH_Mjj700","qqH_Mjj700"),
  ("THU_qqH_Mjj1000","qqH_Mjj1000"),
  ("THU_qqH_Mjj1500","qqH_Mjj1500"),
  ("THU_qqH_PTH25","qqH_PTH25"),
  ("THU_qqH_JET01","qqH_JET01"),
  ("THU_qqH_EWK","qqH_EWK"),
]

for name, vname in thusQQH:
    updown = [vname, '2.-%s' % vname]
    
    nuisances[name] = {
        'name': name,
        'skipCMS': 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
          'qqH_hww': updown,
        }
    }
    for sname in sampleNames:
        if 'qqH_hww' in sname:
          normthu = globals()[name.replace("THU_","thuNormFactors_")][sname.replace('qqH_hww','QQ2HQQ')][0]
          nuisances[name]['samples'].update({sname : [vname+'/'+normthu,'2.-'+vname+'/'+normthu]})
    print nuisances[name]

### QCD STXS accept                                                                                                                           
nuisances['ggH_scale_0jet'] = {                                                                                        
               'name'  : 'ggH_scale_0jet',                                                                             
               'samples'  : {
                   'ggH_hww_0J_PTH_0_10' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_0J_PTH_0_10'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_0J_PTH_0_10'][1]],
                   'ggH_hww_0J_PTH_GT10' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_0J_PTH_GT10'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_0J_PTH_GT10'][1]],
                  },                                                                                                   
               'type'  : 'shape',                                                                                      
               'kind'  : 'weight',                                                                                     
              }

nuisances['ggH_scale_1jet_lowpt'] = {                                                                                  
               'name'  : 'ggH_scale_1jet_lowpt',                                                                       
               'samples'  : {
                   'ggH_hww_1J_PTH_0_60' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_0_60'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_0_60'][1]],
                   'ggH_hww_1J_PTH_60_120' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_60_120'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_60_120'][1]],
                   'ggH_hww_1J_PTH_120_200' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_120_200'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_120_200'][1]],
                  },                                                                                                   
               'type'  : 'shape',                                                                                      
               'kind'  : 'weight',                                                                                     
              }

nuisances['ggH_scale_2jet_lowpt'] = {                                                                                  
               'name'  : 'ggH_scale_2jet_lowpt',                                                                       
               'samples'  : {
                   'ggH_hww_GE2J_MJJ_0_350_PTH_0_60' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_0_60'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_0_60'][1]],
                   'ggH_hww_GE2J_MJJ_0_350_PTH_60_120' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_60_120'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_60_120'][1]],
                   'ggH_hww_GE2J_MJJ_0_350_PTH_120_200' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_120_200'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_120_200'][1]],
                  },                                                                                                   
               'type'  : 'shape',                                                                                      
               'kind'  : 'weight',                                                                                     
              }

nuisances['ggH_scale_highpt'] = {                                                                                      
               'name'  : 'ggH_scale_highpt',                                                                           
               'samples'  : {
                   'ggH_hww_PTH_200_300' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_200_300'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_200_300'][1]],
                   'ggH_hww_PTH_300_450' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_300_450'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_300_450'][1]],
                  },
               'type'  : 'shape',                                                                                      
               'kind'  : 'weight',                                                                                     
              }

nuisances['ggH_scale_very_highpt'] = {                                                                                 
               'name'  : 'ggH_scale_very_highpt',                                                                      
               'samples'  : {
                   'ggH_hww_PTH_450_650' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_450_650'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_450_650'][1]],
                   'ggH_hww_PTH_GT650' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_GT650'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_GT650'][1]],
                  },
               'type'  : 'shape',                                                                                      
               'kind'  : 'weight',                                                                                     
              }

nuisances['ggH_scale_vbf'] = {                                                                                         
               'name'  : 'ggH_scale_vbf',
               'samples'  : {
                   'ggH_hww_GE2J_MJJ_350_700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_0_25'][1]],
                   'ggH_hww_GE2J_MJJ_350_700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_GT25'][1]],
                   'ggH_hww_GE2J_MJJ_GT700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_0_25'][1]],
                   'ggH_hww_GE2J_MJJ_GT700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_GT25'][1]],
                  },
               'type'  : 'shape',                                                                                      
               'kind'  : 'weight',                                                                                     
              }

#### QCD scale uncertainties for Higgs signals other than ggH

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm')

nuisances['QCDscale_qqH'] = {
    'name': 'QCDscale_qqH', 
    'samples': {
        #'qqH_hww': values,
        'qqH_htt': values
    },
    'type': 'lnN'
}

valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm')

nuisances['QCDscale_VH'] = {
    'name': 'QCDscale_VH', 
    'samples': {
        #'WH_hww': valueswh,
        'WH_htt': valueswh,
        #'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm')

nuisances['QCDscale_ggZH'] = {
    'name': 'QCDscale_ggZH', 
    'samples': {
        #'ggZH_hww': values
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm')

nuisances['QCDscale_ttH'] = {
    'name': 'QCDscale_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

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
        #'qqH_hww': '1.003',
        'qqH_htt': '1.003',
        #'WH_hww': '1.010',
        'WH_htt': '1.010',
        #'ZH_hww': '1.015',
        'ZH_htt': '1.015',
        #'VZ': '1.004', # this shouldn't be here because we have full shape-based uncertainty for VZ
    }
}

nuisances['QCDscale_gg_ACCEPT'] = {
    'name': 'QCDscale_gg_ACCEPT',
    'samples': {
        #'ggH_hww': '1.012', # shouldn't be here
        'ggH_htt': '1.012',
        #'ggZH_hww': '1.012',
        'ggWW': '1.012',
    },
    'type': 'lnN',
}

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}

## rate parameters

# WW

nuisances['WWnorm0j_ee']  = {
   'name'     : 'CMS_hww_WWnorm0j_ee_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts0j if 'ee' in cut]
}

nuisances['WWnorm0j_mm']  = {
   'name'     : 'CMS_hww_WWnorm0j_mm_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts0j if 'mm' in cut]
}

nuisances['WWnorm1j_ee']  = {
   'name'     : 'CMS_hww_WWnorm1j_ee_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts1j if 'ee' in cut]
}

nuisances['WWnorm1j_mm']  = {
   'name'     : 'CMS_hww_WWnorm1j_mm_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts1j if 'mm' in cut]
}

nuisances['WWnorm2j_ee']  = {
   'name'     : 'CMS_hww_WWnorm2j_ee_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts2j if 'ee' in cut]
}

nuisances['WWnorm2j_mm']  = {
   'name'     : 'CMS_hww_WWnorm2j_mm_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts2j if 'mm' in cut]
}

nuisances['WWnormhpt_ee']  = {
   'name'     : 'CMS_hww_WWnormhpt_ee_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cutshpt if 'ee' in cut]
}

nuisances['WWnormhpt_mm']  = {
   'name'     : 'CMS_hww_WWnormhpt_mm_2016',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cutshpt if 'mm' in cut]
}


# ggWW

nuisances['ggWWnorm0j_ee']  = {
   'name'     : 'CMS_hww_WWnorm0j_ee_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts0j if 'ee' in cut]
}

nuisances['ggWWnorm0j_mm']  = {
   'name'     : 'CMS_hww_WWnorm0j_mm_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts0j if 'mm' in cut]
}

nuisances['ggWWnorm1j_ee']  = {
   'name'     : 'CMS_hww_WWnorm1j_ee_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts1j if 'ee' in cut]
}

nuisances['ggWWnorm1j_mm']  = {
   'name'     : 'CMS_hww_WWnorm1j_mm_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts1j if 'mm' in cut]
}

nuisances['ggWWnorm2j_ee']  = {
   'name'     : 'CMS_hww_WWnorm2j_ee_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts2j if 'ee' in cut]
}

nuisances['ggWWnorm2j_mm']  = {
   'name'     : 'CMS_hww_WWnorm2j_mm_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts2j if 'mm' in cut]
}

nuisances['ggWWnormhpt_ee']  = {
   'name'     : 'CMS_hww_WWnormhpt_ee_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cutshpt if 'ee' in cut]
}

nuisances['ggWWnormhpt_mm']  = {
   'name'     : 'CMS_hww_WWnormhpt_mm_2016',
   'samples'  : {
      'ggWW'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cutshpt if 'mm' in cut]
}

# Top

nuisances['Topnorm0j_ee']  = {
   'name'     : 'CMS_hww_Topnorm0j_ee_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts0j if 'ee' in cut]
}

nuisances['Topnorm0j_mm']  = {
   'name'     : 'CMS_hww_Topnorm0j_mm_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts0j if 'mm' in cut]
}

nuisances['Topnorm1j_ee']  = {
   'name'     : 'CMS_hww_Topnorm1j_ee_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts1j if 'ee' in cut]
}

nuisances['Topnorm1j_mm']  = {
   'name'     : 'CMS_hww_Topnorm1j_mm_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts1j if 'mm' in cut]
}

nuisances['Topnorm2j_ee']  = {
   'name'     : 'CMS_hww_Topnorm2j_ee_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts2j if 'ee' in cut]
}

nuisances['Topnorm2j_mm']  = {
   'name'     : 'CMS_hww_Topnorm2j_mm_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cuts2j if 'mm' in cut]
}

nuisances['Topnormhpt_ee']  = {
   'name'     : 'CMS_hww_Topnormhpt_ee_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cutshpt if 'ee' in cut]
}

nuisances['Topnormhpt_mm']  = {
   'name'     : 'CMS_hww_Topnormhpt_mm_2016',
   'samples'  : {
      'top'    : '1.00',
      },
   'type'     : 'rateParam',
   'cuts'     : [cut for cut in cutshpt if 'mm' in cut]
}


# Drell-Yan data-driven uncertainties

# Nuisances breakdown 
 
# hpt_mm channel 
nuisances['DYnorm_k_hpt_mm_hww2l2v_13TeV_hpt_mm_pth450_650'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth450_650'] 
}

nuisances['DYnorm_em_hpt_mm_hww2l2v_13TeV_hpt_mm_pth450_650'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth450_650'] 
}

nuisances['DYnorm_R_hpt_mm_hww2l2v_13TeV_hpt_mm_pth450_650'] = {
  'name': 'DYnorm_R_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.884/1.131',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth450_650'] 
}

nuisances['DYnorm_Acc_hpt_mm_hww2l2v_13TeV_hpt_mm_pth450_650'] = {
  'name': 'DYnorm_Acc_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.084/11.919',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth450_650'] 
}

# 2j_ee channel 
nuisances['DYnorm_k_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] 
}

nuisances['DYnorm_em_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] 
}

nuisances['DYnorm_R_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.851/1.176',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] 
}

nuisances['DYnorm_Acc_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.204/4.896',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj25'] 
}

# 2j_mm channel 
nuisances['DYnorm_k_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] 
}

nuisances['DYnorm_em_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] 
}

nuisances['DYnorm_R_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.932/1.073',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] 
}

nuisances['DYnorm_Acc_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.798/1.253',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth60_120'] 
}

# hpt_mm channel 
nuisances['DYnorm_k_hpt_mm_hww2l2v_13TeV_hpt_mm_pth650'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth650'] 
}

nuisances['DYnorm_em_hpt_mm_hww2l2v_13TeV_hpt_mm_pth650'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth650'] 
}

nuisances['DYnorm_R_hpt_mm_hww2l2v_13TeV_hpt_mm_pth650'] = {
  'name': 'DYnorm_R_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.884/1.131',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth650'] 
}

nuisances['DYnorm_Acc_hpt_mm_hww2l2v_13TeV_hpt_mm_pth650'] = {
  'name': 'DYnorm_Acc_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.020/49.419',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth650'] 
}

# 2j_ee channel 
nuisances['DYnorm_k_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] 
}

nuisances['DYnorm_em_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] 
}

nuisances['DYnorm_R_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.851/1.176',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] 
}

nuisances['DYnorm_Acc_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.494/2.025',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth0_60'] 
}

# hpt_mm channel 
nuisances['DYnorm_k_hpt_mm_hww2l2v_13TeV_hpt_mm_pth300_450'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth300_450'] 
}

nuisances['DYnorm_em_hpt_mm_hww2l2v_13TeV_hpt_mm_pth300_450'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth300_450'] 
}

nuisances['DYnorm_R_hpt_mm_hww2l2v_13TeV_hpt_mm_pth300_450'] = {
  'name': 'DYnorm_R_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.884/1.131',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth300_450'] 
}

nuisances['DYnorm_Acc_hpt_mm_hww2l2v_13TeV_hpt_mm_pth300_450'] = {
  'name': 'DYnorm_Acc_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.272/3.681',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth300_450'] 
}

# 0j_mm channel 
nuisances['DYnorm_k_0j_mm_hww2l2v_13TeV_0j_mm_pth0_10'] = {
  'name': 'DYnorm_k_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.004/0.996',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth0_10'] 
}

nuisances['DYnorm_em_0j_mm_hww2l2v_13TeV_0j_mm_pth0_10'] = {
  'name': 'DYnorm_em_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.167/0.857',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth0_10'] 
}

nuisances['DYnorm_R_0j_mm_hww2l2v_13TeV_0j_mm_pth0_10'] = {
  'name': 'DYnorm_R_0j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.862/1.160',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth0_10'] 
}

nuisances['DYnorm_Acc_0j_mm_hww2l2v_13TeV_0j_mm_pth0_10'] = {
  'name': 'DYnorm_Acc_0j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.696/1.436',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth0_10'] 
}

# 2j_ee channel 
nuisances['DYnorm_k_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] 
}

nuisances['DYnorm_em_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] 
}

nuisances['DYnorm_R_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.851/1.176',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] 
}

nuisances['DYnorm_Acc_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.562/1.779',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth120_200'] 
}

# 2j_mm channel 
nuisances['DYnorm_k_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] 
}

nuisances['DYnorm_em_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] 
}

nuisances['DYnorm_R_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.932/1.073',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] 
}

nuisances['DYnorm_Acc_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.636/1.572',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth120_200'] 
}

# 2j_ee channel 
nuisances['DYnorm_k_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] 
}

nuisances['DYnorm_em_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] 
}

nuisances['DYnorm_R_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.851/1.176',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] 
}

nuisances['DYnorm_Acc_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.581/1.722',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj25'] 
}

# hpt_mm channel 
nuisances['DYnorm_k_hpt_mm_hww2l2v_13TeV_hpt_mm_pth200_300'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth200_300'] 
}

nuisances['DYnorm_em_hpt_mm_hww2l2v_13TeV_hpt_mm_pth200_300'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth200_300'] 
}

nuisances['DYnorm_R_hpt_mm_hww2l2v_13TeV_hpt_mm_pth200_300'] = {
  'name': 'DYnorm_R_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.884/1.131',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth200_300'] 
}

nuisances['DYnorm_Acc_hpt_mm_hww2l2v_13TeV_hpt_mm_pth200_300'] = {
  'name': 'DYnorm_Acc_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.501/1.996',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_mm_pth200_300'] 
}

# hpt_ee channel 
nuisances['DYnorm_k_hpt_ee_hww2l2v_13TeV_hpt_ee_pth450_650'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth450_650'] 
}

nuisances['DYnorm_em_hpt_ee_hww2l2v_13TeV_hpt_ee_pth450_650'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth450_650'] 
}

nuisances['DYnorm_R_hpt_ee_hww2l2v_13TeV_hpt_ee_pth450_650'] = {
  'name': 'DYnorm_R_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.873/1.146',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth450_650'] 
}

nuisances['DYnorm_Acc_hpt_ee_hww2l2v_13TeV_hpt_ee_pth450_650'] = {
  'name': 'DYnorm_Acc_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.013/77.116',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth450_650'] 
}

# 2j_ee channel 
nuisances['DYnorm_k_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] 
}

nuisances['DYnorm_em_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] 
}

nuisances['DYnorm_R_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.851/1.176',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] 
}

nuisances['DYnorm_Acc_2j_ee_hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.452/2.212',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj350_700_pthjj0_25'] 
}

# 2j_ee channel 
nuisances['DYnorm_k_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] 
}

nuisances['DYnorm_em_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] 
}

nuisances['DYnorm_R_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.851/1.176',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] 
}

nuisances['DYnorm_Acc_2j_ee_hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.533/1.878',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj700_pthjj0_25'] 
}

# 1j_ee WW channel 
nuisances['DYnorm_k_1j_ee_WW_hww2l2v_13TeV_WW_1j_ee'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_ee'] 
}

nuisances['DYnorm_em_1j_ee_WW_hww2l2v_13TeV_WW_1j_ee'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.102/0.908',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_ee'] 
}

nuisances['DYnorm_R_1j_ee_WW_hww2l2v_13TeV_WW_1j_ee'] = {
  'name': 'DYnorm_R_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.928/1.077',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_ee'] 
}

nuisances['DYnorm_Acc_1j_ee_WW_hww2l2v_13TeV_WW_1j_ee'] = {
  'name': 'DYnorm_Acc_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.748/1.338',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_ee'] 
}

# 2j_ee channel 
nuisances['DYnorm_k_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] 
}

nuisances['DYnorm_em_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] 
}

nuisances['DYnorm_R_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.851/1.176',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] 
}

nuisances['DYnorm_Acc_2j_ee_hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.610/1.639',
  },
  'cuts' : ['hww2l2v_13TeV_2j_ee_mjj0_350_pth60_120'] 
}

# 1j_mm WW channel 
nuisances['DYnorm_k_1j_mm_WW_hww2l2v_13TeV_WW_1j_mm'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_mm'] 
}

nuisances['DYnorm_em_1j_mm_WW_hww2l2v_13TeV_WW_1j_mm'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.099/0.910',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_mm'] 
}

nuisances['DYnorm_R_1j_mm_WW_hww2l2v_13TeV_WW_1j_mm'] = {
  'name': 'DYnorm_R_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.948/1.055',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_mm'] 
}

nuisances['DYnorm_Acc_1j_mm_WW_hww2l2v_13TeV_WW_1j_mm'] = {
  'name': 'DYnorm_Acc_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.796/1.256',
  },
  'cuts' : ['hww2l2v_13TeV_WW_1j_mm'] 
}

# 1j_ee channel 
nuisances['DYnorm_k_1j_ee_hww2l2v_13TeV_1j_ee_pth120_200'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth120_200'] 
}

nuisances['DYnorm_em_1j_ee_hww2l2v_13TeV_1j_ee_pth120_200'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.102/0.908',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth120_200'] 
}

nuisances['DYnorm_R_1j_ee_hww2l2v_13TeV_1j_ee_pth120_200'] = {
  'name': 'DYnorm_R_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.902/1.108',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth120_200'] 
}

nuisances['DYnorm_Acc_1j_ee_hww2l2v_13TeV_1j_ee_pth120_200'] = {
  'name': 'DYnorm_Acc_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.067/14.987',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth120_200'] 
}

# 2j_mm WW channel 
nuisances['DYnorm_k_2j_mm_WW_hww2l2v_13TeV_WW_2j_mm'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_mm'] 
}

nuisances['DYnorm_em_2j_mm_WW_hww2l2v_13TeV_WW_2j_mm'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_mm'] 
}

nuisances['DYnorm_R_2j_mm_WW_hww2l2v_13TeV_WW_2j_mm'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.959/1.043',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_mm'] 
}

nuisances['DYnorm_Acc_2j_mm_WW_hww2l2v_13TeV_WW_2j_mm'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.842/1.188',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_mm'] 
}

# hpt_ee channel 
nuisances['DYnorm_k_hpt_ee_hww2l2v_13TeV_hpt_ee_pth300_450'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth300_450'] 
}

nuisances['DYnorm_em_hpt_ee_hww2l2v_13TeV_hpt_ee_pth300_450'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth300_450'] 
}

nuisances['DYnorm_R_hpt_ee_hww2l2v_13TeV_hpt_ee_pth300_450'] = {
  'name': 'DYnorm_R_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.873/1.146',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth300_450'] 
}

nuisances['DYnorm_Acc_hpt_ee_hww2l2v_13TeV_hpt_ee_pth300_450'] = {
  'name': 'DYnorm_Acc_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.116/8.638',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth300_450'] 
}

# 2j_mm channel 
nuisances['DYnorm_k_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] 
}

nuisances['DYnorm_em_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] 
}

nuisances['DYnorm_R_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.932/1.073',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] 
}

nuisances['DYnorm_Acc_2j_mm_hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.615/1.627',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj0_350_pth0_60'] 
}

# 2j_mm channel 
nuisances['DYnorm_k_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] 
}

nuisances['DYnorm_em_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] 
}

nuisances['DYnorm_R_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.932/1.073',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] 
}

nuisances['DYnorm_Acc_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.650/1.539',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj25'] 
}

# 1j_mm channel 
nuisances['DYnorm_k_1j_mm_hww2l2v_13TeV_1j_mm_pth120_200'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth120_200'] 
}

nuisances['DYnorm_em_1j_mm_hww2l2v_13TeV_1j_mm_pth120_200'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.099/0.910',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth120_200'] 
}

nuisances['DYnorm_R_1j_mm_hww2l2v_13TeV_1j_mm_pth120_200'] = {
  'name': 'DYnorm_R_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.936/1.069',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth120_200'] 
}

nuisances['DYnorm_Acc_1j_mm_hww2l2v_13TeV_1j_mm_pth120_200'] = {
  'name': 'DYnorm_Acc_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.203/4.915',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth120_200'] 
}

# 1j_ee channel 
nuisances['DYnorm_k_1j_ee_hww2l2v_13TeV_1j_ee_pth60_120'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth60_120'] 
}

nuisances['DYnorm_em_1j_ee_hww2l2v_13TeV_1j_ee_pth60_120'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.102/0.908',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth60_120'] 
}

nuisances['DYnorm_R_1j_ee_hww2l2v_13TeV_1j_ee_pth60_120'] = {
  'name': 'DYnorm_R_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.902/1.108',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth60_120'] 
}

nuisances['DYnorm_Acc_1j_ee_hww2l2v_13TeV_1j_ee_pth60_120'] = {
  'name': 'DYnorm_Acc_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.633/1.580',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth60_120'] 
}

# 0j_ee channel 
nuisances['DYnorm_k_0j_ee_hww2l2v_13TeV_0j_ee_pth0_10'] = {
  'name': 'DYnorm_k_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth0_10'] 
}

nuisances['DYnorm_em_0j_ee_hww2l2v_13TeV_0j_ee_pth0_10'] = {
  'name': 'DYnorm_em_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.157/0.864',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth0_10'] 
}

nuisances['DYnorm_R_0j_ee_hww2l2v_13TeV_0j_ee_pth0_10'] = {
  'name': 'DYnorm_R_0j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.893/1.120',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth0_10'] 
}

nuisances['DYnorm_Acc_0j_ee_hww2l2v_13TeV_0j_ee_pth0_10'] = {
  'name': 'DYnorm_Acc_0j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.632/1.582',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth0_10'] 
}

# 0j_mm channel 
nuisances['DYnorm_k_0j_mm_hww2l2v_13TeV_0j_mm_pth10_200'] = {
  'name': 'DYnorm_k_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.004/0.996',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth10_200'] 
}

nuisances['DYnorm_em_0j_mm_hww2l2v_13TeV_0j_mm_pth10_200'] = {
  'name': 'DYnorm_em_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.167/0.857',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth10_200'] 
}

nuisances['DYnorm_R_0j_mm_hww2l2v_13TeV_0j_mm_pth10_200'] = {
  'name': 'DYnorm_R_0j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.862/1.160',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth10_200'] 
}

nuisances['DYnorm_Acc_0j_mm_hww2l2v_13TeV_0j_mm_pth10_200'] = {
  'name': 'DYnorm_Acc_0j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.813/1.229',
  },
  'cuts' : ['hww2l2v_13TeV_0j_mm_pth10_200'] 
}

# 0j_ee WW channel 
nuisances['DYnorm_k_0j_ee_WW_hww2l2v_13TeV_WW_0j_ee'] = {
  'name': 'DYnorm_k_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_ee'] 
}

nuisances['DYnorm_em_0j_ee_WW_hww2l2v_13TeV_WW_0j_ee'] = {
  'name': 'DYnorm_em_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.157/0.864',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_ee'] 
}

nuisances['DYnorm_R_0j_ee_WW_hww2l2v_13TeV_WW_0j_ee'] = {
  'name': 'DYnorm_R_0j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.938/1.066',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_ee'] 
}

nuisances['DYnorm_Acc_0j_ee_WW_hww2l2v_13TeV_WW_0j_ee'] = {
  'name': 'DYnorm_Acc_0j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.796/1.256',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_ee'] 
}

# 0j_ee channel 
nuisances['DYnorm_k_0j_ee_hww2l2v_13TeV_0j_ee_pth10_200'] = {
  'name': 'DYnorm_k_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.003/0.997',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth10_200'] 
}

nuisances['DYnorm_em_0j_ee_hww2l2v_13TeV_0j_ee_pth10_200'] = {
  'name': 'DYnorm_em_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.157/0.864',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth10_200'] 
}

nuisances['DYnorm_R_0j_ee_hww2l2v_13TeV_0j_ee_pth10_200'] = {
  'name': 'DYnorm_R_0j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.893/1.120',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth10_200'] 
}

nuisances['DYnorm_Acc_0j_ee_hww2l2v_13TeV_0j_ee_pth10_200'] = {
  'name': 'DYnorm_Acc_0j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.805/1.243',
  },
  'cuts' : ['hww2l2v_13TeV_0j_ee_pth10_200'] 
}

# 2j_mm channel 
nuisances['DYnorm_k_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] 
}

nuisances['DYnorm_em_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] 
}

nuisances['DYnorm_R_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.932/1.073',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] 
}

nuisances['DYnorm_Acc_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.241/4.147',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj25'] 
}

# 2j_mm channel 
nuisances['DYnorm_k_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] 
}

nuisances['DYnorm_em_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] 
}

nuisances['DYnorm_R_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.932/1.073',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] 
}

nuisances['DYnorm_Acc_2j_mm_hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.269/3.721',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj700_pthjj0_25'] 
}

# 0j_mm WW channel 
nuisances['DYnorm_k_0j_mm_WW_hww2l2v_13TeV_WW_0j_mm'] = {
  'name': 'DYnorm_k_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_mm'] 
}

nuisances['DYnorm_em_0j_mm_WW_hww2l2v_13TeV_WW_0j_mm'] = {
  'name': 'DYnorm_em_0j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.167/0.857',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_mm'] 
}

nuisances['DYnorm_R_0j_mm_WW_hww2l2v_13TeV_WW_0j_mm'] = {
  'name': 'DYnorm_R_0j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.962/1.040',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_mm'] 
}

nuisances['DYnorm_Acc_0j_mm_WW_hww2l2v_13TeV_WW_0j_mm'] = {
  'name': 'DYnorm_Acc_0j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.832/1.202',
  },
  'cuts' : ['hww2l2v_13TeV_WW_0j_mm'] 
}

# 1j_mm channel 
nuisances['DYnorm_k_1j_mm_hww2l2v_13TeV_1j_mm_pth0_60'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth0_60'] 
}

nuisances['DYnorm_em_1j_mm_hww2l2v_13TeV_1j_mm_pth0_60'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.099/0.910',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth0_60'] 
}

nuisances['DYnorm_R_1j_mm_hww2l2v_13TeV_1j_mm_pth0_60'] = {
  'name': 'DYnorm_R_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.936/1.069',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth0_60'] 
}

nuisances['DYnorm_Acc_1j_mm_hww2l2v_13TeV_1j_mm_pth0_60'] = {
  'name': 'DYnorm_Acc_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.760/1.317',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth0_60'] 
}

# 2j_ee WW channel 
nuisances['DYnorm_k_2j_ee_WW_hww2l2v_13TeV_WW_2j_ee'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_ee'] 
}

nuisances['DYnorm_em_2j_ee_WW_hww2l2v_13TeV_WW_2j_ee'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.185/0.844',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_ee'] 
}

nuisances['DYnorm_R_2j_ee_WW_hww2l2v_13TeV_WW_2j_ee'] = {
  'name': 'DYnorm_R_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.940/1.064',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_ee'] 
}

nuisances['DYnorm_Acc_2j_ee_WW_hww2l2v_13TeV_WW_2j_ee'] = {
  'name': 'DYnorm_Acc_2j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.715/1.398',
  },
  'cuts' : ['hww2l2v_13TeV_WW_2j_ee'] 
}

# hpt_ee channel 
nuisances['DYnorm_k_hpt_ee_hww2l2v_13TeV_hpt_ee_pth650'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth650'] 
}

nuisances['DYnorm_em_hpt_ee_hww2l2v_13TeV_hpt_ee_pth650'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth650'] 
}

nuisances['DYnorm_R_hpt_ee_hww2l2v_13TeV_hpt_ee_pth650'] = {
  'name': 'DYnorm_R_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.873/1.146',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth650'] 
}

nuisances['DYnorm_Acc_hpt_ee_hww2l2v_13TeV_hpt_ee_pth650'] = {
  'name': 'DYnorm_Acc_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.002/485.709',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth650'] 
}

# 2j_mm channel 
nuisances['DYnorm_k_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_k_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] 
}

nuisances['DYnorm_em_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_em_2j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.187/0.843',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] 
}

nuisances['DYnorm_R_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_R_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.932/1.073',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] 
}

nuisances['DYnorm_Acc_2j_mm_hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] = {
  'name': 'DYnorm_Acc_2j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.479/2.086',
  },
  'cuts' : ['hww2l2v_13TeV_2j_mm_mjj350_700_pthjj0_25'] 
}

# hpt_mm WW channel 
nuisances['DYnorm_k_hpt_mm_WW_hww2l2v_13TeV_WW_hpt_mm'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.000/1.000',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_mm'] 
}

nuisances['DYnorm_em_hpt_mm_WW_hww2l2v_13TeV_WW_hpt_mm'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_mm'] 
}

nuisances['DYnorm_R_hpt_mm_WW_hww2l2v_13TeV_WW_hpt_mm'] = {
  'name': 'DYnorm_R_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.958/1.043',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_mm'] 
}

nuisances['DYnorm_Acc_hpt_mm_WW_hww2l2v_13TeV_WW_hpt_mm'] = {
  'name': 'DYnorm_Acc_hpt_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.883/1.132',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_mm'] 
}

# 1j_mm channel 
nuisances['DYnorm_k_1j_mm_hww2l2v_13TeV_1j_mm_pth60_120'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth60_120'] 
}

nuisances['DYnorm_em_1j_mm_hww2l2v_13TeV_1j_mm_pth60_120'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.099/0.910',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth60_120'] 
}

nuisances['DYnorm_R_1j_mm_hww2l2v_13TeV_1j_mm_pth60_120'] = {
  'name': 'DYnorm_R_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.936/1.069',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth60_120'] 
}

nuisances['DYnorm_Acc_1j_mm_hww2l2v_13TeV_1j_mm_pth60_120'] = {
  'name': 'DYnorm_Acc_1j_mm_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.399/2.504',
  },
  'cuts' : ['hww2l2v_13TeV_1j_mm_pth60_120'] 
}

# hpt_ee WW channel 
nuisances['DYnorm_k_hpt_ee_WW_hww2l2v_13TeV_WW_hpt_ee'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.000/1.000',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_ee'] 
}

nuisances['DYnorm_em_hpt_ee_WW_hww2l2v_13TeV_WW_hpt_ee'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_ee'] 
}

nuisances['DYnorm_R_hpt_ee_WW_hww2l2v_13TeV_WW_hpt_ee'] = {
  'name': 'DYnorm_R_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.938/1.067',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_ee'] 
}

nuisances['DYnorm_Acc_hpt_ee_WW_hww2l2v_13TeV_WW_hpt_ee'] = {
  'name': 'DYnorm_Acc_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.833/1.200',
  },
  'cuts' : ['hww2l2v_13TeV_WW_hpt_ee'] 
}

# 1j_ee channel 
nuisances['DYnorm_k_1j_ee_hww2l2v_13TeV_1j_ee_pth0_60'] = {
  'name': 'DYnorm_k_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.002/0.998',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth0_60'] 
}

nuisances['DYnorm_em_1j_ee_hww2l2v_13TeV_1j_ee_pth0_60'] = {
  'name': 'DYnorm_em_1j_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.102/0.908',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth0_60'] 
}

nuisances['DYnorm_R_1j_ee_hww2l2v_13TeV_1j_ee_pth0_60'] = {
  'name': 'DYnorm_R_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.902/1.108',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth0_60'] 
}

nuisances['DYnorm_Acc_1j_ee_hww2l2v_13TeV_1j_ee_pth0_60'] = {
  'name': 'DYnorm_Acc_1j_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.674/1.485',
  },
  'cuts' : ['hww2l2v_13TeV_1j_ee_pth0_60'] 
}

# hpt_ee channel 
nuisances['DYnorm_k_hpt_ee_hww2l2v_13TeV_hpt_ee_pth200_300'] = {
  'name': 'DYnorm_k_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.001/0.999',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth200_300'] 
}

nuisances['DYnorm_em_hpt_ee_hww2l2v_13TeV_hpt_ee_pth200_300'] = {
  'name': 'DYnorm_em_hpt_2016',
  'type': 'lnN',
  'samples': {
    'DY': '1.029/0.972',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth200_300'] 
}

nuisances['DYnorm_R_hpt_ee_hww2l2v_13TeV_hpt_ee_pth200_300'] = {
  'name': 'DYnorm_R_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.873/1.146',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth200_300'] 
}

nuisances['DYnorm_Acc_hpt_ee_hww2l2v_13TeV_hpt_ee_pth200_300'] = {
  'name': 'DYnorm_Acc_hpt_ee_2016',
  'type': 'lnN',
  'samples': {
    'DY': '0.316/3.169',
  },
  'cuts' : ['hww2l2v_13TeV_hpt_ee_pth200_300'] 
}


for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))


try:
  for iNP in nuisances:
    if 'cuts' in nuisances[iNP] :
      newCuts = []
      for iCut in nuisances[iNP]['cuts']:
        for iOptim in optim:
           #newCuts.append(iCut+'_'+iOptim)
           newCuts.append(iCut)
      nuisances[iNP]['cuts'] = newCuts
except:
  print "No optim dictionary"
