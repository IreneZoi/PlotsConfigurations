import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(directory_bkg, 'Summer16_102X_nAODv7_Full2016v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')

samples={}

# Steps
mcSteps   = 'MCl1loose2016v7__MCCorr2016v7__MCCombJJLNu2016' 
dataSteps = 'DATAl1loose2016v7__DATACombJJLNu2016'
fakeSteps = 'DATAl1loose2016v7__DATACombJJLNu2016'

##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'

directory_bkg    = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_skim/' + mcSteps
directory_mc    = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_skim/' + mcSteps
directory_signal = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_skim/' + mcSteps
directory_fakes  = treeBaseDir_SMP + 'Run2016_102X_nAODv7_Full2016v7_skim/'  + fakeSteps
directory_data   = treeBaseDir_SMP + 'Run2016_102X_nAODv7_Full2016v7_skim/'  + dataSteps
directory_signalIZ = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7/' + mcSteps

wjets_res_bins = []
directory_wjets_res_bins = {}
nfiles_wjets = [4,4,5,6,8,8,4,4,5,6,8,8,5,5,6,8,8,8,8,8,8]
for i in range(1, 22):
  wjbin = "Wjets_res_{}".format(i)
  wjets_res_bins.append(wjbin)
  directory_wjets_res_bins[wjbin] = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7_WjetsBins_skim/res_bin_{}/'.format(i) + mcSteps

print "Wjets bins: ", wjets_res_bins
print directory_wjets_res_bins
################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='1'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################
  
eleWP='mva_90p_Iso2016'
muWP='cut_Tight80x'

LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight   = 'XSWeight'
SFweight1l = [ 'puWeight', 'SingleLepton_trigEff_corrected[0]',
              'Lepton_RecoSF[0]', 'EMTFbug_veto', 
              LepWPWeight_1l, LepWPCut_1l,
              'PrefireWeight','PUJetIdSF', 
              'btagSF', 'BoostedWtagSF_nominal']

SFweight = '*'.join(SFweight1l)
     
GenLepMatch   = 'Lepton_genmatched[0]'


####
# NVTX reweighting
#SFweight += '*nvtx_reweighting'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2016B-02Apr2020_ver2-v1'],
    ['C','Run2016C-02Apr2020-v1'],
    ['D','Run2016D-02Apr2020-v1'],
    ['E','Run2016E-02Apr2020-v1'],
    ['F','Run2016F-02Apr2020-v1'],
    ['G','Run2016G-02Apr2020-v1'],
    ['H','Run2016H-02Apr2020-v1']
]

DataSets = ['SingleMuon','SingleElectron']


DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl',
}


###########################################
#############  BACKGROUNDS  ###############
###########################################

############ DY ############

# DY_photon_filter = '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))'
DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'


samples['DY'] = {    'name'   :   #nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50-LO_ext1')
                                  nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_ext2') 
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-10to50')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-10to50_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-70to100')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-100to200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-200to400')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-400to600')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-600toinf')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-5to50_HT-600toinf_ext1'),
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+DY_photon_filter+'*btagSF_corr_DY'  ,
                       'FilesPerJob' : 6,
                       'EventsPerJob' : 80000,
                       'suppressNegative' :['all'],
                       'suppressNegativeNuisances' :['all'],
                   }
#addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO-ext1','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')

CombineBaseW(samples, 'DY', ['DYJetsToLL_M-10to50', 'DYJetsToLL_M-10to50_ext1'])
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50_ext1','DY_NLO_pTllrw')

CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-100to200', 'DYJetsToLL_M-50_HT-100to200_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-200to400', 'DYJetsToLL_M-50_HT-200to400_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-400to600', 'DYJetsToLL_M-50_HT-400to600_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-200to400', 'DYJetsToLL_M-5to50_HT-200to400_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-400to600', 'DYJetsToLL_M-5to50_HT-400to600_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-5to50_HT-600toinf', 'DYJetsToLL_M-5to50_HT-600toinf_ext1'])

#addSampleWeight(samples,'DY','DYJetsToLL_M-50-LO_ext1',            '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',               '(LHE_HT < 70)') # last M50 HT bin is missing
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50',                '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50_ext1',           '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100',         'DY_LO_pTllrw') # HT-binned are LO!
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_ext1',   'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1',   'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_ext1',   'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',        'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',      'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-70to100',      'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-100to200',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-200to400_ext1','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-400to600_ext1','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toinf',     'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-5to50_HT-600toinf_ext1','DY_LO_pTllrw')



