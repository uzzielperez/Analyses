#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from Sensitivityfunctions import CalcSensitivity
from Plotfunctions import *
from LambdaUcalc import xsecRatio
import argparse

parser = argparse.ArgumentParser(description="cmsDriver")
parser.add_argument("-a", "--action", default="s", help="s for signalonly. sb for signal+background.")
args = parser.parse_args()

action = args.action

sw = ROOT.TStopwatch()
sw.Start()

gStyle.SetOptStat(0)

#---- M > 2000 Test
print "Min_mgg = 2000"
DATASET2000 = []
DATASET2000.append("../MINisEBEB/OUTSM_pT70_m500_M2000.root")

#du = 1.9
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU2000p0_m500_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU6000p0_m2000_pT70_M2000.root")
#
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU2000p0_m500_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU3000p0_m500_pT70_M2000.root")
#
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU2500p0_m500_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU3000p0_m500_pT70_M2000.root")
#
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU3000p0_m500_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU5000p0_m500_pT70_M2000.root")
#
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU3000p0_m500_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU4000p0_m2000_pT70_M2000.root")
#
DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p1_LU2000p0_m2000_pT70_M2000.root")
DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p1_LU2500p0_m2000_pT70_M2000.root")

DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p1_LU2000p0_m2000_pT70_M2000.root")
DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p1_LU4000p0_m2000_pT70_M2000.root")

#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p1_LU2500p0_m2000_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p1_LU4000p0_m2000_pT70_M2000.root")

DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU2000p0_m2000_pT70_M2000.root")
DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU2500p0_m2000_pT70_M2000.root")

#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU2500p0_m2000_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU4000p0_m2000_pT70_M2000.root")

DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU2000p0_m2000_pT70_M2000.root")
DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p5_LU4000p0_m2000_pT70_M2000.root")

#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU2000p0_m2000_pT70_M2000.root")
#DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU2500p0_m2000_pT70_M2000.root")

DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU2500p0_m2000_pT70_M2000.root")
DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU4000p0_m2000_pT70_M2000.root")

DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU2000p0_m2000_pT70_M2000.root")
DATASET2000.append("../MINisEBEB/OUTUnp_spin2_du1p9_LU4000p0_m2000_pT70_M2000.root")

if action == "s":
	iset = 1
	while iset < len(DATASET2000):
		h1, label1 = createSignalOnly("gendiphotonMinv", DATASET2000[0], DATASET2000[iset])
		h2, label2 = createSignalOnly("gendiphotonMinv", DATASET2000[0], DATASET2000[iset+1])
		PlotRatio(h1, h2, label1, label2)
		iset = iset+2

if action == "sb":
	i = 1
	while i < len(DATASET2000):
		ha, labela = createHist("gendiphotonMinv", DATASET2000[i])
		hb, labelb = createHist("gendiphotonMinv", DATASET2000[i+1])
		print labela
		print labelb
		PlotRatio(ha, hb, labela, labelb)
		i = i + 2
