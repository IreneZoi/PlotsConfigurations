# example of configuration file
treeName= 'Events'


tag = 'fit_v4.5_2018_split_aQGC_cT0_eboliv2'
direc = "conf_fit_v4.5_aQGC"

# used by mkShape to define output directory for root files
outputDir = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_'+tag 
#outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py'

# file with list of variables
variablesFile = direc+'/variables.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# file with list of samples
samplesFile = direc+'/samples_split_withAQGC.py' 
#samplesFile = direc+'/samples_test.py'

#t file with list of samples
plotFile = direc+'/plot_split.py' #irene made

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plot_'+tag +"_rescaled/detajpt_ext"
outputDirPlots = 'plot_'+tag  

# used by mkDatacards to define output directory for datacards
#outputDirDatacard = 'datacards_'+tag 
outputDirDatacard = 'datacards_'+tag

# structure file for datacard
structureFile = direc+'/structure_split.py'


# nuisances file for mkDatacards and for mkShape
#nuisancesFile = direc+'/nuisances.py'
nuisancesFile = direc+'/nuisances_aQGC.py' #aqgc files have a different directory than SM files and so a different path is needed for the nuisance. this was a quick fix
# nuisancesFile = direc + '/nuisances_datacard_split.py' # to make datacard you need to skip VBS samples!


customizeScript = direc + '/customize.py'