
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

############################################
############ MORE MC STAT ##################
############################################

def CombineBaseW(samples, proc, samplelist):
  newbaseW = getBaseWnAOD(directory_bkg, 'Autumn18_102X_nAODv7_Full2018v7', samplelist)
  for s in samplelist:
    addSampleWeight(samples, proc, s, newbaseW+'/baseW')
    
    
samples = {}
################################################
################# SKIMS ########################
################################################

# Steps
mcSteps   = 'MCl1loose2018v7__MCCorr2018v7__MCCombJJLNu2018' 

mcProduction =   'Autumn18_102X_nAODv7_Full2018v7_skim'
mcProductionIZ =   'Autumn18_102X_nAODv7_Full2018v7'

SITE=os.uname()[1]
xrootdPath=''
if  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
  treeBaseDir_SMP = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/'

directory_signal = os.path.join(treeBaseDir_SMP ,  mcProduction , mcSteps) 
directory_signalIZ = os.path.join(treeBaseDir_SMP ,  mcProductionIZ , mcSteps)
##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirSMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

def makeMCDirectorySMPeos(var=''):
    if var:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()

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



################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'




###########################################
#############  SM  SIGNALS  ###############
###########################################


xsweight_new_WpToLNu_WmTo2J='3.21'
xsweight_mcm_WpToLNu_WmTo2J='17.99'
xsweight_new_WpTo2J_WmToLNu='3.205'
xsweight_mcm_WpTo2J_WmToLNu='17.91'
xsweight_new_WpToLNu_WpTo2J='0.7297'
xsweight_mcm_WpToLNu_WpTo2J='3.453'
xsweight_new_WmToLNu_WmTo2J='0.08887'
xsweight_mcm_WmToLNu_WmTo2J='0.5065'
xsweight_new_WmToLNu_ZTo2J='0.1383'
xsweight_mcm_WmToLNu_ZTo2J='0.7416'
xsweight_new_WpToLNu_ZTo2J='0.3992'
xsweight_mcm_WpToLNu_ZTo2J='1.896'

