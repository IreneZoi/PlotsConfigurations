# PlotsConfigurations
Plots configuration for mkShapes, mkPlot, mkDatacards
-> Minimalistic setup for UL sample studies
    

Download the PlotsConfigurations package anywhere, but remember to do 'cmsenv' of the CMSSW release you are using:

    git clone -b VBS_UL_semilep https://github.com/IreneZoi/PlotsConfigurations.git

NB: You need this commit in LatinoAnalysis https://github.com/IreneZoi/LatinoAnalysis/commit/e1531ef2b7cbf60390f213c14a0196353a28a8fb to be able to run on the private UL NanoAODv9 sample production

Directory:

    https://github.com/IreneZoi/PlotsConfigurations/tree/VBS_UL_semilep/Configurations/VBS_UL_semilep

Produce the histograms submitting batch jobs using HTCondor (change here if you wan to run on multiple files or only 1 for testing   https://github.com/IreneZoi/PlotsConfigurations/blob/7ba80ac41afa7c7b879a8177fd531556feec1c04/Configurations/VBS_UL_semilep/Full2018v9/conf_ulsamples/samples.py#L73-L74): 

    mkShapesMulti.py --pycfg=configuration_2018_ulsamples.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch


The operators used for this test are in https://github.com/IreneZoi/PlotsConfigurations/blob/VBS_UL_semilep/Configurations/VBS_UL_semilep/weights_files/operators_short.json with selected working points.

To plot variables for different operator weights use: https://github.com/IreneZoi/PlotsConfigurations/blob/VBS_UL_semilep/Configurations/VBS_UL_semilep/scripts/plotting/plot_ULweights.py

