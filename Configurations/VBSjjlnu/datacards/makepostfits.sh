#!/bin/bash
#years=(2016 2017 2018)
years=(2018)
# categories_boost=(boost_wjetcr_ele boost_wjetcr_mu  boost_topcr_ele boost_topcr_mu )
categories_boost=( boost_wjetcr_mu  boost_topcr_ele boost_topcr_mu )

# categories_boost=(boost_topcr_mu boost_sig_ele boost_sig_mu)
variables_boost=( fit_bins_boost  events DNNoutput_boost Mww Mww_binzv deltaeta_vbs )
# variables_boost=(events Mww deltaeta_vbs fit_bins_boost Zlep nJets_boost w_lep_pt mjj_vbs) # deltaphi_vbs Lepton_pt Lepton_eta  Centr_ww  whad_pt_boost  )

categories_res=(res_wjetcr_ele res_wjetcr_mu res_topcr_ele res_topcr_mu)
variables_res=(events Mww deltaeta_vbs fit_bins_res Zlep w_lep_pt nJets_res mjj_vbs ) # deltaphi_vbs Lepton_pt Lepton_eta  Centr_ww   )

operator=cT0
region=run2_boost
fitvar=Mww_binzv

outdir=Postfit_${operator}_eboliv2_official_${region}_SRvar${fitvar}/
mkdir ${outdir}


for year in ${years[*]}; do
    echo " plotting ${year}"
    for cat in ${categories_boost[*]}; do
        for var in ${variables_boost[*]}; do
            echo " cat: $cat, var:  $var"
            cd 
            source run_VBS_SM_datacard.sh

            datacardDir2=Full${year}v7/datacards_fit_v4.5_${year}_split_aQGC_${operator}_eboliv2_official_testSM # eboliv2
            DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${cat}/${var}/
            text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

            source postfit_loop_Run2_EFT_WV_env.sh ${region} ${cat} ${var} ${year} ${fitvar} false ${operator}
            # source postfit_loop_Run2_EFT_WV_env.sh run2_all boost_wjetcr_ele fit_bins_boost 2018 DNN true cT0
            # source postfit_loop_Run2_EFT_WV_env.sh run2_boost boost_wjetcr_ele fit_bins_boost 2018 Mww true cT0
            mv Postfit_${year}_${operator}_eboliv2_${region}_${cat}_SRvar${fitvar}_PlotVar${var} ${outdir}/
        done
    done


    # for cat in ${categories_res[*]}; do
    #     for var in ${variables_res[*]}; do
    #         echo " cat: $cat, var:  $var"
    #         cd 
    #         source run_VBS_SM_datacard.sh
    #         datacardDir2=Full${year}v7/datacards_fit_v4.5_${year}_split_aQGC_${operator}_eboliv2 # eboliv2
    #         DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${cat}/${var}/
    #         text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

    #         source postfit_loop_Run2_EFT_WV_env.sh ${region} ${cat} ${var} ${year} ${fitvar} false ${operator}
    #         mv Postfit_${year}_${operator}_eboliv2_${region}_${cat}_SRvar${fitvar}_PlotVar${var} ${outdir}/

    #     done
    # done



done


