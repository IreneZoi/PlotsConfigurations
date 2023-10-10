#!/bin/bash

    ##############################################################################################################
    #   TO RUN IT LAUNCH:
    #   sh postfit_loop_2017.sh date folder CATEGORY CUT VARIABLEtoPLOT
    #
    #   example: sh postfit_loop_2017.sh 11May2022_2017 2017_Apr22_v2 Resolved DYcr_bTag DNNoutput_pruned_bReq
    #
    #   note that the fitdiagnostic is automatically chosen as the full-year-combined in this script
    #
    ###############################################################################################################

Category=$1 #boost
CUT=$2 #boost_sig_ele
PLOTVAR=$3 #Mww_binzv
YEAR=$4
SRVAR=$5
DOFIT=$6
operator=$7



# datacardDir=2018_fit_v4.5.5_aQGC_cT0_full_DNN
# datacardDir=2018_fit_v4.5.5_aQGC_cT0_full_MwwDav
#datacardDir=2018_fit_v4.5.5_aQGC_cT0_eboliv2_full_${SRVAR} # eboliv2
datacardDir=fullrun2_fit_v4.5.5_aQGC_${operator}_eboliv2_full_${SRVAR}
# datacardDir=fullrun2_fit_v4.5.5_aQGC_cT0_DNN #MwwDav/ #vbsmjj/ #DNN/
# datacardDir2=Full2081v7/datacards_fit_v4.5_2018_split_aQGC_cT0_NoVBS_WithSignalNuis/ #Mww20/
#datacardDir2=Full2016v7/datacards_fit_v4.5_2016_split_aQGC_cT0/ #Mww20/
# datacardDir2=Full2017v7/datacards_fit_v4.5_2017_split_aQGC_cTO_fixSM/
datacardDir2=Full${YEAR}v7/datacards_fit_v4.5_${YEAR}_split_aQGC_${operator}_eboliv2 # eboliv2
#datacardDir2=datacards_fit_v4.5_2018_split_aQGC_cT0_DNN/ #Mww20/ 

basis=eboliv2
fulloperator=$operator
if [[ $basis -eq eboliv2 ]]
then
  fulloperator=${operator}_${basis}
fi

echo full operator "$fulloperator"
######################   ------ step 0 required !! -----------
# datacards & workspaces are created in Davide's adapted code - step 0 (done in analysis setup)
DATACARD_FIT=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/${datacardDir}/${Category}/combined_${Category} #_postfitRateParam2017 #2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5
#DATACARD_FIT=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/${datacardDir}/2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5

# source postfit_loop_Run2_EFT_WV_env.sh boostonly boost_sig_ele Mww_binzv
# source postfit_loop_Run2_EFT_WV_env.sh boostonly boost_sig_ele mjj_vbs
# source postfit_loop_Run2_EFT_WV_env.sh boostonly boost_sig_ele Mww
# source postfit_loop_Run2_EFT_WV_env.sh boostonly boost_wjetcr_ele DNNoutput_boost
# source postfit_loop_Run2_EFT_WV_env.sh boostonly boost_wjetcr_ele Mww
# source postfit_loop_Run2_EFT_WV_env.sh all_run2 boost_wjetcr_ele DNNoutput_boost
# source postfit_loop_Run2_EFT_WV_env.sh boostonly_run2 boost_wjetcr_ele DNNoutput_boost -> this fit converged!!! Need to see the postfits and check the eft.sh!!!
# source postfit_loop_Run2_EFT_WV_env.sh boostonly_run2 boost_wjetcr_ele Mww
# source postfit_loop_Run2_EFT_WV_env.sh boostonly_run2 boost_topcr_ele Mww_binzv 2018
# source postfit_loop_Run2_EFT_WV_env.sh boostonly_run2 boost_wjetcr_ele DNNoutput_boost 2016
# source postfit_loop_Run2_EFT_WV_env.sh boostonly_run2_rateparam2017 boost_wjetcr_ele DNNoutput_boost 2017
# source postfit_loop_Run2_EFT_WV_env.sh run2_all boost_wjetcr_ele fit_bins_boost 2018 DNN false
# source postfit_loop_Run2_EFT_WV_env.sh run2_all boost_wjetcr_ele deltaeta_vbs 2018 DNN false cT0


LUMI=0
echo year "$YEAR"
if [[ $YEAR -eq 2018 ]]
then
  LUMI='59.7/fb'
elif [[ $YEAR -eq 2017 ]]
then
  LUMI='41.5/fb'
elif [[ $YEAR -eq 2016 ]]
then
  LUMI='35.867/fb'
fi

echo lumi is ${LUMI}


cd 
source run_VBS_SM_datacard.sh

