import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'step7_')

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

#inputfile = "/eos/cms/store/group/phys_higgs/cmshmm/amarini/aQGC_WMLEPWMHADjj_EWK_LO_NPle1_TuneCP5_13TeV-madgraph-pythia8/UL2018-NANOAODSIMv9/220121_144426/0000/step7_"+number+".root"

# Steps
#mcSteps   = 'MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018' 
#dataSteps = 'DATAl1loose2018v7__DATACombJJLNu2018'

mcProduction =   'UL2018-NANOAODSIMv9'
#dataProduction = 'Run2018_102X_nAODv7_Full2018v7_skim'

WMLEPWMHADjj = 'aQGC_WMLEPWMHADjj_EWK_LO_NPle1_TuneCP5_13TeV-madgraph-pythia8'

subidirs = '220121_144426/0000/'

SITE=os.uname()[1]
xrootdPath=''
if  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshmm/amarini/'
  #treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'

#directory_bkg    = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_WMLEPWMHADjj = os.path.join(treeBaseDir , WMLEPWMHADjj, mcProduction , subidirs) 
print("directory_WMLEPWMHADjj ",directory_WMLEPWMHADjj)
#directory_mc     = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
#directory_data   = os.path.join(treeBaseDir_SMP,       dataProduction, dataSteps)
#directory_interference = '/eos/user/g/govoni/valsecchi/LatinosSamples/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018'



################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeightTimesBR   = {}

XSWeightTimesBR["aQGC_WMLEPWMHADjj_EWK"]='0.0222'
XSWeightTimesBR["aQGC_WMLEPZHADjj_EWK" ]='0.0940'
XSWeightTimesBR["aQGC_WPHADWMLEPjj_EWK"]='0.9067'
XSWeightTimesBR["aQGC_WPLEPWMHADjj_EWK"]='0.9067'
XSWeightTimesBR["aQGC_WPLEPWPHADjj_EWK"]='0.1355'
XSWeightTimesBR["aQGC_WPLEPZHADjj_EWK" ]='0.1746'


# ##########################################
# ################ SIGNALS #################
# ##########################################


samples['aQGC_WMLEPWMHADjj_EWK']  = { 'name' :  
                #nanoGetSampleFiles(directory_WMLEPWMHADjj,''),#run on all files 
                nanoGetSampleFiles(directory_WMLEPWMHADjj,'1'),#run on file _1 for testing
        'weight': XSWeightTimesBR['aQGC_WMLEPWMHADjj_EWK'], # +'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
        'FilesPerJob' :15,
        'EventsPerJob' : 1000,
 }

operatorfilename='../weights_files/operators_short.json'
#this should be the same in variables!!
operatorsfile=operatorfilename
jsonoperatorsfile = open(operatorsfile)
# returns JSON object as a dictionary
shortoperatorsdata = json.load(jsonoperatorsfile)
jsonoperatorsfile.close()

for operator in shortoperatorsdata:
    print(" operator ",operator)
    for opweight in shortoperatorsdata[operator]:
        print(" opweight ",opweight)
        variation=operator+"_"+opweight
        samples['aQGC_WMLEPWMHADjj_EWK_'+variation]  = { 'name' :  
                #nanoGetSampleFiles(directory_WMLEPWMHADjj,''),#run on all files 
                nanoGetSampleFiles(directory_WMLEPWMHADjj,'1'),#run on file _1 for testing
        'weight': XSWeightTimesBR['aQGC_WMLEPWMHADjj_EWK']+'*'+str(variation)+'/LHEWeight_originalXWGTUP', # +'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
        'FilesPerJob' :15,
        'EventsPerJob' : 7500,
 }

# samples['VBS_dipoleRecoil']  = { 'name' :  
#                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
#                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil') +
#                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
#        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
#        'FilesPerJob' :15,
#        'EventsPerJob' : 70000,
# }


# # samples['VBS_interf']  = { 'name' :  
# #                nanoGetSampleFiles(directory_interference,'WmToLNuWpTo2J_EWKQCD',) + 
# #                nanoGetSampleFiles(directory_interference,'WpToLNuWmTo2J_EWKQCD', ) +
# #                nanoGetSampleFiles(directory_interference,'WToJJZToLL_EWKQCD', ) +
# #                nanoGetSampleFiles(directory_interference,'WToLNuZTo2J_EWKQCD',) +
# #                nanoGetSampleFiles(directory_interference,'ZToLLZToJJ_EWKQCD') ,
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
# #        'FilesPerJob' :10,
# #        'EventsPerJob' : 70000,
# # }

# # samples['VBS_notop']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
# #               #  nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
# #               #  nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil'),
# #               #  nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil * (Sum$(abs(GenPart_pdgId)==6)==0)',
# #        'FilesPerJob' :16,
# #        'EventsPerJob' : 70000,
# # }

# # samples['VBS_top']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
# #               #  nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
# #               #  nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil') ,
# #               #  nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil * (Sum$(abs(GenPart_pdgId)==6)>0)',
# #        'FilesPerJob' :16,
# #        'EventsPerJob' : 70000,
# # }



# ####################################
# ### VV Samples splitting

# # samples['VBS_ssWW']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil'),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
# #        'FilesPerJob' :15,
# #        'EventsPerJob' : 70000,
# # }

# # samples['VBS_osWW']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil'),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
# #        'FilesPerJob' :15,
# #        'EventsPerJob' : 70000,
# # }


# # samples['VBS_WZjj']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
# #        'FilesPerJob' :15,
# #        'EventsPerJob' : 70000,
# # }

# # samples['VBS_ZZ']  = { 'name' :  
# #                nanoGetSampleFiles(directory_signal,'ZTo2L_ZTo2J_dipoleRecoil',  ),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
# #        'FilesPerJob' :15,
# #        'EventsPerJob' : 70000,
# # }

# # samples['VBS_WZll']  = { 'name' :   
# #                nanoGetSampleFiles(directory_signal,'WmTo2J_ZTo2L_dipoleRecoil', ) +
# #                nanoGetSampleFiles(directory_signal,'WpTo2J_ZTo2L_dipoleRecoil', ),
# #        'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS_dipoleRecoil',
# #        'FilesPerJob' :15,
# #        'EventsPerJob' : 70000,
# # }

# # Then corrected
# fakeW = 'fakeWeight_35'

# ### Fakes
# samples['Fake'] = {
#   'name': [],
#   'weight': METFilter_DATA+'*'+fakeW,
#   'weights': [],
#   'isData': ['all'],
#   'FilesPerJob' : 40,
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
#                        'FilesPerJob' : 60,         
#             }

# for Run in DataRun :
#         for DataSet in DataSets :
#                 FileTarget = nanoGetSampleFiles(directory_data,DataSet+'_'+Run[1])
#                 for iFile in FileTarget:
#                         samples['DATA']['name'].append(iFile)
#                         samples['DATA']['weights'].append(DataTrig[DataSet])


# #samples = {   key:v for key,v in samples.items() if key not in ['VBF-V','VBS_dipoleRecoil']}
# #samples = {key:v for key,v in samples.items() if key in ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]}
# #samples = {key:v for key,v in samples.items() if key in ["DY"]}
# #samples = {k:v for k,v in samples.items() if k == "DATA"}