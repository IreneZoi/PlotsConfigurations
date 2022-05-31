# example of configuration file
treeName= 'Events'


tag = '2018_ulsamples_vbsgenvars_fixdeta'
direc = "conf_ulsamples"

# used by mkShape to define output directory for root files
outputDir = 'rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases.py' #commented

# file with list of variables
variablesFile = direc+'/variables.py' #commented

# file with list of cuts
cutsFile = direc +'/cuts.py' #commented

# file with list of samples
#samplesFile = direc+'/samples_split.py' 
samplesFile = direc+'/samples.py' #done???

#t file with list of samples
plotFile = direc+'/plot_split.py' #todo later

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
structureFile = direc+'/structure_split.py' # todolater


# nuisances file for mkDatacards and for mkShape
nuisancesFile = direc+'/nuisances.py' #commented
#nuisancesFile = direc + '/nuisances_datacard_split.py'


customizeScript = direc + '/customize.py' #todolater