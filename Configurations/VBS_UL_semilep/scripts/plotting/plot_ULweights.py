import ROOT, json
import sys,os
ROOT.gROOT.SetBatch(True)

def getCanvas():
 H_ref = 600
 W_ref = 600
 W = W_ref
 H  = H_ref

 iPeriod = 0

 # references for T, B, L, R                                                                                                                                                                                                                  
 T = 0.08*H_ref
 B = 0.12*H_ref
 L = 0.15*W_ref
 R = 0.04*W_ref
 cname = "c"
 canvas = ROOT.TCanvas(cname,cname,50,50,W,H)
 canvas.SetFillColor(0)
 canvas.SetBorderMode(0)
 canvas.SetFrameFillStyle(0)
 canvas.SetFrameBorderMode(0)
 canvas.SetLeftMargin( L/W )
 canvas.SetRightMargin( R/W )
 canvas.SetTopMargin( T/H )
 canvas.SetBottomMargin( B/H )
 canvas.SetTickx()
 canvas.SetTicky()

 return canvas

def get_canvas_forRatio():

 H_ref = 600 
 W_ref = 600 
 W = W_ref
 H  = H_ref

 # references for T, B, L, R
 T = 0.07*H_ref
 B = 0.12*H_ref 
 L = 0.15*W_ref
 R = 0.05*W_ref

 cname="c"
 canvas = ROOT.TCanvas(cname,cname,W,H)
 canvas.SetFillColor(0)
 canvas.SetBorderMode(0)
 canvas.SetFrameFillStyle(0)
 canvas.SetFrameBorderMode(0)
 canvas.SetFrameBorderSize(0)
 canvas.SetFrameLineWidth(0)
 canvas.SetLeftMargin( L/W )
 canvas.SetRightMargin( R/W )
 canvas.SetTopMargin( T/H )
 canvas.SetBottomMargin( B/H )
 canvas.SetTickx(0)
 canvas.SetTicky(0)
 
 return canvas

def getLegend(x1=0.5809045,y1=0.6363636,x2=0.9522613,y2=0.8020979):
  legend = ROOT.TLegend(x1,y1,x2,y2)
  legend.SetTextSize(0.04)
  legend.SetLineColor(0)
  legend.SetShadowColor(0)
  legend.SetLineStyle(1)
  legend.SetLineWidth(1)
  legend.SetFillColor(0)
  legend.SetFillStyle(0)
  legend.SetMargin(0.35)
  legend.SetTextFont(42)
  return legend

operatorsfile = '../../weights_files/operators_short.json'
#operatorsfile = '../../weights_files/operators_test.json'
basedir='/afs/cern.ch/work/i/izoi/VBSanalysis/CMSSW_11_1_4/src/PlotsConfigurations/Configurations/VBS_UL_semilep/'
year='Full2018v9'
inputdir='rootFile_2018_ulsamples_vbsgenvars_fixdeta'
inputfilename = 'plots_2018_ulsamples_vbsgenvars_fixdeta'
filetype = 'aQGC_WMLEPWMHADjj_EWK'
print( "filetype ",filetype)



jsonoperatorsfile = open(operatorsfile)
# returns JSON object as a dictionary
shortoperatorsdata = json.load(jsonoperatorsfile)
jsonoperatorsfile.close()

cutdir='nominal'
variables = {}
variables["events"] = {'xaxistitle':'events'}
variables["mjj_vbs_Gen"] = {'xaxistitle':'m_{jj}^{VBS}'}
variables["deltaeta_vbs_Gen"] = {'xaxistitle':'#Delta#eta_{jj}^{VBS}'}
variables["eta0_vbs_Gen"] = {'xaxistitle':'#eta_{1}^{VBS}'}
variables["eta1_vbs_Gen"] = {'xaxistitle':'#eta_{2}^{VBS}'}
variables["pt0_vbs_Gen"] = {'xaxistitle':'pt_{1}^{VBS} [GeV]'}
variables["pt1_vbs_Gen"] = {'xaxistitle':'pt_{2}^{VBS} [GeV]'}

colors = ["#4292c6","#41ab5d","#ef3b2c","#17202A","#fdae61","#abd9e9","#2c7bb6"]
linestyle = [1,2,3,4,5,6,7,8,9]
markerstyle = [4,25,31,21,8]
ROOT.gStyle.SetOptStat(0)

