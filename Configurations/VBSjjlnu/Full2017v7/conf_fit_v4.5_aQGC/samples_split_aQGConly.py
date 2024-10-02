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
  treeBaseDir_FNAL = '/store/group/lnujj/aQGC_VVJJ_Private_Production_PreProcessing/'
  xrootdPath='root://cmseos.fnal.gov/'


directory_bkg    = treeBaseDir_SMP + 'Fall2017_102X_nAODv7_Full2017v7_skim/' + mcSteps
directory_mc    = treeBaseDir_SMP +  'Fall2017_102X_nAODv7_Full2017v7_skim/' + mcSteps
directory_signal = treeBaseDir_SMP + 'Fall2017_102X_nAODv7_Full2017v7_skim/' + mcSteps
directory_signalIZ = xrootdPath + treeBaseDir_FNAL + 'Fall2017_102X_nAODv7_Full2017v7/' + mcSteps
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

# Import the operators dictionary from EFT_dict.py
# Execute the contents of EFT_dim8_dictionary.py, please update the path according to your exigency 
with open('/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/EFTcoefficients/EFT_dim8_dictionary_v2.py') as f:
    code = compile(f.read(), 'EFT_dim8_dictionary_v2.py', 'exec')
    exec(code)

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
# samples = {key:v for key,v in samples.items() if key in  VBS_aQGC_samples}

theOperators = ["cT0", "cT2", "cT1", "cT3", "cT4", "cT5", "cT6", "cT7", "cT8", "cT9", "cS0", "cS1", "cM0", "cM1", "cM2", "cM3", "cM4", "cM5", "cM6", "cM7", "cM8", "cM9"]
full_operators_name = []
for op in theOperators: 
    full_operators_name.append("sm_"+op)
    full_operators_name.append("quad_"+op)
    full_operators_name.append("sm_lin_quad_"+op)
full_operators_name.append("sm")
samples = {   key:v for key,v in samples.items() if key in full_operators_name}
