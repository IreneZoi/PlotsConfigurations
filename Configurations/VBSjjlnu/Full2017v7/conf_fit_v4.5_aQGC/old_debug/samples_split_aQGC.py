import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

############################################
############ MORE MC STAT ##################
############################################

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(directory_bkg, 'Fall2017_102X_nAODv7_Full2017v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')

##############################################
###### Tree Directory according to site ######
##############################################

samples={}


# Steps
mcSteps   = 'MCl1loose2017v7__MCCorr2017v7__MCCombJJLNu2017' 
dataSteps = 'DATAl1loose2017v7__DATACombJJLNu2017'
fakeSteps = 'DATAl1loose2017v7__DATACombJJLNu2017'

##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW205/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'

directory_bkg    = treeBaseDir_SMP + 'Fall2017_102X_nAODv7_Full2017v7_skim/' + mcSteps
directory_mc    = treeBaseDir_SMP +  'Fall2017_102X_nAODv7_Full2017v7_skim/' + mcSteps
directory_signal = treeBaseDir_SMP + 'Fall2017_102X_nAODv7_Full2017v7_skim/' + mcSteps
directory_signalIZ = treeBaseDir_SMP + 'Fall2017_102X_nAODv7_Full2017v7/' + mcSteps
directory_fakes  = treeBaseDir_SMP + 'Run2017_102X_nAODv7_Full2017v7_skim/'  + fakeSteps
directory_data   = treeBaseDir_SMP + 'Run2017_102X_nAODv7_Full2017v7_skim/'  + dataSteps

wjets_res_bins = []
directory_wjets_res_bins = {}
nfiles_wjets = [4,4,5,6,8,8,4,4,5,6,8,8,5,5,6,8,8,8,8,8,8]
for i in range(1, 22):
  wjbin = "Wjets_res_{}".format(i)
  wjets_res_bins.append(wjbin)
  directory_wjets_res_bins[wjbin] = treeBaseDir_SMP + 'Fall2017_102X_nAODv7_Full2017v7_WjetsBins_skim/res_bin_{}/'.format(i) + mcSteps

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

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'


LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight   = 'XSWeight'

SFweight1l = [ 'puWeight_noeras[0]', 'SingleLepton_trigEff_corrected[0]',
              'Lepton_RecoSF[0]','EMTFbug_veto', LepWPWeight_1l, LepWPCut_1l,
              'PrefireWeight', 'PUJetIdSF',
              'btagSF',  'BoostedWtagSF_nominal']

SFweight = '*'.join(SFweight1l)

GenLepMatch   = 'Lepton_genmatched[0]'



################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2017B-02Apr2020-v1'] ,
            ['C','Run2017C-02Apr2020-v1'] ,
            ['D','Run2017D-02Apr2020-v1'] ,
            ['E','Run2017E-02Apr2020-v1'] ,
            ['F','Run2017F-02Apr2020-v1']
          ]

DataSets = ['SingleMuon','SingleElectron']

DataTrig = {
            'SingleMuon'     : 'Trigger_sngMu' ,
            'SingleElectron' : '!Trigger_sngMu && ele_passHLT' 
}

###########################################
#############  BACKGROUNDS  ###############
##########################################

########### DY ############

DY_photons_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY'] = {    'name'   :   nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50') 
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-10to50-LO_ext1')
                                  #+ nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200_newpmx') 
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600_newpmx') 
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-100to200_newpmx')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-200to400_newpmx')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-600toInf')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-600toInf_ext1') ,
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+"*"+DY_photons_filter  +'*btagSF_corr_DY',
                       'FilesPerJob' : 8,
                       'EventsPerJob' : 80000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                   }
                   
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext1'])
addSampleWeight(samples,'DY','DYJetsToLL_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext1','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw')

CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-200to400', 'DYJetsToLL_M-50_HT-200to400_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-4to50_HT-400to600', 'DYJetsToLL_M-4to50_HT-400to600_ext1'])
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-4to50_HT-600toInf', 'DYJetsToLL_M-4to50_HT-600toInf_ext1'])
addSampleWeight(samples,'DY','DYJetsToLL_M-50',                      '(LHE_HT < 200)')  # To put 100 when HT100to200 is back
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext1',                 '(LHE_HT < 200)') # To put 100 when HT100to200 is back
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1',               '(LHE_HT < 100)')
#addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_newpmx',   'DY_LO_pTllrw * 1.00') # Added HT stitching  ##TO be added back
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',          'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1',     'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_newpmx',   'DY_LO_pTllrw * 0.990')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',          'DY_LO_pTllrw * 0.975')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',         'DY_LO_pTllrw * 0.907')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',        'DY_LO_pTllrw * 0.833')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',         'DY_LO_pTllrw * 1.015')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200_newpmx',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400_newpmx',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600_ext1',  'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf',       'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf_ext1',  'DY_LO_pTllrw')

