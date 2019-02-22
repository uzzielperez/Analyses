#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivity
from hep_plt.Plotfunctions import *

gStyle.SetOptStat(0)

W2_M750 = True

obj = "diphotonMinv"
#obj = "photon1Pt"
#obj = "photon2Pt"
#obj = "photon1Eta"
#obj = "photon2Eta"
#obj = "photon1Phi"
#obj = "photon2Phi"

DATASET = []

if W2_M750:
	tag = "kMpl02_750_1250"
	(xpos1, ypos1, xpos2, ypos2) = .55, 0.68, .85, .88
	(xmin, xmax) = 300, 2000
	#DATASET.append("RSG_SM_py_GEN.root")
	#DATASET.append("../ResonanceTemplates/OUTRSGravitonToGammaGamma_kMpl001_M_750.root")
        DATASET.append("../ResonanceTemplates/OUTGluGluSpin0ToGammaGamma_W_0p014_M_750.root")

OverlayResonances(obj, DATASET, (xpos1, ypos1, xpos2, ypos2), (xmin, xmax))
