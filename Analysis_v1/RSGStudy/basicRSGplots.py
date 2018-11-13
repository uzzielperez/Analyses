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

kMpl02_SM = False #too close 
kMpl02 = False #too small

kMpl02_750_1250  = False 
kMpl02_1500_2000 = False
kMpl02_2250_3000 = False
kMpl02_3500_4500 = False
kMpl02_4750_5250 = False
kMpl02_5500_5750 = False 
kMpl02_6500_8000 = True

pattern = r'RSG_([^(]*)_py_GEN.root'

DATASET = []
if kMpl02_SM:
	tag = "kMpl02_SM"
	DATASET.append("RSG_SM_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1250_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2250_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_3000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_3500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5250_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_6000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_6500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_7000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_8000_py_GEN.root")
	xmin, xmax = 300, 10000
if kMpl02:
	tag = "kMpl02"
	DATASET.append("RSG_kMpl02_M_750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1250_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2250_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_3000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_3500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5250_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_6000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_6500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_7000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_8000_py_GEN.root")
	DATASET.append("RSG_SM_py_GEN.root")
	xmin, xmax = 300, 10000


if kMpl02_750_1250:
	tag = "kMpl02_750_1250"
	xpos1, ypos1, xpos2, ypos2 = .55, 0.68, .85, .88
	xmin, xmax = 300, 2000
	#DATASET.append("RSG_SM_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1250_py_GEN.root")
if kMpl02_1500_2000:
	
	xpos1, ypos1, xpos2, ypos2 = .55, 0.68, .85, .88
	tag = "kMpl02_1500_2000"
	xmin, xmax = 1000, 2500
	DATASET.append("RSG_kMpl02_M_1500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_1750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2000_py_GEN.root")
if kMpl02_2250_3000:
	tag = "kMpl02_2250_3000"	
	xpos1, ypos1, xpos2, ypos2 = .55, 0.68, .85, .88
	xmin, xmax = 1750, 3500
	DATASET.append("RSG_kMpl02_M_2250_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_2500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_3000_py_GEN.root")
if kMpl02_3500_4500:
	tag = "kMpl02_3500_4500"
	xpos1, ypos1, xpos2, ypos2 = .55, 0.68, .85, .88
	xmin, xmax = 3000, 5000
	DATASET.append("RSG_kMpl02_M_3500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_4500_py_GEN.root")
if kMpl02_4750_5250:
	tag = "kMpl02_4750_5250"
	xmin, xmax = 4000, 6000
	xpos1, ypos1, xpos2, ypos2 = .55, 0.68, .85, .88
	DATASET.append("RSG_kMpl02_M_4750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5250_py_GEN.root")
if kMpl02_5500_5750:
	tag = "kMpl02_5500_5750"
	xmin, xmax = 5000, 6500
	xpos1, ypos1, xpos2, ypos2 = .55, 0.68, .85, .88
	DATASET.append("RSG_kMpl02_M_5500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_5750_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_6000_py_GEN.root")
if kMpl02_6500_8000:
	xmin, xmax = 5500, 9000
	xpos1, ypos1, xpos2, ypos2 = .55, 0.68, .85, .88
	tag = "kMpl02_6500_8000"
	DATASET.append("RSG_kMpl02_M_6500_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_7000_py_GEN.root")
	DATASET.append("RSG_kMpl02_M_8000_py_GEN.root")

print tag 
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
ytitle = r"#scale[0.8]{weighted events}"

uh[0].GetYaxis().SetTitle(ytitle)
uh[0].GetYaxis().SetTitleOffset(1.0)
uh[0].GetXaxis().SetTitle(xtitle)
#uh[0].GetYaxis().SetRangeUser(10**-5, max(eventsmaxlist))
uh[0].GetXaxis().SetRangeUser(xmin, xmax)

legEntry = []
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
		#hist.SetFillColor(48)
	hist.Draw("hist, same")
	label = str(re.findall(pattern, DATASET[i])[0])
	print pattern, label
	leg.AddEntry(hist, "%s" %(label), "l")
	i = i + 1

leg.Draw()
set_CMS_lumi(canvas, 4, 11, "1")
canvas.Update()
canvas.Draw()
canvas.Print("RSGcheck_%s%s.pdf" %(obj,tag))
#canvas.SetLogy()
#canvas.Update()
#canvas.Draw()
#canvas.Print("LOGRSGcheck_%s%s.pdf" %(obj,tag))
