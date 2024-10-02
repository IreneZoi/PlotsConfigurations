#!bin/bash


years=(2016 2017 2018)
operators=(cT2 cT3 cT4 cT5 cT6 cT7 cT8 cT9 cS0 cS1 cM0 cM1 cM2 cM3 cM4 cM5 cM6 cM7)
fulloperator=" "
for operator in ${operators[*]}; do
    fulloperator+="quad_${operator}  sm_lin_quad_${operator} "
done

echo $fulloperator

for year in ${years[*]}; do
    echo $year
        command="python scripts/nuisances_tools/extract_nuisance_norm.py -i /eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_incl_nuis_norm_${year}_aQGC_cT2-cM7_eboliv2_official/plots_incl_nuis_norm_${year}_aQGC_cT2-cM7_eboliv2_official.root  -s $fulloperator -n CMS_PU_${year} PS_ISR PS_FSR -c inclusive -o Full${year}v7/conf_incl_nuis_norm_aQGC/nuisance_incl_norm_factors_${year}_aQGC_cT2-cM7_eboliv2_official.json"
        echo $command
        $command
done