############ Top ############

samples['top'] = {    
            'name'   :  
                        nanoGetSampleFiles(directory_bkg,'ST_s-channel') 
                      + nanoGetSampleFiles(directory_bkg,'ST_t-channel_antitop') 
                      + nanoGetSampleFiles(directory_bkg,'ST_t-channel_top') 
                      + nanoGetSampleFiles(directory_bkg,'ST_tW_antitop') 
                      + nanoGetSampleFiles(directory_bkg,'ST_tW_top') 
                      + nanoGetSampleFiles(directory_bkg,'TTToSemiLeptonic') 
                      + nanoGetSampleFiles(directory_bkg,'TTTo2L2Nu') 
                      + nanoGetSampleFiles(directory_bkg,'TTWJetsToLNu_ext2') 
                      + nanoGetSampleFiles(directory_bkg,'TTZjets'),  
            'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_top',
            'FilesPerJob' : 5,
            'EventsPerJob' : 80000,
            'suppressNegative' :['all'],
            'suppressNegativeNuisances' :['all'],
      }

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
#addSampleWeight(samples,'top','TTZjets','Top_pTrw')
#addSampleWeight(samples,'top','TTWjets_ext1','Top_pTrw')

addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


#######################################################
### W+jets treatment

Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '

samples['Wjets_boost'] = { 'name' :   
          #nanoGetSampleFiles(directory_bkg, 'WJetsToLNu')  #NLO inclusive samples
          nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO_ext2')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT70_100')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200_ext2')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400_ext2')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600_ext1')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800_ext1')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200_ext1')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500_ext1')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf_ext1')
          ,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*'+Wjets_photon_filter + '* EWKnloW * btagSF_corr_Wjets_HT', 
        'FilesPerJob' : 4,
         'subsamples': {
            "1": '(VBS_category==0) && (w_lep_pt < 50)',
            "2": '(VBS_category==0) && (w_lep_pt >= 50 && w_lep_pt < 100)',
            "3": '(VBS_category==0) && (w_lep_pt >= 100 && w_lep_pt < 150)',
            "4": '(VBS_category==0) && (w_lep_pt >= 150 && w_lep_pt < 200)',
            "5": '(VBS_category==0) && (w_lep_pt >= 200 && w_lep_pt < 300)',
            "6": '(VBS_category==0) && (w_lep_pt >= 300 && w_lep_pt < 400)',
            "7": '(VBS_category==0) && (w_lep_pt >= 400)',
        }
       }
# No needed HT stiching corrections
#addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu', '(LHE_HT < 70)') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO_ext2', '(LHE_HT < 70)') 
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu-LO','WJetsToLNu-LO_ext2'])

CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT100_200','WJetsToLNu_HT100_200_ext2'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT200_400','WJetsToLNu_HT200_400_ext2'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT400_600','WJetsToLNu_HT400_600_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT600_800','WJetsToLNu_HT600_800_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT800_1200','WJetsToLNu_HT800_1200_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT1200_2500','WJetsToLNu_HT1200_2500_ext1'])
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu_HT2500_inf','WJetsToLNu_HT2500_inf_ext1'])

# HT bins to LO factors 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT70_100',          '1.21 * 1.0346')  #adding also k-factor
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT100_200',         '1.019') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT100_200_ext2',    '1.019') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT200_400',         '1.012') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT200_400_ext2',    '1.012') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT400_600',         '0.9945') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT400_600_ext1',    '0.9945')
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT600_800',         '0.9537') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT600_800_ext1',    '0.9537') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT800_1200',        '0.8844') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT800_1200_ext1',   '0.8844')
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT1200_2500',       '0.7643') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT1200_2500_ext1',  '0.7643') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT2500_inf',        '0.2422') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT2500_inf_ext1',   '0.2422') 

