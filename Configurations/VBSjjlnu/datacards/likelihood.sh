#!bin/bash

startdir=$(pwd)
#dirs=(res_ele res_mu boost_ele boost_mu boost res all)
dirs=(ele mu)


for channel in ${dirs[*]}; do
    echo $channel
    dir=2018_${channel}_fit_v4.5.5
    echo $dir
    datacard=2018_${channel}_split_Dipole_v4.5
    echo $datacard
    # submitting jobs
    #python ../scripts/prepare_datacard.py -c datacard_config_2018_v4.5.json -b ../ -o $dir -p workspace -d $datacard
    #python ../scripts/prepare_likelihood_scan.py -c datacard_config_2018_v4.5.json -o $dir -q espresso -v 3 -fo 2 --points 100 --rMin -1 --rMax 3 --split 4 --data-unblind  -p scan  -d $datacard
    # when jobs are done
    python ../scripts/prepare_likelihood_scan.py -c datacard_config_2018_v4.5.json -o $dir -q espresso -v 3 -fo 2 --points 100 --rMin -1 --rMax 3 --split 4 --data-unblind  -p hadd  -d $datacard
    cd $dir/$datacard
    python /afs/cern.ch/work/i/izoi/VBSanalysis/forCombine/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/data/tutorials/longexercise/plot1DScan.py likelihood_scan_data/higgsCombine.scan_all.POINTS.root -o scan_data --main-label "Observed"
    cd $startdir
done

cd $startdir