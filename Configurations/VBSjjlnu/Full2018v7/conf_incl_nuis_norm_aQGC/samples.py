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
  newbaseW = getBaseWnAOD(directory_bkg, 'Autumn18_102X_nAODv7_Full2018v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')

##############################################
###### Tree Directory according to site ######
##############################################

samples={}


# Steps
mcSteps   = 'MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018' 
dataSteps = 'DATAl1loose2018v7__DATACombJJLNu2018'

mcProduction =   'Autumn18_102X_nAODv7_Full2018v7'
mcProductionIZ =   'Autumn18_102X_nAODv7_Full2018v7'
dataProduction = 'Run2018_102X_nAODv7_Full2018v7'

SITE=os.uname()[1]
xrootdPath=''
if  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
  treeBaseDir_FNAL = '/store/group/lnujj/aQGC_VVJJ_Private_Production_PreProcessing/'
  xrootdPath='root://cmseos.fnal.gov/'

directory_bkg    = os.path.join(treeBaseDir ,  mcProduction , mcSteps)
directory_signal = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps) 
directory_signalIZ = os.path.join(xrootdPath + treeBaseDir_FNAL ,  mcProductionIZ , mcSteps)
directory_mc     = os.path.join(treeBaseDir ,  mcProduction , mcSteps)
directory_data   = os.path.join(treeBaseDir,       dataProduction, dataSteps)


# def makeMCDirectory(var, smpFolder=False):
#     if not smpFolder:
#         return os.path.join(treeBaseDir, mcProduction, mcSteps +'_'+var)
#     else:
#         return os.path.join(treeBaseDir_SMP, mcProduction, mcSteps +'_'+var)


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
#corrected trigger efficiency

XSWeight   = 'XSWeight'
SFweight1l = [ 'puWeight', 'SingleLepton_trigEff_corrected[0]',
              'Lepton_RecoSF[0]',LepWPWeight_1l, LepWPCut_1l,
              'PUJetIdSF']   #--> no btagSF, no BoostedW SF

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
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['SingleMuon','EGamma']

DataTrig = {
            'SingleMuon' : 'Trigger_sngMu' ,
            'EGamma'     : '!Trigger_sngMu && Trigger_sngEl' 
}
###########################################
#############  BACKGROUNDS  ###############
##########################################

########### DY ############

DY_photon_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY'] = {    'name'   :   nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50') #Don't use LO(_ext0)! DYMVA Training!
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_ext2')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-10to50-LO_ext1')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-70to100')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-100to200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-200to400')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-400to600')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-100to200')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-200to400')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-400to600')
                                  + nanoGetSampleFiles(directory_bkg,'DYJetsToLL_M-4to50_HT-600toInf'),
                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + '*' + DY_photon_filter ,# missing ewkNLOW
                       'FilesPerJob' : 15,
                       'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                   }

CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext2'])
addSampleWeight(samples,'DY','DYJetsToLL_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw') 
addSampleWeight(samples,'DY','DYJetsToLL_M-50',               '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2',          '(LHE_HT < 70)')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1',   '(LHE_HT < 100)')   
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100',    'DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200',   'DY_LO_pTllrw * 1.000') #HT stitching correction
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',   'DY_LO_pTllrw * 0.999')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600',   'DY_LO_pTllrw * 0.990')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',   'DY_LO_pTllrw * 0.975')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',  'DY_LO_pTllrw * 0.907')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500', 'DY_LO_pTllrw * 0.833')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',  'DY_LO_pTllrw * 1.015')  
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200','DY_LO_pTllrw') 
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600','DY_LO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf','DY_LO_pTllrw')


################################
############ Top ############

samples['top'] = {    'name'   :   nanoGetSampleFiles(directory_bkg,'TTTo2L2Nu') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_s-channel_ext1') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_tW_antitop_ext1') 
                                 + nanoGetSampleFiles(directory_bkg,'ST_tW_top_ext1') 
                                 + nanoGetSampleFiles(directory_bkg,'TTToSemiLeptonic') 
                                 + nanoGetSampleFiles(directory_bkg,'TTZjets')
                                 + nanoGetSampleFiles(directory_bkg,'TTWjets'),
                                # +  nanoGetSampleFiles(directory_bkg,'TTWJetsToLNu'), #also this is available
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                     'FilesPerJob' : 15,
                     'EventsPerJob' : 70000,
                     'suppressNegative' :['all'],
                     'suppressNegativeNuisances' :['all'],
                 }
addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
#addSampleWeight(samples,'top','TTZjets','Top_pTrw')
#addSampleWeight(samples,'top','TTWjets','Top_pTrw')

#Not corrected in baseW, so we should correct the XS here
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")


################################
### Wjets samples

