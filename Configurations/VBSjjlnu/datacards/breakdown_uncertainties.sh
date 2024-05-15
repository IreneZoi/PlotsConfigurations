#!/bin/bash
year=2017
label=notoprate
outputname=all_exp_theo_syst_stat_${year}_${label}_wjetnorm0p1_4
# text2workspace.py fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT0sm_Mww_binzv_nuisanceGroups/${year}_boost_notop/combined_${year}_boost_notop.txt -o fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT0sm_Mww_binzv_nuisanceGroups/${year}_boost_notop/combined_${year}_boost_notop.root


text2workspace.py fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT0sm_Mww_binzv_nuisanceGroups_${label}/${year}_boost_notop/combined_${year}_boost_notop.txt -o fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT0sm_Mww_binzv_nuisanceGroups_${label}/${year}_boost_notop/combined_${year}_boost_notop.root
workspace=fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT0sm_Mww_binzv_nuisanceGroups_${label}/${year}_boost_notop/combined_${year}_boost_notop


# default tolerance from Davide 0.2

combine -M MultiDimFit ${workspace}.root -v 2 --toysFrequentist -t -1 --expectSignal=1 -m 120 --algo grid --points 30 --saveWorkspace -n testGroup${year}.total --rMin -0.5 --rMax 2.5 --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 --setParameterRanges 'rgx{.*norm_.*}'=0.1,4 
    
echo .......................... nominal
    #### nominal
combine higgsCombinetestGroup${year}.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
       --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 -v2 \
       --setParameterRanges 'rgx{.*norm_.*}'=0.1,4 \
       --snapshotName MultiDimFit -n testGroup${year}.nominal 

# # echo .......................... ALL non-floating nuisances
# #     ### ALL (non-floating nuisances)
# # combine higgsCombinetestGroup.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
# #        --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 -v2 \
# #        --setParameterRanges 'rgx{.*Top_norm_.*}'=0.1,2:'rgx{.*Wjets_boost_[1-7]_norm_.*}'=-2,4 \
# #        --freezeParameters allConstrainedNuisances --snapshotName MultiDimFit -n testGroup.freeze_all_constrainrates_top0p1-2_wjetsm2-4

echo .......................... ALL non-floating nuisances 
    ### ALL (non-floating nuisances)
combine higgsCombinetestGroup${year}.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
       --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 -v2 \
       --setParameterRanges 'rgx{.*norm_.*}'=0.1,4 \
       --freezeParameters allConstrainedNuisances --snapshotName MultiDimFit -n testGroup${year}.freeze_all

#        --setParameterRanges 'rgx{.*norm_.*}'=-10,10 \

# echo .......................... ALL non-floating nuisances and wjets
#     ### ALL (non-floating nuisances)
# combine higgsCombinetestGroup.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
#        --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 -v2 \
#        --setParameterRanges 'rgx{.*norm_.*}'=0.1,4 \
#        --freezeParameters allConstrainedNuisances --freezeNuisanceGroups Wjetsnorm --snapshotName MultiDimFit -n testGroup.freeze_all_wjetsnorm


echo .......................... norm
    ##### norm
combine higgsCombinetestGroup${year}.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
       --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 -v2 \
       --setParameterRanges 'rgx{.*norm_.*}'=0.1,4 \
       --freezeNuisanceGroups Wjetsnorm --snapshotName MultiDimFit -n testGroup${year}.freeze_RateParams 

echo .......................... theory
    #### theory
combine higgsCombinetestGroup${year}.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
       --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 -v2 \
       --setParameterRanges 'rgx{.*norm_.*}'=0.1,4 \
       --freezeNuisanceGroups Wjetsnorm,theory --snapshotName MultiDimFit -n testGroup${year}.freeze_theory 

echo .......................... autoMCstats
    ### autoMCstats
combine higgsCombinetestGroup${year}.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
       --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001 -v2 \
       --setParameterRanges 'rgx{.*norm_.*}'=0.1,4 \
       --freezeNuisanceGroups Wjetsnorm,theory,autoMCStats  --snapshotName MultiDimFit -n testGroup${year}.freeze_MCstat







outputdir=breakdown_uncertainties/${year}/

mv higgsCombinetestGroup${year}.*.root ${outputdir}/
# mv higgsCombinetestGroup${year}.freeze_all.MultiDimFit.mH120.root ${outputdir}/

echo .......................... plotting
    ## plotting and copying to my webpage
plot1DScan.py ${outputdir}/higgsCombinetestGroup${year}.nominal.MultiDimFit.mH120.root --main-label "Total Uncert. (Asimov)"  \
   --others \
   ${outputdir}'/higgsCombinetestGroup'${year}'.freeze_RateParams.MultiDimFit.mH120.root:Freeze RateParams:920' \
   ${outputdir}'/higgsCombinetestGroup'${year}'.freeze_theory.MultiDimFit.mH120.root:Freeze RateParams+theory:600' \
   ${outputdir}'/higgsCombinetestGroup'${year}'.freeze_MCstat.MultiDimFit.mH120.root:Freeze RateParams+theory+MCstat:416' \
   ${outputdir}'/higgsCombinetestGroup'${year}'.freeze_all.MultiDimFit.mH120.root:Freeze all:800' \
    -o freeze_${outputname} \
    --breakdown "RateParams,theory,MCstat,Exp,stat"
    # --breakdown "Syst,Stat"
#   --breakdown "RateParams,theory,MCstat,Exp,stat"
  


echo .......................... copy
cp freeze_${outputname}.png /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/breakdown/YearsCombination_${outputname}.png
cp freeze_${outputname}.pdf /eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/nuisances/breakdown/YearsCombination_${outputname}.pdf
