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
  treeBaseDir_FNAL = '/store/group/lnujj/aQGC_VVJJ_Private_Production_PreProcessing/'
  xrootdPath='root://cmseos.fnal.gov/'


directory_bkg    = treeBaseDir + 'Summer16_102X_nAODv7_Full2016v7/' + mcSteps
directory_mc    = treeBaseDir + 'Summer16_102X_nAODv7_Full2016v7/' + mcSteps
directory_signal = treeBaseDir_SMP + 'Summer16_102X_nAODv7_Full2016v7/' + mcSteps
directory_signalIZ =  xrootdPath + treeBaseDir_FNAL + 'Summer16_102X_nAODv7_Full2016v7/' + mcSteps

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
              ]#'btagSF', 'BoostedWtagSF_nominal'

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

DY_photon_filter = '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))'

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
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+DY_photon_filter  ,
                       'FilesPerJob' : 9,
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
            'weight' :  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
            'FilesPerJob' : 10,
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


samples['Wjets_HT'] = { 'name' :   
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
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* EWKnloW', 
        'FilesPerJob' : 10,
        #  'subsamples': {
        #     "res_1": '(VBS_category==1) && (w_lep_pt < 100)',
        #     "res_2": '(VBS_category==1) && (w_lep_pt >= 100 && w_lep_pt < 200)',
        #     "res_3": '(VBS_category==1) && (w_lep_pt >= 200 && w_lep_pt < 300)',
        #     "res_4": '(VBS_category==1) && (w_lep_pt >= 300 && w_lep_pt < 400)',
        #     "res_5": '(VBS_category==1) && (w_lep_pt >= 400 && w_lep_pt < 500)',
        #     "res_6": '(VBS_category==1) && (w_lep_pt >= 500)',
        #     "boost_1": '(VBS_category==0) && (w_lep_pt < 75)',
        #     "boost_2": '(VBS_category==0) && (w_lep_pt >= 75 && w_lep_pt < 150)',
        #     "boost_3": '(VBS_category==0) && (w_lep_pt >= 150 && w_lep_pt < 250)',
        #     "boost_4": '(VBS_category==0) && (w_lep_pt >= 250 && w_lep_pt < 400)',
        #     "boost_5": '(VBS_category==0) && (w_lep_pt >= 400)',
        # }
       }

# No needed HT stiching corrections
#addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu', '(LHE_HT < 70)') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO_ext2', '(LHE_HT < 70)') 
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu-LO','WJetsToLNu-LO_ext2'])

CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu_HT100_200','WJetsToLNu_HT100_200_ext2'])
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu_HT200_400','WJetsToLNu_HT200_400_ext2'])
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu_HT400_600','WJetsToLNu_HT400_600_ext1'])
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu_HT600_800','WJetsToLNu_HT600_800_ext1'])
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu_HT800_1200','WJetsToLNu_HT800_1200_ext1'])
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu_HT1200_2500','WJetsToLNu_HT1200_2500_ext1'])
CombineBaseW(samples, 'Wjets_HT', ['WJetsToLNu_HT2500_inf','WJetsToLNu_HT2500_inf_ext1'])

# HT bins to LO factors 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70_100',          '1.21 * 1.0346')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100_200',         '1.019') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100_200_ext2',    '1.019') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200_400',         '1.012') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200_400_ext2',    '1.012') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400_600',         '0.9945') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400_600_ext1',    '0.9945')
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600_800',         '0.9537') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600_800_ext1',    '0.9537') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800_1200',        '0.8844') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800_1200_ext1',   '0.8844')
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200_2500',       '0.7643') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200_2500_ext1',  '0.7643') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500_inf',        '0.2422') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500_inf_ext1',   '0.2422') 

######################################################## 


samples['VV']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD') ,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
        'FilesPerJob' : 15,
        'EventsPerJob' : 70000,
}

############ VVV ############

samples['VVV']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'ZZZ')
                                + nanoGetSampleFiles(directory_bkg,'WZZ')
                                + nanoGetSampleFiles(directory_bkg,'WWZ')
                                + nanoGetSampleFiles(directory_bkg,'WWW'),
                                #+ nanoGetSampleFiles(directory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch  ,
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }

############## VBF-V ########

samples['VBF-V']  = {  'name'   : nanoGetSampleFiles(directory_bkg,'EWK_LNuJJ')
                                + nanoGetSampleFiles(directory_bkg,'EWK_LLJJ'), 
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' : 15
                  }

################ ggWW ##################3

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(directory_bkg,'GluGluWWToLNuQQ'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }

