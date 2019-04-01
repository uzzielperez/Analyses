#!/usr/bin/python

import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import *
from hep_plt.Plotfunctions import *
import argparse

# Command line options
parser = argparse.ArgumentParser(description="NonResonance")
parser.add_argument("--setbatch", action="store_true", help="Set this flag if you want quick plots saving.")
parser.add_argument("-p", "--plot", action="store_true", help="Plot")
parser.add_argument("-b", "--background", action="store_true", help="If overlay Standard Model Background")
parser.add_argument("-s", "--sensitivity", action="store_true", help="Compute Sensitivity")
#parser.add_argument("-lt", "--LambdaT", default=[6], nargs='*', help="List of LambdaTs")
parser.add_argument("-lt", '--LambdaT', default=[6], nargs='+', type=float)
parser.add_argument("-av", '--allvar', action="store_true")
parser.add_argument("-m", "--minv", action="store_true")
parser.add_argument("-cd", "--chidiphoton", action="store_true")
parser.add_argument("-cs", "--costhetastar", action="store_true")
parser.add_argument("-ds", "--drawassignal", action="store_true")
parser.add_argument("-min", "--minvalue", default=500)
parser.add_argument("--chimax", default=20)
parser.add_argument("--tag", default=None)
parser.add_argument("--isolate", action="store_true")
parser.add_argument("--negint1", action="store_true")
parser.add_argument("--negint1dense", action="store_true")


args = parser.parse_args()

sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)


# To suppress canvas from popping up. Speeds up plots production.
if args.setbatch:
	gROOT.SetBatch()
tag = "b"

# SM
doSM 	   = True
GGJets     = False
GGPythia17 = True
GGPythia18 = False

# ADD
doADD         = True
doPythia      = True
doNegInt1     = args.negint1  # GRw
doNegInt0     = False # Hewett -
doNegInt1Dense = args.negint1dense
doSherpa      = False

# Variables to Plot
kinematicsON = False
angularON    = False

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

if args.minv:
	var = "gendiphotonMinv"
elif args.chidiphoton:
	var = "genchidiphoton"
elif args.costhetastar:
	var = "gendiphotoncosthetastar"
else:
	var = "gendiphotonMinv"

signal, signalstack = [], []
labels = []
minx = float(args.minvalue)
chiMax = float(args.chimax)
print "Applying cuts mgg: ", minx,  "chidiphoton: 0-20"
print "Including LambdaT:", args.LambdaT

if doSM:
        DATASETSM = []
        if GGJets:
            tag = "GGJets"
            smls = []
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_60To200.root")
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_200To500.root")
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_500To1000.root")
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_1000To2000.root")
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_2000To4000.root")
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_4000To6000.root")
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_6000To8000.root")
            DATASETSM.append("../NonResonanceTemplates/OUTGGJets_M_8000To13000.root")
            if args.allvar:
       		smhi = [Stitch(DATASETSM, var) for var in obj]
            else:
        	smhi, label = Stitch(DATASETSM, var)
            	if args.background:
        		signalstack.append(smhi)
        		labels.append(label)
        if GGPythia17:
	    tag = "GG17"
            smls = []
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_500To1000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_1000To2000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_2000To4000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_4000To6000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_6000To8000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_8000To13000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")

	    # Implement Invariance mass cuts
	    if minx == 1000:
		DATASETSM.pop(0)
            if minx == 2000:
		DATASETSM.pop(0)
		DATASETSM.pop(0)

            # Stitching
	    if args.allvar:
	    	smhi = [Stitch(DATASETSM, var) for var in obj]
	    else:
		smhi, label = Stitch(DATASETSM, var)
		if args.background:
			signalstack.append(smhi)
			labels.append(label)
        if GGPythia18:
	    tag = "GG18"
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_500To1000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_1000To2000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_2000To4000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_4000To6000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_6000To8000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            DATASETSM.append("../LocalGenTemplates/OUTGG_M_8000To13000_Pt50_TuneCP2_13TeV_pythia8_cfi_py.root")
            if args.allvar:
	    	smhi = [Stitch(DATASETSM, var) for var in obj]
	    else:
		smhi, label = Stitch(DATASETSM, var)
		if args.background:
			signalstack.append(smhi)
			labels.append(label)
