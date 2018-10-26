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

du1p5BASE= False
du1p01 = False
du1p1 = False
du1p2 = False
du1p3 = False
du1p4 = False
du1p6 = False
du1p7 = True
du1p8 = False 
du1p9 = False

#Ufile1 = "../Unparticles_du1p5_LambdaU-1000_TuneCUEP8M1_13TeV.root"
#Ufile2 = "../Unparticles_du1p5_LambdaU-800_TuneCUEP8M1_13TeV.root"
#Ufile3 = "../Unparticles_du1p5_LambdaU-2000_TuneCUEP8M1_13TeV.root"
#Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"
#

if du1p5BASE:
	tag = "du1p5"
	print tag
	Ufile1 = "../Unparticles_du1p5_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p5_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p5_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"
if du1p01:
	tag = "du1p01"	
	print tag
	Ufile1 = "../Unparticles_du1p01_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p01_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p01_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"
if du1p1:
	tag = "du1p1"
	print tag
	Ufile1 = "../Unparticles_du1p1_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p1_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p1_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"
if du1p2:
	tag = "du1p2"
	print tag
	Ufile1 = "../Unparticles_du1p2_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p2_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p2_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"

if du1p3:
	tag = "du1p3"
	print tag
	Ufile1 = "../Unparticles_du1p3_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p3_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p3_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"

if du1p4:
	tag = "du1p4"
	print tag
	Ufile1 = "../Unparticles_du1p4_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p4_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p4_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"

if du1p6:
	tag = "du1p6"
	print tag
	Ufile1 = "../Unparticles_du1p6_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p6_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p6_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"

if du1p7:
	tag = "du1p7"
	print tag
	Ufile1 = "../Unparticles_du1p7_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p7_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p7_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"

if du1p8:
	tag = "du1p8"
	print tag
	Ufile1 = "../Unparticles_du1p8_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p8_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p8_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"

if du1p9:
	tag = "du1p9"
	print tag
	Ufile1 = "../Unparticles_du1p9_LambdaU-1000_TuneCUEP8M1_13TeV.root"
	Ufile2 = "../Unparticles_du1p9_LambdaU-800_TuneCUEP8M1_13TeV.root"
	Ufile3 = "../Unparticles_du1p9_LambdaU-2000_TuneCUEP8M1_13TeV.root"
	Ufile4 = "../Unparticles_SM_TuneCUEP8M1_13TeV.root"


# Draw Options
DrawAsHist = False
gStyle.SetOptStat(0)

# Timer
sw = ROOT.TStopwatch()
sw.Start()


uf1 = ROOT.TFile(Ufile1, "READ")
uf2 = ROOT.TFile(Ufile2, "READ")
uf3 = ROOT.TFile(Ufile3, "READ")
uf4 = ROOT.TFile(Ufile4, "READ")

canvas = ROOT.TCanvas()
#canvas.SetLogy()
obj = "gendiphotonMinv"
uh1 = uf1.Get(obj)
uh2 = uf2.Get(obj)
uh3 = uf3.Get(obj)
uh4 = uf4.Get(obj)

uh1.SetLineColor(1) 
uh2.SetLineColor(2)
uh3.SetLineColor(3) 
uh4.SetLineColor(4)
#uh4.SetLineColor(7)
uh4.SetFillColor(7)
#uh4.SetFillColorAlpha(7, 0.8)
#uh4.SetFillStyle(3944)

xtitle = r"m_{#gamma#gamma}#scale[1.0]{(GeV)}"
xmin, xmax = 300, 4000
ytitle = r"#scale[0.8]{weighted events}"

eventsmaxlist = []
#eventsminlist = []
eventsmaxlist.append(uh1.GetMaximum())
eventsmaxlist.append(uh2.GetMaximum())
eventsmaxlist.append(uh3.GetMaximum())
eventsmaxlist.append(uh4.GetMaximum())
#eventsminlist.append(uh1.GetMinimum())
#eventsminlist.append(uh2.GetMinimum())
#eventsminlist.append(uh3.GetMinimum())
#eventsminlist.append(uh4.GetMinimum())

uh1.GetYaxis().SetTitle(ytitle)
uh1.GetYaxis().SetTitleOffset(1.0)
uh1.GetXaxis().SetTitle(xtitle)
uh1.GetYaxis().SetRangeUser(10**-5, max(eventsmaxlist))
uh1.GetXaxis().SetRangeUser(xmin, xmax)

uh1.Draw("hist")
uh2.Draw("hist, same")
uh3.Draw("hist, same")
uh4.Draw("hist, same")

xpos1, ypos1, xpos2, ypos2 = .50, 0.78, .85, .88

leg = TLegend(xpos1, ypos1, xpos2, ypos2)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)

pattern = r'Unparticles_([^(]*)_TuneCUEP8M1_13TeV.root'
leg.AddEntry(uh2, "%s" %(re.findall(pattern, Ufile2)[0]), "l")
leg.AddEntry(uh1, "%s" %(re.findall(pattern, Ufile1)[0]) ,"l")
leg.AddEntry(uh3, "%s" %(re.findall(pattern, Ufile3)[0]), "l")
leg.AddEntry(uh4, "%s" %(re.findall(pattern, Ufile4)[0]), "l")
leg.Draw()

set_CMS_lumi(canvas, 4, 11, "1")
canvas.Update()
canvas.Draw()
canvas.Print("Unparticles_%s%s.pdf" %(obj,tag))
canvas.SetLogy()
canvas.Update()
canvas.Draw()
canvas.Print("LOGUnparticles_%s%s.pdf" %(obj,tag))