################################
############ Top ############

samples['top'] = {    'name'   :   nanoGetSampleFiles(directory_bkg,'TTTo2L2Nu')
                                 + nanoGetSampleFiles(directory_bkg,'ST_s-channel') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_tW_top') 
                                 + nanoGetSampleFiles(directory_bkg,'TTToSemiLeptonic') 
                                 + nanoGetSampleFiles(directory_bkg,'TTZjets')
                                 + nanoGetSampleFiles(directory_bkg,'TTZjets_ext1')
                                 + nanoGetSampleFiles(directory_bkg,'TTWjets')
                                 + nanoGetSampleFiles(directory_bkg,'TTWjets_ext1'),
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*btagSF_corr_top' ,
                     'FilesPerJob' : 4,
                     'EventsPerJob' : 70000,
                     'suppressNegative' :['all'],
                     'suppressNegativeNuisances' :['all'],
                 }

CombineBaseW(samples, 'top', ['TTZjets', 'TTZjets_ext1'])
CombineBaseW(samples, 'top', ['TTWjets', 'TTWjets_ext1'])

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')

addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


################################
### Wjets samples

Wjets_photon_filter = '!(Sum$( PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.5 ) > 0) '

samples['Wjets_boost'] = { 'name' :   
            nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO_ext1')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT70_100') 
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf'),
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+ Wjets_photon_filter+'* ewknloW * btagSF_corr_Wjets_HT' ,
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

  # Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO', '(LHE_HT < 70)')
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu-LO_ext1', '(LHE_HT < 70)')
CombineBaseW(samples, 'Wjets_boost', ['WJetsToLNu-LO', 'WJetsToLNu-LO_ext1'])

addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT70_100', '1.21 * 0.9582') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT100_200',    '0.9525') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT200_400',    '0.9577') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT400_600',    '0.9613') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT600_800',    '1.0742') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT800_1200',   '1.1698') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT1200_2500',  '1.3046') 
addSampleWeight(samples,'Wjets_boost', 'WJetsToLNu_HT2500_inf',   '2.1910') 
 
###############
# Resolved bins
for iw, wjetbin in enumerate(wjets_res_bins):
  samples[wjetbin] = { 'name' :   
            nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu-LO')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu-LO_ext1')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT70_100') 
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT100_200')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT200_400')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT400_600')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT600_800')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT800_1200')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT1200_2500')
          + nanoGetSampleFiles(directory_wjets_res_bins[wjetbin], 'WJetsToLNu_HT2500_inf'),
        'weight': "( fit_bin_res == {} )*".format(iw+1) +  XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+ Wjets_photon_filter+'* ewknloW * btagSF_corr_Wjets_HT' ,
        'FilesPerJob' : nfiles_wjets[iw],
      }

  # Fix Wjets binned + LO 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu-LO', '(LHE_HT < 70)')
  addSampleWeight(samples,wjetbin, 'WJetsToLNu-LO_ext1', '(LHE_HT < 70)')
  CombineBaseW(samples, wjetbin, ['WJetsToLNu-LO', 'WJetsToLNu-LO_ext1'])

  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT70_100', '1.21 * 0.9582') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT100_200',    '0.9525') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT200_400',    '0.9577') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT400_600',    '0.9613') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT600_800',    '1.0742') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT800_1200',   '1.1698') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT1200_2500',  '1.3046') 
  addSampleWeight(samples,wjetbin, 'WJetsToLNu_HT2500_inf',   '2.1910')


###############################################

# samples['VV']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD' ) +
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD' ) , 
#         'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch  +'*btagSF_corr_VV_VVV_ggWW', # add back ewknlOW
#         'FilesPerJob' : 15,
#         'EventsPerJob' : 70000,
# }

