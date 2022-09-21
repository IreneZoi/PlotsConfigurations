This is the code used in SMP-20-013 and we are trying to reproduce the resutls. The code uses the Latino Framework that will be installed first and the NN https://github.com/UniMiBAnalyses/NNEvaluation that needs CMSSW_11_1_4. 

The analysis is based on branch ```VBSjjlnu_v7``` in https://github.com/UniMiBAnalyses/PlotsConfigurations.git


# PlotsConfigurations
Plots configuration for mkShapes, mkPlot, mkDatacards

# Installation

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

Replace ```d/dvalsecc/private``` or ```i/izoi/VBSanalysis``` with your path to the CMSSW installation directory in several files!

## Control plots

From PlotsConfigurations go to the following directory where year is 2016 or 2017 or 2018 and **VERSION is 7** (so far, maybe it will update tu UL VERSION 9)

    Configurations/VBSjjlnu/FullYEARvVERSION


In my case using the **VBSjjlnu directory, v4.5 and use the split version of the configuration files** to have the correct splitting of the signals.

Produce the histograms submitting batch jobs using HTCondor. NB at the end of the configuration script listed below different samples can be selected.

    mkShapesMulti.py --pycfg=configuration_fit_v4.5_2018_split.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch
    
NB: check that the correct nuisance file is selected! The une with ```_datacard``` should be used with mkDatacard.
Also the QGL stuff should be produced separately with ```configuration_fit_v4.5_2018_qglnuis.py```

If some of your jobs have failed because the wall clock time have been exceeded, you can resubmit the failed ones by going into the jobs directory (the one set in `userConfig.py`), and changing the queue using the following command:

    for i in *jid; do sed -i "s/longlunch/workday/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

For quick tests you can run interactively by just typing `mkShapesMulti.py --pycfg=configuration.py`. Use `mkShapesMulty.py --help` for more options.
You can also run interactively but submitting jobs in parallel with the command `mkShapesMulti.py --pycfg=configuration.py --doThreads=True`.

Once all your jobs are done (you can check job status with `condor_q`), you will find a `rootFile` directory in your area containing all the histograms specified in your configuration. 

If the events in a file do not pass the selections, the job will keep crashing saying someting like:
```
Initializing cut "res_wjetcr_mu"
      0 events
```
In this case just create an empty corresponding file:

    root -l
    TFile f("plots_TAG_Wjets_res_21.root", "RECREATE")

You can proceed by h-adding all the files to get a single one containing everything:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

The `--nThreads=10` option allows for running the Hadd step in multithreading mode (with 10 threads in this case), and is especially useful when your configuration contains many cuts and variables.
The `--doNotCleanup` option is used to keep the input root files. Without this option the input files will be deleted after the hadd step and only the final root file will be kept.

You can now proceed making plots (`mkPlot.py --help` to see all available options):

    mkPlot.py --pycfg configuration.py --inputFile rootFile/plots_TAG.root --showIntegralLegend 1
    
Special treatment for **2017**: due to a special requirement for the electron trigger as per the recommendation on slide 22 of this talk https://indico.cern.ch/event/662751/contributions/2778365/attachments/1561439/2458438/egamma_workshop_triggerTalk.pdf
So: first run mkShape for Fake and Data splitting ele and mu →  this was needed to apply a specific trigger only to the electrons
Then merge them using the "magic" script in https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/VBSjjlnu_v7/Configurations/VBSjjlnu/scripts/sum_data_flavours.py

        python ../../scripts/sum_data_flavours.py  -i plots_fit_v4.5_2017_split.root -y 2017

Now you can proceed with producing the control plots and the rest of the analysis. Remember that to produce the 2017 control plots you need to comment the splitted DATA part and uncomment the correct DATA part in the ```samples_split.py``` file.

## Nuisance shapes treatment for fit v4.5

The output of mkShapes need to be processed to normalize some nuisance, rename and split by sample the Parton Shower (PS) ones and add the QGL uncertainty.

