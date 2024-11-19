#!/bin/bash
# combine model from Massiro: https://github.com/UniMiBAnalyses/D6EFTStudies 

    ### launch it like: 
    ### source eft.sh fullrun2_fit_v4.5.5_aQGC_Aug2024_cT0_noStat_Mww_binzv/run2_boost_notop/combined_run2_boost_notop.txt cT0 boost_Mww_binzv_Aug2024_noStat 0.2 Run2 Mww_binzv Aug2024
    ### source eft_multipleOperators.sh fullrun2_fit_v4.5.5_aQGC_Aug2024_cT0_cT2_noNuis_Mww_binzv/2016_boost_notop/combined_2016_boost_notop.txt cT0 boost_Mww_binzv_Aug2024_noStat 0.3 2016 Mww_binzv Aug2024

datacard=$1
operator=$2
region=$3
range=$4
year=$5
var=$6
isEboli=$7
oplabel=$8
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
   -o model_test_${oplabel}_${region}_${year}.root \
   --PO eftOperators=cT0,cT1,cT2,cT3,cT4,cT5,cT6,cT7,cS0,cS1,cS2,cM0,cM1,cM2,cM3,cM4,cM5,cM7
   # --X-allow-no-signal \
   



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
all_operators=(cT0 cT1 cT2 cT3 cT4 cT5 cT6 cT7 cS0 cS1 cS2 cM0 cM1 cM2 cM3 cM4 cM5 cM7)
# all_operators=(cT0 cT2
# )
# Crea una stringa con tutti gli operatori tranne quello selezionato
freeze_params="r"
set_params="r=1"
for op in "${all_operators[@]}"; do
    if [[ $op != $operator ]]; then
        freeze_params="${freeze_params},k_${op}"
        set_params="${set_params},k_${op}=0"
    fi
done



   #step 2 blind
combine -M MultiDimFit model_test_${oplabel}_${region}_${year}.root \
   -m 125 -t -1 \
   --redefineSignalPOIs k_${operator} \
   --freezeParameters ${freeze_params} \
   --setParameters ${set_params} \
   --setParameterRanges k_${operator}=-${range},${range}:'rgx{.*norm_.*}'=0.1,4 \
   --verbose 2 \
   -n ${2}_${3}_expected \
   --algo=grid --points 120 --robustFit=1 \
   --alignEdges=1 --setRobustFitTolerance=0.1 \
   --cminDefaultMinimizerTolerance 0.1 --cminDefaultMinimizerStrategy=0 \
   --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 \
   --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 \
   --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP \
   --X-rtd FITTER_BOUND --fastScan

echo " DONE BLIND"
# unblind
combine -M MultiDimFit model_test_${oplabel}_${region}_${year}.root \
   -m 125 \
   --redefineSignalPOIs k_${operator} \
   --freezeParameters ${freeze_params} \
   --setParameters ${set_params} \
   --setParameterRanges k_${operator}=-${range},${range}:'rgx{.*norm_.*}'=0.1,4 \
   --verbose 2 \
   -n ${2}_${3}_observed \
   --algo=grid --points 120 --robustFit=1 \
   --alignEdges=1 --setRobustFitTolerance=0.1 \
   --cminDefaultMinimizerTolerance 0.1 --cminDefaultMinimizerStrategy=0 \
   --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 \
   --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 \
   --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP \
   --X-rtd FITTER_BOUND --fastScan




   # --algo=grid --points 120 --robustFit=1 \
   # --cminDefaultMinimizerStrategy=0 
   # --alignEdges=1 --setRobustFitTolerance=0.1 \
   # --cminDefaultMinimizerTolerance 0.1 \
   # --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=99999999999999 \
   # --cminFallbackAlgo Minuit2,Migrad,0:1 --stepSize=0.1 --setRobustFitStrategy=1 \
   # --maxFailedSteps 999999 --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP \
   # --X-rtd FITTER_BOUND --fastScan

echo " DONE UNBLIND"


# --cminDefaultMinimizerStrategy=1 originally


   # --freezeParameters r,k_${operator} \
#    #2a. plot the profile likelihood obtained
#root -l -q  higgsCombine${2}_${3}.MultiDimFit.mH125.root  \
#        higgsCombine${2}_${3}.MultiDimFit.mH125.root $CMSSW_BASE/src/HiggsAnalysis/AnalyticAnomalousCoupling/test/draw.cxx\(\"k_${operator}\"\)


    ##2b. plot the profile likelihood obtained: do this with python plotter

   # step 3

   python drawLS_withData.py \
        higgsCombine${2}_${3}_expected.MultiDimFit.mH125.root k_${operator} ${year} ${region} higgsCombine${2}_${3}_observed.MultiDimFit.mH125.root ${label} #${var} ${isEboli}

mv higgsCombine${2}_${3}_expected.MultiDimFit.mH125.root CIplots/combine/
mv higgsCombine${2}_${3}_observed.MultiDimFit.mH125.root CIplots/combine/
mv k_${2}_${3}_expected.root CIplots/
mv k_${2}_${3}_observed.root CIplots/
mv model_test_${oplabel}_${region}_${year}.root models/
    ##3. backup the plot to webpage
   # step 4
   # outdir=${year}_${region}
   # mkdir ${outdir}
   # mv LS_k_${operator}.* ${outdir}/
   # mv model_test_${operator}_${region}.root ${outdir}/
   # mv higgsCombine${operator}_${region}.MultiDimFit.mH125.root ${outdir}/


