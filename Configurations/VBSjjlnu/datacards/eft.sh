#!/bin/bash
# combine model from Massiro: https://github.com/UniMiBAnalyses/D6EFTStudies 

    ### launch it like: 
    ### sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/YearsCombination_8June2022/combined_boosted_bVeto.txt cT0 boosted_bVeto 
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT0_full/2018_all_split_Dipole_v4.5/combined_2018_all_split_Dipole_v4.5.txt cT0 fullAll 0.02 2018
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT0_full/2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5.txt cT0 boostonly 0.02 2018
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT2_full/2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5.txt cT2 boostonly 0.1 2018
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT2_full_vbsmjj/2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5.txt cT2 boostonly_vbsmjj 0.1 2018
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT0_full_MwwDav/2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5.txt cT0 boostonly_MwwDav 0.02 2018
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT0_full_DNN/2018_all_split_Dipole_v4.5/combined_2018_all_split_Dipole_v4.5.txt cT0 all_DNN 0.02 2018
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT0_full_Mww20/2018_boost_split_Dipole_v4.5/combined_2018_boost_split_Dipole_v4.5.txt cT0 all_Mww20 0.02 2018
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_full_DNN/run2_all/combined_run2_all.txt cT0 all_DNN_eboliv2 0.04 Run2
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_DNN/run2_boost/combined_run2_boost_postfitRateParam2017.txt cT0 boost_DNN_rateparam2017 0.04 Run2
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_cT0_old_Mww/2018_boost_notop/combined_2018_boost_notop.txt cT0 boost_Mww 0.2 2018 Mww false
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_cT0_old_Mww_binzv/2018_boost_notop/combined_2018_boost_notop.txt cT0 boost_Mww_binzv 0.2 2018 Mww_binzv false
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_full_mjj_vbs/run2_all/combined_run2_all.txt cT0 all_mjj_vbs 1 Run2
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT0_eboliv2_full_DNN/2018_all_split_Dipole_v4.5/combined_2018_all_split_Dipole_v4.5.txt cT0 all_DNN 0.04 2018
    ### source eft.sh 2018_fit_v4.5.5_aQGC_cT0_eboliv2_full_MwwRebinned/2018_all_split_Dipole_v4.5/combined_2018_all_split_Dipole_v4.5.txt cT0 all_MwwRebinned 0.04 2018 Mww_rebinned_GiacomoTest true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_JETuncShape_Mww/run2_boost/combined_run2_boost.txt cT0 all_Mww_JETuncShape 0.04 Run2 Mww_JETuncShape true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official/run2_boost/combined_run2_boost.txt cT0 all_Mww 0.04 Run2 Mww true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_testSM_Mww_binzv/run2_boost/combined_run2_boost.txt cT0 boost_Mww_binzv_testSM 0.2 Run2 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_allButFj_Mww_binzv/2017_boost/combined_2017_boost.txt cT0 boost_Mww_binzv_allButFj 0.2 2017 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT1_eboliv2_official_noVVandVVVjetunc_Mww_binzv/2017_boost/combined_2017_boost.txt cT1 boost_Mww_binzv 0.2 2017 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_testDY_Mww_binzv/2017_boost_toponly/combined_2017_boost_toponly.txt cT0 boost_Mww_binzv_testDY 0.2 2017 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT0sm_Mww_binzv/run2_boost_notop/combined_run2_boost_notop.txt cT0 boost_Mww_binzv_cT0sm 0.2 Run2 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT1_eboliv2_official_cT0sm_Mww_binzv/run2_boost_notop/combined_run2_boost_notop.txt cT1 boost_Mww_binzv_cT0sm 0.2 Run2 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_TEST4_Mww_binzv/2018_boost_notop_merged/combined_2018_boost_notop_merged.txt cT0 boost_notop_merged_Mww_binzv 0.2 2018 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT_Mww_binzv/2018_boost_notop/combined_2018_boost_notop.txt cT0 boost_notop_SMP18002_Mww_binzv 0.2 2018 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_SMP18006_noratetop_Mww_binzv/2016_boost_notop/combined_2016_boost_notop.txt cT0 boost_notop_SMP18006_noratetop_Mww_binzv 0.2 2016 Mww_binzv true
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_eboliv2_official_cT0_smDipole_noSignalSyst_Mww_binzv/2018_boost_notop/combined_2018_boost_notop.txt cT0 boost_Mww_binzv_smDipole_noSignalSyst_centralProd 0.2 2018 Mww_binzv true
datacard=$1
operator=$2
region=$3
range=$4
year=$5
var=$6
isEboli=$7