#************* sm VBS ewk with (old) global recoil option, for EFT limits *******#
samples['sm_global'] ={ # should not use dipole recoil for aqgc SM part
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

addSampleWeight(samples,'sm_global','WpToLNu_WmTo2J',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
addSampleWeight(samples,'sm_global','WpTo2J_WmToLNu',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
addSampleWeight(samples,'sm_global','WpToLNu_WpTo2J',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
addSampleWeight(samples,'sm_global','WmToLNu_WmTo2J',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
addSampleWeight(samples,'sm_global','WmToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
addSampleWeight(samples,'sm_global','WpToLNu_ZTo2J',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj



    #************ sm VBS ewk with dipole recoil *********************#
samples['sm_dipole']  = { 'name' :  
               nanoGetSampleFiles(directory_signal,'WmToLNu_ZTo2J_dipoleRecoil',) + 
               nanoGetSampleFiles(directory_signal,'WpToLNu_ZTo2J_dipoleRecoil',) +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WpTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WmToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpToLNu_WmTo2J_dipoleRecoil') +
               nanoGetSampleFiles(directory_signal,'WpTo2J_WmToLNu_dipoleRecoil') ,
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch,
       'FilesPerJob' :15,
       'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_dipole','WpToLNu_WmTo2J_dipoleRecoil',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
addSampleWeight(samples,'sm_dipole','WpTo2J_WmToLNu_dipoleRecoil',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
addSampleWeight(samples,'sm_dipole','WpToLNu_WpTo2J_dipoleRecoil',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
addSampleWeight(samples,'sm_dipole','WmToLNu_WmTo2J_dipoleRecoil',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
addSampleWeight(samples,'sm_dipole','WmToLNu_ZTo2J_dipoleRecoil',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
addSampleWeight(samples,'sm_dipole','WpToLNu_ZTo2J_dipoleRecoil',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj

########################################
#######       EFT weights       ########
########################################
sm_cS0 = 'LHEReweightingWeight[526]'
sm_cS0_eboliv2 = 'LHEReweightingWeight[40]'
quadReweight_cS0 = '( 0.5* (1/50) * (1/50) * (LHEReweightingWeight[568] + LHEReweightingWeight[567] - 2*LHEReweightingWeight[526]) )'
quadReweight_cS0_eboliv2 = '( 0.5* (1/30) * (1/30) * (LHEReweightingWeight[0] + LHEReweightingWeight[80] - 2*LHEReweightingWeight[40]) )'



#************ OLD eboli basis, GLOBAL recoil ************#
samples['sm_aQGC'] = {
    'name':   
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC')  + #VBS_WZjj
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC'),   #VBS_WZjj
    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + sm_cS0 , 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_aQGC','WpToLNu_WmTo2J_aQGC',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
addSampleWeight(samples,'sm_aQGC','WpTo2J_WmToLNu_aQGC',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
addSampleWeight(samples,'sm_aQGC','WpToLNu_WpTo2J_aQGC',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
addSampleWeight(samples,'sm_aQGC','WmToLNu_WmTo2J_aQGC',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
addSampleWeight(samples,'sm_aQGC','WmToLNu_ZTo2J_aQGC',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
addSampleWeight(samples,'sm_aQGC','WpToLNu_ZTo2J_aQGC',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj




#************ new eboli basis, dipole recoil ************#
samples['sm_aQGC_eboliv2'] = {
    'name':   
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),   #VBS_WZjj   
    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + sm_cS0_eboliv2, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_aQGC_eboliv2','WmToLNu_ZTo2J_aQGC_eboliv2', '(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_aQGC_eboliv2','WpToLNu_ZTo2J_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0)')  #VBS_WZjj


###########################################
#############  EFT QUAD FSO ###############
###########################################
samples['quad_cS0'] = {
    'name':
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC')  + #VBS_WZjj
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC'),   #VBS_WZjj
       'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cS0,
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}

addSampleWeight(samples,'quad_cS0','WpToLNu_WmTo2J_aQGC',      xsweight_new_WpToLNu_WmTo2J+' / '+xsweight_mcm_WpToLNu_WmTo2J ) #VBS_osWW
addSampleWeight(samples,'quad_cS0','WpTo2J_WmToLNu_aQGC',      xsweight_new_WpTo2J_WmToLNu+' / '+xsweight_mcm_WpTo2J_WmToLNu)  #VBS_osWW
addSampleWeight(samples,'quad_cS0','WpToLNu_WpTo2J_aQGC',      xsweight_new_WpToLNu_WpTo2J+' / '+xsweight_mcm_WpToLNu_WpTo2J ) #VBS_ssWW
addSampleWeight(samples,'quad_cS0','WmToLNu_WmTo2J_aQGC',      xsweight_new_WmToLNu_WmTo2J+' / '+xsweight_mcm_WmToLNu_WmTo2J)  #VBS_ssWW
addSampleWeight(samples,'quad_cS0','WmToLNu_ZTo2J_aQGC',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WmToLNu_ZTo2J+' / '+xsweight_mcm_WmToLNu_ZTo2J ) #VBS_WZjj
addSampleWeight(samples,'quad_cS0','WpToLNu_ZTo2J_aQGC',      '(Sum$(abs(GenPart_pdgId)==6)==0)  * '+ xsweight_new_WpToLNu_ZTo2J+' / '+xsweight_mcm_WpToLNu_ZTo2J)  #VBS_WZjj


#************ new eboli basis, dipole recoil ************#
samples['quad_cS0_eboliv2'] = {
    'name':
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WmTo2J_aQGC_eboliv2') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpTo2J_WmToLNu_aQGC_eboliv2') + #VBS_osWW
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_WpTo2J_aQGC_eboliv2') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_WmTo2J_aQGC_eboliv2') + #VBS_ssWW
              nanoGetSampleFiles(directory_signalIZ,'WmToLNu_ZTo2J_aQGC_eboliv2')  + #VBS_WZjj
              nanoGetSampleFiles(directory_signalIZ,'WpToLNu_ZTo2J_aQGC_eboliv2'),   #VBS_WZjj
    'weight': XSWeight+'*'+SFweight+'*'+METFilter_MC+'*'+GenLepMatch + '*' + quadReweight_cS0_eboliv2,
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cS0_eboliv2','WmToLNu_ZTo2J_aQGC_eboliv2', '(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'quad_cS0_eboliv2','WpToLNu_ZTo2J_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0)')  #VBS_WZjj

# samples = {   key:v for key,v in samples.items() if key == 'sm_dipole'}