############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'ZZZ')
                                + nanoGetSampleFiles(directory_bkg,'WZZ')
                                + nanoGetSampleFiles(directory_bkg,'WWZ')
                                + nanoGetSampleFiles(directory_bkg,'WWW'),
                                #+ nanoGetSampleFiles(directory,'WWG'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_VV_VVV_ggWW',
                    'FilesPerJob' : 16,
                    'EventsPerJob' : 70000,
                  }

 ############## VBF-V ########

# ###
# samples['VBF-V']  = {  'name'   : 
#                                   nanoGetSampleFiles(directory_bkg,'WLNuJJ_EWK')
#                                 + nanoGetSampleFiles(directory_bkg,'EWKZ2Jets_ZToLL_M-50_newpmx'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch +'*btagSF_corr_Vg_VgS_VBFV',
#                     'FilesPerJob' : 16,
#                     'EventsPerJob' : 70000,
#                   }

samples['VBF-V_dipole']  = {  'name'   :  
                                    nanoGetSampleFiles(directory_bkg,'EWK_LNuJJ_herwig') +
                                  nanoGetSampleFiles(directory_bkg,'EWK_LLJJ_herwig'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_Vg_VgS_VBFV',
                    'FilesPerJob' : 6,
                    'EventsPerJob' : 70000,
                  }


################ ggWW ##################3

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(directory_bkg,'GluGluWWToLNuQQ'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VV_VVV_ggWW',
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }

##################################################
############ Vg ###################################

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(directory_bkg,'ZGToLLG'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0) *btagSF_corr_Vg_VgS_VBFV',
                    'FilesPerJob' : 16,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }

#the following baseW correction is needed in v5 and should be removed in v6
#addSampleWeight(samples,'Vg','ZGToLLG','0.448')


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(directory_bkg,'ZGToLLG')
                                 + nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14) *btagSF_corr_Vg_VgS_VBFV',
                      'FilesPerJob' : 16,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
#0.448 needed in v5 and should be removed in v6
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') #*0.448
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')


################ DATA

fake_weight_corrected = "fakeWeight_35"

samples['Fake'] = {
  'name': [],
  'weight': METFilter_DATA+'*'+ fake_weight_corrected,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob' : 45
}

#### Fakes
# samples['Fake_ele'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+ fake_weight_corrected,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob' : 45
# }

# samples['Fake_mu'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+ fake_weight_corrected,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob' : 45
# }

# # #
# for _, sd in DataRun:
#   for pd in DataSets:
#     files = nanoGetSampleFiles(directory_data, pd + '_' + sd)
#     if pd == "SingleMuon":
#       # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
#       samples['Fake_mu']['name'].extend(files)
#       samples['Fake_mu']['weights'].extend([DataTrig[pd]] * len(files))
#     elif pd == "SingleElectron":
#       # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
#       samples['Fake_ele']['name'].extend(files)
#       samples['Fake_ele']['weights'].extend([DataTrig[pd]] * len(files))


##########################################
################# DATA ###################
##########################################


# samples['DATA_mu']  = {   'name': [ ] ,
#                        'weight' : METFilter_DATA+'*'+LepWPCut,
#                        'weights' : [ ],
#                        'isData': ['all'],
#                        'FilesPerJob' : 45,
#                   }

# samples['DATA_ele']  = {   'name': [ ] ,
#                        'weight' : METFilter_DATA+'*'+LepWPCut,
#                        'weights' : [ ],
#                        'isData': ['all'],
#                        'FilesPerJob' : 45,
#                   }


# for Run in DataRun :
#         for DataSet in DataSets :
#                 FileTarget = nanoGetSampleFiles(directory_data,DataSet+'_'+Run[1])
#                 for iFile in FileTarget:
#                   if DataSet == "SingleElectron":
#                     samples['DATA_ele']['name'].append(iFile)
#                     samples['DATA_ele']['weights'].append(DataTrig[DataSet])
#                   if DataSet == "SingleMuon":
#                     samples['DATA_mu']['name'].append(iFile)
#                     samples['DATA_mu']['weights'].append(DataTrig[DataSet])

samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 45,
                  }

####################################
####################################
### VV Samples splitting

samples['VBS_ssWW']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil'),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

samples['VBS_osWW']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil'),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}


samples['VBS_WZjj']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

samples['VBS_WZll']  = { 'name' :   
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}


samples['VBS_ZZ']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
       'FilesPerJob' :5,
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

###########################################
#############  SM  SIGNALS  ###############
###########################################


