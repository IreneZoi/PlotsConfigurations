#!bin/bash


all_operators=(cT0 cT1 cT2 cT3 cT4 cT5 cT6 cT7 cS0 cS1 cS2 cM0 cM1 cM2 cM3 cM4 cM5 cM7)
ranges=(0.3 0.3 0.7 1 1 1 1 5 6 6 2 4 5 3 5 5)

# all_operators=(cT0 cT2)
# ranges=(0.3 0.7)


directory=fullrun2_fit_v4.5.5_aQGC_Aug2024_cT0_cT2_noNuis_Mww_binzv/2016_boost_notop/combined_2016_boost_notop.txt
year=2016
label=cT0_cT2
outdir=/eos/home-i/izoi/www/VBS_SM_WV_semilep_aQGC/limits/${label}_${year}/
mkdir -p ${outdir}
cp       /eos/home-i/izoi/www/index.php ${outdir}

for op in "${!all_operators[@]}"; do
    target_operator=${all_operators[${op}]}
    range=${ranges[${op}]}
    echo operator ${target_operator} range ${range}
    source eft_multipleOperators.sh ${directory} ${target_operator} boost_Mww_binzv_Aug2024_noStat ${range} ${year} Mww_binzv Aug2024 ${label}
    mv LS_k_${target_operator}.png ${outdir}
    cp yearCI_*-pLHE_${label}.txt ${outdir}
done
