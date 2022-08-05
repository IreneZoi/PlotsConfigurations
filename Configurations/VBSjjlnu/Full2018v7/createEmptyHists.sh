#!bin/bash 
startdir=$(pwd)
basedir=rootFile_fit_v4.5_2018_split_minimalvar/
filetag=plots_fit_v4.5_2018_split_minimalvar_ALL
missingsamples=(
Wjets_res_21.1 )
filedir=${startdir}/${basedir}
echo $filedir

for sample in ${missingsamples[*]}; do
    echo $sample
    filename=${filedir}/${filetag}_${sample}.root
    echo ${filename}
    root -q createEmptyFile.C\(\"$filename\"\)
done

