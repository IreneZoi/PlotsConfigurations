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


Date2016=23May2022_2016
Date2017=29May2022_2017
Date2018=8June2022_2018

# datacardDir=2018_fit_v4.5.5_aQGC_cT0_full_DNN
datacardDir=2018_fit_v4.5.5_aQGC_cT0_eboliv2_full
# datacardDir=fullrun2_fit_v4.5.5_aQGC_cT0_DNN #MwwDav/ #vbsmjj/ #DNN/
#datacardDir2=Full2081v7/datacards_fit_v4.5_2018_split_aQGC_cT0_NoVBS_WithSignalNuis/ #Mww20/
#datacardDir2=Full2016v7/datacards_fit_v4.5_2016_split_aQGC_cT0/ #Mww20/
# datacardDir2=Full2017v7/datacards_fit_v4.5_2017_split_aQGC_cTO_fixSM/
datacardDir2=Full2018v7/datacards_fit_v4.5_2018_split_aQGC_cT0_eboliv2
#datacardDir2=datacards_fit_v4.5_2018_split_aQGC_cT0_DNN/ #Mww20/ 
operator=cT0
basis=eboliv2
fulloperator=$operator
if [[ $basis -eq eboliv2 ]]
then
  fulloperator=${operator}_${basis}
fi

echo full operator "$fulloperator"
######################   ------ step 0 required !! -----------
# datacards & workspaces are created in Davide's adapted code - step 0 (done in analysis setup)
#DATACARD_FIT=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/${datacardDir}/run2_boost/combined_run2_boost_postfitRateParam2017 #2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5
DATACARD_FIT=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/${datacardDir}/2018_all_split_Dipole_v4.5/combined_2018_all_split_Dipole_v4.5

# source postfit_loop_Run2_EFT_WV.sh boostonly boost_sig_ele Mww_binzv
# source postfit_loop_Run2_EFT_WV.sh boostonly boost_sig_ele mjj_vbs
# source postfit_loop_Run2_EFT_WV.sh boostonly boost_sig_ele Mww
# source postfit_loop_Run2_EFT_WV.sh boostonly boost_wjetcr_ele DNNoutput_boost
# source postfit_loop_Run2_EFT_WV.sh boostonly boost_wjetcr_ele Mww
# source postfit_loop_Run2_EFT_WV.sh all_run2 boost_wjetcr_ele DNNoutput_boost
# source postfit_loop_Run2_EFT_WV.sh boostonly_run2 boost_wjetcr_ele DNNoutput_boost -> this fit converged!!! Need to see the postfits and check the eft.sh!!!
# source postfit_loop_Run2_EFT_WV.sh boostonly_run2 boost_wjetcr_ele Mww
# source postfit_loop_Run2_EFT_WV.sh boostonly_run2 boost_topcr_ele Mww_binzv 2018
# source postfit_loop_Run2_EFT_WV.sh boostonly_run2 boost_wjetcr_ele DNNoutput_boost 2016
# source postfit_loop_Run2_EFT_WV.sh boostonly_run2_rateparam2017 boost_wjetcr_ele DNNoutput_boost 2017
# source postfit_loop_Run2_EFT_WV.sh boostonly_2018 boost_wjetcr_ele DNNoutput_boost 2018 

Category=$1 #boost
CUT=$2 #boost_sig_ele
PLOTVAR=$3 #Mww_binzv
YEAR=$4
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
#Category=$1 #Resolved
#CUT=$2 #SR_bTag
#PLOTVAR=$3 #DNNoutput_pruned_bReq_morebins


    #########################################################################
    #   the fit is performed on all CRs and SRs of the three years (or 1 year for now), all categories
    #
    #
echo "${DATACARD_FIT}"

# ->->->->->->->    step - 1a: prepare workspace (done in datacard setup) - here use ALL CATEGORIES to have the proper fit

# text2workspace.py ${DATACARD_FIT}.txt -o ${DATACARD_FIT}.root

