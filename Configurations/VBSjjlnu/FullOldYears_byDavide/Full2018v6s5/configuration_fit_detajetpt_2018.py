# example of configuration file
treeName= 'Events'


tag = 'fit_detajetpt_2018'
direc = "conf_fit_detajetpt"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py'

# file with list of variables
variablesFile = direc+'/variables.py'

# file with list of cuts
cutsFile = direc +'/cuts.py' 

# file with list of samples
samplesFile = direc+'/samples.py' 

# file with list of samples
plotFile = direc+'/plot.py' 
#plotFile = direc +'/plot_rescaled_ele.py'



# luminosity to normalize to (in 1/fb)
lumi = 59.74

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
#outputDirPlots = 'plot_'+tag +"_rescaled/detajpt_ext"
outputDirPlots = 'plot_'+tag

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_'+tag


# structure file for datacard
structureFile = direc+'/structure.py'


# nuisances file for mkDatacards and for mkShape
#nuisancesFile = direc+'/nuisances.py'
nuisancesFile = direc+'/nuisances_datacard.py'

