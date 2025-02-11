# example of configuration file
treeName= 'Events'

tag = 'fit_v4.5_2016_split_aQGC_Aug2024_cT2rehadded' #_cT0_noStat'
direc = 'conf_fit_v4.5_aQGC'

# used by mkShape to define output directory for root files
outputDir = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_'+tag 

# file with TTree aliases
aliasesFile = direc+'/aliases_split.py'

# file with list of variables
variablesFile = direc+'/variables.py'
# variablesFile = direc+'/variables_DNN.py'

# file with list of cuts
cutsFile = direc+'/cuts.py'
# cutsFile = direc+'/cuts_SMP-18-006.py'
# cutsFile = direc+'/cuts_DNN.py'

# file with list of samples
# samplesFile = direc+'/samples_split_aQGConly_testS0.py'
# samplesFile = direc+'/samples_split_aQGConly.py'   # produce signals only
samplesFile = direc+'/samples_split_aQGC_all.py'     # make datacard
# samplesFile = direc+'/samples_split_aQGC_1file.py' # debug
# samplesFile = direc+'/samples_split_aQGC_sameBKG_asSMP-18-006.py'

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
nuisancesFile = direc+'/nuisances_datacard_asMatteo.py'  # make datacards
# nuisancesFile = direc+'/nuisances_aQGC_Aug2024.py'     # produce signals with nuisances

customizeScript = direc + '/customize.py'