#step 0
#rm -rf model_test.root
   # create rootfit workspace from datacard
ulimit -s unlimited

if [ -f "${datacard}" ]; then
  echo "Found ${datacard}"
else
   echo "The file ${datacard} does not exist!!"
   return
fi

#step1
text2workspace.py  "${datacard}" \
   -v 2 \
   -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative \
   -o model_test_${operator}_${region}_${year}.root \
   --X-allow-no-signal \
   --PO  addDim8 \
   --PO eftOperators=${operator}  #cT0,cT1,cT2,cT5,cT6,cT7,cT8,cT9



   #########################
   # Looping on operators ##
   #########################
    #declare -a StringArray=( "cT1" "cT2" "cT5" "cT6" "cT7" "cT8" "cT8" "cT9")      
    #for OP in "${StringArray[@]}"; do                                      

   #######################################
   #       run  for single operator:    #
   #######################################    
   #1. fit 
   # ,k_cT1,k_cT5,k_cT6,k_cT7,k_cT8,k_cT9,  \
#--PO  addDim8   combine -M MultiDimFit model_test.root \
#--PO  addDim8      --algo=grid --points 500 -m 125 -t -1 \
#--PO  addDim8      --redefineSignalPOIs k_${operator} \
#--PO  addDim8      --freezeParameters r,k_${operator} \
#--PO  addDim8      --setParameters r=1 \
#--PO  addDim8      --setParameterRanges k_${operator}=-${range},${range} \
#--PO  addDim8      --verbose -1 \
#--PO  addDim8      -n ${2}_${3}


   #################################################################
   #       run  for single operator, fitting options improved:     #
   #################################################################
   #1. fit 
   # ,k_cT1,k_cT5,k_cT6,k_cT7,k_cT8,k_cT9,  \

   #step 2
combine -M MultiDimFit model_test_${operator}_${region}_${year}.root \
   -m 125 -t -1 \
   --redefineSignalPOIs k_${operator} \
   --freezeParameters r \
   --setParameters r=1 \
   --setParameterRanges k_${operator}=-${range},${range}:'rgx{.*norm_.*}'=0.1,4 \
   --verbose 2 \
   -n ${2}_${3} \
   --algo=grid --points 50 --robustFit=1 \
   --alignEdges=1 --setRobustFitTolerance=0.1 \
   --cminDefaultMinimizerTolerance 0.1 --cminDefaultMinimizerStrategy=0 \
   --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 \
   --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 \
   --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP \
   --X-rtd FITTER_BOUND --fastScan

# --cminDefaultMinimizerStrategy=1 originally


   # --freezeParameters r,k_${operator} \
#    #2a. plot the profile likelihood obtained
#root -l -q  higgsCombine${2}_${3}.MultiDimFit.mH125.root  \
#        higgsCombine${2}_${3}.MultiDimFit.mH125.root $CMSSW_BASE/src/HiggsAnalysis/AnalyticAnomalousCoupling/test/draw.cxx\(\"k_${operator}\"\)


    ##2b. plot the profile likelihood obtained: do this with python plotter

   # step 3
python drawLS.py \
        higgsCombine${2}_${3}.MultiDimFit.mH125.root k_${operator} ${year} ${region} ${var} ${isEboli}

mv higgsCombine${2}_${3}.MultiDimFit.mH125.root CIplots/combine/
mv model_test_${operator}_${region}_${year}.root models/
    ##3. backup the plot to webpage
   # step 4
   # outdir=${year}_${region}
   # mkdir ${outdir}
   # mv LS_k_${operator}.* ${outdir}/
   # mv model_test_${operator}_${region}.root ${outdir}/
   # mv higgsCombine${operator}_${region}.MultiDimFit.mH125.root ${outdir}/