if doADD:
	if doPythia:
	    tag = tag + "pythia"
        if doNegInt1:
		if minx is not 500:
			tag = tag + str(minx)

		if 6.0 in args.LambdaT:
		    DATASETS = []
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000.root')

		    # Implement Invariance mass cuts
		    if minx == 1000:
			DATASETS.pop(0)
		    if minx == 2000:
			DATASETS.pop(0)
			DATASETS.pop(0)

		    # Stitching
	            if args.allvar:
		    	sig = [Stitch(DATASETS, var) for var in obj]
                    	signal.append(sig)
		    else:
			sig, label = Stitch(DATASETS, var)
			signalstack.append(sig)
			labels.append(label)

                if 8.0 in args.LambdaT:
	            DATASETS = []
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_500To1000.root')
		    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_4000To8000.root')

		    # Implement Invariance mass cuts
		    if minx == 1000:
			DATASETS.pop(0)
		    if minx == 2000:
			DATASETS.pop(0)
			DATASETS.pop(0)

		    # Stitching
		    if args.allvar:
		    	sig = [Stitch(DATASETS, var) for var in obj]
                    	signal.append(sig)
		    else:
			sig, label = Stitch(DATASETS, var)
			signalstack.append(sig)
			labels.append(label)

                if 10.0 in args.LambdaT:
	            DATASETS = []
		    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_500To1000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_4000To10000.root')

		    # Implement Invariance mass cuts
		    if minx == 1000:
			DATASETS.pop(0)
		    if minx == 2000:
			DATASETS.pop(0)
			DATASETS.pop(0)

		    # Stitching
		    if args.allvar:
		    	sig = [Stitch(DATASETS, var) for var in obj]
                    	signal.append(sig)
		    else:
			sig, label = Stitch(DATASETS, var)
			signalstack.append(sig)
			labels.append(label)

        if doNegInt0:
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
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_8000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

                if 10 in args.LambdaT:
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_1000To2000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_2000To4000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_4000To10000.root')
                    DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_0_LambdaT_10000_M_500To1000.root')
                    sig = [Stitch(DATASETS, var) for var in obj]
                    signal.append(sig)

	if doNegInt1Dense:
		tag = "grwDense"
		if minx is not 500:
			tag = tag + str(minx)
		if 6.0 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
				DATASETS.pop(0)
			   if minx == 2000:
				DATASETS.pop(0)
				DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
			   	sig, label = Stitch(DATASETS, var)
			   	signalstack.append(sig)
				labels.append(label)
		if 6.5 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_4000To6500.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
				DATASETS.pop(0)
			   if minx == 2000:
			   	DATASETS.pop(0)
			   	DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
			   	sig, label = Stitch(DATASETS, var)
			   	signalstack.append(sig)
				labels.append(label)
		if 7.0 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_4000To7000.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
				DATASETS.pop(0)
			   if minx == 2000:
				DATASETS.pop(0)
				DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			  	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
			   	sig, label = Stitch(DATASETS, var)
			   	signalstack.append(sig)
			   	labels.append(label)
		if 7.5 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_4000To7500.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
				DATASETS.pop(0)
			   if minx == 2000:
			   	DATASETS.pop(0)
			   	DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
			   	sig, label = Stitch(DATASETS, var)
			   	signalstack.append(sig)
			   	labels.append(label)
		if 8.0 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_4000To8000.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
			   	DATASETS.pop(0)
			   if minx == 2000:
			 	DATASETS.pop(0)
			    	DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
				sig, label = Stitch(DATASETS, var)
				signalstack.append(sig)
				labels.append(label)
		if 8.5 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_4000To8500.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
			   	DATASETS.pop(0)
			   if minx == 2000:
			   	DATASETS.pop(0)
				DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
			   	sig, label = Stitch(DATASETS, var)
			  	signalstack.append(sig)
			   	labels.append(label)
		if 9.0 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_4000To9000.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
			   	DATASETS.pop(0)
			   if minx == 2000:
			   	DATASETS.pop(0)
			   	DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
				sig, label = Stitch(DATASETS, var)
				signalstack.append(sig)
				labels.append(label)
		if 10.0 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_4000To10000.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
				DATASETS.pop(0)
			   if minx == 2000:
				DATASETS.pop(0)
				DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                    	signal.append(sig)
			   else:
				sig, label = Stitch(DATASETS, var)
				signalstack.append(sig)
				labels.append(label)
		if 11 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_4000To11000.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
				DATASETS.pop(0)
			   if minx == 2000:
				DATASETS.pop(0)
				DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
				sig, label = Stitch(DATASETS, var)
				signalstack.append(sig)
				labels.append(label)
		if 13 in args.LambdaT:
			   DATASETS = []
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_500To1000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_1000To2000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_2000To4000.root')
	                   DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_4000To13000.root')
			   # Implement Invariance mass cuts
			   if minx == 1000:
				DATASETS.pop(0)
			   if minx == 2000:
				DATASETS.pop(0)
				DATASETS.pop(0)
			   # Stitching
		           if args.allvar:
			   	sig = [Stitch(DATASETS, var) for var in obj]
	                   	signal.append(sig)
			   else:
			  	sig, label = Stitch(DATASETS, var)
			   	signalstack.append(sig)
			    	labels.append(label)

###### STANDALONE
if args.isolate:
	leglabel = "GG2017"

	if args.tag is not None:
		leglabel = leglabel + args.tag

	PlotContinuous(var, smhi, leglabel, lumi=137, Mrange=(minx, 13000), chiMax=None)

	leglabel = "ADD" + args.tag

	PlotContinuous(var, sig, leglabel, lumi=137, Mrange=(minx, 13000), chiMax=None)

#################

if args.plot:
	print "CALLING PLOTTER FUNCTIONS..."
	if args.background:
		if args.minv:
			OverlayHists(var, signalstack, labels, tag=tag, lumi=137, Background="Y", Mrange=(minx, 13000))
		elif args.chidiphoton:
			OverlayHists(var, signalstack, labels, tag=tag, lumi=137, Background="Y", Mrange=(minx, 13000), chiMax=chiMax)
		else:
			OverlayHists(var, signalstack, labels, tag=tag, lumi=137, Background="Y",  Mrange=(minx, 13000))

	CalcSigADD(var, signalstack, labels, lumi=137, MassRange=(minx, 13000), chiMax=chiMax)

if args.sensitivity:
	CalcSensitivityADD(var, signalstack, labels, lumi=137, MassRange=(minx, 13000), chiMax=chiMax)

#################

# Use this rarely or when you are super sure everything works

if args.allvar:
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
