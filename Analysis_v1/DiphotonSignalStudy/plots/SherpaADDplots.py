#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivityADD
from hep_plt.Plotfunctions import *
import argparse

# Command line options
parser = argparse.ArgumentParser(description="NonResonance")
parser.add_argument("-p", "--plot", action="store_true", help="Clean directory and delete copied files")
parser.add_argument("-s", "--sensitivity", action="store_true", help="Run os.system(cmd) to get CRAB files.")
args = parser.parse_args()

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)


# To suppress canvas from popping up. Speeds up plots production.
gROOT.SetBatch()

doSM  = True
doADD = True

# Variables to Plot
kinematicsON = True
genON        = False
angularON    = False 

isEBEB       = False

obj = []
if kinematicsON:
        obj.append("diphotonMinv")
#        obj.append("photon1Pt")
#        obj.append("photon2Pt")
#        obj.append("photon1Eta")
#        obj.append("photon2Eta")
#       	obj.append("photon1Phi")
#        obj.append("photon2Phi")
	if isEBEB:
		obj.append("diphotonMinvisEBEB")
if angularON:
        obj.append("chidiphoton")
        obj.append("diphotoncosthetastar")
	if isEBEB:
		obj.append("chidiphotonisEBEB")
		obj.append("diphotoncosthetastarisEBEB")
if genON:
        obj.append("gendiphotonMinv")
#        obj.append("genphoton1Pt")
#        obj.append("genphoton2Pt")
#        obj.append("genphoton1Eta")
#        obj.append("genphoton2Eta")
#        obj.append("genphoton1Phi")
#        obj.append("genphoton2Phi")
        if angularON:
                obj.append("genchidiphoton")
                obj.append("gendiphotoncosthetastar")

if doSM:
        DATASETSM = []
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_500To1000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_1000To2000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_2000To4000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_4000To6000_Pt_50.root")
        DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_6000To8000_Pt_50.root")
        varhistsm = [Stitch(DATASETSM, var) for var in obj]
        #for var, histl in zip(obj, varhistsm):
            #histSM, label = histl
            #print var, label
if doADD:
    signal = []
    DATASET_A, DATASET_B, DATASET_C = [], [], []
    DATASET_A.append("../NonResonanceTemplates/OUTADDGravToGG_MS_4000_NED_4_KK_1_M_1000To2000.root")
    DATASET_A.append("../NonResonanceTemplates/OUTADDGravToGG_MS_4000_NED_4_KK_1_M_2000To4000.root")
    DATASET_A.append("../NonResonanceTemplates/OUTADDGravToGG_MS_4000_NED_4_KK_1_M_200To500.root")
    DATASET_A.append("../NonResonanceTemplates/OUTADDGravToGG_MS_4000_NED_4_KK_1_M_500To1000.root")
    sigA = [Stitch(DATASET_A, var) for var in obj]

    DATASET_B.append("../NonResonanceTemplates/OUTADDGravToGG_MS_8000_NED_4_KK_1_M_1000To2000.root")
    DATASET_B.append("../NonResonanceTemplates/OUTADDGravToGG_MS_8000_NED_4_KK_1_M_2000To4000.root")
    DATASET_B.append("../NonResonanceTemplates/OUTADDGravToGG_MS_8000_NED_4_KK_1_M_4000To8000.root")
    DATASET_B.append("../NonResonanceTemplates/OUTADDGravToGG_MS_8000_NED_4_KK_1_M_500To1000.root")
    sigB = [Stitch(DATASET_B, var) for var in obj]

    DATASET_C.append("../NonResonanceTemplates/OUTADDGravToGG_MS_10000_NED_4_KK_1_M_1000To2000.root")
    DATASET_C.append("../NonResonanceTemplates/OUTADDGravToGG_MS_10000_NED_4_KK_1_M_2000To4000.root")
    DATASET_C.append("../NonResonanceTemplates/OUTADDGravToGG_MS_10000_NED_4_KK_1_M_4000To10000.root")
    DATASET_C.append("../NonResonanceTemplates/OUTADDGravToGG_MS_10000_NED_4_KK_1_M_500To1000.root")
    sigC = [Stitch(DATASET_C, var) for var in obj]

    #for var, histl in zip(obj, sigC):
	#hist, label = histl
	#print var, label
    signal.append(sigA)
    signal.append(sigB)
    signal.append(sigC)

ipts, ivar = 0, 0 #signal[modelptindex][varindex][hist(0)/label(1)]
for var, sm in zip(obj, varhistsm):
	# New stack for each variable
	hstack, labels = [], []
	hstack.append(sm[0])
	labels.append(sm[1])
	for sig in signal:
		#print sig[ivar][1]
		hstack.append(sig[ivar][0])
		labels.append(sig[ivar][1])
	#print labels
	ivar = ivar + 1

	# Plots
	if args.plot:
	       OverlayHists(var, hstack, labels, tag="sherpa", lumi=137)

    	if args.sensitivity:
		if "Minv" in var or "chidiphoton" in var or "costhetastar" in var:
			#CalcSensitivityADD(var, hstack, labels, lumi=137, McutList=mcuts)
			CalcSensitivityADD(var, hstack, labels, lumi=137)
    #PlotSets()