samples['Wjets_HT'] = { 'name' :   
          nanoGetSampleFiles(directory_bkg, 'WJetsToLNu-LO')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT70_100')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT100_200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT200_400')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT400_600')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT600_800')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT800_1200')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT1200_2500')
          + nanoGetSampleFiles(directory_bkg, 'WJetsToLNu_HT2500_inf'),
				'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '* ewknloW',
				'FilesPerJob' : 15   
		}

# Fix Wjets binned + LO 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu-LO', '(LHE_HT < 70)') 
############
# HT stiching corrections 2018
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT70_100',    '1.21 * 0.95148')  #adding also k-factor
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT100_200',   '0.9471') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT200_400',   '0.9515') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT400_600',   '0.9581') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT600_800',   '1.0582') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT800_1200',  '1.1285') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT1200_2500', '1.3268') 
addSampleWeight(samples,'Wjets_HT', 'WJetsToLNu_HT2500_inf',  '2.7948') 
 


###############################################

samples['VV']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_QCD',) +
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_QCD', ) +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_QCD') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_QCD', ) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_QCD') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_QCD',) +
               nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_QCD',  ) ,
        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch, # still missing EWKnlowW 
        'FilesPerJob' : 20,
        'EventsPerJob' : 70000,
}

############ VVV ############
  
samples['VVV']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'ZZZ')
                                + nanoGetSampleFiles(directory_bkg,'WZZ')
                                + nanoGetSampleFiles(directory_bkg,'WWZ')
                                + nanoGetSampleFiles(directory_bkg,'WWW'),
                                #+ nanoGetSampleFiles(directory_bkg,'WWG'), #should this be included? or is it already taken into account in the WW sample?
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch ,
                    'FilesPerJob' : 20,
                     'EventsPerJob' : 70000,
                  }

 ############## VBF-V ########

samples['VBF-V']  = {  'name'   :  
                                    nanoGetSampleFiles(directory_bkg,'WLNuJJ_EWK') +
                                  nanoGetSampleFiles(directory_bkg,'EWKZ2Jets_ZToLL_M-50'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' : 20,
                    'EventsPerJob' : 70000,
                  }

################ ggWW ##################3

samples['ggWW']  = {  'name'   :  
                                  nanoGetSampleFiles(directory_bkg,'GluGluWWToLNuQQ'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
                    'FilesPerJob' : 15,
                    'EventsPerJob' : 70000,
                  }
##################################################
############ Vg ###################################

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(directory_bkg,'ZGToLLG'),
                    'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC+'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 20,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }

# the following baseW correction is needed in both v5 and v6 (for Zg, Not for ZGToLLG)
#addSampleWeight(samples, 'Vg', 'Zg', '0.448')


############ VgS ############

samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(directory_bkg,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(directory_bkg,'ZGToLLG')
                                 + nanoGetSampleFiles(directory_bkg,'WZTo3LNu_mllmin01'),
                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 20,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                      # 'subsamples': {
                      #   'L': 'gstarLow',
                      #   'H': 'gstarHigh'
                      # }
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') # *0.448 XS correction for Zg
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')


##########################################
################ SIGNALS #################
##########################################

#
samples['VBS']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J',) +
               nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L', ) +
               nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L', ) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J',) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu') +
               nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J',  ),
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
       'FilesPerJob' : 20,
       'EventsPerJob' : 70000,
}

# # Then corrected
# fakeW = 'fakeWeight_35'

# ### Fakes
# samples['Fake'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+fakeW,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob' : 40
# }

# for _, sd in DataRun:
#   for pd in DataSets:
#     # BE Careful --> we use directory_data because the Lepton tight cut was not applied in post-processing
#     files = nanoGetSampleFiles(directory_data, pd + '_' + sd)
#     samples['Fake']['name'].extend(files)
#     samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))


# #########################################
# ################ DATA ###################
# #########################################

# samples['DATA']  = {   'name': [ ] ,
#                        'weight' : METFilter_DATA+'*'+LepWPCut,
#                        'weights' : [ ],
#                        'isData': ['all'],
#                        'FilesPerJob' : 40,         
#             }

# for Run in DataRun :
#         for DataSet in DataSets :
#                 FileTarget = nanoGetSampleFiles(directory_data,DataSet+'_'+Run[1])
#                 for iFile in FileTarget:
#                         samples['DATA']['name'].append(iFile)
#                         samples['DATA']['weights'].append(DataTrig[DataSet])

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


VBS_aQGC_samples_labels = ["cT0","cT1","cT2", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cS2", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
VBS_aQGC_samples = []
for op in VBS_aQGC_samples_labels:
   VBS_aQGC_samples.append("quad_"+op)
   VBS_aQGC_samples.append("sm_lin_quad_"+op)
VBS_aQGC_samples.append("sm")
# VBS_aQGC_samples = ["quad_cT1","sm_lin_quad_cT1"]
# VBS_aQGC_samples = ["quad_cT2","sm_lin_quad_cT2"] #,"sm"]

samples = {   key:v for key,v in samples.items() if key  in VBS_aQGC_samples}