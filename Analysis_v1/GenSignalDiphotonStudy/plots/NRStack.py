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
parser.add_argument("-b", "--barrelonly", action="store_true")
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
    if args.barrelonly:
	obj.append("gendiphotonMinvisEBEB")
    else:
    	obj.append("gendiphotonMinv")
elif args.chidiphoton:
    if args.barrelonly:
	obj.append("genchidiphotonisEBEB")
    else:
    	obj.append("genchidiphoton")
elif args.costhetastar:
    if args.barrelonly:
	obj.append("gendiphotoncosthetastarisEBEB")
    else:
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

if args.barrelonly:
	tag = tag + 'isEBEB'

if "Minv" in obj[0]:
    xr = (0, 13000)

PlotRatio(histPyLT6, histShMS6, label1, label2, tag=tag, xRange=xr, yratioRange=(0,3), binning=130)

#### 6000
DATASETS = []
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_1000To2000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_2000To4000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_4000To8000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_8000_M_500To1000.root')
histPyLT6, lLT6 = Stitch(DATASETS, obj[0])
histPyLT6.SetDirectory(0)

DATASETS = []
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_1000To2000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_2000To4000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_4000To6000.root')
DATASETS.append('../NonResonanceTemplates/OUTADDGravToGG_NegInt_1_LambdaT_6000_M_500To1000.root')

histShMS6, lMS6 =  Stitch(DATASETS, obj[0])
histShMS6.SetDirectory(0)

hstack, labels = [], []

DATASETSM = []
DATASETSM.append("../LocalGenTemplates/OUTGG_M_1000To2000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
DATASETSM.append("../LocalGenTemplates/OUTGG_M_2000To4000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
DATASETSM.append("../LocalGenTemplates/OUTGG_M_4000To6000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
DATASETSM.append("../LocalGenTemplates/OUTGG_M_6000To8000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
DATASETSM.append("../LocalGenTemplates/OUTGG_M_8000To13000_Pt50_TuneCP2_13TeV_pythia8_cfi_2017.root")
smhist, smlabel = Stitch(DATASETSM, obj[0])

hstack.append(smhist)
labels.append(r"GG #gamma#gamma Pythia8")
hstack.append(histPyLT6)
hstack.append(histShMS6)
labels.append(r"ADD, LT-8000, +TuneCP2")
labels.append(r"ADD, LT-6000, +TuneCP2")
label1, label2 = labels[0], labels[1]

tag = "GRW6000y8000" + obj[0]

if args.barrelonly:
	tag = tag + 'isEBEB'

if "Minv" in obj[0]:
    xr = (0, 13000)

PlotRatio(histPyLT6, histShMS6, label1, label2, tag=tag, xRange=xr, yratioRange=(0,3), binning=130)
h1, h2 = hstack[1], hstack[2]
label1, label2 = labels[1], labels[2]
c, pad1, pad2 = createCanvasPads()
#pad1.SetLogy()
pad1.cd()
h1.SetLineColor(kRed)
h2.SetLineColor(kBlue)
h1.Draw()
x1 = h1.GetXaxis()
y1 = h1.GetYaxis()
binn = "125"
ytitle = r"#scale[1.0]{Events/%sGeV}" %(binn)
x1.SetRangeUser(0, 13000)
h2.Draw("same")
h3  = smhist
h3.SetFillStyle(3144)
h3.Draw("same")
legpos = .55, 0.58, .80, .88
leg = makeLegend(legpos, legendtitle="#bf{Sensitivity Studies}")
leg.AddEntry(h1, label1)
leg.AddEntry(h2, label2)
leg.Draw()

pad2.cd()
hRatio = createRatio(h1, h2)
hRatio.Fit("pol0")
hRatio.GetFunction("pol0").SetLineColor(kRed)
stats = hRatio.FindObject("stats")
if not stats:
	#continue
	stats.__class__ = ROOT.TPaveStats
   	#gStyle.SetOptFit(1111)
y = hRatio.GetYaxis()
y.SetRangeUser(0, 2)
y.SetTitle("Ratio")
y.SetTitleSize(20)
y.SetTitleFont(43)
x = hRatio.GetXaxis()
hRatio.SetMarkerStyle(20)
hRatio.Draw("esamex0")
outputdir = "RatioPlots"
if not os.path.exists(outputdir):
	os.mkdir(outputdir)
os.chdir(outputdir)
print "Saving in %s" %(outputdir)
c.Print("Ratio%s.pdf" %(tag))
os.chdir("..")
