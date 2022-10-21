#!bin/bash startdir=$(pwd)
basedir=/afs/cern.ch/work/i/izoi/VBSanalysis/logs/jobs/
jobsname=mkShapes__fit_v4.5_2018_split_aQGC__ALL
missingsamples=(
VV_osWW.0 VV_osWW.1 VV_osWW.2 VV_osWW.3 VV_osWW.4 VV_osWW.5 VV_osWW.6 VV_osWW.7 VV_osWW.8 VV_osWW.9 VV_osWW.10 VV_osWW.11 VV_osWW.12 VV_osWW.13 VV_ssWW VV_ZZ VBS_ssWW.3 VBS_ssWW.6 VBS_ssWW.9 VV_WZll.0 VV_WZll.1 VV_WZll.2 VV_WZll.3 VBS_ZZ.1 VBS_ZZ.2 VBS_ZZ.3 VBS_WZjj.1 VBS_WZjj.9 VBS_WZjj.13 Wjets_res_21.1 VV_WZjj.0 VV_WZjj.1 VV_WZjj.2 VV_WZjj.3 VV_WZjj.4 VV_WZjj.5 VV_WZjj.6 
)
startdir=$pwd
jobsdir=$basedir$jobsname
echo $jobsdir
cd $jobsdir
for sample in ${missingsamples[*]}; do
    echo $sample
    cd $sample
    #for i in *jid; do sed -i s/longlunch/workday/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done
    for i in *jid; do sed -i s/workday/testmatch/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done
    cd $jobsdir
done

cd $startdir