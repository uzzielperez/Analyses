#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivity
from hep_plt.Plotfunctions import *

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)

doSM = True
dospin0du1p5 = True
dospin0du1p1 = True
dospin0du1p9 = True

dospin2du1p1 = True
dospin2du1p5 = True
dospin2du1p9 = True

HISTS_TO_OVERLAY, labelList = [], []
TempHistsList, templabelList = [None]*4, [None]*4

def PlotSets():
    histA, labelA = Stitch(DATASET_A, "gendiphotonMinv")
    histB, labelB = Stitch(DATASET_B, "gendiphotonMinv")
    histC, labelC = Stitch(DATASET_C, "gendiphotonMinv")

    TempHistsList[1], templabelList[1] = histA, labelA
    TempHistsList[2], templabelList[2] = histB, labelB
    TempHistsList[3], templabelList[3] = histC, labelC

    HISTS_TO_OVERLAY.append(histA)
    HISTS_TO_OVERLAY.append(histB)
    HISTS_TO_OVERLAY.append(histC)

    labelList.append(labelA)
    labelList.append(labelB)
    labelList.append(labelC)

    # Calculate Sensitivity
    #CalcSensitivity("gendiphotonMinv", TempHistsList, 137, templabelList)
    # Plot Histograms (Overlay)
    OverlayHists("gendiphotonMinv", TempHistsList, templabelList)

if doSM:
    DATASETSM = []
    DATASETSM.append("../MCIisEBEB/OUTSM_pT70_M500_1000.root")
    DATASETSM.append("../MCIisEBEB/OUTSM_pT70_M1000_2000.root")
    DATASETSM.append("../MCIisEBEB/OUTSM_pT70_M2000_4000.root")
    DATASETSM.append("../MCIisEBEB/OUTSM_pT70_M4000.root")

    histSM, labelSM = Stitch(DATASETSM, "gendiphotonMinv")
    HISTS_TO_OVERLAY.append(histSM)
    labelList.append(labelSM)
    TempHistsList[0], templabelList[0] = histSM, labelSM
    print type(histSM)

if dospin2du1p1:
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU2000_pT70_M500_1000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU2000_pT70_M1000_2000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU2000_pT70_M2000.root")

    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3000_pT70_M500_1000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3000_pT70_M1000_2000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3000_pT70_M2000_3000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3000_pT70_M3000.root")

    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3500_pT70_M500_1000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3500_pT70_M1000_2000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3500_pT70_M2000_3500.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU3500_pT70_M3500.root")
    PlotSets()
if dospin2du1p5:
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU2000_pT70_M500_1000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU2000_pT70_M1000_2000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU2000_pT70_M2000.root")

    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU2500_pT70_M500_1000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU2500_pT70_M1000_2500.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU2500_pT70_M2500.root")

    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU3000_pT70_M500_1000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU3000_pT70_M1000_2000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU3000_pT70_M2000_3000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p5_LU3000_pT70_M3000.root")
    PlotSets()
if dospin2du1p9:
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU2000_pT70_M500_1000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU2000_pT70_M1000_2000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU2000_pT70_M2000.root")

    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU2500_pT70_M500_1000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU2500_pT70_M1000_2500.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU2500_pT70_M2500.root")

    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU3500_pT70_M500_1000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU3500_pT70_M1000_2000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU3500_pT70_M2000_3500.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin2_du1p9_LU3500_pT70_M3500.root")
    PlotSets()
if dospin0du1p5:
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU2000_pT70_M500_1000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU2000_pT70_M1000_2000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU2000_pT70_M2000.root")

    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU2500_pT70_M500_1000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU2500_pT70_M1000_2500.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU2500_pT70_M2500.root")

    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU3500_pT70_M500_1000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU3500_pT70_M1000_2000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU3500_pT70_M2000_3500.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p5_LU3500_pT70_M3500.root")
    PlotSets()
if dospin0du1p1:
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU4000_pT70_M500_1000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU4000_pT70_M1000_2000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU4000_pT70_M2000_4000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU4000_pT70_M4000.root")

    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU8000_pT70_M500_1000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU8000_pT70_M1000_2000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU8000_pT70_M2000_4000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU8000_pT70_M4000.root")

    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU9500_pT70_M500_1000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU9500_pT70_M1000_2000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU9500_pT70_M2000_4000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p1_LU9500_pT70_M4000.root")
    PlotSets()
if dospin0du1p9:
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU2000_pT70_M500_1000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU2000_pT70_M1000_2000.root")
    DATASET_A.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU2000_pT70_M2000.root")

    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU2500_pT70_M500_1000.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU2500_pT70_M1000_2500.root")
    DATASET_B.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU2500_pT70_M2500.root")

    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU3500_pT70_M500_1000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU3500_pT70_M1000_2000.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU3500_pT70_M2000_3500.root")
    DATASET_C.append("../MCIisEBEB/OUTUnp_spin0_du1p9_LU3500_pT70_M3500.root")
    PlotSets()

CalcSensitivity("gendiphotonMinv", HISTS_TO_OVERLAY, 137, labelList)
