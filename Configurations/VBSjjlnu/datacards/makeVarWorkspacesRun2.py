import os
import fileinput
import sys


years=["2016", "2017", "2018"]

categories=["boost_wjetcr_mu", "boost_wjetcr_ele",   "boost_sig_ele", "boost_sig_mu"]
variables=["fit_bins_boost", "events", "Mww", "Mww_binzv", "deltaeta_vbs" ]
# categories=(boost_sig_ele) # boost_wjetcr_mu boost_sig_mu)
# variables=("Mww_binzv" ) #fit_bins_boost )
operator="cT0"
label="cT0sm"
fitvar="Mww_binzv"
baseRun2Dir="../FullRun2v7/datacards_fit_v4.5_Run2_split_aQGC_{}_eboliv2_official_{}/".format(operator,label)
os.system("mkdir {}".format(baseRun2Dir))
arraylength=len(categories)
yearslength=len(years)
for i in range(0, arraylength):

    print( "index: {}, cat: {}".format(i,categories[i])) #, var:  ${variables[$i]}"
    run2Dir=baseRun2Dir+categories[i]+"/"
    os.system("mkdir {}".format(run2Dir))
    for variable in variables:
        run2DirVar=run2Dir+variable+"/"
        os.system("mkdir {}".format(run2DirVar))
        print(run2DirVar)
        command='combineCards.py '
        for j in range(0, yearslength):
        
            
            command+=' {}_{}='.format(categories[i],years[j])
            print(" plotting {}".format(years[j]))
            datacardDir2="Full{}v7/datacards_fit_v4.5_{}_split_aQGC_{}_eboliv2_official_{}".format(years[j],years[j],operator,label) #_NOpdfPSqcdMinorBkg # eboliv2
            DatacardPATHpartial="/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBSjjlnu/{}/{}/{}/".format(datacardDir2,categories[i],variable)
            command+='{}/datacard.txt'.format(DatacardPATHpartial)
            if (years[j]== "2018"):
            
                command+=' > {}/datacard.txt'.format(run2DirVar)
            
            
        
        print(command)
        os.system(command)
        newcommand='text2workspace.py {}/datacard.txt -o {}/datacard.root'.format(run2DirVar,run2DirVar)
        print(newcommand)
        os.system(newcommand)

# os.system("cp -r fullrun2_fit_v4.5.5_aQGC_{}_eboliv2_official_{}_{} fullrun2_fit_v4.5.5_aQGC_{}_eboliv2_official_{}_{}_testpath".format(operator,label,fitvar,operator,label,fitvar))

