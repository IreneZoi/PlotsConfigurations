import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

# Import the operators dictionary from EFT_dict.py
# Execute the contents of EFT_dim8_dictionary.py, please update the path according to your exigency 
with open('/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/EFTcoefficients/EFT_dim8_dictionary_v2.py') as f:
    code = compile(f.read(), 'EFT_dim8_dictionary_v2.py', 'exec')
    exec(code)

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

mcProduction =   'Autumn18_102X_nAODv7_Full2018v7_skim'
mcProductionIZ =   'Autumn18_102X_nAODv7_Full2018v7'
dataProduction = 'Run2018_102X_nAODv7_Full2018v7_skim'

SITE=os.uname()[1]
xrootdPath=''
if  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'
  treeBaseDir_FNAL = '/store/group/lnujj/aQGC_VVJJ_Private_Production_PreProcessing/'
  xrootdPath='root://cmseos.fnal.gov/'


directory_bkg    = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_signal = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps) 
directory_signalIZ = os.path.join(treeBaseDir_SMP ,  mcProductionIZ , mcSteps)
directory_mc     = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps)
directory_data   = os.path.join(treeBaseDir_SMP,       dataProduction, dataSteps)
directory_interference = '/eos/user/g/govoni/valsecchi/LatinosSamples/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018'

wjets_res_bins = []
wjets_boost_bins = []
directory_wjets_bins = {}
nfiles_wjets_res = [4,4,5,6,8,8,4,4,5,6,8,8,5,5,6,8,8,8,8,8,8]
nfiles_wjets_boost = [6,6,6,6,7,8,8]
for i in range(1, 22):
  wjbin = "Wjets_res_{}".format(i)
  wjets_res_bins.append(wjbin)
  directory_wjets_bins[wjbin] = treeBaseDir_SMP + 'Autumn18_102X_nAODv7_Full2018v7_WjetsBins_skim/res_bin_{}/'.format(i) + mcSteps
for i in range(1, 8):
  wjbin = "Wjets_boost_{}".format(i)
  wjets_boost_bins.append(wjbin)
  directory_wjets_bins[wjbin] = treeBaseDir_SMP + 'Autumn18_102X_nAODv7_Full2018v7_WjetsBins_skim/boost_bin_{}/'.format(i) + mcSteps

wjets_all_bins = wjets_res_bins + wjets_boost_bins

# print "Wjets bins: ", wjets_res_bins, wjets_boost_bins

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
              'btagSF','PUJetIdSF', 'BoostedWtagSF_nominal']

SFweight = '*'.join(SFweight1l)

GenLepMatch   = 'Lepton_genmatched[0]'

LHEWeight_originalXWGTUP='LHEWeight_originalXWGTUP'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'


###########     ----------------- sm VBS ewk with dipole recoil -----------------    ############
samples['sm']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil') ,
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
       'FilesPerJob' :1,
       'EventsPerJob' : 7000000,
}

#************          EFT samples       ************#
# new development from Matteo calulating all reweights in another input file
#++++++ these are the centrally produced samples ++++#
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
        'FilesPerJob': 10
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
        'FilesPerJob': 10
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
        'FilesPerJob': 10
    }
    addSampleWeight(samples, 'sm_'+operator, 'WpToLNu_WmTo2J_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WpTo2J_WmToLNu_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WpToLNu_WpTo2J_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WmToLNu_WmTo2J_aQGC_Aug2024', smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WmToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
    addSampleWeight(samples, 'sm_'+operator, 'WpToLNu_ZTo2J_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
    
    


VBS_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VV_samples = ["VV_osWW", "VV_ssWW", "VV_WZjj", "VV_WZll", "VV_ZZ"]
#VBS_aQGC_samples = ["quad_cT0","sm_lin_quad_cT0",'sm']
signal_samples = ["VBS_osWW", "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]
VBS_aQGC_samples = ["quad_cT0","sm_lin_quad_cT0","sm"]
# sm_samples = ["sm_FT0_WmToLNu_ZTo2J", "sm_FT0_WpToLNu_ZTo2J","sm_FT0_WpToLNu_WpTo2J","sm_FT0_WmToLNu_WmTo2J","sm_FT0_WpToLNu_WmTo2J","sm_FT0_WpTo2J_WmToLNu","sm_dipole_WmToLNu_ZTo2J", "sm_dipole_WpToLNu_ZTo2J","sm_dipole_WpToLNu_WpTo2J","sm_dipole_WmToLNu_WmTo2J","sm_dipole_WpToLNu_WmTo2J","sm_dipole_WpTo2J_WmToLNu"]
#samples = {key:v for key,v in samples.items() if 'quad_cT0' == key} #, "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]}
#samples = {key:v for key,v in samples.items() if key in VBS_samples+VV_samples+VBS_aQGC_samples} #, "VBS_ssWW", "VBS_WZjj", "VBS_WZll", "VBS_ZZ"]}
#samples = {   key:v for key,v in samples.items() if key == 'sm'}

################################################
# ---------->        to make datacard you need to skip VBS samples and other operators!!
operators_to_exclude = ["cT2", "cT1", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
full_operators_name_to_exclude = []
for op in operators_to_exclude:
   full_operators_name_to_exclude.append("quad_"+op)
   full_operators_name_to_exclude.append("sm_lin_quad_"+op)
# full_operators_name_to_exclude.append("sm_dipole")
# test_weights=['sm_all','sm_FT0','sm_weights','sm_noweights']
# samples = {   key:v for key,v in samples.items() if key  == 'DY'}
# samples = {   key:v for key,v in samples.items() if key in test_weights}
# samples = {   key:v for key,v in samples.items() if key == "sm_lin_quad_cT0"}
# samples = {   key:v for key,v in samples.items() if key not in VBS_samples and key not in full_operators_name_to_exclude} #'cT2' not in key and 'cT1' not in key}
# samples = {   key:v for key,v in samples.items() if key == 'sm_dipole'}
# samples = {   key:v for key,v in samples.items() if key in VBS_aQGC_samples}
# samples = {   key:v for key,v in samples.items() if key in sm_samples }operators_to_exclude = ["cT2", "cT1", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
theOperators = ["cT0", "cT2", "cT1", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
full_operators_name = []
for op in theOperators:
     full_operators_name.append("sm_"+op)
     full_operators_name.append("quad_"+op)
     full_operators_name.append("sm_lin_quad_"+op)
full_operators_name.append("sm")
samples = {   key:v for key,v in samples.items() if key in full_operators_name}