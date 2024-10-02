import os

path  = '/eos/user/i/izoi/VBS_SM_WV_semilep_aQGC/rootFile_fit_v4.5_2016_split_aQGC_eboliv2_official_allOperators/'
# files = [f for f in os.listdir(path)] # if os.path.isfile(f)]
# # print(files)
# for f in files:
#     print(f)
#     # r = f.replace("echoplots","plots")
#     r = f.replace("echoplots","plots")
#     os.rename(f,f.replace("echoplots","plots"))
#     print(f)
#     # if( r != f):
#     #     os.rename(f,r)
    
for fileName in os.listdir(path):
    # newname = fileName.replace("2_17", "2017").replace('sssis','split').replace('_____','_').replace('pbssiv2_sffi_ias_assOsprassrs','eboliv2_official_allOperators').replace(".rsss|sr'sffi\_ias'sffilias'",".root")
    newname = fileName.replace("_cT0_eboliv2","_eboliv2")
    
    os.rename(path+'/'+fileName, path+'/'+newname)
    
    