# # ->->->->->->->    step - 1b: make fit (done in datacard setup)
# blind
combine -M FitDiagnostics ${DATACARD_FIT}.root \
      --out ${datacardDir}/ \
      -t -1 --toysFreq --rMin -10 \
      -n ${Category}_${PLOTVAR} \
      --saveNormalizations --saveWithUncertainties \
      --expectSignal 1 --cminDefaultMinimizerStrategy 0 --robustFit=1
# # # unblind
# # combine -M FitDiagnostics ${DATACARD_FIT}.root \
# #         -v 2 \
# #       --out ${datacardDir}/ \
# #          --rMin -10 \
# #       -n ${Category}_${PLOTVAR} \
# #       --saveNormalizations --saveWithUncertainties \
# #       --expectSignal 1 --cminDefaultMinimizerStrategy 0 --robustFit=1



DatacardPATH=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/ #2018_fit_v4.5.5_aQGC_cT0/2018_all_split_Dipole_v4.5/

#     #########################################################################
#     #   make workspace for single category or 
#     #   combine the datacards of the signal regions we want to plot & then make corresponding workspace
#     #
#     #

DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${CUT}/${PLOTVAR}/

# # ->->->->->->->    step - 2a: make fit (done in datacard setup)

text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

# # # # # # ##############################################
# # # # # # ##                                           #
# # # # # # ##         pre / post-fit      plotting      #
# # # # # # ##         (mjj, DNN, any var.)              #
# # # # # # ##                                           #
# # # # # # ##############################################
# # # # # # #
# # # # # # # ->->->->->->->    step - 2b: as the description below says: get post fit shapes from workspace (done in datacard setup)

# # # # ########PostfitfromWorkspace
 PostFitShapesFromWorkspace \
    -d ${DatacardPATHpartial}/datacard.txt \
    -w ${DatacardPATHpartial}/datacard.root \
    -o output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
    --postfit --sampling \
    -f ${datacardDir}/fitDiagnostics${Category}_${PLOTVAR}.root:fit_s \
    --total-shapes

  #  This below with the whole workspace would work only if I had the same variables fitted for all cuts, but I do not so I have to select only cuts with the same variable (as done above)
  #  -w ${DatacardPATH}/combined_2018_all_split_Dipole_v4.5_aQGC_cT0.root \
  #  -d ${DatacardPATH}/combined_2018_all_split_Dipole_v4.5_aQGC_cT0.txt \


# ###################################################################
#         ###      uncomment for postfit  ######


# ->->->->->->->    step - 2c: make the postfit (done in analysis setup)

# #    create the folders where to backup files

# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/
# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/
# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/
# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/${PLOTVAR}
# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/
# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/
# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/
# mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/${PLOTVAR}

# # # clean local folder
# rm -r plot_combined/*

# mkPostFitCombinedPlot.py \
#   --inputFilePostFitShapesFromWorkspace output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
#   --outputFile output_postfit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
#   --kind P \
#   --cutName ${CUT} \
#   --variable ${PLOTVAR} \
#   --structureFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/structure_split.py \
#   --plotFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/plot_split_bins.py \
#   --lumiText ${LUMI} 
 
# # # ->->->->->->->    step - 2d: make the postfit plot (done in analysis setup)

# mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000

# cp -r plot_combined/*png /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/${PLOTVAR}/


# # ###################################################################
# #         ###      uncomment for prefit   ######

# # # ->->->->->->->    step - 2e: make the prefit (done in analysis setup)

# mkPostFitCombinedPlot.py \
#   --inputFilePostFitShapesFromWorkspace output_histograms_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
#   --outputFile output_prefit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root \
#   --kind p \
#   --cutName ${CUT} \
#   --variable ${PLOTVAR} \
#   --structureFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/structure_split.py \
#   --plotFile ../Full${YEAR}v7/conf_fit_v4.5_aQGC/plot_split_bins.py \
#   --lumiText ${LUMI}

# #     # clean up local plotter folder
# rm -r plot_combined/*

# # ->->->->->->->    step - 2f: make the prefit plot (done in analysis setup)

# mkPlot.py --pycfg=configuration_combined.py --inputFile=output_prefit_${YEAR}_EFT_WV_${fulloperator}_${CUT}.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000

# cp -r plot_combined/*png /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_${YEAR}/${fulloperator}/${Category}/${CUT}/${PLOTVAR}/