# xsweight_new_WpToLNu_WmTo2J='3.21'
# xsweight_mcm_WpToLNu_WmTo2J='17.99'
# xsweight_new_WpTo2J_WmToLNu='3.205'
# xsweight_mcm_WpTo2J_WmToLNu='17.91'
# xsweight_new_WpToLNu_WpTo2J='0.7297'
# xsweight_mcm_WpToLNu_WpTo2J='3.453'
# xsweight_new_WmToLNu_WmTo2J='0.08887'
# xsweight_mcm_WmToLNu_WmTo2J='0.5065'
# xsweight_new_WmToLNu_ZTo2J='0.1383'
# xsweight_mcm_WmToLNu_ZTo2J='0.7416'
# xsweight_new_WpToLNu_ZTo2J='0.3992'
# xsweight_mcm_WpToLNu_ZTo2J='1.896'

############     -----------------             sm          -----------------    ############

# samples['sm'] ={ # should not use dipole recoil for aqgc SM part
#   'name' :  nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J') + #VBS_ssWW
#             nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J') + #VBS_ssWW
#             nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J') + #VBS_osWW
#             nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu') + #VBS_osWW
#             nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J')  + #VBS_WZjj
#             nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J'),  #VBS_WZjj
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, #+'*btagSF_corr_VBS',
#        'FilesPerJob' :5,
#        'EventsPerJob' : 70000,
# }
# addSampleWeight(samples,'sm','WpToLNu_WmTo2J',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
# addSampleWeight(samples,'sm','WpTo2J_WmToLNu',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
# addSampleWeight(samples,'sm','WpToLNu_WpTo2J',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
# addSampleWeight(samples,'sm','WmToLNu_WmTo2J',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
# addSampleWeight(samples,'sm','WmToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
# addSampleWeight(samples,'sm','WpToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj

############     ----------------- sm VBS ewk with dipole recoil -----------------    ############
# samples['sm']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil') ,
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
#        'FilesPerJob' :1,
#        'EventsPerJob' : 7000000,
# }
# addSampleWeight(samples,'sm_dipole','WpToLNu_WmTo2J_dipoleRecoil',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
# addSampleWeight(samples,'sm_dipole','WpTo2J_WmToLNu_dipoleRecoil',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
# addSampleWeight(samples,'sm_dipole','WpToLNu_WpTo2J_dipoleRecoil',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
# addSampleWeight(samples,'sm_dipole','WmToLNu_WmTo2J_dipoleRecoil',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
# addSampleWeight(samples,'sm_dipole','WmToLNu_ZTo2J_dipoleRecoil',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
# addSampleWeight(samples,'sm_dipole','WpToLNu_ZTo2J_dipoleRecoil',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj



##############################################################################################
#########      aQGC samples !!!!!!!!!!!!!
##############################################################################################
# same implementation as Matteo https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/2018_Jul22/samples.py
# samples name are crucial!! And you can run on 1 operator at the time!!
# calculation for weights and coefficients as in http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2020_204_v6.pdf
# but for k = 2 -> i.e. LinReweight_cT0 = '(0.5 * 1/k * (LHEReweightingWeight[69] - LHEReweightingWeight[68]) )' 
# the k value comes from the largest variation value ft0_2p0 => k = 2
# The index number comes from the reweight card (for instance https://raw.githubusercontent.com/stalbrec/genproductions/VBS_Summer20/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/VBS/aQGC_VVjj_semileptonic/aQGC_WPlepWMhadJJ_EWK_LO_SM_mjj100_pTj10/aQGC_WPlepWMhadJJ_EWK_LO_SM_mjj100_pTj10_reweight_card.dat)
# and the expressions are obtained from Matteo's script https://github.com/mpresill/PlotsConfigurations/blob/matteo/Configurations/VBS_ZV/EFT/ReweightFactory/readWCs.py
# also, signal samples with a W and a Z were wrongly produced including also tZq and similar diagrams. To avoid their inclusion, the filter (Sum$(abs(GenPart_pdgId)==6)==0) is added at Gen level ?????

############     -----------------             FT0          -----------------    ############

