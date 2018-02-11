#!/usr/bin/python

import os
import argparse
import re

import ROOT
from ROOT import TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
from CMSlumi import CMS_lumi

path = "/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/macros/DiphotonAnalysis/"
filename = "diphoton2016bkg_histograms.root"

##########################################
# Extra Cosmetics
gStyle.SetOptStat(0)

#CMS_lumi( TPad* pad, int iPeriod=3, int iPosX=10 )
##########################################
f = ROOT.TFile(path+filename)
f.ls()

c=ROOT.TCanvas("mycanvas","mycanvas",600,600)
#c.SetGrid()
diphoton_Minvn = f.Get("diphotonMinvn")
diphoton_Minvn.GetXaxis().SetTitleOffset(1.4)
diphoton_Minvn.GetXaxis().SetTitle(r"m_{#gamma#gamma} #scale[0.8]{(GeV)}")
diphoton_Minvn.GetYaxis().SetTitleOffset(1.4)
diphoton_Minvn.GetYaxis().SetTitle("weighted events/ 80 GeV")
diphoton_Minvn.SetAxisRange(200, 1600) #To draw hist from 200 1600
diphoton_Minvn.Draw("hist") #have to add hist to not draw with error bars

legend1 = TLegend(.60, 0.75, .97, .85)
legend1.SetBorderSize(0)
legend1.SetFillColor(0)
legend1.SetFillStyle(0)
legend1.SetTextFont(42)
legend1.SetTextSize(0.035)
legend1.AddEntry(diphoton_Minvn,"SM Diphoton","l")
legend1.Draw()

CMS_lumi(c, 4, 11) 

c.SetLogy()
c.Draw()
#c.Print("BKGPlots.pdf[", "minv")
c.Print("BKGPlotsminv.pdf")
c.Print("BKGPlotsminv.png")
############################################
canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
canvas.Clear()


hphoton1pTn = f.Get("photon1Ptn")
hphoton2pTn = f.Get("photon2Ptn")

hphoton1pTn.GetXaxis().SetTitleOffset(1.4)
hphoton1pTn.GetXaxis().SetTitle(r"p_{T} (GeV)")
hphoton1pTn.SetAxisRange(200, 2000)
hphoton1pTn.GetYaxis().SetTitleOffset(1)
hphoton1pTn.GetYaxis().SetTitle("weighted events/ 80 GeV")

hphoton1pTn.Draw("hist")
hphoton2pTn.SetLineColor(kBlack)
hphoton2pTn.Draw("hist same")

leg = TLegend(.75, 0.75, .97, .85)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.AddEntry(hphoton1pTn,r"#gamma_{1} p_{T}")
leg.AddEntry(hphoton2pTn,r"#gamma_{2} p_{T}")
leg.Draw()

CMS_lumi(canvas, 4, 11)

canvas.SetLogy()
canvas.Draw()
#canvas.Print("BKGPlots.pdf", "pT")
canvas.Print("BKGPlotspT.pdf")
canvas.Print("BKGPlotspT.png")
############################################
mcanvas = ROOT.TCanvas("mcanv", "mcanv", 800, 400)
mcanvas.Clear()
mcanvas.Divide(2,1)

hphoton1etan = f.Get("photon1Etan")
hphoton1phin = f.Get("photon1Phin")
hphoton2etan = f.Get("photon2Etan")
hphoton2phin = f.Get("photon2Phin")

mcanvas.cd(1)

hphoton1etan.GetXaxis().SetTitleOffset(1)
hphoton1etan.GetXaxis().SetTitle(r"#eta")
hphoton1etan.GetYaxis().SetTitleOffset(1.2)
hphoton1etan.GetYaxis().SetTitle("weighted events/ 80 GeV")

hphoton1etan.Draw("hist")
hphoton2etan.SetLineColor(kBlack)
hphoton2etan.Draw("hist same")

leg2 = TLegend(.68, 0.75, .97, .85)
leg2.SetBorderSize(0)
leg2.SetFillColor(0)
leg2.SetFillStyle(0)
leg2.SetTextFont(42)
leg2.SetTextSize(0.035)
leg2.AddEntry(hphoton1etan,r"#gamma_{1} p_{T}")
leg2.AddEntry(hphoton2etan,r"#gamma_{2} p_{T}")
leg2.Draw()
CMS_lumi(mcanvas, 4, 11)
mcanvas.cd(2)

hphoton1phin.GetXaxis().SetTitleOffset(1)
hphoton1phin.GetXaxis().SetTitle(r"#phi")
hphoton1phin.GetYaxis().SetTitleOffset(1.2)
hphoton1phin.GetYaxis().SetTitle("weighted events/ 80 GeV")

hphoton1phin.Draw("hist")
hphoton2phin.SetLineColor(kBlack)
hphoton2phin.Draw("hist same")

leg3 = TLegend(.68, 0.75, .97, .85)
leg3.SetBorderSize(0)
leg3.SetFillColor(0)
leg3.SetFillStyle(0)
leg3.SetTextFont(42)
leg3.SetTextSize(0.035)
leg3.AddEntry(hphoton1phin,r"#gamma_{1}")
leg3.AddEntry(hphoton2phin,r"#gamma_{2}")
leg3.Draw()

CMS_lumi(mcanvas, 4, 11)
mcanvas.Draw()
mcanvas.Print("BKGPlots.pdf]", "angles")

mcanvas.Print("BKGPlotsang.pdf")
mcanvas.Print("BKGPlotsang.png")
raw_input("Press enter to continue...")

#############################################
# Save canvas as pdf or png

