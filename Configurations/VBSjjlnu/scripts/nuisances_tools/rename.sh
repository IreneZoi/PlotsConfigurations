#!/bin/bash
years=(2017)
#samples=(quad_cT0 sm_lin_quad_cT0 sm)
samples=(sm_lin_quad_cT0)



for year in ${years[*]}; do
    echo " plotting ${year}"
    for sample in ${samples[*]}; do
        echo " plotting ${sample}"        

        python rename_shape_root.py  -i /eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_${year}_split_aQGC_cT0_eboliv2/plots_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_withBKG.root --shape-name QCDscale_signal -s      ${sample} --rename QCDscale_EWK_WV
        # python rename_shape_root.py  -i /eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_${year}_split_aQGC_cT0_eboliv2/plots_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_withBKG.root --shape-name QCDscale_signalV0Var -s ${sample} --rename QCDscale_EWK_WVV0Var
        # python rename_shape_root.py  -i /eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_${year}_split_aQGC_cT0_eboliv2/plots_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_withBKG.root --shape-name QCDscale_signalV1Var -s ${sample} --rename QCDscale_EWK_WVV1Var
        # python rename_shape_root.py  -i /eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_${year}_split_aQGC_cT0_eboliv2/plots_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_withBKG.root --shape-name QCDscale_signalV2Var -s ${sample} --rename QCDscale_EWK_WVV2Var
        # python rename_shape_root.py  -i /eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_${year}_split_aQGC_cT0_eboliv2/plots_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_withBKG.root --shape-name QCDscale_signalV3Var -s ${sample} --rename QCDscale_EWK_WVV3Var
        # python rename_shape_root.py  -i /eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_${year}_split_aQGC_cT0_eboliv2/plots_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_withBKG.root --shape-name QCDscale_signalV4Var -s ${sample} --rename QCDscale_EWK_WVV4Var
        # python rename_shape_root.py  -i /eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_${year}_split_aQGC_cT0_eboliv2/plots_fit_v4.5_${year}_split_aQGC_cT0_eboliv2_withBKG.root --shape-name QCDscale_signalV5Var -s ${sample} --rename QCDscale_EWK_WVV5Var

    done

done

