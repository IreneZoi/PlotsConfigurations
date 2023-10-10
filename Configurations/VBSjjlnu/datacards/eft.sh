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
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_Mww/run2_boost/combined_run2_boost.txt cT0 boost_Mww 0.04 Run2
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_full_mjj_vbs/run2_all/combined_run2_all.txt cT0 all_mjj_vbs 1 Run2

datacard=$1
operator=$2
region=$3
range=$4
year=$5

#step 0
#rm -rf model_test.root
   # create rootfit workspace from datacard
ulimit -s unlimited

#step1
text2workspace.py  "${datacard}" \
   -v 2 \
   -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative \
   -o model_test_${operator}_${region}.root \
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
combine -M MultiDimFit model_test_${operator}_${region}.root \
   -m 125 -t -1 \
   --redefineSignalPOIs k_${operator} \
   --freezeParameters r,k_${operator} \
   --setParameters r=1 \
   --setParameterRanges k_${operator}=-${range},${range} \
   --verbose 2 \
   -n ${2}_${3} \
   --algo=grid --points 500 --robustFit=1 \
   --alignEdges=1 --setRobustFitTolerance=0.1 \
   --cminDefaultMinimizerTolerance 0.1 --cminDefaultMinimizerStrategy=1 \
   --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 \
   --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 \
   --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP \
   --X-rtd FITTER_BOUND --fastScan


#    #2a. plot the profile likelihood obtained
#root -l -q  higgsCombine${2}_${3}.MultiDimFit.mH125.root  \
#        higgsCombine${2}_${3}.MultiDimFit.mH125.root $CMSSW_BASE/src/HiggsAnalysis/AnalyticAnomalousCoupling/test/draw.cxx\(\"k_${operator}\"\)


    ##2b. plot the profile likelihood obtained: do this with python plotter

   # step 3
python drawLS.py \
        higgsCombine${2}_${3}.MultiDimFit.mH125.root k_${operator} ${year} ${region}


    ##3. backup the plot to webpage
   # step 4
   # outdir=${year}_${region}
   # mkdir ${outdir}
   # mv LS_k_${operator}.* ${outdir}/
   # mv model_test_${operator}_${region}.root ${outdir}/
   # mv higgsCombine${operator}_${region}.MultiDimFit.mH125.root ${outdir}/


