import ROOT as R 
R.gStyle.SetPalette(R.kLightTemperature)
import sys
from math import sqrt
import pandas as pd 
import canvas_utils
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--postfit", type=str)
parser.add_argument("--prefit", type=str)
parser.add_argument("--postfit-err", type=str)
parser.add_argument("-c","--cat", help="Wjets Category", type=str)
args = parser.parse_args()

df = pd.read_csv(args.postfit, sep=";")
df_pre = pd.read_csv(args.prefit, sep=";")
df_postfiterr = pd.read_csv(args.postfit_err, sep=";")
cat = args.cat
print(df)
print(df_pre)

import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
tdrStyle.setTDRStyle()


Wjets_bins = {"res":[],"boost":[]}
for ir in range(1,7):
    Wjets_bins["res"].append("Wjets_HT_res_"+str(ir))
for ir in range(1,6):
    Wjets_bins["boost"].append("Wjets_HT_boost_"+str(ir))


c = canvas_utils.get_canvas('2016+2017+2018',900,1400)
mg = R.TMultiGraph()
mg.SetTitle("Wjets categories prefit/postfit norms;Wjets categories;post(pre)fit SF")

leg = R.TLegend(0.35,0.8,0.95,0.9)
leg.SetNColumns(4)

offset = 0


Max = 0
Min = 2


for iy, year in enumerate((2016,2017,2018)):
    for lepfl in ("ele","mu"):
        i = 0
        g = R.TGraphErrors()
        g_err = R.TGraphAsymmErrors()
        g_pre = R.TGraphAsymmErrors()
        leg.AddEntry(g, "{}_{} postfit".format(lepfl,year), "p")
        leg.AddEntry(g_pre, "{}_{} prefit".format(lepfl,year),"f" )
        
        channel = "{}_wjet_{}_{}".format(cat, lepfl, year)
        if lepfl=="ele": offset = (iy)*0.15 - 0.40
        else: offset = (iy)*0.15 + 0.1
        
        for wjetbin in Wjets_bins[cat]:
            data = df[(df.channel==channel) & (df.bin==wjetbin)]
            data_err = df_postfiterr[(df.channel==channel) & (df.bin==wjetbin)]
            y = float((data.norm/data.prefitnorm).values[0])
            g.SetPoint(i, i+1+offset, y)
            g_err.SetPoint(i, i+1+offset,data.norm/data.prefitnorm )
            g_err.SetPointError(i, 0.035,0.035, data_err.err,data_err.err )

            if y > Max : Max = y
            if y < Min : Min = y

            data_pre = df_pre[(df_pre.channel==channel) & (df_pre.bin==wjetbin)]
            
            g_pre.SetPoint(i, i+1+offset, float(data_pre.weight) )
            g_pre.SetPointError(i, 0.06, 0.06, data_pre.syst_do, data_pre.syst_up )
        
            i+=1
        mg.Add(g_pre, "5")
        mg.Add(g, "P")
        mg.Add(g_err,"2")

        if lepfl =="ele":   g.SetMarkerStyle(21)
        else: g.SetMarkerStyle(22)

        g.SetMarkerSize(3)
        g.SetLineWidth(3)
        g_err.SetLineColor(12)
        g_err.SetFillColor(12)
        g_err.SetLineWidth(0)
        g_err.SetFillStyle(3001)

        # g_pre.SetLineWidth(3)
        # g_pre.SetMarkerStyle(6)
        # g_pre.SetLineWidth(3)
        g_pre.SetFillStyle(0)
        g_pre.SetLineWidth(2)

mg.Draw("AP PMC PFC PLC")
mg.GetYaxis().SetRangeUser(Min - 0.6,Max + 0.4)
if cat == "res":  mg.GetXaxis().SetRangeUser(0.4 , 6.5)
elif cat == "boost":  mg.GetXaxis().SetRangeUser(0.4 , 5.5)

mg.Draw("AP PMC PFC PLC")

i = 0
tt = []

for wjetbin in Wjets_bins[cat]:
    t = R.TText(i+1-0.45, Min-0.5 , wjetbin)

    t.SetTextFont(25)
    t.SetTextSize(25)
    t.SetTextAngle(0)
    i+=1
    t.Draw("same")
    tt.append(t)


ls = []
if cat == "res": nlines = 5
elif cat == "boost": nlines = 4
for i in range(nlines):
    line = R.TLine(i+1.495, Min-0.6, i+1.495,Max+0.4)
    line.SetLineStyle(8)
    line.Draw("same")
    ls.append(line)


leg.Draw("same")

# R.gPad.SetRightMargin(0.1)
# R.gPad.SetLeftMargin(R.gPad.GetLeftMargin()*1.2)

# R.gStyle.SetTitleColor(1, "XYZ");
# R.gStyle.SetTitleFont(42, "XYZ");
# R.gStyle.SetTitleSize(0.06, "XYZ");
# R.gStyle.SetTitleXOffset(0.9);
# R.gStyle.SetTitleYOffset(1.25);

canvas_utils.finalize(c, mg)
c.SaveAs("output_plot_{}.png".format(cat))