####################
#Resolved bin 
for iw, wjetbin in enumerate(wjets_res_bins):
  samples[wjetbin] = { 'name' :   
            #nanoGetSampleFiles(directory_bkg, 'WJetsToLNu')  #NLO inclusive samples
            nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu-LO')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu-LO_ext2')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT70_100')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT100_200')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT100_200_ext2')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT200_400')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT200_400_ext2')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT400_600')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT400_600_ext1')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT600_800')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT600_800_ext1')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT800_1200')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT800_1200_ext1')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT1200_2500')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT1200_2500_ext1')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT2500_inf')
            + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT2500_inf_ext1')
            ,
          'weight': "( fit_bin_res == {} )*".format(iw+1) + XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*'+Wjets_photon_filter + '* EWKnloW * btagSF_corr_Wjets_HT', 
          'FilesPerJob' : nfiles_wjets[iw],
        }
  # No needed HT stiching corrections
  addSampleWeight(samples,wjetbin, 'WJetsToLNu-LO', '(LHE_HT < 70)') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu-LO_ext2', '(LHE_HT < 70)') 
  CombineBaseW(samples, wjetbin, ['WJetsToLNu-LO','WJetsToLNu-LO_ext2'])

  CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT100_200','WJetsToLNu_HT100_200_ext2'])
  CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT200_400','WJetsToLNu_HT200_400_ext2'])
  CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT400_600','WJetsToLNu_HT400_600_ext1'])
  CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT600_800','WJetsToLNu_HT600_800_ext1'])
  CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT800_1200','WJetsToLNu_HT800_1200_ext1'])
  CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT1200_2500','WJetsToLNu_HT1200_2500_ext1'])
  CombineBaseW(samples, wjetbin, ['WJetsToLNu_HT2500_inf','WJetsToLNu_HT2500_inf_ext1'])

  # HT bins to LO factors 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT70_100',          '1.21 * 1.0346')  #adding also k-factor
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT100_200',         '1.019') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT100_200_ext2',    '1.019') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT200_400',         '1.012') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT200_400_ext2',    '1.012') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT400_600',         '0.9945') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT400_600_ext1',    '0.9945')
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT600_800',         '0.9537') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT600_800_ext1',    '0.9537') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT800_1200',        '0.8844') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT800_1200_ext1',   '0.8844')
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT1200_2500',       '0.7643') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT1200_2500_ext1',  '0.7643') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT2500_inf',        '0.2422') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT2500_inf_ext1',   '0.2422') 

# #############################################################################
# ###########################################################################


# samples['VV']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD') ,
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW',
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }

############ VVV ############

samples['VVV']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'ZZZ')
                                + nanoGetSampleFiles(directory_bkg,'WZZ')
                                + nanoGetSampleFiles(directory_bkg,'WWZ')
                                + nanoGetSampleFiles(directory_bkg,'WWW'),
                                #+ nanoGetSampleFiles(directory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW'  ,
                    'FilesPerJob' : 12,
                    'EventsPerJob' : 70000,
                  }

############## VBF-V ########

# samples['VBF-V']  = {  'name'   : nanoGetSampleFiles(directory_signal,'EWK_LNuJJ')
#                                 + nanoGetSampleFiles(directory_signal,'EWK_LLJJ'), 
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_Vg_VgS_VBFV',
#                     'FilesPerJob' : 15
#                   }

samples['VBF-V_dipole']  = {  'name'   : nanoGetSampleFiles(directory_signal,'EWK_LNuJJ_herwig')
                                       + nanoGetSampleFiles(directory_signal,'EWK_LLJJ_herwig'), 
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_Vg_VgS_VBFV',
                    'FilesPerJob' : 6
                  }

################ ggWW ##################3

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(directory_bkg,'GluGluWWToLNuQQ'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW',
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }

########################

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(directory_bkg,'Zg'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(!(Gen_ZGstar_mass > 0))*btagSF_corr_Vg_VgS_VBFV', # 14.02.2020: Changed Vg treatment
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }

#addSampleWeight(samples,'Vg','Zg','(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(directory_bkg,'Zg')
                                 + nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01'),
                                 #+ nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01_ext1'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14) *btagSF_corr_Vg_VgS_VBFV',
                      'FilesPerJob' : 15,
                      'EventsPerJob' : 80000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                
                   }
#CombineBaseW(samples, 'VgS', ['WZTo3LNu_mllmin01', 'WZTo3LNu_mllmin01_ext1'])

# 14.02.2020: Changed Vg treatment
addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')
#addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01_ext1', '(Gen_ZGstar_mass > 0.1)')

#fakeW = 'fakeW_ele_' + eleWP + '_mu_' +muWP+ '_1l_mu35_ele35'
# from alias
fakeW = 'fakeWeight_35'
#### Fakes
samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+fakeW,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 40
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(directory_data, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


##########################################
################# DATA ###################
##########################################

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 40,
                  }

