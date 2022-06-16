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
                nanoGetSampleFiles(directory_WMLEPWMHADjj,''),#run on all files 
                #nanoGetSampleFiles(directory_WMLEPWMHADjj,'1'),#run on file _1 for testing
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
                nanoGetSampleFiles(directory_WMLEPWMHADjj,''),#run on all files 
                #nanoGetSampleFiles(directory_WMLEPWMHADjj,'1'),#run on file _1 for testing
        'weight': XSWeightTimesBR['aQGC_WMLEPWMHADjj_EWK']+'*'+str(variation)+'/LHEWeight_originalXWGTUP', # +'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch+'*btagSF_corr_VBS',
        'FilesPerJob' :15,
        'EventsPerJob' : 7500,
 }
