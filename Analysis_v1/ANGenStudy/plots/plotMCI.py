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
from MCIStitchFunctions import PlotDatasets

sw = ROOT.TStopwatch()
sw.Start()

dospin0 = False
dospin2 = False
dospin2varLambda = False
dospin0varLambda = False
dospincomp = True
doOTHERS = False


DATASET = []
ptag = "M1000"
if dospin0:
   ptag = ptag + "Unpspin0"
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p5_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p5_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p6_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p6_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p8_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p8_spin0_M2000.root")
   PlotDatasets("gendiphotonMinv", DATASET)
   PlotDatasets("gendiphotoncosthetastar", DATASET)
   PlotDatasets("genchidiphoton", DATASET)
   PlotDatasets("genphoton1Pt", DATASET)
   PlotDatasets("genphoton2Pt", DATASET)
   PlotDatasets("genphoton1Eta", DATASET)
   PlotDatasets("genphoton2Eta", DATASET)
if dospin2:
   ptag = ptag + "Unpspin1"
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p5_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p5_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p6_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p6_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p8_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p8_spin2_M2000.root")

   PlotDatasets("gendiphotonMinv", DATASET)
   PlotDatasets("gendiphotoncosthetastar", DATASET)
   PlotDatasets("genchidiphoton", DATASET)
   PlotDatasets("genphoton1Pt", DATASET)
   PlotDatasets("genphoton2Pt", DATASET)
   PlotDatasets("genphoton1Eta", DATASET)
   PlotDatasets("genphoton2Eta", DATASET)
if dospin2varLambda:
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p1_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p1_spin2_M2000.root")
   PlotDatasets("gendiphotonMinv", DATASET)
   PlotDatasets("gendiphotoncosthetastar", DATASET)
   PlotDatasets("genchidiphoton", DATASET)
   PlotDatasets("genphoton1Pt", DATASET)
   PlotDatasets("genphoton2Pt", DATASET)
   PlotDatasets("genphoton1Eta", DATASET)
   PlotDatasets("genphoton2Eta", DATASET)

if dospin0varLambda:
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU2000_du1p1_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p1_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p1_spin0_M2000.root")
   PlotDatasets("gendiphotonMinv", DATASET)
   PlotDatasets("gendiphotoncosthetastar", DATASET)
   PlotDatasets("genchidiphoton", DATASET)
   PlotDatasets("genphoton1Pt", DATASET)
   PlotDatasets("genphoton2Pt", DATASET)
   PlotDatasets("genphoton1Eta", DATASET)
   PlotDatasets("genphoton2Eta", DATASET)
if dospincomp:
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU1000_du1p1_spin2_M2000.root")

   PlotDatasets("gendiphotonMinv", DATASET)
   PlotDatasets("gendiphotoncosthetastar", DATASET)
   PlotDatasets("genchidiphoton", DATASET)
   PlotDatasets("genphoton1Pt", DATASET)
   PlotDatasets("genphoton2Pt", DATASET)
   PlotDatasets("genphoton1Eta", DATASET)
   PlotDatasets("genphoton2Eta", DATASET)

if doOTHERS:

   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p1_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p5_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p5_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p6_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p6_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p8_spin2_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p8_spin2_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p1_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p1_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p5_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p5_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p6_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p6_spin0_M500_2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p8_spin0_M2000.root")
   DATASET.append("../EBEBEBEEEEE/OUTLU5000_du1p8_spin0_M500_2000.root")


#dulabel = r"d_{u} = %s" %(dutag)
# Draw Options
DrawAsHist = False
gStyle.SetOptStat(0)
