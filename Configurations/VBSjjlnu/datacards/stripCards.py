import os

channelsnames=["res_sig_mu", "res_sig_ele", "boost_sig_mu", "boost_sig_ele", "res_wjet_mu", "res_wjet_ele", "boost_wjet_mu", "boost_wjet_ele", "res_top_mu", "res_top_ele", "boost_top_mu","boost_top_ele"]
years=["2016", "2017", "2018"]
res_processes=39
boost_processes=25
channels=12


def getProcessesRate(infile,outfilelabel):
    start=1
    end=res_processes #first channel is a res channel

    for year in years:
        print year
        for channel in channelsnames:
            processes = res_processes
            if "boost" in channel: processes = boost_processes
            end=start+processes
            print channel, start, end
            f=open(infile,"r")  
            lines=f.readlines()
            fout=open(year+"_"+channel+"_"+outfilelabel+".txt","w")
            foutcsv=open(year+"_"+channel+"_"+outfilelabel+".csv","w")
            for x in lines:
                columns = len(x.split(" "))
                
                string=x.split(" ")[0]
                for i in range(start,end):
                    #print x.split(" ")[i]
                    string=string+" "+x.split()[i]
                fout.write(string+"\n")
                foutcsv.write(string.replace(" ",",")+"\n")
            processes = res_processes
            if "boost" in channel: processes = boost_processes
            start=start+processes
            f.close()
            fout.close()
            foutcsv.close()


def getNuis(infile,outfilelabel):
    start=1
    end=res_processes #first channel is a res channel

    for year in years:
        print year
        for channel in channelsnames:
            processes = res_processes
            if "boost" in channel: processes = boost_processes
            end=start+processes
            print channel, start, end
            f=open(infile,"r")  
            lines=f.readlines()
            fout=open(year+"_"+channel+"_"+outfilelabel+"_nuis.txt","w")
            foutcsv=open(year+"_"+channel+"_"+outfilelabel+"_nuis.csv","w")
            countline=1
            for x in lines:
                # print " count ",countline
                if countline <=2:
                    #prepare header
                    string=x.split(" ")[0]+" "+"empty"
                    for i in range(start,end):
                        string=string+" "+x.split()[i]
                else:
                    string=x.split(" ")[0]+" "+x.split(" ")[1]
                    for i in range(start+1,end+1):
                        string=string+" "+x.split()[i]
                fout.write(string+"\n")
                foutcsv.write(string.replace(" ",",")+"\n")
                countline=countline+1    
            processes = res_processes
            if "boost" in channel: processes = boost_processes
            start=start+processes
            f.close()
            fout.close()
            foutcsv.close()
########################################################################


# infile="fullrun2_fit_v4.5.5/run2_all/combined_run2_all_short_process.txt"
outfilelabel1="Irene"
# print "  ----------------------- ",outfilelabel1
# getProcessesRate(infile,outfilelabel1)


# infile="combined_run2_all_fromDavide_process.txt"
outfilelabel2="Davide"
# print "  ----------------------- ",outfilelabel2
# getProcessesRate(infile,outfilelabel2)

# print "  --------------------------- DIFFERENCES "
# for year in years:
#     print year
#     for channel in channelsnames:
#         print channel
#         filename=year+"_"+channel+"_processDiff.txt"
#         os.system("diff "+year+"_"+channel+"_"+outfilelabel1+".txt "+year+"_"+channel+"_"+outfilelabel2+".txt > "+filename)
#         if os.stat(filename).st_size == 0:
#             print " Irene & Davide processes are identical for ",year+"_"+channel
#         else:
#             print "created txt file ",filename
#             foutcsvDiff=open(year+"_"+channel+"_processDiff.csv","w")
#             f1=open(year+"_"+channel+"_"+outfilelabel1+".csv","r")  
#             lines=f1.readlines()
#             for x in lines:
#                 if "rate" in x: x=x.replace("rate","rate"+outfilelabel1)
#                 foutcsvDiff.write(x)
#             f2=open(year+"_"+channel+"_"+outfilelabel2+".csv","r")  
#             last_line = f2.readlines()[-1].replace("rate","rate"+outfilelabel2)
#             foutcsvDiff.write(last_line)
#             foutcsvDiff.close()
            

print "-------------------------------------- NUISANCES!! ----------------------------"
infile="fullrun2_fit_v4.5.5/run2_all/combined_run2_all_short_nuis.txt"
print "  ----------------------- ",outfilelabel1
getNuis(infile,outfilelabel1)

# infile="combined_run2_all_fromDavide_nuis.txt"
# print "  ----------------------- ",outfilelabel2
# getNuis(infile,outfilelabel2)

print "  --------------------------- DIFFERENCES "
for year in years:
    print year
    for channel in channelsnames:
        print channel
        filename=year+"_"+channel+"_nuisDiff.txt"
        os.system("diff "+year+"_"+channel+"_"+outfilelabel1+"_nuis.txt "+year+"_"+channel+"_"+outfilelabel2+"_nuis.txt > "+filename)
        if os.stat(filename).st_size == 0:
            print " Irene & Davide nuisances are identical for ",year+"_"+channel
        else:
            print "created txt file ",filename
            foutcsvDiff=open(year+"_"+channel+"_nuisDiff.csv","w")
            f1=open(year+"_"+channel+"_"+outfilelabel1+"_nuis.csv","r")
            f2=open(year+"_"+channel+"_"+outfilelabel2+"_nuis.csv","r")
            lines=f1.readlines()
            lines2=f2.readlines()
            countline=0
            for x in lines:
                print "count ",countline
                print x
                if countline <=1:
                    #prepare header
                    foutcsvDiff.write(x)
                else:
                    if x != lines2[countline]:
                        foutcsvDiff.write("irene_"+x)
                        print lines2[countline]
                        foutcsvDiff.write(lines2[countline])
                countline=countline+1    
 
            foutcsvDiff.close()
