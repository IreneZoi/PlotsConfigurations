import ROOT
import sys
import copy

def process_graph(graph):
    x_std = []
    x_y_map = []
    x_value = ROOT.Double()
    y_value = ROOT.Double()

    ip = 0
    while ip < graph.GetN():
        graph.GetPoint(ip, x_value, y_value)

        if x_value in x_std:
            graph.RemovePoint(ip)
            ip -= 1
        else:
            x_std.append(copy.deepcopy(x_value))
            x_y_map.append([copy.deepcopy(x_value), copy.deepcopy(y_value)])

        ip += 1

    graph.Set(0)
    
    if len(x_y_map) > 0:
        min_x = -100.
        minimum = 1000.

        for it in x_y_map:
            if it[1] < minimum:
                minimum = it[1]
                min_x = it[0]

        for it in x_y_map:
            it[1] =  it[1] - minimum
  
        ip = 0
        for it in x_y_map:
            graph.SetPoint(ip, it[0], it[1])
            ip += 1

    return graph, min_x

cc = ROOT.TCanvas("cc","", 800, 600);
ROOT.gROOT.SetBatch()

lumi = {
    '2016': 35.9,
    "2017": 41.53,
    "2018": 59.7,
    "2017,2018": 101.23,
    "Run2": 138,
}

_file1 = ROOT.TFile.Open(str(sys.argv[1]), "READ")          # file with expected limits
operator = str(sys.argv[2])                                 # cT0
year = str(sys.argv[3])                                     # Run2
region = str(sys.argv[4])                                   # combined_boosted
_file2 = ROOT.TFile.Open(str(sys.argv[5]), "READ")          # file with observed limits
label = str(sys.argv[6]) 


limit = _file1.Get("limit")
print " expected = ", _file1.GetName()

toDraw = ROOT.TString(ROOT.Form("2*deltaNLL:"+operator))

graphScan = ROOT.TGraph(limit.Draw(toDraw.Data(), "deltaNLL<50 && deltaNLL>-30", "l"), limit.GetV2(), limit.GetV1())
graphScan.RemovePoint(0)

limitData = _file2.Get("limit")  
print " observed = ", _file2.GetName(), "\n"
graphScanData = ROOT.TGraph(limitData.Draw(toDraw.Data(), "deltaNLL<50 && deltaNLL>-30", "l"), limitData.GetV2(), limitData.GetV1())
graphScanData.RemovePoint(0)
graphScanData.SetTitle("")
graphScanData.SetMarkerStyle(21)
graphScanData.SetLineWidth(2)
graphScanData.SetMarkerColor(ROOT.kRed)
graphScanData.SetLineColor(ROOT.kRed)

cc.SetGrid()

graphScan, mc_min_x = process_graph(graphScan)
graphScanData, data_min_x = process_graph(graphScanData)

graphScan.SetTitle("")
graphScan.SetMarkerStyle(21)
graphScan.SetLineWidth(2)
graphScan.SetMarkerColor(ROOT.kBlue)
graphScan.SetLineColor(ROOT.kBlue)

cc.SetTicks()
cc.SetFillColor(0)
cc.SetBorderMode(0)
cc.SetBorderSize(2)
cc.SetTickx(1)
cc.SetTicky(1)
cc.SetRightMargin(0.05)
cc.SetBottomMargin(0.12)
cc.SetFrameBorderMode(0)

tex = ROOT.TLatex(0.94,0.92,"13 TeV")
tex.SetNDC()
tex.SetTextAlign(31)
tex.SetTextFont(42)
tex.SetTextSize(0.04)
tex.SetLineWidth(2)

tex2 = ROOT.TLatex(0.14,0.92,"CMS")
tex2.SetNDC()
tex2.SetTextFont(61)
tex2.SetTextSize(0.04)
tex2.SetLineWidth(2)

tex3 = ROOT.TLatex(0.236,0.92,"L = " + str(lumi[year]) + " fb^{-1}  Preliminary")
tex3.SetNDC()
tex3.SetTextFont(52)
tex3.SetTextSize(0.035)
tex3.SetLineWidth(2)

minX = min(graphScan.GetXaxis().GetXmin(), graphScanData.GetXaxis().GetXmin())
maxX = max(graphScan.GetXaxis().GetXmax(), graphScanData.GetXaxis().GetXmax())

graphScan.GetXaxis().SetTitle(operator)
graphScan.GetYaxis().SetTitle("-2 #Delta lnL")
  
graphScan.Draw("al")
graphScan.GetYaxis().SetRangeUser(-0.1, 10.)

if graphScanData: 
    graphScanData.Draw("l")
  
tex.Draw("same")
tex2.Draw("same")
tex3.Draw("same")
  
line1 = ROOT.TLine(minX,1.0,maxX,1.0)
line1.SetLineWidth(2)
line1.SetLineStyle(2)
line1.SetLineColor(ROOT.kRed)
line1.Draw() 
  
line2 = ROOT.TLine(minX,3.84,maxX,3.84)
line2.SetLineWidth(2)
line2.SetLineStyle(2)
line2.SetLineColor(ROOT.kRed)
line2.Draw()
  
leg = ROOT.TLegend(0.43,0.75,0.63,0.9)
leg.AddEntry(graphScan,"Expected","l")
if graphScanData:
    leg.AddEntry(graphScanData,"Observed","l")

leg.SetFillColor(0)
leg.Draw()
  
print " (expected) MC   at minimum:   ",   mc_min_x, "\n"
print " (observed) data at minimum:   ", data_min_x, "\n"
  
cc.SaveAs("LS_" + str(operator) + ".png")

outfile_exp = ROOT.TFile.Open(operator+ "_" +str(region)+ "_expected.root" ,"RECREATE")
outfile_exp.cd()
graphScan.Write()
outfile_exp.Close()

outfile_obs = ROOT.TFile.Open(operator+ "_" +str(region)+ "_observed.root" ,"RECREATE")
outfile_obs.cd()
graphScanData.Write()
outfile_obs.Close()

def myfunc(x):
    return graphScan.Eval(x[0])

func_exp = ROOT.TF1("func", myfunc, -1000, 1000, 0)
s2down_exp=func_exp.GetX(3.84,-1000,0)
s2up_exp=func_exp.GetX(3.84,0,1000)
print " -2sigma (expected) :", s2down_exp, "\n"
print " +2sigma (expected) :", s2up_exp, "\n"
CIs_exp=operator+"    "+year+"    "+region+"    "+str(s2down_exp)+"    "+str(s2up_exp)
print CIs_exp

with open('yearCI_exp-pLHE_'+label+'.txt', 'a') as f:
    f.write(CIs_exp)
    f.writelines('\n')
    f.close()

def myfunc(x):
    return graphScanData.Eval(x[0])

func_obs = ROOT.TF1("func", myfunc, -1000, 1000, 0)
s2down_obs=func_obs.GetX(3.84,-1000,0)
s2up_obs=func_obs.GetX(3.84,0,1000)
print " -2sigma (observed) :", s2down_obs, "\n"
print " +2sigma (observed) :", s2up_obs, "\n"
CIs_obs=operator+"    "+year+"    "+region+"    "+str(s2down_obs)+"    "+str(s2up_obs)
print CIs_obs

with open('yearCI_obs-pLHE_'+label+'.txt', 'a') as f:
    f.write(CIs_obs)
    f.writelines('\n')
    f.close()
