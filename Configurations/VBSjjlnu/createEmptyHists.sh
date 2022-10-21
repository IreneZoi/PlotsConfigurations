#!bin/bash 
startdir=$(pwd)
yeardir=Full2017v7/
basedir=rootFile_fit_v4.5_2017_split_minimalvar/
filetag=plots_fit_v4.5_2017_split_minimalvar_ALL
missingsamples=(
Wjets_boost.51 )
filedir=${startdir}/${yeardir}/${basedir}
echo $filedir

for sample in ${missingsamples[*]}; do
    echo $sample
    filename=${filedir}/${filetag}_${sample}.root
    echo ${filename}
    root -q createEmptyFile.C\(\"$filename\"\)
done