- 2018  
    a) Join the QCDscale variations of the W+jets bins since there were splitted in the jobs configuration 
    
        cd rootFile_fit_v4.5_2018_split/
        python ../../scripts/nuisances_tools/join_systematic_samples.py plots_fit_v4.5_2018_split.root QCDscale
    b - extra) The PS ISR and FSR for VBF-V_dipole (Herwig) are taken from Davide, that took them from VBF-V (Pythia)
        
        python ../../scripts/nuisances_tools/extract_nuisances_effect.py -i /eos/user/i/izoi/VBS_SM_WV_semilep_SM/fromDavide/plots_fit_v4.5_2018_split.root_fromDavide_withFSRandISR -o PS_effect_fit_v4.5_2018_split_VBF-V_dipole.root -s VBF-V_dipole -cf ../cuts_PS_extraction.txt -v ALL -n CMS_PS_ISR CMS_PS_FSR
        python ../../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_v4.5_2018_split.root -o plots_fit_v4.5_2018_split.root_PSnuis.root --nuisance-effect ../../Full2018v7/rootFile_fit_v4.5_2018_split/PS_effect_fit_v4.5_2018_split_VBF-V_dipole.root -sf VBF-V_dipole -n CMS_PS_FSR CMS_PS_ISR
        hadd plots_fit_v4.5_2018_split_minimalvar.root_all plots_fit_v4.5_2018_split_minimalvar.root plots_fit_v4.5_2018_split.root_PSnuis.root
   
    c) extract also the PDF effect:
    
        python ../../scripts/nuisances_tools/extract_nuisances_effect.py -i plots_fit_v4.5_2018_split.root -o PDF_effect_bkg_fit_v4.5_2018.root -sf ../samples_PDF_extraction.txt -cf ../cuts_PS_extraction.txt -v ALL -n pdf_weight_1718
        
        python ../../scripts/nuisances_tools/extract_nuisances_effect.py -i plots_fit_v4.5_2018_split.root -o PDF_effect_bkg_fit_v4.5_2018.root -sf  ../samples_PDF_extraction_accept.txt -cf ../cuts_PS_extraction.txt -v ALL -n pdf_weight_1718_accept
        
    d) Normalize the nuisance effect between regions (mainly PS, QCD scale and PU for Wjets and top). The behaviour is described in the config file ```../../scripts/nuisances_tools/nuisance_norm_conf_v4.5.py```: 
        
        python ../../scripts/nuisances_tools/normalize_nuisance_effect.py -i plots_fit_v4.5_2018_split.root -c ../../scripts/nuisances_tools/nuisance_norm_conf_v4.5.py -y 2018 -o ratio_normalize.json
     
    e) Then split the PS uncertainties for each sample and W+jets bin:
    
        python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_v4.5_2018_split.root --shape-name CMS_PS_ISR -sf ../samples_PS_extraction.txt 
        python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_v4.5_2018_split.root --shape-name CMS_PS_FSR -sf ../samples_PS_extraction.txt
            
    f) Run on the QGL nuisance 
        
        mkShapesMulti.py --pycfg=configuration_fit_v4.5_2018_split_qglnuis.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch
        mkShapesMulti.py --pycfg=configuration_fit_v4.5_2018_split_qglnuis.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10
        mkPlot.py --pycfg=configuration_fit_v4.5_2018_split_qglnuis.py --inputFile rootFile/plots_TAG.root --showIntegralLegend 1
        # Then extract the shape variations
        cd rootFile_fit_v4.5_2018_split_qglnuis/
        python ../../scripts/QGL_morphing/rename_qglnuis_shapes.py -i plots_fit_v4.5_2018_split_qglnuis.root -o qgl_morph_shapes_2018.root --outputfile-fit plots_fit_v4.5_2018_onlyvariations.root --name 1718
        # Hadd the main file with the onlyvariations one for qgl 
        cd ../rootFile_fit_v4.5_2018_split/
        hadd plots_fit_v4.5_2018_split_withqglnuis.root plots_fit_v4.5_2018_split.root ../rootFile_fit_v4.5_2018_split_qglnuis/plots_fit_v4.5_2018_onlyvariations.root
        #Add empty fake nuisance shapes to make mkDatacard not complaining
        python ../../scripts/nuisances_tools/fake_nuisance_shapes.py -i plots_fit_v4.4_2018_split.root --nuisances QGLmorph_quark_higheta_1718 QGLmorph_quark_loweta_1718 QGLmorph_gluon_higheta_1718 QGLmorph_gluon_loweta_1718