########################

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(directory_bkg,'Zg'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(!(Gen_ZGstar_mass > 0))', # 14.02.2020: Changed Vg treatment
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
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
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

##########################################
################ SIGNALS #################
##########################################


samples['VBS']  = { 'name' :  
                 nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L')
               + nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J')
               + nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J')
               + nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu')
               + nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L')
               + nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J') 
               + nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J')
               + nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J') 
               + nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J' ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
       'FilesPerJob' : 15,
        'EventsPerJob' : 70000,
}



#************          EFT samples       ************#
# new development from Matteo calulating all reweights in another input file
with open('/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/EFTcoefficients/EFT_dim8_dictionary_v2.py') as f:
    code = compile(f.read(), 'EFT_dim8_dictionary_v2.py', 'exec')
    exec(code)
    
smReweight = operators['cS0']['sm']
samples['sm'] = {
    'name': nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WmTo2J_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpTo2J_WmToLNu_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WpTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_WmTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_ZTo2J_aQGC_Aug2024')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_ZTo2J_aQGC_Aug2024'),  #VBS_WZjj
    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
    # 'EventsPerJob': 100000,
    'FilesPerJob': 2
}
addSampleWeight(samples, 'sm', 'WpToLNu_WmTo2J_aQGC_Aug2024', smReweight)
addSampleWeight(samples, 'sm', 'WpTo2J_WmToLNu_aQGC_Aug2024', smReweight)
addSampleWeight(samples, 'sm', 'WpToLNu_WpTo2J_aQGC_Aug2024', smReweight)
addSampleWeight(samples, 'sm', 'WmToLNu_WmTo2J_aQGC_Aug2024', smReweight)
addSampleWeight(samples, 'sm', 'WmToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
addSampleWeight(samples, 'sm', 'WpToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)


for operator, expressions in operators.items():
    # Adding the quadratic sample for each operator:
    samples['quad_'+operator] = { 'name':  
             nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WmTo2J_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpTo2J_WmToLNu_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WpTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_WmTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_ZTo2J_aQGC_Aug2024')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_ZTo2J_aQGC_Aug2024'),  #VBS_WZjj
 
        'weight':  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
        'FilesPerJob': 2
    }
    
    quadReweight = expressions['quadReweight']
    
    addSampleWeight(samples, 'quad_'+operator, 'WpToLNu_WmTo2J_aQGC_Aug2024', quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WpTo2J_WmToLNu_aQGC_Aug2024', quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WpToLNu_WpTo2J_aQGC_Aug2024', quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WmToLNu_WmTo2J_aQGC_Aug2024', quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WmToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WpToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)

    # Adding sm_lin_quad sample for each operator:
    smLinQuadReweight = expressions['sm'] + expressions['LinReweight'] + expressions['quadReweight']
    samples['sm_lin_quad_'+operator] = { 'name':
             nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WmTo2J_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpTo2J_WmToLNu_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WpTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_WmTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_ZTo2J_aQGC_Aug2024')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_ZTo2J_aQGC_Aug2024'),  #VBS_WZjj
        'weight':  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
        'FilesPerJob': 2
    }
    addSampleWeight(samples, 'sm_lin_quad_'+operator, 'WpToLNu_WmTo2J_aQGC_Aug2024', smLinQuadReweight)
    addSampleWeight(samples, 'sm_lin_quad_'+operator, 'WpTo2J_WmToLNu_aQGC_Aug2024', smLinQuadReweight)
    addSampleWeight(samples, 'sm_lin_quad_'+operator, 'WpToLNu_WpTo2J_aQGC_Aug2024', smLinQuadReweight)
    addSampleWeight(samples, 'sm_lin_quad_'+operator, 'WmToLNu_WmTo2J_aQGC_Aug2024', smLinQuadReweight)
    addSampleWeight(samples, 'sm_lin_quad_'+operator, 'WmToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight)
    addSampleWeight(samples, 'sm_lin_quad_'+operator, 'WpToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight)

    smReweight = expressions['sm']
    samples['sm_'+operator] = { 'name':
             nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WmTo2J_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpTo2J_WmToLNu_aQGC_Aug2024') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_WpTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_WmTo2J_aQGC_Aug2024') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ, 'WmToLNu_ZTo2J_aQGC_Aug2024')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ, 'WpToLNu_ZTo2J_aQGC_Aug2024'),  #VBS_WZjj
        'weight':  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
        'FilesPerJob': 2
    }
    addSampleWeight(samples, 'sm_'+operator, 'WpToLNu_WmTo2J_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WpTo2J_WmToLNu_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WpToLNu_WpTo2J_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WmToLNu_WmTo2J_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WmToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WpToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)

    
theOperators = ["cT0", "cT1", "cT2", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cS1", "S2", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
full_operators_name = []
for op in theOperators:
    #  full_operators_name.append("sm_"+op)
     full_operators_name.append("quad_"+op)
     full_operators_name.append("sm_lin_quad_"+op)
full_operators_name.append("sm")
samples = {   key:v for key,v in samples.items() if key in full_operators_name}