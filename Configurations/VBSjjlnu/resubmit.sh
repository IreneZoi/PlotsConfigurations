#!bin/bash 
startdir=$(pwd)
basedir=/afs/cern.ch/work/i/izoi/VBSanalysis/logs/jobs/
jobsname=mkShapes__fit_v4.5_2016_split_qglnuis_aQGC_cT0__ALL/
missingsamples=(
sm.18 sm.28
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

cd ${startdir}