quadReweight_cT0 = "( 0.5* (1/(2)) * (1/(2)) * ( LHEReweightingWeight[890] + LHEReweightingWeight[810] - 2 * LHEReweightingWeight[850]))"
LinReweight_cT0 = "( 0.5* (1/(2)) * ( LHEReweightingWeight[890] - LHEReweightingWeight[810] ))"
sm_cT0 = "( LHEReweightingWeight[850] )"
LinQuadReweight_cT0 = '('+LinReweight_cT0+' + '+quadReweight_cT0+')'
SMLinQuadReweight_cT0 = '('+ sm_cT0+' + '+LinQuadReweight_cT0+')' 

#default coupling, quadratic EFT
samples['sm']  = { 'name' :  
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  + #VBS_WZjj
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),   #VBS_WZjj

                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),   #VBS_WZjj
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + sm_cT0,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

samples['quad_cT0']  = { 'name' :  
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  + #VBS_WZjj
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),   #VBS_WZjj

                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),   #VBS_WZjj
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT0,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT0'] = {
   'name':   nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT0,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

#FIXME : remove xsec reweight and add SMLinQuad rescaling

############     -----------------              FT1          -----------------    ############

quadReweight_cT1 = "( 0.5* (1/(2)) * (1/(2)) * ( LHEReweightingWeight[971] + LHEReweightingWeight[891] - 2 * LHEReweightingWeight[931]))"
LinReweight_cT1 = "( 0.5* (1/(2)) * ( LHEReweightingWeight[971] - LHEReweightingWeight[891] ))"
sm_cT1 = "( LHEReweightingWeight[931] )"
LinQuadReweight_cT1 = '('+LinReweight_cT1+' + '+quadReweight_cT1+')'
SMLinQuadReweight_cT1 = '('+ sm_cT1+' + '+LinQuadReweight_cT1+')' 
#default coupling, quadratic EFT
samples['quad_cT1']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
                
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') + #VBS_osWW
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_ssWW
                nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  + #VBS_WZjj
                nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),   #VBS_WZjj


       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT1,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT1'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_osWW
            nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') + #VBS_osWW
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') + #VBS_ssWW
            nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') + #VBS_ssWW
            nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  + #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),   #VBS_WZjj

   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT0,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------             FT2          -----------------    ############

