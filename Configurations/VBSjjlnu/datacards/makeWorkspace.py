import os
import fileinput
import sys

def checkregion(region, datacard):
    with open(datacard) as f:
        if region not in f.read():
            sys.exit(" region {} not in datacard {}".format(region,datacard))



# years    = ["2016"] #,"2017","2018","run2"]
LABEL="testSM"
DATACARD2016="datacards_fit_v4.5_2016_split_aQGC_cT0_eboliv2_official_testSM"
DATACARD2017="datacards_fit_v4.5_2017_split_aQGC_cT0_eboliv2_official_testSM"
DATACARD2018="datacards_fit_v4.5_2018_split_aQGC_cT0_eboliv2_official_testSM"

RES_VAR="Mww_binzv" # DNNoutput_res_v1
BOOST_VAR="Mww_binzv" # DNNoutput_boost

datacardbase="datacard_config_fullrun2_v4.5.5_TEMPLATE.json"
datacardout=datacardbase.replace("TEMPLATE",LABEL)
print(datacardout)
filein = open('{}'.format(datacardbase))
fileout = open(datacardout,"wt")
for line in filein:
    fileout.write(line.replace('{DATACARD2016}', DATACARD2016).replace('{DATACARD2017}', DATACARD2017).replace('{DATACARD2018}',DATACARD2018).replace('{RES_VAR}',RES_VAR).replace('{BOOST_VAR}',BOOST_VAR))
filein.close()
fileout.close()



operator="cT0_eboliv2_official"

region="run2_boost"
checkregion(region, datacardout)
datacard_comand = "python ../scripts/prepare_datacard.py -c {} -b ../ -o fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/ -p workspace -d {} --redo-workspace".format(datacardout,operator,LABEL,BOOST_VAR,region)
print (" creating datacard with command:")
print(datacard_comand)
os.system(datacard_comand)
print("datacard directory fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/".format(operator,LABEL,BOOST_VAR))

region="2018_boost"
checkregion(region, datacardout)
datacard_comand = "python ../scripts/prepare_datacard.py -c {} -b ../ -o fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/ -p workspace -d {} --redo-workspace".format(datacardout,operator,LABEL,BOOST_VAR,region)
print (" creating datacard with command:")
print(datacard_comand)
os.system(datacard_comand)
print("datacard directory fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/".format(operator,LABEL,BOOST_VAR))

region="2017_boost"
checkregion(region, datacardout)
datacard_comand = "python ../scripts/prepare_datacard.py -c {} -b ../ -o fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/ -p workspace -d {} --redo-workspace".format(datacardout,operator,LABEL,BOOST_VAR,region)
print (" creating datacard with command:")
print(datacard_comand)
os.system(datacard_comand)
print("datacard directory fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/".format(operator,LABEL,BOOST_VAR))

region="2016_boost"
checkregion(region, datacardout)
datacard_comand = "python ../scripts/prepare_datacard.py -c {} -b ../ -o fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/ -p workspace -d {} --redo-workspace".format(datacardout,operator,LABEL,BOOST_VAR,region)
print (" creating datacard with command:")
print(datacard_comand)
os.system(datacard_comand)
print("datacard directory fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/".format(operator,LABEL,BOOST_VAR))

# region="2018_boost_sigonly"
# checkregion(region, datacardout)
# datacard_comand = "python ../scripts/prepare_datacard.py -c {} -b ../ -o fullrun2_fit_v4.5.5_aQGC_{}_{}_{}/ -p workspace -d {} --redo-workspace".format(datacardout,operator,LABEL,BOOST_VAR,region)
# print (" creating datacard with command:")
# print(datacard_comand)
# os.system(datacard_comand)