for Run in DataRun :
        for DataSet in DataSets :
                FileTarget = nanoGetSampleFiles(directory_data,DataSet+'_'+Run[1])
                for iFile in FileTarget:
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])


##########################################
################ SIGNALS #################
##########################################

samples['VBS_ssWW']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil'),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :10,
       'EventsPerJob' : 70000,
}

samples['VBS_osWW']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil'),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :10,
       'EventsPerJob' : 70000,
}


samples['VBS_WZjj']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :10,
       'EventsPerJob' : 70000,
}

samples['VBS_WZll']  = { 'name' :   
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :10,
       'EventsPerJob' : 70000,
}


samples['VBS_ZZ']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :10,
       'EventsPerJob' : 70000,
}



###############################################
#############################################

samples['VV_ssWW']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
        'FilesPerJob' : 15,
        'EventsPerJob' : 70000,
}


samples['VV_osWW']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
        'FilesPerJob' : 15,
        'EventsPerJob' : 70000,
}


samples['VV_WZjj']  = { 'name' :      
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD',) ,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
        'FilesPerJob' : 15,
        'EventsPerJob' : 70000,
}


samples['VV_WZll']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
        'FilesPerJob' : 15,
        'EventsPerJob' : 70000,
}


samples['VV_ZZ']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD',  ) ,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW', # still missing EWKnlowW 
        'FilesPerJob' : 15,
        'EventsPerJob' : 70000,
}

##############################################################################################
#########      aQGC samples !!!!!!!!!!!!!
##############################################################################################
# same implementation as Matteo https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/2018_Jul22/samples.py
# samples name are crucial!! And you can run on 1 operator at the time!!
# to understand the weight numbering scheme https://github.com/singh-ramanpreet/VBS-customNanoAODProduction/blob/main/NanoAODProduction/data/initrwgt_aQGC17.header#L152
# line 152 is like zero, where this weight part starts in the document linked above. Example for cTO: the SM value is at line 187 => line 187 - line 152 = 35 => sm_cT0 = 'LHEReweightingWeight[35]'. The largest variations of +/- 2 are at line 221 & 220: 221(0) -152 = 69(8).
# calculation for weights and coefficients as in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2020_204_v6.pdf
# but for k = 2 -> i.e. LinReweight_cT0 = '(0.5 * 1/k * (LHEReweightingWeight[69] - LHEReweightingWeight[68]) )'
# also, xsec saved in the samples are wrong and Jay updated them -> samples need to be rescaled by xsec_Jay/xsec_mcm
# --------------------------------------------------- from a screenshoot that Matteo gave me ---------
# aQGC sample cross sections | old CUE (xsec_mcm) | new CUE..  | CP5 (xsec_jay)|
# W+(Iv)W-(ji)               |        17.99       |   4.174    |     3.21      |
# W-(Iv)W+()                 |        17.91       |   4.173    |     3.205     |
# W+(Iv)W+(ji)               |        3.453       |   0.782    |     0.7297    | 
# W-(Iv)W-(i)                |        0.5065      |   0.143    |     0.08887   |
# W+(IV)Z(])                 |        1.896       |   0.4556   |     0.3992    |
# W-(IV)Z(j)                 |        0.7416      |   0.1963   |     0.1383    |
# Z(I)W+ (ji)                |        0.569       |   0.1365   |     0.1199    |
# Z(1)W-(ji)                 |        0.2222      |   0.05862  |     0.04146   |  
# Z(Il)Z(i)                  |        3.361       |   0.799    |     0.6361    | 
# ------------------------------------------------------------------------------
# also, signal samples with a W and a Z were wrongly produced including also tZq and similar diagrams. To avoid their inclusion, the filter (Sum$(abs(GenPart_pdgId)==6)==0) is added at Gen level

# /eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Samples/NanoAOD/aQGCs/2016/WplusTo2LZTo2JJJ_EWK_LO_aQGC_MJJ100PTJ10_TuneCP5_13TeV-madgraph-pythia8/ missing for 2016


############     -----------------             FT0          -----------------    ############