quadReweight_cT2 = "( 0.5* (1/(4)) * (1/(4)) * ( LHEReweightingWeight[1052] + LHEReweightingWeight[972] - 2 * LHEReweightingWeight[1012]))"
LinReweight_cT2 = "( 0.5* (1/(4)) * ( LHEReweightingWeight[1052] - LHEReweightingWeight[972] ))"
sm_cT2 = "( LHEReweightingWeight[1012] )"
LinQuadReweight_cT2 = '('+LinReweight_cT2+' + '+quadReweight_cT2+')'
SMLinQuadReweight_cT2 = '('+ sm_cT2+' + '+LinQuadReweight_cT2+')' 
#default coupling, quadratic EFT
samples['quad_cT2']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
                
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT2,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# # SM + lin + quad 
samples['sm_lin_quad_cT2'] = {  'name':   
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT2,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FT3          -----------------    ############

quadReweight_cT3 = "( 0.5* (1/(4.0)) * (1/(4.0)) * ( LHEReweightingWeight[1133] + LHEReweightingWeight[1053] - 2 * LHEReweightingWeight[1093]))"
LinReweight_cT3 = "( 0.5* (1/(4.0)) * ( LHEReweightingWeight[1133] - LHEReweightingWeight[1053] ))"
sm_cT3 = "( LHEReweightingWeight[1093] )"
LinQuadReweight_cT3 = '('+LinReweight_cT3+' + '+quadReweight_cT3+')'
SMLinQuadReweight_cT3 = "("+ sm_cT3 + " + " +LinQuadReweight_cT3+")"

samples['quad_cT3']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
                
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT3,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT3'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT3,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}


############     -----------------              FT4          -----------------    ############

quadReweight_cT4 = "( 0.5* (1/(4.0)) * (1/(4.0)) * ( LHEReweightingWeight[1214] + LHEReweightingWeight[1134] - 2 * LHEReweightingWeight[1174]))"
LinReweight_cT4 = "( 0.5* (1/(4.0)) * ( LHEReweightingWeight[1214] - LHEReweightingWeight[1134] ))"
sm_cT4 = "( LHEReweightingWeight[1174] )"
LinQuadReweight_cT4 = '('+LinReweight_cT4+' + '+quadReweight_cT4+')'
SMLinQuadReweight_cT4 = "("+ sm_cT4 + " + " +LinQuadReweight_cT4+")"

samples['quad_cT4']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
                
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT4,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT4'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT4,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}


# ############     -----------------              FT5          -----------------    ############

quadReweight_cT5 = "( 0.5* (1/(8)) * (1/(8)) * ( LHEReweightingWeight[1295] + LHEReweightingWeight[1215] - 2 * LHEReweightingWeight[1255]))"
LinReweight_cT5 = "( 0.5* (1/(8)) * ( LHEReweightingWeight[1295] - LHEReweightingWeight[1215] ))"
sm_cT5 = "( LHEReweightingWeight[1255] )"
LinQuadReweight_cT5 = '('+LinReweight_cT5+' + '+quadReweight_cT5+')'
SMLinQuadReweight_cT5 = '('+ sm_cT5+' + '+LinQuadReweight_cT5+')' 
#default coupling, quadratic EFT
samples['quad_cT5']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
                
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT5,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT5'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT5,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

# ############     -----------------              FT6          -----------------    ############

quadReweight_cT6 = "( 0.5* (1/(8)) * (1/(8)) * ( LHEReweightingWeight[1376] + LHEReweightingWeight[1296] - 2 * LHEReweightingWeight[1336]))"
LinReweight_cT6 = "( 0.5* (1/(8)) * ( LHEReweightingWeight[1376] - LHEReweightingWeight[1296] ))"
sm_cT6 = "( LHEReweightingWeight[1336] )"
LinQuadReweight_cT6 = '('+LinReweight_cT6+' + '+quadReweight_cT6+')'
SMLinQuadReweight_cT6 = '('+ sm_cT6+' + '+LinQuadReweight_cT6+')' 
#default coupling, quadratic EFT
samples['quad_cT6']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT6,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT6'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT6,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}


# ############     -----------------              FT7          -----------------    ############

quadReweight_cT7 = "( 0.5* (1/(16)) * (1/(16)) * ( LHEReweightingWeight[1457] + LHEReweightingWeight[1377] - 2 * LHEReweightingWeight[1417]))"
LinReweight_cT7 = "( 0.5* (1/(16)) * ( LHEReweightingWeight[1457] - LHEReweightingWeight[1377] ))"
sm_cT7 = "( LHEReweightingWeight[1417] )"
LinQuadReweight_cT7 = '('+LinReweight_cT7+' + '+quadReweight_cT7+')'
SMLinQuadReweight_cT7 = '('+ sm_cT7+' + '+LinQuadReweight_cT7+')' 
#default coupling, quadratic EFT
samples['quad_cT7']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT7,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT7'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

             nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT7,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

# ############     -----------------              FT8          -----------------    ############

quadReweight_cT8 = "( 0.5* (1/(20)) * (1/(20)) * ( LHEReweightingWeight[1538] + LHEReweightingWeight[1458] - 2 * LHEReweightingWeight[1498]))"
LinReweight_cT8 = "( 0.5* (1/(20)) * ( LHEReweightingWeight[1538] - LHEReweightingWeight[1458] ))"
sm_cT8 = "( LHEReweightingWeight[1498] )"
LinQuadReweight_cT8 = '('+LinReweight_cT8+' + '+quadReweight_cT8+')'
SMLinQuadReweight_cT8 = '('+ sm_cT8+' + '+LinQuadReweight_cT8+')' 
#default coupling, quadratic EFT
samples['quad_cT8']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT8,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT8'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

             nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT8,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}


# ############     -----------------              FT9          -----------------    ############

quadReweight_cT9 = "( 0.5* (1/(20)) * (1/(20)) * ( LHEReweightingWeight[1619] + LHEReweightingWeight[1539] - 2 * LHEReweightingWeight[1579]))"
LinReweight_cT9 = "( 0.5* (1/(20)) * ( LHEReweightingWeight[1619] - LHEReweightingWeight[1539] ))"
sm_cT9 = "( LHEReweightingWeight[1579] )"
LinQuadReweight_cT9 = '('+LinReweight_cT9+' + '+quadReweight_cT9+')'
SMLinQuadReweight_cT9 = '('+ sm_cT9+' + '+LinQuadReweight_cT9+')' 
#default coupling, quadratic EFT
samples['quad_cT9']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cT9,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cT9'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cT9,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}


