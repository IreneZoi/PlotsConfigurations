from ROOT import *
from array import *
import CMS_lumi, tdrstyle
import sys

tdrstyle.setTDRStyle()
CMS_lumi.lumi_13TeV = "2.3 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.writeExtraText2 = 1
CMS_lumi.extraText = "Preliminary"

iPos=11

def makeCanvas(name="c"):

  H_ref = 700
  W_ref = 800
  W = W_ref
  H  = H_ref

  canvas = TCanvas(name,name)

  # references for T, B, L, R
  T = 0.08*H_ref
  B = 0.12*H_ref
  L = 0.18*W_ref
  R = 0.05*W_ref

  canvas.SetFillColor(0)
  canvas.SetBorderMode(0)
  canvas.SetFrameFillStyle(0)
  canvas.SetFrameBorderMode(0)
  canvas.SetLeftMargin( L/W)
  canvas.SetRightMargin( R/W)
  canvas.SetTopMargin( T/H )
  canvas.SetBottomMargin( B/H )
  canvas.SetTickx(1)
  canvas.SetTicky(1)
 
  return canvas


def extract(file):
  expLimit = {}
  for line in file:
    if "Expected" in line:
      res = line.split()
      expLimit[res[1].replace('%:','')] = res[4]

  return expLimit


def getXsec(mass,process,model):
  
  kp = float(model[1]+"."+model[2])*float(model[1]+"."+model[2])
  brn = float((model[6]+"."+model[7]))

  sf = kp*(1-brn)
  print "ewk singlet SF = ",sf

  if process=="ggH":

    rootFile = TFile("eos/user/x/xjanssen/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_GluGluHToWWTo2L2Nu_M"+mass+".root")
    latino = rootFile.Get("latino")
    htemp = TH1F("htemp","htemp",1,0,1)
    latino.Draw("Xsec>>htemp")

    return htemp.GetMean()*sf

  elif process=="VBF":

    rootFile = TFile("eos/user/x/xjanssen/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_VBFHToWWTo2L2Nu_M"+mass+".root")
    latino = rootFile.Get("latino")
    htemp = TH1F("htemp","htemp",1,0,1)
    latino.Draw("Xsec>>htemp")
    
    return htemp.GetMean()*sf
    