if [ $DOFIT = true ]
then 

    #########################################################################
    #   the fit is performed on all CRs and SRs of the three years (or 1 year for now), all categories
    #
    #
    echo "***********************************"
    echo "Fitting enabled on ${DATACARD_FIT}"



    # ->->->->->->->    step - 1a: prepare workspace (done in datacard setup) - here use ALL CATEGORIES to have the proper fit
    # python ../scripts/prepare_datacard.py -c datacard_config_fullrun2_v4.5.5_split_aQGC_cT0_eboliv2_DNN.json -b ../ -o fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_full_DNN/ -p workspace -d run2_all --redo-workspace
    #text2workspace.py ${DATACARD_FIT}.txt -o ${DATACARD_FIT}.root

    # # ->->->->->->->    step - 1b: make fit (done in datacard setup)
    # blind
    # combine -M FitDiagnostics ${DATACARD_FIT}.root \
    #       --out ${datacardDir}/ \
    #       -t -1 --toysFreq --rMin -10 \
    #       -n ${Category}_${PLOTVAR} \
    #       --saveNormalizations --saveWithUncertainties \
    #      --expectSignal 1 \
    #      --robustFit=1 --stepSize=0.001 --robustHesse=1 --cminDefaultMinimizerStrategy 0 --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND

          # --expectSignal 1 --robustFit=1  --cminDefaultMinimizerStrategy 0

    # unblind
    combine -M FitDiagnostics ${DATACARD_FIT}.root \
            -v 2 \
            --out ${datacardDir}/ \
            --rMin -10 \
            -n ${Category}_${SRVAR} \
            --saveNormalizations --saveWithUncertainties \
            --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001
            #--cminDefaultMinimizerStrategy 0 --robustFit=1





    echo "Fit done"
    echo "***********************************"
fi

DatacardPATH=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/ #2018_fit_v4.5.5_aQGC_cT0/2018_all_split_Dipole_v4.5/

#     #########################################################################
#     #   make workspace for single category or 
#     #   combine the datacards of the signal regions we want to plot & then make corresponding workspace
#     #
#     #


DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${CUT}/${PLOTVAR}/

# # # ->->->->->->->    step - 2a: make fit (done in datacard setup)

# text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

# # # # # # ##############################################
# # # # # # ##                                           #
# # # # # # ##         pre / post-fit      plotting      #
# # # # # # ##         (mjj, DNN, any var.)              #
# # # # # # ##                                           #
# # # # # # ##############################################
# # # # # # #
# # # # # # # ->->->->->->->    step - 2b: as the description below says: get post fit shapes from workspace (done in datacard setup)

# # # ########PostfitfromWorkspace
 PostFitShapesFromWorkspace \
    -d ${DatacardPATHpartial}/datacard.txt \
    -w ${DatacardPATHpartial}/datacard.root \
    -o output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
    --postfit --sampling \
    -f ${datacardDir}/fitDiagnostics${Category}_${SRVAR}.root:fit_s \
    --total-shapes

#  PostFitShapesFromWorkspace \
#     -d ${DATACARD_FIT}_fullpath.txt \
#     -w ${DATACARD_FIT}.root \
#     -o output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
#     --postfit --sampling \
#     -f ${datacardDir}/fitDiagnostics${Category}_${SRVAR}.root:fit_s \
#     --total-shapes




  #  This below with the whole workspace would work only if I had the same variables fitted for all cuts, but I do not so I have to select only cuts with the same variable (as done above)
  #  -w ${DatacardPATH}/combined_2018_all_split_Dipole_v4.5_aQGC_cT0.root \
  #  -d ${DatacardPATH}/combined_2018_all_split_Dipole_v4.5_aQGC_cT0.txt \


cd 
source run_VBS_eboliv2.sh
cd datacards

# ###################################################################
#         ###      uncomment for postfit  ######


# # ->->->->->->->    step - 2c: make the postfit (done in analysis setup)

#    create the folders where to backup files

mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/
mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/
mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/
mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}
# mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}
# cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}
#mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}/${LABEL}

mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/
mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/
mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/
mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}
cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}
# mkdir -p /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}
# cp       /eos/user/i/izoi/www/index.php /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}
#mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/PlotVar${PLOTVAR}/${LABEL}


# # clean local folder
rm -r plot_combined/* 

mkPostFitCombinedPlot.py \
  --inputFilePostFitShapesFromWorkspace output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
  --outputFile output_postfit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
  --kind P \
  --cutName ${CUT} \
  --variable ${PLOTVAR} \
  --structureFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/structure_split.py \
  --plotFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/plot_split.py \
  --lumiText ${LUMI} 
 
# # ->->->->->->->    step - 2d: make the postfit plot (done in analysis setup)

mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000

cp -r plot_combined/*png /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/


# ###################################################################
#         ###      uncomment for prefit   ######

# # ->->->->->->->    step - 2e: make the prefit (done in analysis setup)

mkPostFitCombinedPlot.py \
  --inputFilePostFitShapesFromWorkspace output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
  --outputFile output_prefit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
  --kind p \
  --cutName ${CUT} \
  --variable ${PLOTVAR} \
  --structureFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/structure_split.py \
  --plotFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/plot_split.py \
  --lumiText ${LUMI}

#     # clean up local plotter folder
rm -r plot_combined/*

# ->->->->->->->    step - 2f: make the prefit plot (done in analysis setup)

mkPlot.py --pycfg=configuration_combined.py --inputFile=output_prefit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000

cp -r plot_combined/*png /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/SRvar${SRVAR}/

outdir=Postfit_${YEAR}_${fulloperator}_${Category}_${CUT}_SRvar${SRVAR}_PlotVar${PLOTVAR}/
echo output directory: $outdir
mkdir $outdir
mv variables_combined.py $outdir
mv structure_combined.py $outdir
mv plot_combined.py $outdir
mv cuts_combined.py $outdir
mv configuration_combined.py $outdir
mv output_prefit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root $outdir
mv output_postfit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root $outdir
mv output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root $outdir
mv higgsCombine${Category}_${SRVAR}.FitDiagnostics.mH120.root $outdir
