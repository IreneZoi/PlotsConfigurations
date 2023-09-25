#!/bin/bash
years=(2016 2017 2018)

categories_boost=(boost_wjetcr_ele boost_wjetcr_mu  boost_topcr_ele boost_topcr_ele )
variables_boost=(events Mww deltaeta_vbs deltaphi_vbs fit_bins_boost Lepton_pt Lepton_eta mjj_vbs nJets_boost Centr_ww Zlep whad_pt_boost w_lep_pt )

categories_res=(res_wjetcr_ele res_wjetcr_mu res_topcr_ele res_topcr_mu)
variables_res=(events Mww deltaeta_vbs deltaphi_vbs fit_bins_res Lepton_pt Lepton_eta mjj_vbs nJets_res Centr_ww Zlep w_lep_pt )


for year in ${years[*]}; do
    echo " plotting ${year}"
    for cat in ${categories_boost[*]}; do
        for var in ${variables_boost[*]}; do
            echo " cat: $cat, var:  $var"
            cd 
            source run_VBS_SM_datacard.sh

            datacardDir2=Full${year}v7/datacards_fit_v4.5_${year}_split_aQGC_cT0_eboliv2 # eboliv2
            #DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variables[$i]}/
            DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${cat}/${var}/
            text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

            source postfit_loop_Run2_EFT_WV_env.sh run2_all ${cat} ${var} ${year} DNN false
        done
    done


    for cat in ${categories_res[*]}; do
        for var in ${variables_res[*]}; do
            echo " cat: $cat, var:  $var"
            cd 
            source run_VBS_SM_datacard.sh
            datacardDir2=Full${year}v7/datacards_fit_v4.5_${year}_split_aQGC_cT0_eboliv2 # eboliv2
            #DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variables[$i]}/
            DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${cat}/${var}/
            text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

            source postfit_loop_Run2_EFT_WV_env.sh run2_all ${cat} ${var} ${year} DNN false
        done
    done



done


