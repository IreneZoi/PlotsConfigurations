# PlotsConfigurations
Plots configuration for mkShapes, mkPlot, mkDatacards
-> Minimalistic setup for UL sample studies
    
First, setup the LatinoAnalysis framework:

    cmsrel CMSSW_10_6_4
    cd CMSSW_10_6_4/src/
    cmsenv
    git clone --branch 13TeV git@github.com:latinos/setup.git LatinosSetup
    source LatinosSetup/SetupShapeOnly.sh
    scram b -j4

Download the PlotsConfigurations package anywhere, but remember to do 'cmsenv' of the CMSSW release you are using:

    git clone -b VBS_UL_semilep https://github.com/IreneZoi/PlotsConfigurations.git
NB: You need this commit in LatinoAnalysis https://github.com/IreneZoi/LatinoAnalysis/commit/e1531ef2b7cbf60390f213c14a0196353a28a8fb
Make a copy and edit the following python file (`userConfig.py`) to specify your base directory, i.e. the directory in which your job related information will be stored:

    cd LatinoAnalysis/Tools/python/
    cp userConfig_TEMPLATE.py userConfig.py
    cd -

Directory:

    https://github.com/IreneZoi/PlotsConfigurations/tree/VBS_UL_semilep/Configurations/VBS_UL_semilep

Produce the histograms submitting batch jobs using HTCondor (change here if you wan to run on multiple files or only 1 for testing   https://github.com/IreneZoi/PlotsConfigurations/blob/7ba80ac41afa7c7b879a8177fd531556feec1c04/Configurations/VBS_UL_semilep/Full2018v9/conf_ulsamples/samples.py#L73-L74): 

    mkShapesMulti.py --pycfg=configuration_2018_ulsamples.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch


If some of your jobs have failed because the wall clock time have been exceeded, you can resubmit the failed ones by going into the jobs directory (the one set in `userConfig.py`), and changing the queue using the following command:

    for i in *jid; do sed -i "s/longlunch/workday/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done


The operators used for this test are in https://github.com/IreneZoi/PlotsConfigurations/blob/VBS_UL_semilep/Configurations/VBS_UL_semilep/weights_files/operators_short.json with selected working points.

To plot variables for different operator weights use: https://github.com/IreneZoi/PlotsConfigurations/blob/VBS_UL_semilep/Configurations/VBS_UL_semilep/scripts/plotting/plot_ULweights.py

For quick tests you can run interactively by just typing `mkShapesMulti.py --pycfg=configuration.py`. Use `mkShapesMulty.py --help` for more options.
You can also run interactively but submitting jobs in parallel with the command `mkShapesMulti.py --pycfg=configuration.py --doThreads=True`.

Once all your jobs are done (you can check job status with `condor_q`), you will find a `rootFile` directory in your area containing all the histograms specified in your configuration. 
You can proceed by h-adding all the files to get a single one containing everything:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

The `--nThreads=10` option allows for running the Hadd step in multithreading mode (with 10 threads in this case), and is especially useful when your configuration contains many cuts and variables.
The `--doNotCleanup` option is used to keep the input root files. Without this option the input files will be deleted after the hadd step and only the final root file will be kept.

You can now proceed making plots (`mkPlot.py --help` to see all available options):

    mkPlot.py --pycfg configuration.py --inputFile rootFile/plots_TAG.root --showIntegralLegend 1

and datacards (`mkDatacards.py --help` to see all available options):

    mkDatacards.py --pycfg configuration.py --inputFile rootFile/plots_TAG.root

If you need yield tables in either .tex or .csv format, after running the FitDiagnostics method of Combine on a workspace obtained from the datacards:

    combine -M FitDiagnostics -d WORKSPACE.root --saveNormalizations --saveWithUncertainties
    
you can feed the output to mkTable (`mkTable.py --help` to see all available options):

    mkTable.py fitDiagnostics.root
    
in case you want to merge a set of categories and/or processes in the table, you can define a merging scheme. A template, as well as more detailed instructions on mkTable, can be found in LatinoAnalysis/ShapeAnalysis/data/.

Congratulations! You have done the analysis, or at least a very first step...


# Useful information

 - For fits and combine general info check the following:
 
    http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/
    
 - The current Latinos framework is based on the NanoAOD format. The list of available `nanoLatino` trees can be found here:
 
    https://twiki.cern.ch/twiki/bin/view/CMS/LatinosTreesRun2

 - The NanoAOD-nanoLatino MC sample mapping is defined in the following python dictionaries:
 
    https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/samples/Summer16_102X_nAODv5.py
    
    https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/samples/fall17_102X_nAODv5.py
    
    https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/samples/Autumn18_102X_nAODv5.py
     
