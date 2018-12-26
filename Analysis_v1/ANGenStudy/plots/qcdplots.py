#!/usr/bin/python
import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
#from ROOT import kBlack, kBlue, kRed, kGreen, kMagenta, kCyan, kOrange, kViolet, kSpring
from ROOT import kBlue, kOrange, kCyan, kRed, kMagenta, kGreen, kViolet, kSpring, kPink, kAzure
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
#from legend import *
#from plotsHelpercomp import *
import re
from Plotfunctions import PlotDatasets

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


obj = "gendiphotonMinv"
#obj = "gendiphotoncosthetastar"
#obj = "genchidiphoton"
#obj = "genphoton1Eta"
#obj = "genphoton2Eta"


DATASET_qcd = []
DATASET_qcd.append("../qcdtest/OUTgg2qqbar.root")
DATASET_qcd.append("../qcdtest/OUTqqbar2gg.root")

# Draw Options
DrawAsHi = False
gStyle.SetOptStat(0)

PlotDatasets("genchidiphoton", DATASET_qcd)
PlotDatasets("genchidiphoton", DATASET_qcd)
