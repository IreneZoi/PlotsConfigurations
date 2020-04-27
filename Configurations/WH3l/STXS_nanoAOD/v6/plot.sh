#!/bin/bash

set -e 

DIR=$PWD

for year in Full2016nano_STXS_1p1 Full2017nano_STXS_1p1 Full2018nano_STXS_1p1
do
    echo " --> $year"
    YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "nano" '{print $1}'`
    cd $DIR; cd $year
    
    for region in OSSF SSSF
    do
        echo "  --> $region"
	echo "mkPlot.py --pycfg configuration_${region}.py --inputFile rootFiles_WH3l_${YEAR}_v6_STXS_${region}/plots_WH3l_${YEAR}_v6_STXS_${region}.root --showIntegralLegend 1 --onlyPlot cratio"
	mkPlot.py --pycfg configuration_${region}.py --inputFile rootFiles_WH3l_${YEAR}_v6_STXS_${region}/plots_WH3l_${YEAR}_v6_STXS_${region}.root --showIntegralLegend 1 --onlyPlot cratio
    done
done