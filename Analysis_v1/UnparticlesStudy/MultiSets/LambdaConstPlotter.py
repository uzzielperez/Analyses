#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
#from legend import *
#from plotsHelpercomp import *
import re

import sys
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)
from CMSlumi import CMS_lumi, set_CMS_lumi
import argparse

# Command line options
parser = argparse.ArgumentParser(description="ratioPlotter")
parser.add_argument("-i", "--inputfiles", dest="inputfiles", default=["TestADDG2gg_LambdaT-10000_M-500-pythia8.root"], nargs='*', help="List of input files")
args = parser.parse_args()

L800 = False
L1000 = False
L2000 = True

DATASET = []
if L800:
	tag = "L800"
	print tag
	DATASET.append("../Unparticles_du1p01_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p1_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p2_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p3_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p4_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p5_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p6_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p7_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p8_LambdaU-800_TuneCUEP8M1_13TeV.root")
	#DATASET.append("../Unparticles_du1p9_LambdaU-800_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_SM_TuneCUEP8M1_13TeV.root")
if L1000:
	tag = "L1000"
	print tag
	DATASET.append("../Unparticles_du1p01_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p1_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p2_LambdaU-1000_TuneCUEP8M1_13TeV.root")
        DATASET.append("../Unparticles_du1p3_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p4_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p5_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p6_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p7_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p8_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	#DATASET.append("../Unparticles_du1p9_LambdaU-1000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_SM_TuneCUEP8M1_13TeV.root")
if L2000:
	tag = "L2000"
	print tag
        DATASET.append("../Unparticles_du1p01_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p1_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p2_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p3_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p4_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p5_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p6_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p7_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_du1p8_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	#DATASET.append("../Unparticles_du1p9_LambdaU-2000_TuneCUEP8M1_13TeV.root")
	DATASET.append("../Unparticles_SM_TuneCUEP8M1_13TeV.root")

# Draw Options
DrawAsHist = False
gStyle.SetOptStat(0)

# Timer
sw = ROOT.TStopwatch()
sw.Start()

uf = []

for datafile in DATASET:
	uf.append(ROOT.TFile(datafile, "READ"))

canvas = ROOT.TCanvas()
#canvas.SetLogy()
obj = "gendiphotonMinv"
uh = []

for openfile in uf:
	uh.append(openfile.Get(obj))
	#uh1 = uf1.Get(obj)

xtitle = r"m_{#gamma#gamma}#scale[1.0]{(GeV)}"
xmin, xmax = 300, 4000
ytitle = r"#scale[0.8]{weighted events}"

uh[0].GetYaxis().SetTitle(ytitle)
uh[0].GetYaxis().SetTitleOffset(1.0)
uh[0].GetXaxis().SetTitle(xtitle)
#uh[0].GetYaxis().SetRangeUser(10**-5, max(eventsmaxlist))
uh[0].GetXaxis().SetRangeUser(xmin, xmax)

legEntry = []
xpos1, ypos1, xpos2, ypos2 = .55, 0.58, .85, .88
leg = TLegend(xpos1, ypos1, xpos2, ypos2)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)

i = 0

for hist in uh:
	hist.SetLineColor(i+1)
	if i == 9:
		hist.SetLineColor(46)
		#hist.SetLineStyle(9)
		hist.SetFillColor(48)
	hist.Draw("hist, same")
	pattern = r'Unparticles_([^(]*)_TuneCUEP8M1_13TeV.root'
	label = str(re.findall(pattern, DATASET[i])[0])
	print pattern, label
	leg.AddEntry(hist, "%s" %(label), "l")
	i = i + 1

leg.Draw()
set_CMS_lumi(canvas, 4, 11, "1")
canvas.Update()
canvas.Draw()
canvas.Print("Unparticles_%s%s.pdf" %(obj,tag))
canvas.SetLogy()
canvas.Update()
canvas.Draw()
canvas.Print("LOGUnparticles_%s%s.pdf" %(obj,tag))
