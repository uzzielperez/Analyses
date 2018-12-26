#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from Sensitivityfuncs import CalcSensitivity
from Plotfunctions import *

sw = ROOT.TStopwatch()
sw.Start()

gStyle.SetOptStat(0)

#---- M > 2000 Test
DATASET2000 = []
DATASET2000.append("../isEBEB/OUTSM_M2000.root")
#DATASET2000.append("../isEBEB/OUTUnp_LU2500_du1p9_spin2_ggONM2000.root")
#DATASET2000.append("../isEBEB/OUTUnp_LU4000_du1p9_spin2_ggONM2000.root")
#DATASET2000.append("../isEBEB/OUTUnp_LU4500_du1p9_spin2_ggONM2000.root")

#CalcSensitivity("gendiphotonMinv", DATASET2000, 35.9)
#CalcSensitivity("gendiphotonMinv", DATASET2000, 137)
#PlotDatasets("gendiphotonMinv", DATASET2000)
#h1, matchlabel1 = createSignalOnly("gendiphotonMinv", DATASET2000[0], DATASET2000[1])
#h2, matchlabel2 = createSignalOnly("gendiphotonMinv", DATASET2000[0], DATASET2000[2])
#print type(h1), type(h2)
#PlotRatio(h1, h2, matchlabel1, matchlabel2)

#----- M > 2000 Test,

#DATASET2000.append("../isEBEB/OUTUnp_LU3000_du1p1_spin2_ggONM2000.root")
#DATASET2000.append("../isEBEB/OUTUnp_LU3750_du1p1_spin2_ggONM2000.root")
#DATASET2000.append("../isEBEB/OUTUnp_LU4250_du1p1_spin2_ggONM2000.root")

#DATASET2000.append("../isEBEB/OUTUnp_LU3000_du1p4_spin2_ggONM2000.root")
#DATASET2000.append("../isEBEB/OUTUnp_LU3500_du1p4_spin2_ggONM2000.root")

DATASET2000.append("../isEBEB/OUTUnp_LU4000_du1p8_spin2_ggONM2000.root")
#DATASET2000.append("../isEBEB/OUTUnp_LU5000_du1p8_spin2_ggONM1500.root")

DATASET2000.append("../isEBEB/OUTUnp_LU4000_du1p5_spin2_ggONM2000.root")



#CalcSensitivity("gendiphotonMinv", DATASET2000, 35.9)
CalcSensitivity("gendiphotonMinv", DATASET2000, 137)
#PlotDatasets("gendiphotonMinv", DATASET2000)

#h1, matchlabel1 = createSignalOnly("gendiphotonMinv", DATASET2000[0], DATASET2000[1])
#h2, matchlabel2 = createSignalOnly("gendiphotonMinv", DATASET2000[0], DATASET2000[2])
#print type(h1), type(h2)
#PlotRatio(h1, h2, matchlabel1, matchlabel2)


#---- M > 1500 Test
DATASET1500 = []
#DATASET1500.append("../isEBEB/OUTSM_M1500.root")
#DATASET1500.append("../isEBEB/OUTUnp_LU4500_du1p01_spin2_ggONM1500.root")
#DATASET1500.append("../isEBEB/OUTUnp_LU4750_du1p01_spin2_ggONM1500.root")
#DATASET1500.append("../isEBEB/OUTUnp_LU5000_du1p01_spin2_ggONM1500.root")
#DATASET1500.append("../isEBEB/OUTUnp_LU1500_du1p8_spin2_ggONM1500.root")
#DATASET1500.append("../isEBEB/OUTUnp_LU4500_du1p9_spin2_ggONM1500.root")
#DATASET1500.append("../isEBEB/OUTLU5000_du1p1_spin2_M2000.root")
#DATASET1500.append("../isEBEB/OUTUnp_LU1500_du1p8_spin0_ggffONM1500.root")

#CalcSensitivity("gendiphotonMinv", DATASET1500, 35.9)
#CalcSensitivity("gendiphotonMinv", DATASET1500, 137)
#PlotDatasets("gendiphotonMinv", DATASET1500)

#-----------------------------------------
#PlotSignalOnly("gendiphotonMinv", DATASET1500[0], DATASET[1])
#PlotSignalOnly(ROOT.TFile(DATASET1500[0], "READ").openfile.Get("gendiphotonMinv"), ROOT.TFile(DATASET1500[2], "READ")openfile.Get("gendiphotonMinv"))
#PlotSignalOnly("gendiphotonMinv", DATASET1500[0], DATASET1500[1])

#PlotDatasets("gendiphotoncosthetastar", DATASET1500)
#PlotDatasets("genchidiphoton", DATASET1500)
#PlotDatasets("genphoton1Pt", DATASET1500)
#PlotDatasets("genphoton2Pt", DATASET1500)
#PlotDatasets("genphoton1Eta", DATASET1500)
#PlotDatasets("genphoton2Eta", DATASET1500)
