#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
#from ROOT import kBlack, kBlue, kRed, kGreen, kMagenta, kCyan, kOrange, kViolet, kSpring
from ROOT import kBlue, kOrange, kCyan, kRed, kMagenta, kGreen, kViolet, kSpring, kPink, kAzure
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
#from legend import *
#from plotsHelpercomp import *
import re
from datetime import date

import sys
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)
from CMSlumi import CMS_lumi, set_CMS_lumi
import argparse

sw = ROOT.TStopwatch()
sw.Start()

dodu1p1 = False
dodu1p8 = False
dodu1p9 = True
#du_tag = "1p01"
Lambda_tag = "LU"
obj = "gendiphotonMinv"
#obj = "gendiphotoncosthetastar"
#obj = "genchidiphoton"

SM = True
UNP = True
zoom = False
#drawstyle = "hist, same"
drawstyle = "same"
intlumi = 130
today = str(date.today())
xtratag = "isEBEB"
#xtratag = ""
#xtratag = "b"
path = "/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/UnparticlesSplitStudy/isEBEB"
BKG = []
BKG.append("%s/Unparticles_SM_M_500-2000.root" %(path))
BKG.append("%s/Unparticles_SM_M-2000.root" %(path))

DATASET = []
if dodu1p1:
	dutag = "1.1"
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp1500p0_spin-0_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp1500p0_spin-0_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp1500p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp1500p0_spin-2_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp2500p0_spin-0_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp2500p0_spin-0_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp2500p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp2500p0_spin-2_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp4000p0_spin-0_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp4000p0_spin-0_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp4000p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p1Unp4000p0_spin-2_M_2000_py_GEN.root")
if dodu1p8:
	dutag = "1.8"
	DATASET.append("../varCutsTemplates/OUTTestSTest1p8Unp1500p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p8Unp1500p0_spin-2_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p8Unp2500p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p8Unp2500p0_spin-2_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p8Unp4000p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p8Unp4000p0_spin-2_M_2000_py_GEN.root")

if dodu1p9:
	dutag = "1.9"
	DATASET.append("../varCutsTemplates/OUTTestSTest1p9Unp1500p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p9Unp1500p0_spin-2_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p9Unp2500p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p9Unp2500p0_spin-2_M_2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p9Unp4000p0_spin-2_M_500-2000_py_GEN.root")
	DATASET.append("../varCutsTemplates/OUTTestSTest1p9Unp4000p0_spin-2_M_2000_py_GEN.root")

dulabel = r"d_{u} = %s" %(dutag)
# Draw Options
DrawAsHist = False
gStyle.SetOptStat(0)

bkgf = []
for fi in BKG:
	bkgf.append(ROOT.TFile(fi, "READ"))

uf = []
for datafile in DATASET:
	uf.append(ROOT.TFile(datafile, "READ"))

canvas = ROOT.TCanvas()
canvas.SetLogy()

uh = []
bkgh = []

for ofile in bkgf:
	bkgh.append(ofile.Get(obj))

for openfile in uf:
	uh.append(openfile.Get(obj))

if "Minv" in obj:
	xtitle = r"m_{#gamma#gamma}#scale[1.0]{(GeV)}"
	ytitle = r"#scale[1.0]{Nevents}"
	xmin, xmax = 500, 13000
if "chidiphoton" in obj:
	xtitle = r"#Chi_{#gamma#gamma}"
	ytitle = r"#scale[1.0]{Nevents}"
	xmin, xmax = 0, 300
if "costhetastar" in obj:
	xtitle = r"cos#theta^{*}"
	ytitle = r"#scale[1.0]{Nevents}"
	xmin, xmax = -1, 1

if zoom:
	xmin, xmax = 500, 2500
x_range = "%s-%s" %(str(xmin), str(xmax))

xpos1, ypos1, xpos2, ypos2 = .55, 0.58, .85, .88
legendtitle = "#bf{Scaling dimension:} %s (%s)" %(dulabel, xtratag)
leg = TLegend(xpos1, ypos1, xpos2, ypos2)
leg.SetHeader(legendtitle, "C")
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
#pattern = r'Unparticles_([^(]*).root'

if SM:
	tag = "SM"
	histSM = bkgh[0].Clone("histSM")
	histSM.Add(bkgh[1], 1.0)
	histSM.SetFillStyle(3144)
	histSM.SetFillColor(7)
	histSM.Scale(intlumi)
	histSM.Draw("hist")
	label = "SM"
	leg.AddEntry(histSM, "%s" %(label), "f")
    	print "Drawn", label

colorlist = [kBlue, kOrange, kRed, kMagenta, kGreen, kViolet, kSpring, kPink, kAzure, kBlue+4, kOrange+3, kRed+5, kMagenta+7]
labels = []
histClones = []
iset = 0
icolor = 0
i = 0
while iset < len(DATASET):
	#OUTTestSTest1p1Unp1500p0_spin-0_M_500-2000_py_GEN.root
	pattern = "OUTTestSTest%sUnp([^(]*)p0_spin-([^(]*)_M" %(dutag.replace(".", "p"))
	match = re.findall(pattern, DATASET[iset])
	LambdaU, spin = match[0]
    	label = "LambdaU = %s, spin-%s" %(LambdaU, spin)
    	labels.append(label)
    	tag = label
    	iset = iset + 1

while i < len(DATASET):
    histClone = uh[i].Clone("hist%s" %(labels[i]))
    histClone.Add(uh[i+1], 1.0)
    histClones.append(histClone)
    i = i + 2

j = 0
for histclone in histClones:
	histclone.SetLineColor(colorlist[icolor])
	histclone.Scale(intlumi)
	histclone.Draw(drawstyle)
	print labels[j], histclone.GetEntries()
    	leg.AddEntry(histclone, "%s" %(labels[j]), "l")

	j = j+2

    	icolor = icolor + 1
print tag

histSM.GetYaxis().SetTitle(ytitle)
histSM.GetYaxis().SetTitleOffset(1.0)
histSM.GetXaxis().SetTitle(xtitle)
histSM.GetXaxis().SetRangeUser(xmin, xmax)

leg.Draw()
set_CMS_lumi(canvas, 4, 11, intlumi)
canvas.Update()
canvas.Draw()
canvas.Print("Unparticles_du%s_spin0y2_%sfb-1_%s%s.pdf" %(dutag, intlumi,obj, xtratag))
