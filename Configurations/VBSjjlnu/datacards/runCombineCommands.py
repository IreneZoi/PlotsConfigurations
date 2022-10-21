import os

years=["2017"] #["2016","2017","2018"]
categories={"res":"DNNoutput_res_v1","boost":"DNNoutput_boost"}
channels=["ele","mu"]
runcmd = True
for year in years:
    print year
    datacard=year+"_DNNoutput"
    print " datacard ",datacard
    directory=year+"_fit_v4.5.5"
    print " directory ",directory
    cmd="python ../scripts/prepare_datacard.py -c datacard_config_fullrun2_v4.5.5_split.json -b ../ -o "+directory+" -p workspace -d "+datacard+" --redo-workspace"
    print cmd
    if runcmd: os.system(cmd)
    filename=directory+"/"+datacard+"/combined_"+datacard
    filename1=directory+"/"+datacard+"/combined_"+datacard+"_tmp"
    os.system("cp "+filename+".txt "+filename1+".txt")
    print " filename ",filename+".txt"
    print " filename1 ",filename1+".txt"
    f1=open(filename1+".txt","r")  
    f=open(filename+".txt","w")
    lines=f1.readlines()
    for x in lines:
        x = x.replace("res_sig_ele_2017 autoMCStats 10 1 1","res_sig_ele_2017 autoMCStats 200 1 1")
    f.writelines( lines )
    cmd="text2workspace.py "+filename+".txt -o "+filename+".root --X-pack-asympows"
    print cmd
    if runcmd: os.system(cmd)
    cmd="python ../scripts/prepare_datacard.py -c datacard_config_fullrun2_v4.5.5_split.json -b ../ -o "+directory+" -p significance -d "+datacard+" -fo sig3 --unblind"
    print cmd
    if runcmd: os.system(cmd)
    print " done ",year
    for cat in categories.keys():
        print cat
        datacard=year+"_"+cat+"_"+categories[cat]
        print " datacard ",datacard
        directory=year+"_fit_v4.5.5_"+cat
        print " directory ",directory
        cmd="python ../scripts/prepare_datacard.py -c datacard_config_fullrun2_v4.5.5_split.json -b ../ -o "+directory+" -p workspace -d "+datacard+" --redo-workspace"
        print cmd
        if runcmd: os.system(cmd)
        filename=directory+"/"+datacard+"/combined_"+datacard
        filename1=directory+"/"+datacard+"/combined_"+datacard+"_tmp"
        os.system("cp "+filename+".txt "+filename1+".txt")
        print " filename ",filename
        f1=open(filename1+".txt","r")  
        f=open(filename+".txt","w")
        lines=f1.readlines()
        for x in lines:
            x = x.replace("res_sig_ele_2017 autoMCStats 10 1 1","res_sig_ele_2017 autoMCStats 200 1 1")
        f.writelines( lines )

       
        print " filename ",filename
        cmd="text2workspace.py "+filename+".txt -o "+filename+".root --X-pack-asympows"
        print cmd
        if runcmd: os.system(cmd)
        cmd="python ../scripts/prepare_datacard.py -c datacard_config_fullrun2_v4.5.5_split.json -b ../ -o "+directory+" -p significance -d "+datacard+" -fo sig3 --unblind"
        print cmd
        if runcmd: os.system(cmd)
        print " done ",year," ",cat
        for channel in channels:
            print channel
            datacard=year+"_"+cat+"_"+channel+"_"+categories[cat]
            print " datacard ",datacard
            directory=year+"_fit_v4.5.5_"+cat+"_"+channel
            print " directory ",directory
            cmd="python ../scripts/prepare_datacard.py -c datacard_config_fullrun2_v4.5.5_split.json -b ../ -o "+directory+" -p workspace -d "+datacard+" --redo-workspace"
            print cmd
            if runcmd: os.system(cmd)
            filename=directory+"/"+datacard+"/combined_"+datacard
            filename1=directory+"/"+datacard+"/combined_"+datacard+"_tmp"
            os.system("cp "+filename+".txt "+filename1+".txt")
            print " filename ",filename
            f1=open(filename1+".txt","r")  
            f=open(filename+".txt","w")
            lines=f1.readlines()
            for x in lines:
                x = x.replace("res_sig_ele_2017 autoMCStats 10 1 1","res_sig_ele_2017 autoMCStats 200 1 1")
            f.writelines( lines )
            cmd="text2workspace.py "+filename+".txt -o "+filename+".root --X-pack-asympows"
            print cmd
            if runcmd: os.system(cmd)
            cmd="python ../scripts/prepare_datacard.py -c datacard_config_fullrun2_v4.5.5_split.json -b ../ -o "+directory+" -p significance -d "+datacard+" -fo sig3 --unblind"
            print cmd
            if runcmd: os.system(cmd)
            print " done ",year," ",cat," ",channel