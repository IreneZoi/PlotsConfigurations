tag = "WH3l_2016_v7_STXS_test"

treeName= 'Events'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with plot configuration
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 35.867

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances_dummy.py'

# used by mkShape to define output directory for root files
outputDir = 'rootFiles_'+tag

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plot_'+tag

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag
