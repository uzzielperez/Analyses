#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory

from legend import *
from plotsHelper import *

import re

import sys
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)
from CMSlumi_ratio import CMS_lumi
import argparse

# Command line options
parser = argparse.ArgumentParser(description="ratioPlotter")
#parser.add_argument("-p", "--pathtofiles", dest="filespath", default="/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/ADDGravToGGPythiaStudy",
#		   help="Path to files. It's recommended that they are together")
parser.add_argument("-i", "--inputfiles", dest="inputfiles", default=["TestADDG2gg_LambdaT-10000_M-500-pythia8.root"], nargs='*', help="List of input files")
#parser.add_argument("-s", "--study", dest="study", default="SomeStudy", help="Study Name")
#parser.add_argument("-t", "--ttree", dest="ttree", default="diphoton/fTree", help="TTree Name")
args = parser.parse_args()

isMD = False

#study = "Pythia-Sherpa-NED-4_Ms_4000"
study = "Pythia"
#study = "Pythia-LambdaT-4000-VarMD"
#--------------------------------------------------------------------------------
path = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/ADDGravToGGPythiaStudy'

if isMD:
	File1 = 'Test_MD-1128-ADDG2gg_LambdaT-4000_M-500-pythia8.root'
	File2 = 'Test_MD-1410-ADDG2gg_LambdaT-4000_M-500-pythia8.root'
 	File3 = 'Test_MD-1974-ADDG2gg_LambdaT-4000_M-500-pythia8.root'
	File4 = 'Test_MD-2820-ADDG2gg_LambdaT-4000_M-500-pythia8.root'

	fileDesc1 = 'LambdaT-4000_MD-1128'
	fileDesc2 = 'LambdaT-4000_MD-1410'
	fileDesc3 = 'LambdaT-4000_MD-1974'
	fileDesc4 = 'LambdaT-4000_MD-2820'
	
	outName = 'MD'
else:
	File4 = 'TestADDG2gg_LambdaT-10000_M-500-pythia8.root'
	File1 = 'TestADDG2gg_LambdaT-4000_M-500-pythia8.root'
	File2 = 'TestADDG2gg_LambdaT-5000_M-500-pythia8.root'
	File3 = 'TestADDG2gg_LambdaT-7000_M-500-pythia8.root'

	fileDesc4 = 'LambdaT-10000'
	fileDesc1 = 'LambdaT-4000'
	fileDesc2 = 'LambdaT-5000'
	fileDesc3 = 'LambdaT-7000'
	
	outName   = 'noMD'
FileList = [File1, File2, File3, File4]
#FileList = args.inputfiles

print FileList
#--------------------------------------------------------------------------------
openFileList = []
ID = []
h_i = []
obj_i = []
canv_i = []

for fi in FileList:
	openFileList.append(ROOT.TFile(path+"/"+fi, "READ"))
	#print fi
	# Arrays for Canvases, histograms and objects
	if isMD:
		pattern = r'MD-\s+(.*)'
	else:
		pattern = r'LambdaT-([^(]*)\_M-500'
	match = re.findall(pattern, fi)
	print fi, match
	#ID.append(match[0])
	h_i.append([])
	obj_i.append([])
	canv_i.append([])
#-----------------------
# Draw style option (mc)
#s2 = "esamex0"
s2 = "same"
s1 = "hist same"
#-----------------------

# Timer
sw = ROOT.TStopwatch()
sw.Start()

##########################################
# Extra Cosmetics
gStyle.SetOptStat(0)
#CMS_lumi( TPad* pad, int iPeriod=3, int iPosX=10 )
##########################################
# Arrays for file objects
ROOT.gROOT.SetBatch(True)

# Get obj and Keys
# Create Histograms for each
i = 0
for fi in openFileList:
	LoopObjKeys(fi, obj_i[i], canv_i[i], h_i[i], i)
	i = i + 1

#print canv_i
#obj[0], canv_i[0], should be identical to others
LoopOverHistogramsPerFile(study, obj_i[0], h_i, FileList, canv_i[0], outName, isMD)


sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")
