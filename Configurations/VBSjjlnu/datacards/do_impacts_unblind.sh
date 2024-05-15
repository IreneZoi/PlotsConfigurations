#!/bin/bash
Date=20March2024
tag=run2_boost_notop_cT0_eboliv2_official

#options="--cminFallbackAlgo Minuit2,Simplex,0:0.1  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=9999999"
#options="--robustFit=1 --robustHesse=1 --cminDefaultMinimizerStrategy 0  --cminFallbackAlgo Minuit2,Migrad,0:0.1  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=9999999"
options1="--cminFallbackAlgo Minuit2,Migrad,0:1  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --X-rtd=MINIMIZER_analytic --X-rtd MINIMIZER_MaxCalls=9999999"#
#options="" #--robustFit=1 --robustHesse=1 --cminDefaultMinimizerStrategy 0 "
options3="--robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001"
options4="--robustFit=1 --cminDefaultMinimizerStrategy 2 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001"
options5="--robustFit=1 --cminDefaultMinimizerStrategy 0" # --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2 --setRobustFitTolerance 0.1 --stepSize=0.001"
options6=""

ranges="--setParameterRanges "
#rateParamsRanges="'rgx{.*norm_.*}'=-2,4:CMS_eff_prefiring_2018=-6,2:CMS_jetpuid_2018=-2,6:CMS_scale_JESBBEC1_2018=-2,6:CMS_scale_JESRelativeBal=-2,6" #:QCDscale_VBF-V=-6,6" 
rateParamsRanges="'rgx{.*norm_.*}'=-2,4" #:QCDscale_other=2,6:QCDscale_sm_dipole=-6,6:prop_binresolved_2016_sr1_bin0=-1,5:prop_binboosted_2016_sr1_bin14=-4,2:prop_binboosted_2017_topcr2_bin0=-4,2" #:'rgx{.*PS_ISR.*}'=-6,2:CMS_eff_prefiring_2018=-6,2:CMS_jetpuid_2018=-2,6"


#	first we need to copy the datacard from cernbox (as it is still produced via lxplus)
# rm -rf tmp/
# mkdir tmp
cd tmp

# cp ../fullrun2_fit_v4.5.5_aQGC_cT0_eboliv2_official_cT0sm_Mww_binzv/run2_boost_notop/combined_run2_boost_notop.root datacard.root

# xrdcp root://eosuser.cern.ch//eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/YearsCombination_6Dec2023_QCDscaleDY_corr_ln_2018btagDNNfrom2017_DNN_bReq_resolved_topcr__finalUnblinded__13March2024/combined.root datacard.root

inputCard=datacard
              ########################################################
              #   updating the rateparameters for DY samples in the  #
              #   combined datacards that will be used for impacts   #
              ########################################################
	#python ../scaripts/Utilities_nuisances/update_rateParam_initialization.py /eos/user/m/mpresill/www/VBS/diffNuisances/fit_${Date}.html ${inputCard}.txt
              ########################################################
              #               start impact calculation               #
              ########################################################
	#text2workspace.py ${inputCard}.txt ${inputCard}.root

# outputFolder=impacts/Impacts_${Date}_${tag}
# mkdir -p ${outputFolder}

# combineTool.py -M Impacts -d ${inputCard}.root --rMin -10 --rMax 10 --doInitialFit --allPars -m 1 -n ${tag} --parallel 50  ${options5} ${ranges}${rateParamsRanges} #--autoBoundsPOIs r

# combineTool.py -M Impacts -d ${inputCard}.root -o ${outputFolder}/impacts_t1.json  --rMin -10 --rMax 10 --doFits -m 1 -n ${tag} --parallel 50 ${options5} ${ranges}${rateParamsRanges} #--autoBoundsPOIs r

# combineTool.py -M Impacts -d ${inputCard}.root -m 1 -n ${tag} -o ${outputFolder}/impacts_${tag}.json --parallel 50

plotImpacts.py -i  ${outputFolder}/impacts_${tag}.json -o  impacts_${tag}_${Date} #--summary #--blind
xrdcp -f impacts_${tag}_${Date}.pdf root://eosuser.cern.ch//eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/impacts/${Date}/impacts_${tag}.pdf
# xrdcp -f tmp/impacts_${tag}_${Date}_summary.pdf root://eosuser.cern.ch//eos/user/i/izoi/www/VBS_SM_WV_semilep_aQGC/impacts/${Date}/impacts_${tag}_Summary.pdf

# cd ..


