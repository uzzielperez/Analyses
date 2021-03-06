import ROOT
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
from hep_plt.Sensitivityfunctions import CalcSensitivityADD
from hep_plt.Plotfunctions import *
#from hep_plt.ratios import *

import argparse


# Command line options
parser = argparse.ArgumentParser(description="NonResonance")
parser.add_argument("-cd", "--chidiphoton", action="store_true")
parser.add_argument("-m", "--minv", action="store_true")
parser.add_argument("-cs", "--costhetastar", action="store_true")
args = parser.parse_args()



sw = ROOT.TStopwatch()
sw.Start()
gStyle.SetOptStat(0)

# To suppress canvas from popping up. Speeds up plots production.
gROOT.SetBatch()
tag = "b"
doSM 	   = True

# Stitch Datasets
tiny          = False
doADD         = True
doPythia      = True  #Pythia
doSherpa      = True

# Variables to Plot
kinematicsON = False
angularON    = True

obj = []
if args.minv:
    obj.append("gendiphotonMinv")
elif args.chidiphoton:
    obj.append("genchidiphoton")
elif args.costhetastar:
    obj.append("gendiphotoncosthetastar")
else:
    obj.append("gendiphotonMinv")

xr = (0, 13000)
if "chidiphoton" in obj[0]:
    xr = (0,20)
if "gendiphotoncosthetastar" in obj[0]:
    xr = (-1, 1)

#### 6000
DATASETS = []
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000.root')
histPyLT6, lLT6 = Stitch(DATASETS, obj[0])
histPyLT6.SetDirectory(0)

DATASETS = []
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000_TuneCUEP8M1.root')
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000_TuneCUEP8M1.root')
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000_TuneCUEP8M1.root')
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000_TuneCUEP8M1.root')

histShMS6, lMS6 =  Stitch(DATASETS, obj[0])
histShMS6.SetDirectory(0)

hstack, labels = [], []
hstack.append(histPyLT6)
hstack.append(histShMS6)
labels.append(r"LT-6000, +")
labels.append(r"LT-6000, , NED-4")
label1, label2 = labels[0], labels[1]

tag = "GRW6000_TuneCP2-TuneCUEP8M1" + obj[0]
if "Minv" in obj[0]:
    xr = (0, 6000)

PlotRatio(histPyLT6, histShMS6, label1, label2, tag=tag, xRange=xr, yratioRange=(0,3), binning=130)

#### 6000
DATASETS = []
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000_TuneCUEP8M1.root')
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000_TuneCUEP8M1.root')
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000_TuneCUEP8M1.root')
DATASETS.append('../LocalGenTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000_TuneCUEP8M1.root')
histPyLT6, lLT6 = Stitch(DATASETS, obj[0])
histPyLT6.SetDirectory(0)

DATASETS = []
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_MS_6000_NED_4_KK_1_M_1000To2000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_MS_6000_NED_4_KK_1_M_2000To4000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_MS_6000_NED_4_KK_1_M_4000To6000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_MS_6000_NED_4_KK_1_M_500To1000.root')
histShMS6, lMS6 =  Stitch(DATASETS, obj[0])
histShMS6.SetDirectory(0)

hstack, labels = [], []
hstack.append(histPyLT6)
hstack.append(histShMS6)
labels.append(r"LT-6000, +")
labels.append(r"MS-6000, KK-1, NED-4")
label1, label2 = labels[0], labels[1]

tag = "GRW6000_SherpaNNLOas0118_TuneCUEP8M1" + obj[0]
if "Minv" in obj[0]:
    xr = (0, 6000)

PlotRatio(histPyLT6, histShMS6, label1, label2, tag=tag, xRange=xr, yratioRange=(0,3), binning=130)
