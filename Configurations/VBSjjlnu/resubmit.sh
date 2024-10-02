#!/bin/bash 
startdir=$(pwd)
basedir=/afs/cern.ch/work/i/izoi/VBSanalysis/logs/jobs/
jobsname=mkShapes__fit_v4.5_2018_split_aQGC_eboliv2_official_allOperators_XSonly__ALL/
missingsamples=(
# 3
sm_lin_quad_cT0.15
sm_lin_quad_cT0.87
sm_cT8.20




) 



startdir=$(pwd)
echo "${startdir}"
jobsdir=$basedir$jobsname
echo "${jobsdir}"
cd ${jobsdir}
for sample in ${missingsamples[*]}; do
    echo "${sample}"
    cd ${sample}
    for i in *jid; do sed -i s/longlunch/workday/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done
    #for i in *jid; do sed -i s/workday/testmatch/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done
    #for i in *jid; do sed -i s/testmatch/nextweek/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done
    cd ${jobsdir}
done

cd ${startdir}/Full2018v7/
