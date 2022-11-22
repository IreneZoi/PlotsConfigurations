#!bin/bash 
startdir=$(pwd)
yeardir=Full2017v7/
basedir=/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2018_split_aQGC_cT2/
filetag=plots_fit_v4.5_2018_split_aQGC_cT2_ALL
missingsamples=(
sm_lin_quad_cT2.21

 )
filedir=${basedir}
#filedir=${startdir}/${yeardir}/${basedir}
echo $filedir

for sample in ${missingsamples[*]}; do
    echo $sample
    filename=${filedir}/${filetag}_${sample}.root
    echo ${filename}
    root -q createEmptyFile.C\(\"$filename\"\)
done

