#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
#from ROOT import kBlack, kBlue, kRed, kGreen, kMagenta, kCyan, kOrange, kViolet, kSpring
from ROOT import kBlue, kOrange, kCyan, kRed, kMagenta, kGreen, kViolet, kSpring, kPink, kAzure
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

LambdaT = "ALL"

SMPythia8 = True
SM = False
ADD = True

tag = "b"
zoom = False
#drawstyle = "hist, same"
drawstyle = "same"
intlumi = 130

BKG = []
path = "/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/UnparticlesSplitStudy"

BKG.append("%s/Unparticles_SM_M_500-2000.root" %(path))
BKG.append("%s/Unparticles_SM_M-2000.root" %(path))
BKG.append("../processed/GGJetsAN_M-1000.root")

DATASET = []
DATASET.append("../processed/TestADD_NI-1_LambdaT-4000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-4500_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-5000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-5500_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-6000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-6500_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-7000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-7500_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-8000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-8500_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-9000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-10000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-11000_M-1000.root")
DATASET.append("../processed/TestADD_NI-1_LambdaT-13000_M-1000.root")
#
# Draw Options
DrawAsHi = False
gStyle.SetOptStat(0)

bkgf = []
for fi in BKG:
	bkgf.append(ROOT.TFile(fi, "READ"))

uf = []
for datafile in DATASET:
	uf.append(ROOT.TFile(datafile, "READ"))

canvas = ROOT.TCanvas()
canvas.SetLogy()
obj = "gendiphotonMinv"
uh = []
bkgh = []

for ofile in bkgf:
	bkgh.append(ofile.Get(obj))

for openfile in uf:
	uh.append(openfile.Get(obj))

xtitle = r"m_{#gamma#gamma}#scale[1.0]{(GeV)}"
ytitle = r"#scale[1.0]{Nevents}"
xmin, xmax = 500, 13000

if zoom:
	xmin, xmax = 1000, 2500
x_range = "%s-%s" %(str(xmin), str(xmax))

xpos1, ypos1, xpos2, ypos2 = .55, 0.58, .85, .88
leg = TLegend(xpos1, ypos1, xpos2, ypos2)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)

if SMPythia8:
	tag = tag + "SM"
	histSM = bkgh[0].Clone("histSM")
	histSM.Add(bkgh[1], 1.0)
	histSM.SetFillStyle(3144)
	histSM.SetFillColor(7)
	histSM.Scale(intlumi)
	histSM.Draw("hist")
	label = "SM"
	leg.AddEntry(histSM, "%s" %(label), "f")
    	print "Drawn", label

if SM:
	tag = tag + "SM"
	histSM = bkgh[3].Clone("histSM")
	#histSM.Add(bkgh[1], 1.0)
	histSM.SetFillStyle(3144)
	histSM.SetFillColor(7)
	histSM.Scale(intlumi)
	#histSM.Draw("hist")
	label = "SM"
	leg.AddEntry(histSM, "%s" %(label), "f")
    	print "Drawn", label

colorlist = [kBlue, kOrange, kCyan, kRed, kMagenta, kGreen, kViolet, kSpring, kPink, kAzure, kOrange+8, kGreen+8, kRed+8, kViolet+8, kMagenta+5]
labels = []
histClones = []
iset = 0
icolor = 0
i = 0
while iset < len(DATASET):
	pattern = "TestADD_NI-1_([^(]*)_M-1000.root"
	label = re.findall(pattern, DATASET[iset])
    	labels.append(label[0])
    	tag = tag + label[0]
    	#histClone.delete
    	iset = iset + 1

while i < len(DATASET):
	histClone = uh[i].Clone("histdu%s" %(labels[i]))
    	#histClone.Add(uh[i+1], 1.0)
    	histClones.append(histClone)
    	i = i + 1

j = 0
for histclone in histClones:
	histclone.SetLineColor(colorlist[icolor])
	histclone.Scale(intlumi)
	histclone.Draw(drawstyle)
	print labels[j]
	leglabel = r"d#Lambda_{T} = %s" %(labels[j])
    	leg.AddEntry(histclone, "%s" %(leglabel), "l")

	j = j+1
    	icolor = icolor + 1

#iclone = 0
#while iclone < len(histClones):
    # histClones[iclone].Add(uh[iclone+1], 1.0)
    # iclone.SetLineColor(colorlist[icolor])
    # iclone.Scale(intlumi)
    # iclone.Draw(drawstyle)
    # leglabel = r"du = %s, #Lambda_{U} = %s" %(label)
    # leg.AddEntry(histClone, "%s" %(leglabel), "l")
    # histClone.delete
	#
    # icolor = icolor + 1
print tag

histSM.GetYaxis().SetTitle(ytitle)
histSM.GetYaxis().SetTitleOffset(1.0)
histSM.GetXaxis().SetTitle(xtitle)
histSM.GetXaxis().SetRangeUser(xmin, xmax)

leg.Draw()
set_CMS_lumi(canvas, 4, 11, intlumi)
canvas.Update()
canvas.Draw()
canvas.Print("LOG%s_SMvsADD_%sfb-1_%s_%s.pdf" %(intlumi, LambdaT, obj,tag))
