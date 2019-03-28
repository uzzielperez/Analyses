#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivityADD
from hep_plt.Plotfunctions import *
import argparse

# Command line options
parser = argparse.ArgumentParser(description="NonResonance")
parser.add_argument("-p", "--plot", action="store_true", help="Plot")
parser.add_argument("-b", "--background", action="store_true", help="If overlay Standard Model Background")
parser.add_argument("-s", "--sensitivity", action="store_true", help="Compute Sensitivity")
#parser.add_argument("-lt", "--LambdaT", default=[6], nargs='*', help="List of LambdaTs")
parser.add_argument("-lt", '--LambdaT', default=[6], nargs='+', type=float)
args = parser.parse_args()

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)


# To suppress canvas from popping up. Speeds up plots production.
gROOT.SetBatch()
tag = "b"

# SM
doSM 	   = True
GGPythia17 = True
GGPythia18 = False

# ADD
doADD         = True
doPythia      = True
doNegInt1     = True  # GRw
doNegInt0     = False # Hewett -
doSherpa      = False

# Variables to Plot
kinematicsON = False
angularON    = True

isEBEB       = False

obj = []
obj.append("gendiphotonMinv")
if kinematicsON:
        obj.append("genphoton1Pt")
        obj.append("genphoton2Pt")
        obj.append("genphoton1Eta")
        obj.append("genphoton2Eta")
        obj.append("genphoton1Phi")
        obj.append("genphoton2Phi")
if angularON:
        obj.append("genchidiphoton")
        obj.append("gendiphotoncosthetastar")


if doSM:
        DATASETSM = []
        if GGPythia17:
            smls = []
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_1000To2000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_2000To4000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_4000To6000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_6000To8000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_8000To13000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            smhi = [Stitch(DATASETSM, var) for var in obj]
        if GGPythia18:
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_1000To2000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_2000To4000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_4000To6000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_6000To8000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_8000To13000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            smhi = [Stitch(DATASETSM, var) for var in obj]
if doADD:
	signal = []
	if doPythia:
	    tag = tag + "pythia"
        if doNegInt1:
                DATASETS = []

                if 6 in args.LambdaT:
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

                if 8 in args.LambdaT:
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_4000To8000.root')
                    #DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

                if 10 in args.LambdaT:
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_4000To10000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

        elif doNegInt0:
                DATASETS = []
                if 6 in args.LambdaT:
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_6000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_6000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_6000_M_4000To6000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_6000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

                if 8 in args.LambdaT:
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_8000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_8000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_8000_M_4000To8000.root')
                    #DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_8000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

                if 10 in args.LambdaT:
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

ipts, ivar = 0, 0 #signal[modelptindex][varindex][hist(0)/label(1)]
for var, sm in zip(obj, smhi):
	
	# New stack for each variable
	hstack, labels = [], []
	hstack.append(sm[0])
	labels.append(sm[1])
	
	#print hstack, var, labels
	
	for sig in signal:
		hstack.append(sig[ivar][0])
		labels.append(sig[ivar][1])
	ivar = ivar + 1

	if args.plot:
           if args.background:
          	OverlayHists(var, hstack, labels, tag=tag, lumi=137, Background="Y", Mrange=(500,13000))
    	   
	   else:
	   	OverlayHists(var, hstack, labels, tag=tag, lumi=137, Mrange=(500,10000))
	
	if args.sensitivity:
		if "Minv" in var or "chidiphoton" in var or "costhetastar" in var:
			CalcSensitivityADD(var, hstack, labels, lumi=137)
            		#CalcSensitivityADD(var, hstack, labels, lumi=137, McutList=['2000'], chiMax=3.0)
