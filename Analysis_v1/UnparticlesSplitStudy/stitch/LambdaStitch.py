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

#du_tag = "1p01"
Lambda_tag = "3000"

SM = True
UNP = True

tag = "b"

zoom = False
#drawstyle = "hist, same"
drawstyle = "same"

intlumi = 130

BKG = []
BKG.append("../Unparticles_SM_M_500-2000.root")
BKG.append("../Unparticles_SM_M-2000.root")

DATASET = []
DATASET.append("../TestSTest1p01Unp%sp0_M_2000.root" %(Lambda_tag))
DATASET.append("../TestSTest1p01Unp%sp0_M_500-2000.root" %(Lambda_tag))
DATASET.append("../TestSTest1p1Unp%sp0_M_2000.root" %(Lambda_tag))
DATASET.append("../TestSTest1p1Unp%sp0_M_500-2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p2_LambdaU-%sp0_M_2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p2_LambdaU-%sp0_M_500-2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p3_LambdaU_%s_M_2000_py_GEN.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p3_LambdaU_%s_M_500-2000_py_GEN.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p4_LambdaU_%s_M_2000_py_GEN.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p4_LambdaU_%s_M_500-2000_py_GEN.root" %(Lambda_tag))
DATASET.append("../TestSTest1p5Unp%sp0_M_2000.root" %(Lambda_tag))
DATASET.append("../TestSTest1p5Unp%sp0_M_500-2000.root" %(Lambda_tag))
DATASET.append("../TestSTest1p6Unp%sp0_M_2000.root" %(Lambda_tag))
DATASET.append("../TestSTest1p6Unp%sp0_M_500-2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p7_LambdaU_%sp0_M_2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p7_LambdaU_%sp0_M_500-2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p8_LambdaU_%s_M_2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p8_LambdaU_%s_M_500-2000.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p9_LambdaU_%s_M_2000_py_GEN.root" %(Lambda_tag))
DATASET.append("../Unparticles_du1p9_LambdaU_%s_M_500-2000_py_GEN.root" %(Lambda_tag))
# Unparticles_1p8_LambdaU_%s_M_2000.root
# Unparticles_1p8_LambdaU_%s_M_500-2000.root
#DATASET.append("../Unparticles_du1p8_LambdaU_1000_M_500-2000.root")
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
	xmin, xmax = 500, 2500
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
	histSM = bkgh[0].Clone("histSM")
	histSM.Add(bkgh[1], 1.0)
	histSM.SetFillStyle(3144)
	histSM.SetFillColor(7)
	histSM.Scale(intlumi)
	histSM.Draw("hist")
	label = "SM"
	leg.AddEntry(histSM, "%s" %(label), "f")
    	print "Drawn", label

colorlist = [kBlue, kOrange, kCyan, kRed, kMagenta, kGreen, kViolet, kSpring, kPink, kAzure]
labels = []
histClones = []
iset = 0
icolor = 0
i = 0
while iset < len(DATASET):
    pattern1 = r'Unparticles_du([^(]*).root'
    pattern2 = r"TestSTest([^(]*).root"
    label1 = re.findall(pattern1, DATASET[iset])
    label2 = re.findall(pattern2, DATASET[iset])
    if not label1:
	#then it is empty. choose label2
	pattern = r'([^(]*)Unp'
	label = re.findall(pattern, label2[0])[0]
  	#print "label2: ", label
    if not label2:
	pattern = r'([^(]*)_LambdaU'
	label = re.findall(pattern, label1[0])[0]
	#print "label1: ", label
    labels.append(label)
    tag = tag + label
    #histClone.delete
    iset = iset + 1

while i < len(DATASET):
    histClone = uh[i].Clone("histdu%s" %(labels[i]))
    histClone.Add(uh[i+1], 1.0)
    histClones.append(histClone)

     #histClones.append(histClone)
    #histClone.SetLineColor(colorlist[icolor])
    #histClone.Scale(intlumi)
    #histClone.Draw(drawstyle)
    #print labels[i]
    #leglabel = r"du = %s, #Lambda_{U} = %s" %(labels[i])
    #leg.AddEntry(histClone, "%s" %(leglabel), "l")
    i = i + 2

j = 0
for histclone in histClones:
	histclone.SetLineColor(colorlist[icolor])
	histclone.Scale(intlumi)
	histclone.Draw(drawstyle)
	print labels[j]
	leglabel = r"du = %s, #Lambda_{U} = %s" %(labels[j], Lambda_tag)
    	leg.AddEntry(histclone, "%s" %(leglabel), "l")

	j = j+2

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
canvas.Print("LOG%s_Unparticles_LambdaU_%sfb-1_%s%s.pdf" %(intlumi, Lambda_tag, obj,tag))
