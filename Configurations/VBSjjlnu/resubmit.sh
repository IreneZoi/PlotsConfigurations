#!bin/bash 
startdir=$(pwd)
basedir=/afs/cern.ch/work/i/izoi/VBSanalysis/logs/jobs/
jobsname=mkShapes__fit_v4.5_2018_split_qglnuis_aQGC_cT0_eboliv2__ALL/
missingsamples=(

DY.43 
DATA.35 
Wjets_res_4.3 
Wjets_res_1.3 
top.81 
top.93 
quad_cT0.12 
quad_cT0.82 
quad_cT0.107 
quad_cT0.190 
quad_cT0.280 
quad_cT0.313 
quad_cT0.325 
quad_cT0.330 
quad_cT0.393 
quad_cT0.396 
quad_cT0.586 
sm_lin_quad_cT0.65 
sm_lin_quad_cT0.68 
sm_lin_quad_cT0.258 
sm_lin_quad_cT0.315 
sm.88 

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