def plotLimit(mass,model,option="mu",cat="all"):


	xcentral = array("d") # masses
        ycentral_mu = array("d") # limits
        ycentral_xs = array("d") # limits
        ycentral_ggH = array("d")
        ycentral_VBF = array("d")
	xerr = array("d")
	up1s_mu = array("d")
        up1s_xs = array("d")
        up1s_ggH = array("d")
        up1s_VBF = array("d")
	down1s_mu = array("d")
        down1s_xs = array("d")
        down1s_ggH = array("d")
        down1s_VBF = array("d")
	up2s_mu = array("d")
        up2s_xs = array("d")
        up2s_ggH = array("d")
        up2s_VBF = array("d")
	down2s_mu = array("d")
        down2s_xs = array("d")
        down2s_ggH = array("d")
        down2s_VBF = array("d")


        if option=="mu":

  	  for m in masses:

            xsec_ggH = getXsec(m,"ggH",model)
            xsec_VBF = getXsec(m,"VBF",model)

            if cat=="all":
              #fitfile = "/afs/cern.ch/work/l/lviliani/LatinosFramework13TeV_clean/CMSSW_7_6_3/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv_VBF/combine/Limit.Moriond2016.v1.txt.pruned.mH"+m+"_"+model+".txt"
              fitfile = "/afs/cern.ch/work/l/lviliani/LatinosFramework13TeV_clean/CMSSW_7_6_3/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv_VBF/combineLSF/Limit.ICHEP2016.mH"+m+"_"+model+".txt"

              CMS_lumi.extraText2 = "0+1+2 jets "
            else:
              #fitfile = "/afs/cern.ch/work/l/lviliani/LatinosFramework13TeV_clean/CMSSW_7_6_3/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv_VBF/combine/Limit.Moriond2016."+cat+".mH"+m+"_"+model+".txt"
              fitfile = "/afs/cern.ch/work/l/lviliani/LatinosFramework13TeV_clean/CMSSW_7_6_3/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv_VBF/combineLSF/Limit.ICHEP2016."+cat+".mH"+m+"_"+model+".txt"

              CMS_lumi.extraText2 = cat.replace("jet"," jet ")

            fitFile = open(fitfile)#"/afs/cern.ch/work/l/lviliani/LatinosFramework13TeV_clean/CMSSW_7_6_3/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv_VBF/combine/Limit.Moriond2016.2jet.mH"+m+".txt")
	    expLimit = extract(fitFile)

            xcentral.append(float(m))
  	    xerr.append(0)
	    ycentral_mu.append( float(expLimit['50.0']) )
            down1s_mu.append( float(expLimit['50.0'])-float(expLimit['16.0']) )
	    up1s_mu.append( float(expLimit['84.0'])-float(expLimit['50.0']) )
	    down2s_mu.append( float(expLimit['50.0'])-float(expLimit['2.5']) )
	    up2s_mu.append( float(expLimit['97.5'])-float(expLimit['50.0']) )

            ycentral_xs.append( float(expLimit['50.0'])*(xsec_ggH+xsec_VBF) )
            down1s_xs.append( (float(expLimit['50.0'])-float(expLimit['16.0']))*(xsec_ggH+xsec_VBF) )
            up1s_xs.append( (float(expLimit['84.0'])-float(expLimit['50.0']))*(xsec_ggH+xsec_VBF) )
            down2s_xs.append( (float(expLimit['50.0'])-float(expLimit['2.5']))*(xsec_ggH+xsec_VBF) )
            up2s_xs.append( (float(expLimit['97.5'])-float(expLimit['50.0']))*(xsec_ggH+xsec_VBF) )


  	  c1 = makeCanvas("c1")
       
          CMS_lumi.extraText2 += model.replace("c","\nc'= ").replace("0","0.").replace("brn"," BR_{new} = ").replace("0.0.","0.0").replace("10.","1.0")

  
	  graphcentral_mu = TGraph(len(xcentral),xcentral,ycentral_mu)
	  graphcentral_mu.SetLineStyle(2)

	  graph2s_mu = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_mu,xerr,xerr,down2s_mu,up2s_mu)
	  graph2s_mu.SetFillColor(kYellow)
	  graph2s_mu.SetTitle("")
	  graph2s_mu.GetYaxis().SetTitle("95% CL limit on #sigma/#sigma_{SM}")
	  graph2s_mu.GetXaxis().SetTitle("M_{X} [GeV]")
	  graph2s_mu.GetXaxis().SetRangeUser(200,1000)
          graph2s_mu.GetYaxis().SetRangeUser(0,15)

	  graph1s_mu = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_mu,xerr,xerr,down1s_mu,up1s_mu)
	  graph1s_mu.SetFillColor(kGreen)

          leg1 = TLegend(0.65, 0.7, 0.95, 0.9)
          leg1.SetBorderSize(0)
          leg1.SetFillStyle(0)
          leg1.AddEntry(graphcentral_mu,"Expected","l")
          leg1.AddEntry(graph1s_mu,"#pm 1 #sigma Expected","f")
          leg1.AddEntry(graph2s_mu,"#pm 2 #sigma Expected","f")
 
	  graph2s_mu.Draw("A3")
	  graph1s_mu.Draw("3 same")
	  graphcentral_mu.Draw("L same")
          leg1.Draw()
          CMS_lumi.CMS_lumi(c1, 4, iPos)
          gPad.RedrawAxis()


          c2 = makeCanvas("c2")

          if cat=="all":
            CMS_lumi.extraText2 = "0+1+2 jets "
          else:
            CMS_lumi.extraText2 = cat.replace("jet"," jet ")
 
          graphcentral_xs = TGraph(len(xcentral),xcentral,ycentral_xs)
          graphcentral_xs.SetLineStyle(2)

          graph2s_xs = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_xs,xerr,xerr,down2s_xs,up2s_xs)
          graph2s_xs.SetFillColor(kYellow)
          graph2s_xs.SetTitle("")
          graph2s_xs.GetYaxis().SetTitle("95% CL limit on #sigma_{ggH}+#sigma_{VBF} [pb]")
          graph2s_xs.GetXaxis().SetTitle("M_{X} [GeV]")
          graph2s_xs.GetXaxis().SetRangeUser(200,1000)
          graph2s_xs.GetYaxis().SetRangeUser(0,5)          

          graph1s_xs = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_xs,xerr,xerr,down1s_xs,up1s_xs)
          graph1s_xs.SetFillColor(kGreen)

          leg2 = TLegend(0.65, 0.7, 0.95, 0.9)
          leg2.SetBorderSize(0)
          leg2.SetFillStyle(0)
          leg2.AddEntry(graphcentral_mu,"Expected","l")
          leg2.AddEntry(graph1s_mu,"#pm 1 #sigma Expected","f")
          leg2.AddEntry(graph2s_mu,"#pm 2 #sigma Expected","f")

          graph2s_xs.Draw("A3")
          graph1s_xs.Draw("3 same")
          graphcentral_xs.Draw("L same")
          leg2.Draw()

          CMS_lumi.CMS_lumi(c2, 4, iPos)

	  gPad.RedrawAxis()














	elif option=="xsec":

          for m in masses:

            fitFile = open("/afs/cern.ch/work/l/lviliani/LatinosFramework13TeV_clean/CMSSW_7_6_3/src/LatinoAnalysis/ShapeAnalysis/PlotsConfigurations/Configurations/EXO/WWlvlv_VBF/combine/Limit.Moriond2016.v1.txt.pruned.mH"+m+".txt")
            expLimit = extract(fitFile)
       
            xsec_ggH = getXsec(m,"ggH")
            xsec_VBF = getXsec(m,"VBF")
       
            print "Mass: ", m
            print "ggH xsec(pb) = ", xsec_ggH
            print "VBF xsec(pb) = ", xsec_VBF
   
            xcentral.append(float(m))
            xerr.append(0)

            ## draw ggH xsec limits
            ycentral_ggH.append( float(expLimit['50.0'])*xsec_ggH )
            down1s_ggH.append( (float(expLimit['50.0'])-float(expLimit['16.0']))*xsec_ggH )
            up1s_ggH.append( (float(expLimit['84.0'])-float(expLimit['50.0']))*xsec_ggH )
            down2s_ggH.append( (float(expLimit['50.0'])-float(expLimit['2.5']))*xsec_ggH )
            up2s_ggH.append( (float(expLimit['97.5'])-float(expLimit['50.0']))*xsec_ggH )

            ## draw VBF xsec limits
            ycentral_VBF.append( float(expLimit['50.0'])*xsec_VBF )
            down1s_VBF.append( (float(expLimit['50.0'])-float(expLimit['16.0']))*xsec_VBF )
            up1s_VBF.append( (float(expLimit['84.0'])-float(expLimit['50.0']))*xsec_VBF )
            down2s_VBF.append( (float(expLimit['50.0'])-float(expLimit['2.5']))*xsec_VBF )
            up2s_VBF.append( (float(expLimit['97.5'])-float(expLimit['50.0']))*xsec_VBF )

          c1 = TCanvas()
          c1.cd()
          c1.SetTicky()
          c1.SetTickx()

          graphcentral_ggH = TGraph(len(xcentral),xcentral,ycentral_ggH)
          graphcentral_ggH.SetLineStyle(2)

          graph2s_ggH = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_ggH,xerr,xerr,down2s_ggH,up2s_ggH)
          graph2s_ggH.SetFillColor(kYellow)
          graph2s_ggH.SetTitle("")
          graph2s_ggH.GetYaxis().SetTitle("95% CL limit on #sigma(gg #rightarrow X) [pb]")
          graph2s_ggH.GetXaxis().SetTitle("M_{X} [GeV]")
          graph2s_ggH.GetXaxis().SetRangeUser(200,1000)

          graph1s_ggH = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_ggH,xerr,xerr,down1s_ggH,up1s_ggH)
          graph1s_ggH.SetFillColor(kGreen)

          leg = TLegend(0.45, 0.10, 3, 0.015)
          leg.AddEntry(graphcentral_mu,"Expected","l")
          leg.AddEntry(graph1s_mu,"#pm 1 #sigma Expected","f")
          leg.AddEntry(graph2s_mu,"#pm 2 #sigma Expected","f")

          graph2s_ggH.Draw("A3")
          graph1s_ggH.Draw("3 same")
          graphcentral_ggH.Draw("L same")
          leg.Draw()

          gPad.RedrawAxis()

          c2 = TCanvas()
          c2.cd()
          c2.SetTicky()
          c2.SetTickx()

          graphcentral_VBF = TGraph(len(xcentral),xcentral,ycentral_VBF)
          graphcentral_VBF.SetLineStyle(2)

          graph2s_VBF = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_VBF,xerr,xerr,down2s_VBF,up2s_VBF)
          graph2s_VBF.SetFillColor(kYellow)
          graph2s_VBF.SetTitle("")
          graph2s_VBF.GetYaxis().SetTitle("95% CL limit on #sigma(qq #rightarrow X) [pb]")
          graph2s_VBF.GetXaxis().SetTitle("M_{X} [GeV]")
          graph2s_VBF.GetXaxis().SetRangeUser(200,1000)

          graph1s_VBF = TGraphAsymmErrors(len(xcentral),xcentral,ycentral_VBF,xerr,xerr,down1s_VBF,up1s_VBF)
          graph1s_VBF.SetFillColor(kGreen)

          leg = TLegend(0.45, 0.45, 0.9, 0.9)
          leg.AddEntry(graphcentral_mu,"Expected","l")
          leg.AddEntry(graph1s_mu,"#pm 1 #sigma Expected","f")
          leg.AddEntry(graph2s_mu,"#pm 2 #sigma Expected","f")

          graph2s_VBF.Draw("A3")
          graph1s_VBF.Draw("3 same")
          graphcentral_VBF.Draw("L same")
          leg.Draw()

          gPad.RedrawAxis()


	a=raw_input()


masses = ["200","250","300","350","400","450","500","550","600","650","750","800","1000"]
model = "c10brn00"
cat = sys.argv[1]

plotLimit(masses,model,"mu",cat)
