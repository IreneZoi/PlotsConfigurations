#!/bin/bash 
startdir=$(pwd)
basedir=/afs/cern.ch/work/i/izoi/VBSanalysis/logs/jobs/
jobsname=mkShapes__fit_v4.5_2017_split_aQGC_cT0_eboliv2_official_SMP18006__ALL/
missingsamples=(
# 77

sm_lin_quad_cT0.1
sm_lin_quad_cT0.11
sm_lin_quad_cT0.20
sm_lin_quad_cT0.38
sm_lin_quad_cT0.39
VV_ssWW.0
sm.6
sm.19
sm.23
sm.29
sm.30
sm.36
sm.46
sm.63
sm.78
sm.83
sm.84
DATA_ele.2
DATA_ele.4
DATA_ele.5
DATA_ele.6
DATA_ele.7
top.3
top.4
top.8
top.14
top.25
top.35
top.52
top.65
quad_cT0.21
quad_cT0.25
quad_cT0.31
quad_cT0.37
quad_cT0.47
quad_cT0.64
quad_cT0.77
quad_cT0.78
quad_cT0.84
VV_osWW.12
VV_osWW.13
VV_osWW.18
VV_osWW.20
VV_osWW.24
VV_osWW.30
VV_osWW.36
VV_osWW.46
VV_WZjj.0
VV_WZjj.13
VV_WZjj.16
VV_WZjj.18
VV_WZjj.22
Wjets_boost.1
Wjets_boost.10
Wjets_boost.18
Wjets_boost.40
Wjets_boost.43
Wjets_boost.47
Wjets_boost.50
Wjets_boost.60
Fake_ele.2
DY.9
DY.11
DY.14
DY.21
DY.38
VBF-V_dipole.0
VBF-V_dipole.3
VBF-V_dipole.13
VV_WZll.9
VV_WZll.11
DATA_mu.2
VgS.1
VgS.2
VgS.7
VgS.15
VgS.16




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
    # for i in *jid; do sed -i s/workday/testmatch/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done
    # for i in *jid; do sed -i s/longlunch/testmatch/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done

    #for i in *jid; do sed -i s/testmatch/nextweek/g ${i/jid/jds}; condor_submit ${i/jid/jds}; done
    cd ${jobsdir}
done

cd ${startdir}/Full2017v7/
