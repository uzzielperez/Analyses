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
parser.add_argument("-s", "--sensitivity", action="store_true", help="Compute Sensitivity")
parser.add_argument("--tag", default=None, help="For File naming tag")

# Variables
parser.add_argument("-m", "--minv", action="store_true")
parser.add_argument("-cd", "--chidiphoton", action="store_true")
parser.add_argument("-cs", "--costhetastar", action="store_true")
parser.add_argument("--pt1", action="store_true")
parser.add_argument("--pt2", action="store_true")
parser.add_argument("--eta1", action="store_true")
parser.add_argument("--eta2", action="store_true")
parser.add_argument("--phi1", action="store_true")
parser.add_argument("--phi2", action="store_true")

# Extra options
parser.add_argument("--gen", action="store_true")
parser.add_argument("--isolate", action="store_true")
parser.add_argument("-od", "--outdir", default=None)

# Parameters Settings
parser.add_argument("-lt", '--LambdaT', default=[6], nargs='+', type=float)
parser.add_argument("--min", default=500)
parser.add_argument("--max", default=13000)
parser.add_argument("--chimax", default=20)
parser.add_argument("--barrel", action="store_true")
parser.add_argument("--M2000", action="store_true")

args = parser.parse_args()
sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)

# To suppress canvas from popping up. Speeds up plots production.
#if args.setbatch:
gROOT.SetBatch()

tag = "17"
minx = 500
chiMax = args.chimax 

if args.tag is not None:
	tag = args.tag
	print "Working on %s" %(tag)
if args.minv:
	var = "gendiphotonMinv"
elif args.chidiphoton:
	var = "genchidiphoton"
elif args.costhetastar:
	var = "gendiphotoncosthetastar"
elif args.pt1:
	var = "genphoton1Pt"
elif args.pt2:
	var = "genphoton2Pt"
elif args.eta1:
	var = "genphoton1Eta"
elif args.eta2:
	var = "genphoton2Eta"
elif args.phi1:
	var = "genphoton1Phi"
elif args.phi2:
	var = "genphoton2Phi"
else:
	var = "gendiphotonMinv"

if args.barrel:
	var = var + "isEBEB"

if args.M2000:
	var = var + "_M2000"
        minx = 2000

signalstack = []
DATASETSM   = []
labels      = []

# Pythia8 Fall Request
DATASETSM.append("../LocalGenTemplates/OUTGG_M_500To1000_Pt70_TuneCP2_13TeV_pythia8_cfi_py.root")
DATASETSM.append("../LocalGenTemplates/OUTGG_M_1000To2000_Pt70_TuneCP2_13TeV_pythia8_cfi_py.root")
DATASETSM.append("../LocalGenTemplates/OUTGG_M_2000To4000_Pt70_TuneCP2_13TeV_pythia8_cfi_py.root")
DATASETSM.append("../LocalGenTemplates/OUTGG_M_4000To13000_Pt70_TuneCP2_13TeV_pythia8_cfi_py.root")

smhi, label = Stitch(DATASETSM, var)
signalstack.append(smhi)
labels.append(label)

if 6.0 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000.root')

	sig, label = Stitch(DATASETS, var)
        signalstack.append(sig)
	labels.append(label)
if 6.5 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6500_M_4000To6500.root')

	sig, label = Stitch(DATASETS, var)
	signalstack.append(sig)
	labels.append(label)

if 7.0 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7000_M_4000To7000.root')

        sig, label = Stitch(DATASETS, var)
        signalstack.append(sig)
        labels.append(label)
if 7.5 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_7500_M_4000To7500.root')

	sig, label = Stitch(DATASETS, var)
	signalstack.append(sig)
	labels.append(label)
if 8.0 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_4000To8000.root')

        sig, label = Stitch(DATASETS, var)
        signalstack.append(sig)
        labels.append(label)
if 8.5 in args.LambdaT:
        DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8500_M_4000To8500.root')

	sig, label = Stitch(DATASETS, var)
        signalstack.append(sig)
	labels.append(label)
if 9.0 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_9000_M_4000To9000.root')

        sig, label = Stitch(DATASETS, var)
        signalstack.append(sig)
        labels.append(label)
if 10.0 in args.LambdaT:
        DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_10000_M_4000To10000.root')

	sig, label = Stitch(DATASETS, var)
	signalstack.append(sig)
	labels.append(label)
if 11 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_11000_M_4000To11000.root')

	sig, label = Stitch(DATASETS, var)
	signalstack.append(sig)
	labels.append(label)
if 13 in args.LambdaT:
	DATASETS = []
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_500To1000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_1000To2000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_2000To4000.root')
	DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_13000_M_4000To13000.root')

	sig, label = Stitch(DATASETS, var)
	signalstack.append(sig)
	labels.append(label)

if args.plot:
	if args.min is not None and args.max is not None: 
		xr = (args.min, args.max)
	if args.outdir is not None:
		outdir = args.outdir
	OverlayHists(var, signalstack, labels, tag=tag, lumi=137, Background="Y", xRange=xr, Outputdir=args.outdir)

	# Only Calc Sig for Minv, chidiphoton or vars of interest
	if args.minv or args.chidiphoton:
		CalcSigADD(var, signalstack, labels, lumi=137, MassRange=(minx, 13000), chiMax=chiMax)

if args.sensitivity:
	CalcSensitivityADD(var, signalstack, labels, lumi=137, MassRange=(minx, 13000), chiMax=chiMax)