sm_cT0 = 'LHEReweightingWeight[35]'
LinReweight_cT0 = '(0.5 * 0.5 * (LHEReweightingWeight[69] - LHEReweightingWeight[68]) )'
quadReweight_cT0 = '(0.5 * 0.5 * 0.5 * (LHEReweightingWeight[69] + LHEReweightingWeight[68] - 2*LHEReweightingWeight[35]) )'
LinQuadReweight_cT0 = '(0.5 * 0.5 * (LHEReweightingWeight[69] - LHEReweightingWeight[68]) ) + (0.5 * 0.5 * 0.5 * (LHEReweightingWeight[69] + LHEReweightingWeight[68] - 2*LHEReweightingWeight[35]) )'

#default coupling, quadratic EFT
samples['quad_cT0']  = { 'name' :  
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC'),   #VBS_WZjj
#                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC'),   #VBS_WZjj
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT0,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}
xsweight_new_WpToLNu_WmTo2J='3.21'
xsweight_mcm_WpToLNu_WmTo2J='17.99'
addSampleWeight(samples,'quad_cT0','WpToLNu_WmTo2J_aQGC',xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J) #VBS_osWW
xsweight_new_WpTo2J_WmToLNu='3.205'
xsweight_mcm_WpTo2J_WmToLNu='17.91'
addSampleWeight(samples,'quad_cT0','WpTo2J_WmToLNu_aQGC',xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu) #VBS_osWW

xsweight_new_WpToLNu_WpTo2J='0.7297'
xsweight_mcm_WpToLNu_WpTo2J='3.453'
addSampleWeight(samples,'quad_cT0','WpToLNu_WpTo2J_aQGC',xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J) #VBS_ssWW
xsweight_new_WmToLNu_WmTo2J='0.08887'
xsweight_mcm_WmToLNu_WmTo2J='0.5065'
addSampleWeight(samples,'quad_cT0','WmToLNu_WmTo2J_aQGC',xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J) #VBS_ssWW

