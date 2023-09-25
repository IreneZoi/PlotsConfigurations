#!/bin/bash
years=$1 #(2016 2017 2018)
categories=$2 #(boost_wjetcr_ele boost_wjetcr_mu res_wjetcr_ele res_wjetcr_mu boost_topcr_ele boost_topcr_ele res_topcr_ele res_topcr_mu res_sig_ele res_sig_mu boost_sig_ele boost_sig_mu )
#variables=(fit_bins_boost    fit_bins_boost  fit_bins_res  fit_bins_res events events events events DNNoutput_res_v1 DNNoutput_res_v1 DNNoutput_boost DNNoutput_boost)
variable=$3 #deltaeta_vbs

arraylength=${#categories[@]}
for year in ${years[*]}; do
    echo " plotting ${year}"
    for (( i=0; i<${arraylength}; i++ ));
    do
        echo "index: $i, cat: ${categories[$i]}, var:  ${variables[$i]}"
        datacardDir2=Full${year}v7/datacards_fit_v4.5_${year}_split_aQGC_cT0_eboliv2 # eboliv2
        #DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variables[$i]}/
        DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variable}/


        text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root

    done

done