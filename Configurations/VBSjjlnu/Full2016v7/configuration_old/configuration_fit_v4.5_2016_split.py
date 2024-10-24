# example of configuration file
treeName= 'Events'

tag = 'fit_v4.5_2016_split_complete'
direc = 'conf_fit_v4.5'

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases_split.py'

# file with list of variables
variablesFile = direc+'/variables.py'

# file with list of cuts
cutsFile = direc+'/cuts.py'

# file with list of samples
samplesFile = direc+'/samples_split.py' 

# file with list of samples
plotFile = direc+'/plot.py'



# luminosity to normalize to (in 1/fb)
lumi = 36.33

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot_'+tag 
# used by mkDatacards to define output directory for datacards

outputDirDatacard = 'datacards_' +tag + "_Dipole_v6_mu"

# structure file for datacard
structureFile = direc+'/structure_split.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = direc+'/nuisances_datacard_split.py'
# nuisancesFile = direc+'/nuisances.py'

customizeScript = direc + '/customize.py'