- 2017

    0) If you did not do it already, merge ele & mu data:
    
      python ../../scripts/sum_data_flavours.py  -i plots_fit_v4.5_2017_split.root -y 2017
        
    a) Join the QCDscale and QCDscale_Wjets_boost that was not split in bins variations of the W+jets bins since there were splitted in the jobs configuration     
    
         python ../../scripts/nuisances_tools/join_systematic_samples.py plots_fit_v4.5_2017_split.root QCDscale
         python ../../scripts/nuisances_tools/join_systematic_samples.py plots_fit_v4.5_2017_split.root QCDscale_Wjets_boost
         
    b) Apply PS: 
 
        python ../../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_v4.5_2017_split.root -o plots_fit_v4.5_2017_split.root_PSnuis.root --nuisance-effect ../../Full2018v7/rootFile_fit_v4.5_2018_split/PS_effect_fit_v4.5_2018_split.root -sf ../../Full2018v7/samples_PS_extraction.txt -n CMS_PS_FSR CMS_PS_ISR

    Then proceed as 2018:
    
    c) extract also the PDF effect:
    
        python ../../scripts/nuisances_tools/extract_nuisances_effect.py -i plots_fit_v4.5_2017_split.root -o PDF_effect_bkg_fit_v4.5_2017.root -sf ../../Full2018v7/samples_PDF_extraction.txt -cf ../../Full2018v7/cuts_PS_extraction.txt -v ALL -n pdf_weight_1718
        
         python ../../scripts/nuisances_tools/extract_nuisances_effect.py -i plots_fit_v4.5_2017_split.root -o PDF_effect_bkg_fit_v4.5_2017.root -sf  ../../Full2018v7/samples_PDF_extraction_accept.txt -cf ../../Full2018v7/cuts_PS_extraction.txt -v ALL -n pdf_weight_1718_accept
        
    d) Normalize the nuisance effect between regions (mainly PS, QCD scale and PU for Wjets and top). The behaviour is described in the config file ```../../scripts/nuisances_tools/nuisance_norm_conf_v4.5.py```: 
        
        hadd plots_fit_v4.5_2017_split.root_all plots_fit_v4.5_2017_split.root plots_fit_v4.5_2017_split.root_PSnuis.root
        python ../../scripts/nuisances_tools/normalize_nuisance_effect.py -i plots_fit_v4.5_2017_split.root_all -c ../../scripts/nuisances_tools/nuisance_norm_conf_v4.5.py -y 2017 -o ratio_normalize.json
     
    e) Then split the PS uncertainties for each sample and W+jets bin:
    
        python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_v4.5_2017_split.root_all --shape-name CMS_PS_ISR -sf ../../Full2018v7/samples_PS_extraction.txt 
        python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_v4.5_2017_split.root_all --shape-name CMS_PS_FSR -sf ../../Full2018v7/samples_PS_extraction.txt
        
    f) Run on the QGL nuisance 
        
        mkShapesMulti.py --pycfg=configuration_fit_v4.5_2017_split_qglnuis.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch
        mkShapesMulti.py --pycfg=configuration_fit_v4.5_2017_split_qglnuis.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10
        mkPlot.py --pycfg=configuration_fit_v4.5_2017_split_qglnuis.py --inputFile rootFile/plots_TAG.root --showIntegralLegend 1
        # Then extract the shape variations
        cd rootFile_fit_v4.5_2017_split_qglnuis/
        python ../../scripts/QGL_morphing/rename_qglnuis_shapes.py -i plots_fit_v4.5_2017_split_qglnuis.root -o qgl_morph_shapes_2017.root --outputfile-fit plots_fit_v4.5_2017_onlyvariations.root --name 1718
        # Hadd the main file with the onlyvariations one for qgl 
        cd ../rootFile_fit_v4.5_2017_split/
        hadd plots_fit_v4.5_2017_split_withqglnuis.root plots_fit_v4.5_2017_split.root ../rootFile_fit_v4.5_2017_split_qglnuis/plots_fit_v4.5_2017_onlyvariations.root
        #Add empty fake nuisance shapes to make mkDatacard not complaining
        python ../../scripts/nuisances_tools/fake_nuisance_shapes.py -i plots_fit_v4.4_2017_split.root --nuisances QGLmorph_quark_higheta_1718 QGLmorph_quark_loweta_1718 QGLmorph_gluon_higheta_1718 QGLmorph_gluon_loweta_1718
        