# ############     -----------------              FS0          -----------------    ############
quadReweight_cS0 = "( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[80] + LHEReweightingWeight[0] - 2 * LHEReweightingWeight[40]))"
LinReweight_cS0 = "( 0.5* (1/(30)) * ( LHEReweightingWeight[80] - LHEReweightingWeight[0] ))"
sm_cS0 = "( LHEReweightingWeight[40] )"
LinQuadReweight_cS0 = '('+LinReweight_cS0+' + '+quadReweight_cS0+')'
SMLinQuadReweight_cS0 = '('+ sm_cS0+' + '+LinQuadReweight_cS0+')' 
#default coupling, quadratic EFT
samples['quad_cS0']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
                
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cS0,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cS0'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cS0,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FS1          -----------------    ############
quadReweight_cS1 = "( 0.5* (1/(30)) * (1/(30)) * ( LHEReweightingWeight[161] + LHEReweightingWeight[81] - 2 * LHEReweightingWeight[121]))"
LinReweight_cS1 = "( 0.5* (1/(30)) * ( LHEReweightingWeight[161] - LHEReweightingWeight[81] ))"
sm_cS1 = "( LHEReweightingWeight[121] )"
LinQuadReweight_cS1 = '('+LinReweight_cS1+' + '+quadReweight_cS1+')'
SMLinQuadReweight_cS1 = '('+ sm_cS1+' + '+LinQuadReweight_cS1+')' 
#default coupling, quadratic EFT
samples['quad_cS1']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
                
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cS1,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cS1'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cS1,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FM0          -----------------    ############
quadReweight_cM0 = "( 0.5* (1/(36)) * (1/(36)) * ( LHEReweightingWeight[323] + LHEReweightingWeight[243] - 2 * LHEReweightingWeight[283]))"
LinReweight_cM0 = "( 0.5* (1/(36)) * ( LHEReweightingWeight[323] - LHEReweightingWeight[243] ))"
sm_cM0 = "( LHEReweightingWeight[283] )"
LinQuadReweight_cM0 = '('+LinReweight_cM0+' + '+quadReweight_cM0+')'
SMLinQuadReweight_cM0 = '('+ sm_cM0+' + '+LinQuadReweight_cM0+')' 
#default coupling, quadratic EFT
samples['quad_cM0']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cM0,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cM0'] = {  'name':   
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cM0,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FM1          -----------------    ############
quadReweight_cM1 = "( 0.5* (1/(28)) * (1/(28)) * ( LHEReweightingWeight[404] + LHEReweightingWeight[324] - 2 * LHEReweightingWeight[364]))"
LinReweight_cM1 = "( 0.5* (1/(28)) * ( LHEReweightingWeight[404] - LHEReweightingWeight[324] ))"
sm_cM1 = "( LHEReweightingWeight[364] )"
LinQuadReweight_cM1 = '('+LinReweight_cM1+' + '+quadReweight_cM1+')'
SMLinQuadReweight_cM1 = '('+ sm_cM1+' + '+LinQuadReweight_cM1+')' 
#default coupling, quadratic EFT
samples['quad_cM1']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cM1,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cM1'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cM1,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}


############     -----------------              FM2          -----------------    ############
quadReweight_cM2 = "( 0.5* (1/(60)) * (1/(60)) * ( LHEReweightingWeight[485] + LHEReweightingWeight[405] - 2 * LHEReweightingWeight[445]))"
LinReweight_cM2 = "( 0.5* (1/(60)) * ( LHEReweightingWeight[485] - LHEReweightingWeight[405] ))"
sm_cM2 = "( LHEReweightingWeight[445] )"
LinQuadReweight_cM2 = '('+LinReweight_cM2+' + '+quadReweight_cM2+')'
SMLinQuadReweight_cM2 = '('+ sm_cM2+' + '+LinQuadReweight_cM2+')' 
#default coupling, quadratic EFT
samples['quad_cM2']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cM2,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cM2'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cM2,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FM3          -----------------    ############
quadReweight_cM3 = "( 0.5* (1/(80)) * (1/(80)) * ( LHEReweightingWeight[566] + LHEReweightingWeight[486] - 2 * LHEReweightingWeight[526]))"
LinReweight_cM3 = "( 0.5* (1/(80)) * ( LHEReweightingWeight[566] - LHEReweightingWeight[486] ))"
sm_cM3 = "( LHEReweightingWeight[526] )"
LinQuadReweight_cM3 = '('+LinReweight_cM3+' + '+quadReweight_cM3+')'
SMLinQuadReweight_cM3 = '('+ sm_cM3+' + '+LinQuadReweight_cM3+')' 
#default coupling, quadratic EFT
samples['quad_cM3']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cM3,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cM3'] = {  'name':   
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj

            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cM3,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FM4          -----------------    ############
