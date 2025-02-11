#!bin/bash


# all_operators=(cT0 cT1 cT2 cT3 cT4 cT5 cT6 cT7 cS0 cS1 cS2 cM0 cM1 cM2 cM3 cM4 cM5 cM7)
# ranges=(       0.3 0.3 0.7 0.8 4   1   2   4    8   10  10   2   5   2   8   5   8    7)
# all_operators=(cT1 cT2 cT3 cT4 cT5 cT6 cT7 cS0 cS1 cS2 cM0 cM1 cM2 cM3 cM4 cM5 cM7)
# ranges=(       0.3 0.7 0.8 4   1   2   4    8   10  10   2   5   2   8   5   8    7)

all_operators=(cT5) # cS0)
ranges=(2 )
# all_operators=(cM7)
# ranges=(7 )
label=cT2rehadded
mkdir CIplots/${label}
region=boost_notop
# AllOperators_withNuis_Mww_binzv
year=2016
# directory=fullrun2_fit_v4.5.5_aQGC_Aug2024_cT0_cS0_DNN_Mww_Mww/${year}_${region}/combined_${year}_${region}.txt
directory=fullrun2_fit_v4.5.5_aQGC_Aug2024_cT2rehadded_Mww_binzv/${year}_${region}/combined_${year}_${region}.txt

outdir=/eos/home-i/izoi/www/VBS_SM_WV_semilep_aQGC/limits/${label}_${year}/
mkdir -p ${outdir}
cp       /eos/home-i/izoi/www/index.php ${outdir}

for op in "${!all_operators[@]}"; do
    target_operator=${all_operators[${op}]}
    range=${ranges[${op}]}
    echo operator ${target_operator} range ${range}
    source eft_multipleOperators.sh ${directory} ${target_operator} boost_Mww_rebinned_Aug2024_noStat ${range} ${year} Mww Aug2024 ${label}
    mkdir CIplots/${label}/${year}
    cp LS_k_${target_operator}.png CIplots/${label}/${year}/
    mv LS_k_${target_operator}.png ${outdir}
    cp yearCI_*-pLHE_${label}.txt ${outdir}
done


# year=2017
# directory=fullrun2_fit_v4.5.5_aQGC_Aug2024_cT0_cS0_DNN_Mww_Mww/${year}_${region}/combined_${year}_${region}.txt

# outdir=/eos/home-i/izoi/www/VBS_SM_WV_semilep_aQGC/limits/${label}_${year}/
# mkdir -p ${outdir}
# cp       /eos/home-i/izoi/www/index.php ${outdir}

# for op in "${!all_operators[@]}"; do
#     target_operator=${all_operators[${op}]}
#     range=${ranges[${op}]}
#     echo operator ${target_operator} range ${range}
#     source eft_multipleOperators.sh ${directory} ${target_operator} boost_Mww_binzv_Aug2024_noStat ${range} ${year} Mww_binzv Aug2024 ${label}
#     mkdir CIplots/${label}/${year}
#     cp LS_k_${target_operator}.png CIplots/${label}/${year}/
#     mv LS_k_${target_operator}.png ${outdir}
#     cp yearCI_*-pLHE_${label}.txt ${outdir}
# done


# year=2018
# directory=fullrun2_fit_v4.5.5_aQGC_Aug2024_cT0_cS0_DNN_Mww_Mww/${year}_${region}/combined_${year}_${region}.txt

# outdir=/eos/home-i/izoi/www/VBS_SM_WV_semilep_aQGC/limits/${label}_${year}/
# mkdir -p ${outdir}
# cp       /eos/home-i/izoi/www/index.php ${outdir}

# for op in "${!all_operators[@]}"; do
#     target_operator=${all_operators[${op}]}
#     range=${ranges[${op}]}
#     echo operator ${target_operator} range ${range}
#     source eft_multipleOperators.sh ${directory} ${target_operator} boost_Mww_binzv_Aug2024_noStat ${range} ${year} Mww_binzv Aug2024 ${label}
#     mkdir CIplots/${label}/${year}
#     cp LS_k_${target_operator}.png CIplots/${label}/${year}/
#     mv LS_k_${target_operator}.png ${outdir}
#     cp yearCI_*-pLHE_${label}.txt ${outdir}
# done

# year=Run2
# directory=fullrun2_fit_v4.5.5_aQGC_Aug2024_cT0_cS0_DNN_Mww_Mww/${year}_${region}/combined_${year}_${region}.txt

# outdir=/eos/home-i/izoi/www/VBS_SM_WV_semilep_aQGC/limits/${label}_${year}/
# mkdir -p ${outdir}
# cp       /eos/home-i/izoi/www/index.php ${outdir}

# for op in "${!all_operators[@]}"; do
#     target_operator=${all_operators[${op}]}
#     range=${ranges[${op}]}
#     echo operator ${target_operator} range ${range}
#     source eft_multipleOperators.sh ${directory} ${target_operator} boost_Mww_binzv_Aug2024_noStat ${range} ${year} Mww_binzv Aug2024 ${label}
#     mkdir CIplots/${label}/${year}
#     cp LS_k_${target_operator}.png CIplots/${label}/${year}/
#     mv LS_k_${target_operator}.png ${outdir}
#     cp yearCI_*-pLHE_${label}.txt ${outdir}
# done
