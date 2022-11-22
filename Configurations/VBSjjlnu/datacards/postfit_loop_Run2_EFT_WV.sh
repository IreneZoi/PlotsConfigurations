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

datacardDir=2018_fit_v4.5.5_aQGC_cT0_full_vbsmjj/ #MwwDav/ #vbsmjj/
datacardDir2=datacards_fit_v4.5_2018_split_aQGC_cT0_NoVBS_WithSignalNuis/ 
operator=cT0
# datacards & workspaces are created in Davide's adapted code - step 0 (done in analysis setup)
DATACARD_FIT=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/${datacardDir}/2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5

# source postfit_loop_Run2_EFT_WV.sh boostonly boost_sig_ele Mww_binzv
# source postfit_loop_Run2_EFT_WV.sh boostonly boost_sig_ele mjj_vbs
# source postfit_loop_Run2_EFT_WV.sh boostonly boost_sig_ele Mww
Category=$1 #boost
CUT=$2 #boost_sig_ele
PLOTVAR=$3 #Mww_binzv

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

# combine -M FitDiagnostics ${DATACARD_FIT}.root \
#       --out ${datacardDir}/ \
#       -t -1 --toysFreq --rMin -10 \
#       -n ${Category}_${PLOTVAR} \
#       --saveNormalizations --saveWithUncertainties \
#       --expectSignal 1 --cminDefaultMinimizerStrategy 0 --robustFit=1


DatacardPATH=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/datacards/ #2018_fit_v4.5.5_aQGC_cT0/2018_all_split_Dipole_v4.5/

    #########################################################################
    #   make workspace for single category or 
    #   combine the datacards of the signal regions we want to plot & then make corresponding workspace
    #
    #

DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/Full2018v7/${datacardDir2}/${CUT}/${PLOTVAR}/

# ->->->->->->->    step - 2a: make fit (done in datacard setup)

# text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

# ##############################################
# ##                                           #
# ##         pre / post-fit      plotting      #
# ##         (mjj, DNN, any var.)              #
# ##                                           #
# ##############################################
# #
# # ->->->->->->->    step - 2b: as the description below says: get post fit shapes from workspace (done in datacard setup)

# ########PostfitfromWorkspace
#  PostFitShapesFromWorkspace \
#     -d ${DatacardPATHpartial}/datacard.txt \
#     -w ${DatacardPATHpartial}/datacard.root \
#     -o output_histograms_2018_EFT_WV_${operator}_${CUT}.root \
#     --postfit --sampling \
#     -f ${datacardDir}/fitDiagnostics${Category}_${PLOTVAR}.root:fit_s \
#     --total-shapes

#    This below with the whole workspace would work only if I had the same variables fitted for all cuts, but I do not so I have to select only cuts with the same variable (as done above)
#    -w ${DatacardPATH}/combined_2018_all_split_Dipole_v4.5_aQGC_cT0.root \
#    -d ${DatacardPATH}/combined_2018_all_split_Dipole_v4.5_aQGC_cT0.txt \


###################################################################
        ###      uncomment for postfit  ######


# ->->->->->->->    step - 2c: make the postfit (done in analysis setup)

# #    create the folders where to backup files
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_2018/${operator}/
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_2018/${operator}/${Category}/
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_2018/${operator}/${Category}/${CUT}/
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_2018/${operator}/${Category}/${CUT}/${PLOTVAR}
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_2018/${operator}/
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_2018/${operator}/${Category}/
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_2018/${operator}/${Category}/${CUT}/
mkdir -p /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_2018/${operator}/${Category}/${CUT}/${PLOTVAR}

# clean local folder
rm -r plot_combined/*

mkPostFitCombinedPlot.py \
  --inputFilePostFitShapesFromWorkspace output_histograms_2018_EFT_WV_${operator}_${CUT}.root \
  --outputFile output_postfit_2018_EFT_WV_${operator}_${CUT}.root \
  --kind P \
  --cutName ${CUT} \
  --variable ${PLOTVAR} \
  --structureFile ../Full2018v7/conf_fit_v4.5_aQGC/structure_split.py \
  --plotFile ../Full2018v7/conf_fit_v4.5_aQGC/plot_split.py \
  --lumiText '57/fb' 
 
# ->->->->->->->    step - 2d: make the postfit plot (done in analysis setup)

mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit_2018_EFT_WV_${operator}_${CUT}.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000

cp -r plot_combined/*png /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/postfit/WV_2018/${operator}/${Category}/${CUT}/${PLOTVAR}/


###################################################################
        ###      uncomment for prefit   ######

# ->->->->->->->    step - 2e: make the prefit (done in analysis setup)

mkPostFitCombinedPlot.py \
  --inputFilePostFitShapesFromWorkspace output_histograms_2018_EFT_WV_${operator}_${CUT}.root \
  --outputFile output_prefit_2018_EFT_WV_${operator}_${CUT}.root \
  --kind p \
  --cutName ${CUT} \
  --variable ${PLOTVAR} \
  --structureFile ../Full2018v7/conf_fit_v4.5_aQGC/structure_split.py \
  --plotFile ../Full2018v7/conf_fit_v4.5_aQGC/plot_split_bins.py \
  --lumiText '57/fb' 

#     # clean up local plotter folder
rm -r plot_combined/*

# ->->->->->->->    step - 2f: make the prefit plot (done in analysis setup)

mkPlot.py --pycfg=configuration_combined.py --inputFile=output_prefit_2018_EFT_WV_${operator}_${CUT}.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000

cp -r plot_combined/*png /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/prefit/WV_2018/${operator}/${Category}/${CUT}/${PLOTVAR}/

