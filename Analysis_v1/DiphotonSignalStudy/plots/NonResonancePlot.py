#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivity
from hep_plt.Plotfunctions import *

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)

doSMstitch = False
doADDstitch= False
doADD      = False 
doHH       = True
doRSG 	   = True

HISTS_TO_OVERLAY, labelList = [], []
TempHistsList, templabelList = [None]*4, [None]*4

def PlotSets(DATASET_LIST, obj):
    i = 1
    for dset in DATASET_LIST:
        hist, label = Stitch(dset, obj)
        TempHistsList[i], templabelList[i] = hist, label
        i = i + 1
        HISTS_TO_OVERLAY.append(hist)
        labelList.append(label)
    # Calculate Sensitivity
    #CalcSensitivity("gendiphotonMinv", TempHistsList, 137, templabelList)
    # Plot Histograms (Overlay)
    OverlayHists(obj, TempHistsList, templabelList)

if doSMstitch:
    DATASETSM = []
    DATASETSM.append("../mkClassTemplate/OUTSM_pT70_M500_1000.root")
    DATASETSM.append("../mkClassTemplate/OUTSM_pT70_M1000_2000.root")
    #DATASETSM.append("../mkClassTemplate/OUTSM_pT70_M2000_4000.root")
    #DATASETSM.append("../mkClassTemplate/OUTSM_pT70_M4000.root")

    histSM, labelSM = Stitch(DATASETSM, "gendiphotonMinv")
    HISTS_TO_OVERLAY.append(histSM)
    labelList.append(labelSM)
    TempHistsList[0], templabelList[0] = histSM, labelSM
    print type(histSM)

if doADDstitch:
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    # DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU2000_pT70_M500_1000.root")
    # DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU2000_pT70_M1000_2000.root")
    # DATASET_A.append("../MCIisEBEB/OUTUnp_spin2_du1p1_LU2000_pT70_M2000.root")
    DSETLIST = [DATASET_A, DATASET_B, DATASET_C]
    PlotSets(DSETLIST, "gendiphotonMinv")

obj = "gendiphotonMinv"

if doADD: 
	histADD, labelADD = createHist("gendiphotonMinv", "../mkClassTemplate/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_2000To4000.root" )
	HISTS_TO_OVERLAY.append(histADD)
	labelList.append(labelADD)

if doHH:
	histHH, labelHH = createHist(obj, "../mkClassTemplate/OUTGluGluSpin0ToGammaGamma_W_0p014_M_750.root")
	HISTS_TO_OVERLAY.append(histHH)
	labelList.append(labelHH)

if doRSG:
	histRSG, labelRSG = createHist(obj, "../mkClassTemplate/OUTRSGravitonToGammaGamma_kMpl001_M_750.root")
	HISTS_TO_OVERLAY.append(histRSG)
	labelList.append(labelRSG)

OverlayHists("gendiphotonMinv", HISTS_TO_OVERLAY, labelList)

#OverlayHists("gendiphotonMinv", HISTS_TO_OVERLAY, labelList)
#OUTADDGravToGG_NegInt_0_LambdaT_10000_M_2000To4000.root
#CalcSensitivity("gendiphotonMinv", HISTS_TO_OVERLAY, 137, labelList)
