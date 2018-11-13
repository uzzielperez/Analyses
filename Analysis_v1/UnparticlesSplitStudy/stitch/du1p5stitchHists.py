#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed, kGreen, kMagenta, kCyan, kOrange, kViolet, kSpring
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
#from legend import *
#from plotsHelpercomp import *
import re

import sys
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)
from CMSlumi import CMS_lumi, set_CMS_lumi
import argparse

sw = ROOT.TStopwatch()
sw.Start()

du_tag = "1p5"
SM = True
LU1500 = True
LU2000 = True
LU2500 = True
LU3000 = True
LU4000 = True

tag = "b"

zoom = False
#drawstyle = "hist, same"
drawstyle = "same"

intlumi = 130

DATASET = []
DATASET.append("../Unparticles_SM_M_500-2000.root")
DATASET.append("../Unparticles_SM_M-2000.root")
DATASET.append("../TestSTest1p5Unp1500p0_M_2000.root")
DATASET.append("../TestSTest1p5Unp1500p0_M_500-2000.root")
DATASET.append("../TestSTest1p5Unp2000p0_M_2000.root")
DATASET.append("../TestSTest1p5Unp2000p0_M_500-2000.root")
DATASET.append("../TestSTest1p5Unp2500p0_M_2000.root")
DATASET.append("../TestSTest1p5Unp2500p0_M_500-2000.root")
DATASET.append("../TestSTest1p5Unp3000p0_M_2000.root")
DATASET.append("../TestSTest1p5Unp3000p0_M_500-2000.root")
DATASET.append("../TestSTest1p5Unp4000p0_M_2000.root")
DATASET.append("../TestSTest1p5Unp4000p0_M_500-2000.root")
#DATASET.append("../Unparticles_du1p8_LambdaU_1000_M_500-2000.root")
# Draw Options
DrawAsHi = False
gStyle.SetOptStat(0)

uf = []
for datafile in DATASET:
        uf.append(ROOT.TFile(datafile, "READ"))

canvas = ROOT.TCanvas()
obj = "gendiphotonMinv"
uh = []

for openfile in uf:
	uh.append(openfile.Get(obj))

xtitle = r"m_{#gamma#gamma}#scale[1.0]{(GeV)}"
ytitle = r"#scale[1.0]{Nevents}"
xmin, xmax = 500, 13000

if zoom:
	xmin, xmax = 500, 1500
x_range = "%s-%s" %(str(xmin), str(xmax))

xpos1, ypos1, xpos2, ypos2 = .55, 0.58, .85, .88
leg = TLegend(xpos1, ypos1, xpos2, ypos2)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
#pattern = r'Unparticles_([^(]*).root'

if SM:
	tag = tag + "SM"
	histSM = uh[0].Clone("histSM")
	histSM.Add(uh[1], 1.0)
	histSM.SetFillStyle(3144)
	histSM.SetFillColor(7)
	histSM.Scale(intlumi)
	histSM.Draw("hist")
	label = "SM"
	leg.AddEntry(histSM, "%s" %(label), "f")
if LU1500:
	tag = tag+"LU1p5"
	histLU1500 = uh[2].Clone("histLU1500")
	histLU1500.Add(uh[3], 1.0)
	histLU1500.SetLineColor(kGreen +4)
	histLU1500.Scale(intlumi)
	histLU1500.Draw(drawstyle)
	label = r"du = %s, #Lambda_{U} = 1500" %(du_tag)
	leg.AddEntry(histLU1500, "%s" %(label), "l")
if LU2000:
	tag = tag+"LU2"
	histLU2000 = uh[4].Clone("histLU2000")
	histLU2000.Add(uh[5], 1.0)
	histLU2000.SetLineColor(kOrange)
	histLU2000.Scale(intlumi)
	histLU2000.Draw(drawstyle)
	label = r"du = %s, #Lambda_{U} = 2000" %(du_tag)
	leg.AddEntry(histLU2000, "%s" %(label), "l")
if LU2500:
	tag = tag+"LU2p5"
	histLU2500 = uh[6].Clone("histLU2500")
	histLU2500.Add(uh[7], 1.0)
	histLU2500.SetLineColor(kRed)
	histLU2500.Scale(intlumi)
	histLU2500.Draw(drawstyle)
	label = r"du = %s, #Lambda_{U} = 2500" %(du_tag)
	leg.AddEntry(histLU2500, "%s" %(label), "l")
if LU3000:
	tag = tag + "LU3"
	histLU3000 = uh[8].Clone("histLU3000")
	histLU3000.Add(uh[9], 1.0)
	histLU3000.SetLineColor(kBlue)
	histLU3000.Scale(intlumi)
	histLU3000.Draw(drawstyle)
	label = r"du = %s, #Lambda_{U} = 3000" %(du_tag)
	leg.AddEntry(histLU3000, "%s" %(label), "l")
if LU4000:
	tag = tag + "LU4"
	histLU4000 = uh[10].Clone("histLU4000")
	histLU4000.Add(uh[11], 1.0)
	histLU4000.SetLineColor(kMagenta)
	histLU4000.Scale(intlumi)
	histLU4000.Draw(drawstyle)
	label = r"du = %s, #Lambda_{U} = 4000" %(du_tag)
	leg.AddEntry(histLU4000, "%s" %(label), "l")
print tag

histSM.GetYaxis().SetTitle(ytitle)
histSM.GetYaxis().SetTitleOffset(1.0)
histSM.GetXaxis().SetTitle(xtitle)
histSM.GetXaxis().SetRangeUser(xmin, xmax)

leg.Draw()
set_CMS_lumi(canvas, 4, 11, intlumi)
#canvas.Update()
#canvas.Draw()
#canvas.Print("Unparticles_%sfb-1_%s%s_M-%s.pdf" %(intlumi, obj,tag, x_range))
canvas.SetLogy()
canvas.Update()
canvas.Draw()
canvas.Print("LOGdu%s_Unparticles_%sfb-1_%s%s.pdf" %(intlumi, du_tag, obj,tag))