completefilename=basedir+"/"+year+"/"+inputdir+"/"+inputfilename+".root"
print("completefilename ",completefilename)
inputfile = ROOT.TFile(completefilename,'READ')

for var in variables:
  for operator in shortoperatorsdata:
    print(" operator ",operator)
    canvas = get_canvas_forRatio()
    canvas.SetTitle(operator)
    legend = getLegend()
    # Upper histogram plot is pad1
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.31, 1, 1.0)
    pad1.SetBottomMargin(0)  # joins upper and lower plot
    pad1.SetRightMargin(0.05)
    pad1.SetLeftMargin(0.15)
    pad1.SetTopMargin(0.1)
    pad1.Draw()

    # Lower ratio plot is pad2
    canvas.cd()  # returns to main canvas before defining pad2
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.00, 1, 0.3)
    pad2.SetTopMargin(0)  # joins upper and lower plot
    pad2.SetBottomMargin(0.25)
    pad2.SetRightMargin(0.05)
    pad2.SetLeftMargin(0.15)
    pad2.Draw()

    pad1.cd()
    hist_r = []
    for i,opweight in enumerate(shortoperatorsdata[operator]):
      print(" opweight ",opweight)
      for k in inputfile.GetListOfKeys():
        cut = k.ReadObj()
        if isinstance(cut, ROOT.TDirectoryFile):
            for kk in cut.GetListOfKeys():
                histvar = kk.ReadObj()
                if isinstance(histvar, ROOT.TDirectoryFile) and histvar.GetName() == var:
                    for kkk in histvar.GetListOfKeys():
                        hist_tmp = kkk.ReadObj()
                        if isinstance(hist_tmp, ROOT.TH1):                        
                            name_tmp = hist_tmp.GetName()
                            if operator+"_"+opweight in name_tmp:
                              hist = hist_tmp
                              print(hist.GetXaxis().GetTitle())  
                        else: 
                            print("the hist you want is missing so I am going to crash!")

      if opweight == "0p00": histSM = hist
      hist.SetTitle(operator)
      hist.SetLineColor(ROOT.TColor.GetColor(colors[i]))                                                                                                                                                                                                                
      hist.SetLineWidth(2)
      hist.SetLineStyle(linestyle[i])
      hist.SetMarkerColor(ROOT.TColor.GetColor(colors[i]))                                                                                                                                                                                                                
      hist.SetLineWidth(2)
      hist.SetMarkerStyle(markerstyle[i])
      hist_r.append(hist)
      if "pt" in var or "mjj" in var: pad1.SetLogy()
      legend.AddEntry(hist,opweight.replace("m","-").replace("p","."))
      hist.Draw("Psame")
    legend.Draw("same")
    pad2.cd()
    
    h = []
    for i,opweight in enumerate(shortoperatorsdata[operator]):
      if opweight != "0p00":
        h.append(hist_r[i].Clone())
        h[-1].Divide(histSM)
        h[-1].SetTitle("")
        h[-1].Draw("Psame")
    h[0].GetXaxis().SetTitle(variables[var]['xaxistitle'])
    h[0].GetXaxis().SetTitleSize(0.11)
    h[0].GetXaxis().SetLabelSize(0.11)
    h[0].GetYaxis().SetTitleSize(0.11)
    h[0].GetYaxis().SetTitle("weight/SM")
    h[0].GetYaxis().SetTitleOffset(0.5)
    h[0].GetYaxis().SetLabelSize(0.11)
    h[0].GetYaxis().SetRangeUser(0.,10.)
    h[0].GetYaxis().SetNdivisions(5)
    linea =  ROOT.TLine(histSM.GetXaxis().GetXmin(),1.,histSM.GetXaxis().GetXmax(),1.)
    linea.SetLineColor(17)
    linea.SetLineWidth(2)
    linea.SetLineStyle(2)
    linea.Draw("same")
    outdirname=basedir+year+"/"+filetype
    try:
      os.mkdir(outdirname)
    except:
      print()  
    canvas.SaveAs(outdirname+"/"+var+"_"+operator+".pdf")  
    canvas.SaveAs(outdirname+"/"+var+"_"+operator+".png")  