xsweight_new_WmToLNu_ZTo2J='0.1383'
xsweight_mcm_WmToLNu_ZTo2J='0.7416'
addSampleWeight(samples,'quad_cT0','WmToLNu_ZTo2J_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J) #VBS_WZjj
xsweight_new_WpToLNu_ZTo2J='0.3992'
xsweight_mcm_WpToLNu_ZTo2J='1.896'
#addSampleWeight(samples,'quad_cT0','WpToLNu_ZTo2J_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J) #VBS_WZjj

# SM + lin + quad 
samples['sm_lin_quad_cT0'] = {
   'name':   nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J')      #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu')      #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J')      #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J')      #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J')      #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J'),      #VBS_WZjj
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cT0','WpToLNu_WmTo2J_aQGC', xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J+' * ' + LinQuadReweight_cT0 ) #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_WmToLNu_aQGC', xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu+' * ' + LinQuadReweight_cT0 ) #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT0','WpToLNu_WmTo2J',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_WmToLNu',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT0','WpToLNu_WpTo2J_aQGC', xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J+' * ' + LinQuadReweight_cT0 ) #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT0','WmToLNu_WmTo2J_aQGC', xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J+' * ' + LinQuadReweight_cT0 ) #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT0','WpToLNu_WpTo2J',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT0','WmToLNu_WmTo2J',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT0','WmToLNu_ZTo2J_aQGC', '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J+' * ' + LinQuadReweight_cT0 ) #VBS_WZjj
# addSampleWeight(samples,'sm_lin_quad_cT0','WpToLNu_ZTo2J_aQGC', '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J+' * ' + LinQuadReweight_cT0 ) #VBS_WZjj
addSampleWeight(samples,'sm_lin_quad_cT0','WmToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
addSampleWeight(samples,'sm_lin_quad_cT0','WpToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj

############     -----------------             FT2          -----------------    ############

sm_cT2 = 'LHEReweightingWeight[70]'
LinReweight_cT2 = '(0.5 * (1/4.5) * (LHEReweightingWeight[104] - LHEReweightingWeight[103]) )'
quadReweight_cT2 = '(0.5 * (1/4.5) * (1/4.5) * (LHEReweightingWeight[104] + LHEReweightingWeight[103] - 2*LHEReweightingWeight[70]) )'
LinQuadReweight_cT2 = '(0.5 * (1/4.5) * (LHEReweightingWeight[104] - LHEReweightingWeight[103]) ) + (0.5 * (1/4.5) * (1/4.5) * (LHEReweightingWeight[104] + LHEReweightingWeight[103] - 2*LHEReweightingWeight[70]) )'


#default coupling, quadratic EFT
samples['quad_cT2']  = { 'name' :  
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC'),   #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC'),  #VBS_WZjj
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT2,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}
xsweight_new_WpToLNu_WmTo2J='3.21'
xsweight_mcm_WpToLNu_WmTo2J='17.99'
addSampleWeight(samples,'quad_cT2','WpToLNu_WmTo2J_aQGC',xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J) #VBS_osWW
xsweight_new_WpTo2J_WmToLNu='3.205'
xsweight_mcm_WpTo2J_WmToLNu='17.91'
addSampleWeight(samples,'quad_cT2','WpTo2J_WmToLNu_aQGC',xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu) #VBS_osWW

xsweight_new_WpToLNu_WpTo2J='0.7297'
xsweight_mcm_WpToLNu_WpTo2J='3.453'
addSampleWeight(samples,'quad_cT2','WpToLNu_WpTo2J_aQGC',xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J) #VBS_ssWW
xsweight_new_WmToLNu_WmTo2J='0.08887'
xsweight_mcm_WmToLNu_WmTo2J='0.5065'
addSampleWeight(samples,'quad_cT2','WmToLNu_WmTo2J_aQGC',xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J) #VBS_ssWW

xsweight_new_WmToLNu_ZTo2J='0.1383'
xsweight_mcm_WmToLNu_ZTo2J='0.7416'
addSampleWeight(samples,'quad_cT2','WmToLNu_ZTo2J_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J) #VBS_WZjj
xsweight_new_WpToLNu_ZTo2J='0.3992'
xsweight_mcm_WpToLNu_ZTo2J='1.896'
# addSampleWeight(samples,'quad_cT2','WpToLNu_ZTo2J_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J) #VBS_WZjj

# SM + lin + quad 
samples['sm_lin_quad_cT2'] = {
   'name':   nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J')      #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu')      #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J')      #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J')      #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J')       #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J'),      #VBS_WZjj
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cT2','WpToLNu_WmTo2J_aQGC', xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J+' * ' + LinQuadReweight_cT2 ) #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_WmToLNu_aQGC', xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu+' * ' + LinQuadReweight_cT2 ) #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT2','WpToLNu_WmTo2J',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_WmToLNu',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
addSampleWeight(samples,'sm_lin_quad_cT2','WpToLNu_WpTo2J_aQGC', xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J+' * ' + LinQuadReweight_cT2 ) #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT2','WmToLNu_WmTo2J_aQGC', xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J+' * ' + LinQuadReweight_cT2 ) #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT2','WpToLNu_WpTo2J',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT2','WmToLNu_WmTo2J',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
addSampleWeight(samples,'sm_lin_quad_cT2','WmToLNu_ZTo2J_aQGC', '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J+' * ' + LinQuadReweight_cT2 ) #VBS_WZjj
# addSampleWeight(samples,'sm_lin_quad_cT2','WpToLNu_ZTo2J_aQGC', '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J+' * ' + LinQuadReweight_cT2 ) #VBS_WZjj
addSampleWeight(samples,'sm_lin_quad_cT2','WmToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
addSampleWeight(samples,'sm_lin_quad_cT2','WpToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj


############     -----------------             sm          -----------------    ############

samples['sm'] ={ # should not use dipole recoil for aqgc SM part
  'name' :  nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J') + #VBS_ssWW
            nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J') + #VBS_ssWW
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J') + #VBS_osWW
            nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu') + #VBS_osWW
            nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J')  + #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J'),  #VBS_WZjj
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, #+'*btagSF_corr_VBS',
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

#samples = {   key:v for key,v in samples.items() if key in ['sm','quad_cT0','sm_lin_quad_cT0','quad_cT0','sm_lin_quad_cT2']}

VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]
VBS_aQGC_all_samples = ['sm','quad_cT0','sm_lin_quad_cT0','quad_cT2','sm_lin_quad_cT2']
VBS_aQGC_cT0_samples = ['sm','quad_cT0','sm_lin_quad_cT0']
VBS_aQGC_cT2_samples = ['sm','quad_cT2','sm_lin_quad_cT2']


samples = {   key:v for key,v in samples.items() if key not in VBS_samples + VBS_aQGC_cT2_samples } #and 'Fake' not in key}
#samples = {   key:v for key,v in samples.items() if 'sm' == key} # in VBS_aQGC_cT0_samples }
