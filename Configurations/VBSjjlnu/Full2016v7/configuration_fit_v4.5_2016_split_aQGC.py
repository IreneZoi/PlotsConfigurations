# example of configuration file
treeName= 'Events'

tag = 'fit_v4.5_2016_split_aQGC_cT0'
direc = 'conf_fit_v4.5_aQGC'

# used by mkShape to define output directory for root files
outputDir = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases_split.py'

# file with list of variables
variablesFile = direc+'/variables.py'

# file with list of cuts
cutsFile = direc+'/cuts.py'

# file with list of samples
samplesFile = direc+'/samples_split_aQGC.py' 

# file with list of samples
plotFile = direc+'/plot_split.py'



# luminosity to normalize to (in 1/fb)
lumi = 36.33

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot_'+tag 
# used by mkDatacards to define output directory for datacards

outputDirDatacard = 'datacards_' +tag

# structure file for datacard
structureFile = direc+'/structure_split.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = direc+'/nuisances_datacard_split.py'
#nuisancesFile = direc+'/nuisances.py'
#nuisancesFile = direc+'/nuisances_aQGC.py'

customizeScript = direc + '/customize.py'