- 2016 (similar to 2017 but no need to merge ele and mu data, instead it will need an extra step with the PDFs)
        
    a) Join the QCDscale and QCDscale_Wjets_boost that was not split in bins variations of the W+jets bins since there were splitted in the jobs configuration     
    
         python ../../scripts/nuisances_tools/join_systematic_samples.py plots_fit_v4.5_2016_split.root QCDscale
         python ../../scripts/nuisances_tools/join_systematic_samples.py plots_fit_v4.5_2016_split.root QCDscale_Wjets_boost
         
    b) Apply PS: 
 
        python ../../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_v4.5_2016_split.root -o plots_fit_v4.5_2016_split.root_PSnuis.root --nuisance-effect ../../Full2018v7/rootFile_fit_v4.5_2018_split/PS_effect_fit_v4.5_2018_split.root -sf ../../Full2018v7/samples_PS_extraction.txt -n CMS_PS_FSR CMS_PS_ISR
    
    c) ATTENTION: here instead we apply the 2018 pdf shapes to backgrounds and signals, separately
    
        python ../../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_v4.5_2016_split.root -o plots_fit_v4.5_2016_split.root_PDFbkgnuis.root --nuisance-effect ../../Full2018v7/rootFile_fit_v4.5_2018_split/PDF_effect_bkg_fit_v4.5_2018.root -sf ../samples_pdfbkg.txt -n pdf_weight_1718 -nr pdf_weight_16
        
        python ../../scripts/nuisances_tools/apply_nuisances_effect.py -i plots_fit_v4.5_2016_split.root -o plots_fit_v4.5_2016_split.root_PDFsignuis.root --nuisance-effect ../../Full2018v7/rootFile_fit_v4.5_2018_split/PDF_effect_bkg_fit_v4.5_2018.root -s VBS_osWW VBS_ssWW VBS_WZjj VBS_WZll VBS_ZZ -n pdf_weight_1718_accept -nr pdf_weight_16_accept
                 
    d) Normalize the nuisance effect between regions (mainly PS, QCD scale and PU for Wjets and top). The behaviour is described in the config file ```../../scripts/nuisances_tools/nuisance_norm_conf_v4.5.py```: 
        
        hadd plots_fit_v4.5_2016_split.root_all plots_fit_v4.5_2016_split.root plots_fit_v4.5_2016_split.root_PSnuis.root
        python ../../scripts/nuisances_tools/normalize_nuisance_effect.py -i plots_fit_v4.5_2016_split.root_all -c ../../scripts/nuisances_tools/nuisance_norm_conf_v4.5.py -y 2016 -o ratio_normalize.json
     
    e) Then split the PS uncertainties for each sample and W+jets bin:
    
        python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_v4.5_2016_split.root_all --shape-name CMS_PS_ISR -sf ../../Full2018v7/samples_PS_extraction.txt 
        python ../../scripts/nuisances_tools/rename_shape_root.py -i plots_fit_v4.5_2016_split.root_all --shape-name CMS_PS_FSR -sf ../../Full2018v7/samples_PS_extraction.txt
        
    f) Run on the QGL nuisance 
        
        mkShapesMulti.py --pycfg=configuration_fit_v4.5_2016_split_qglnuis.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch
        mkShapesMulti.py --pycfg=configuration_fit_v4.5_2016_split_qglnuis.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10
        mkPlot.py --pycfg=configuration_fit_v4.5_2016_split_qglnuis.py --inputFile rootFile/plots_TAG.root --showIntegralLegend 1
        # Then extract the shape variations
        cd rootFile_fit_v4.5_2016_split_qglnuis/
        python ../../scripts/QGL_morphing/rename_qglnuis_shapes.py -i plots_fit_v4.5_2016_split_qglnuis.root -o qgl_morph_shapes_2016.root --outputfile-fit plots_fit_v4.5_2016_onlyvariations.root --name 16
        # Hadd the main file with the onlyvariations one for qgl 
        cd ../rootFile_fit_v4.5_2016_split/
        hadd plots_fit_v4.5_2016_split_withqglnuis.root plots_fit_v4.5_2016_split.root ../rootFile_fit_v4.5_2016_split_qglnuis/plots_fit_v4.5_2016_onlyvariations.root
        #Add empty fake nuisance shapes to make mkDatacard not complaining
        python ../../scripts/nuisances_tools/fake_nuisance_shapes.py -i plots_fit_v4.4_2016_split.root --nuisances QGLmorph_quark_higheta_16 QGLmorph_quark_loweta_16 QGLmorph_gluon_higheta_16 QGLmorph_gluon_loweta_16

        
## Datacards
You can now proceed making datacards (`mkDatacards.py --help` to see all available options). Remember to use the correct nuisance in the config file. Example command:

    mkDatacards.py --pycfg configuration.py --inputFile rootFile/plots_TAG.root


Let's start with the EWK only fit.
Be sure the correct nuisance configuration is in the config file. In this case it should be `nuisances_datacard_split.py` and it should have the correct exclusion set at the end of the file, so the lines here https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/b35ac085ce0f5374e3d2ca24b938fc7d94666669/Configurations/VBSjjlnu/Full2018v7/conf_fit_v4.5/nuisances_datacard_split.py#L926-L927 . 

- For 2018:

        mkDatacards.py --pycfg=configuration_fit_v4.5_2018_split.py --inputFile rootFile_fit_v4.5_2018_split_minimalvar/plots_fit_v4.5_2018_split_withqglnuis.root --skipMissingNuisance

You also need to install combine following instructions in http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/

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
     
