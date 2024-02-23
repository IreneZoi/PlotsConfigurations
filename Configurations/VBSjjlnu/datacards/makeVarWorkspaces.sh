#!/bin/bash
years=(2016 2017 2018)
categories=(boost_wjetcr_mu boost_wjetcr_ele boost_topcr_ele boost_topcr_mu     boost_sig_ele boost_sig_mu )
variables=(fit_bins_boost  events DNNoutput_boost Mww Mww_binzv deltaeta_vbs )

arraylength=${#categories[@]}
for year in ${years[*]}; do
    echo " plotting ${year}"
    for (( i=0; i<${arraylength}; i++ ));
    do
        echo "index: $i, cat: ${categories[$i]}" #, var:  ${variables[$i]}"
        for variable in ${variables[*]}; do
            datacardDir2=Full${year}v7/datacards_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_official_testSM #_NOpdfPSqcdMinorBkg # eboliv2
            DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variable}/
            # DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variable}/


            text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root
        done
    done

done
