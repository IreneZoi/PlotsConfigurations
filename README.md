This is the code used in SMP-21-013 and we are trying to reproduce the resutls. The code uses the Latino Framework that will be installed first and the NN https://github.com/UniMiBAnalyses/NNEvaluation that needs CMSSW_11_1_4. 

The analysis is based on branch ```VBSjjlnu_v7``` in https://github.com/UniMiBAnalyses/PlotsConfigurations.git


# PlotsConfigurations
Plots configuration for mkShapes, mkPlot, mkDatacards

First, setup the LatinoAnalysis framework:

    cmsrel CMSSW_11_1_4
    cd CMSSW_11_1_4/src/
    cmsenv    
    git cms-init
    git clone --branch 13TeV https://github.com/latinos/setup.git LatinosSetup
    # in LatinosSetup/SetupShapeOnly.sh I had to change github-addext with git clone and changed from the git@ to the https version
    source LatinosSetup/SetupShapeOnly.sh
    #it seems that MelaAnalytics and ZZMatrixElement in the setup are not needed? I deleted them because the next compiling step was failing on that.
    scram b -j4

Download the DNN package and install TensorFlow:

    git cms-addpkg PhysicsTools/TensorFlow
    scram b -j 8
    git clone https://github.com/UniMiBAnalyses/NNEvaluation.git


Download the PlotsConfigurations package anywhere, but remember to do 'cmsenv' of the CMSSW release you are using:

    git clone https://github.com/UniMiBAnalyses/PlotsConfigurations.git

Make a copy and edit the following python file (`userConfig.py`) to specify your base directory, i.e. the directory in which your job related information will be stored:

    cd LatinoAnalysis/Tools/python/
    cp userConfig_TEMPLATE.py userConfig.py
change the path for were to save the log files but eos didn't work for me
  
    cd -
Ask access to the directory  ```/eos/home-d/dvalsecc/www/VBSPlots/DNN_archive/FullRun2_v7/FullRun2_v7/```

Replace ```d/dvalsecc/private``` with your path in several files!

From PlotsConfigurations go to the following directory (this is based on 2018 data and MC):

    Configurations/VBSjjlnu/Full2018v7

In my case using the VBSjjlnu directory, v4.5

Produce the histograms submitting batch jobs using HTCondor. NB at the end of the configuration script listed below different samples can be selected.

    mkShapesMulti.py --pycfg=configuration_fit_v4.5_2018.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch
NB: check that the correct nuisance file is selected! The une with ```_datacard``` should be used with mkDatacard.
Also the QGL stuff should be produced separately with ```configuration_fit_v4.5_2018_qglnuis.py```

Once the jobs are over, add the hists together:

     mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files

If some of your jobs have failed because the wall clock time have been exceeded, you can resubmit the failed ones by going into the jobs directory (the one set in `userConfig.py`), and changing the queue using the following command:

    for i in *jid; do sed -i "s/longlunch/workday/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

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
     