quadReweight_cM4 = "( 0.5* (1/(80)) * (1/(80)) * ( LHEReweightingWeight[647] + LHEReweightingWeight[567] - 2 * LHEReweightingWeight[607]))"
LinReweight_cM4 = "( 0.5* (1/(80)) * ( LHEReweightingWeight[647] - LHEReweightingWeight[567] ))"
sm_cM4 = "( LHEReweightingWeight[607] )"
LinQuadReweight_cM4 = '('+LinReweight_cM4+' + '+quadReweight_cM4+')'
SMLinQuadReweight_cM4 = '('+ sm_cM4+' + '+LinQuadReweight_cM4+')' 
#default coupling, quadratic EFT
samples['quad_cM4']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cM4,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cM4'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cM4,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FM5          -----------------    ############
quadReweight_cM5 = "( 0.5* (1/(160)) * (1/(160)) * ( LHEReweightingWeight[728] + LHEReweightingWeight[648] - 2 * LHEReweightingWeight[688]))"
LinReweight_cM5 = "( 0.5* (1/(160)) * ( LHEReweightingWeight[728] - LHEReweightingWeight[648] ))"
sm_cM5 = "( LHEReweightingWeight[688] )"
LinQuadReweight_cM5 = '('+LinReweight_cM5+' + '+quadReweight_cM5+')'
SMLinQuadReweight_cM5 = '('+ sm_cM5+' + '+LinQuadReweight_cM5+')' 
#default coupling, quadratic EFT
samples['quad_cM5']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cM5,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cM5'] = {  'name':
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cM5,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}

############     -----------------              FM7          -----------------    ############
quadReweight_cM7 = "( 0.5* (1/(80)) * (1/(80)) * ( LHEReweightingWeight[809] + LHEReweightingWeight[729] - 2 * LHEReweightingWeight[769]))"
LinReweight_cM7 = "( 0.5* (1/(80)) * ( LHEReweightingWeight[809] - LHEReweightingWeight[729] ))"
sm_cM7 = "( LHEReweightingWeight[769] )"

LinQuadReweight_cM7 = '('+LinReweight_cM7+' + '+quadReweight_cM7+')'
SMLinQuadReweight_cM7 = '('+ sm_cM7+' + '+LinQuadReweight_cM7+')' 
#default coupling, quadratic EFT
samples['quad_cM7']  = { 'name' :  
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
                # nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
                # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cM7,
       'FilesPerJob' :5,
       'EventsPerJob' : 70000,
}

# SM + lin + quad 
samples['sm_lin_quad_cM7'] = {  'name':   
            # nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') #VBS_osWW
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') #VBS_ssWW
            # +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            # +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2')  #VBS_WZjj
            nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2_official') #VBS_osWW
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2_official') #VBS_ssWW
            +nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2_official')  #VBS_WZjj
            +nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2_official'),  #VBS_WZjj
 
   'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*'+SMLinQuadReweight_cM7,
   'FilesPerJob': 10,
   'EventsPerJob' : 70000,
}


VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]
VBS_aQGC_samples = ["quad_cT2","sm_lin_quad_cT2","sm"]
VV_VVV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ","VVV","ggWW"]
################################################                                                                                                                     
# ---------->        to make datacard you need to skip VBS samples and other operators!!                                                                             
operators_to_exclude = ["cT0", "cT1", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
full_operators_name_to_exclude = []
for op in operators_to_exclude:
   full_operators_name_to_exclude.append("quad_"+op)
   full_operators_name_to_exclude.append("sm_lin_quad_"+op)
# full_operators_name_to_exclude.append("sm")
# samples = {   key:v for key,v in samples.items() if key not in VBS_samples and key not in full_operators_name_to_exclude} #'cT2' not in key and 'cT1' not in key}    
# samples = {key:v for key,v in samples.items() if key == "sm_dipole"}

# samples = {key:v for key,v in samples.items() if key not in  VBS_samples} # and "Fake" not in key} #, "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]}
# samples = {key:v for key,v in samples.items() if key == "DY"}
samples = {key:v for key,v in samples.items() if key in  VBS_aQGC_samples}
