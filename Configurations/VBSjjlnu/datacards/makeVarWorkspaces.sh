#!/bin/bash
# years=(2016 2017 2018)
years=(2017)
categories=( boost_sig_ele boost_sig_mu ) #boost_wjetcr_mu boost_wjetcr_ele      )
variables=( mjj_vbs)  #fit_bins_boost  events  Mww Mww_binzv deltaeta_vbs  )
# categories=(boost_sig_ele) # boost_wjetcr_mu boost_sig_mu)
# variables=(Mww_binzv ) #fit_bins_boost )
operator=cT0

arraylength=${#categories[@]}
for year in ${years[*]}; do
    echo " plotting ${year}"
    for (( i=0; i<${arraylength}; i++ ));
    do
        echo "index: $i, cat: ${categories[$i]}" #, var:  ${variables[$i]}"
        for variable in ${variables[*]}; do
            datacardDir2=Full${year}v7/datacards_fit_v4.5_${year}_split_aQGC_${operator}_eboliv2_official_cT0sm #SMP18006 #_NOpdfPSqcdMinorBkg # eboliv2
            DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variable}/
            # DatacardPATHpartial=/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/${datacardDir2}/${categories[$i]}/${variable}/


            text2workspace.py ${DatacardPATHpartial}/datacard.txt -o ${DatacardPATHpartial}/datacard.root
            echo ${DatacardPATHpartial}
        done
    done

done
