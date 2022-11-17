#!/bin/bash
# combine model from Massiro: https://github.com/UniMiBAnalyses/D6EFTStudies 

    ### launch it like: 
    ### sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/YearsCombination_8June2022/combined_boosted_bVeto.txt cT0 boosted_bVeto 


datacard=$1
operator=$2
region=$3
range=$4
year=$5

#step 0
#rm -rf model_test.root
   # create rootfit workspace from datacard

#step1
# text2workspace.py  ${datacard} \
#    -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative \
#    -o model_test.root \
#    --X-allow-no-signal \
#    --PO  addDim8 \
#    --PO eftOperators=${operator}  #cT0,cT1,cT2,cT5,cT6,cT7,cT8,cT9



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
combine -M MultiDimFit model_test.root \
   -m 125 -t -1 \
   --redefineSignalPOIs k_${operator} \
   --freezeParameters r,k_${operator} \
   --setParameters r=1 \
   --setParameterRanges k_${operator}=-${range},${range} \
   --verbose -1 \
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
python drawLS.py \
        higgsCombine${2}_${3}.MultiDimFit.mH125.root k_${operator} ${year} ${region}
    ##3. backup the plot to webpage
#mkdir -p /eos/user/m/mpresill/www/VBS/EFTlimits/
#cp /eos/user/m/mpresill/www/VBS/EFTlimits/index.php /eos/user/m/mpresill/www/VBS/EFTlimits/.
cp  LS_k_${operator}.png /eos/user/m/mpresill/www/VBS/EFTlimits/${operator}_${region}_${year}.png

    #######################################
    #     run  for two operators a time:  #
    ####################################### 

