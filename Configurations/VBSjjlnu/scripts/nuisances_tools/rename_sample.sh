#!/bin/bash

# file=/eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_cT0_eboliv2_official/plots_fit_v4.5_2016_split_aQGC_cT0_eboliv2_official_withBKG_GiacomoTest2_addingNuis.root
# echo $file
# python rename_sample_root.py  -i $file -s sm_dipole --rename sm

# file=/eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2017_split_aQGC_cT0_eboliv2_official/plots_fit_v4.5_2017_split_aQGC_cT0_eboliv2_official_withBKG_GiacomoTest2_addingNuis.root
# echo $file
# python rename_sample_root.py  -i $file -s sm_dipole --rename sm

file=/eos/home-i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_cT0_eboliv2_official/plots_fit_v4.5_2018_split_aQGC_cT0_eboliv2_official_withPDFweight_withBKG_GiacomoTest2_addNuis.root
echo $file
python rename_sample_root.py  -i $file -s sm_dipole --rename sm


