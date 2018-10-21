#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad,TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory

#from legend import *
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

path = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/UnparticlesStudy'
study = "Unparticles"

File3 = 'Unparticles106.root'
File2 = 'Unparticles109.root'
File1 = 'Unparticles2x1.root'

File4 = "Unparticles106_LambdaU-1000.root"
File5 = "Unparticles109_LambdaU-1000.root"
File6 = "Unparticles2x1_LambdaU-1000.root"

fileDesc3 = 'du = 1.06'
fileDesc2 = 'du = 1.09'
fileDesc1 = 'du = 2.1'

fileDesc4 = 'du = 1.06, LambdaU = 1000'
fileDesc5 = 'du = 1.09, LambdaU = 1000'
fileDesc6 = 'du = 2.1, LambdaU = 1000'

outName = "Unparticles"

FileList = [File1, File2, File3, File4, File5, File6]
#FileList = args.inputfiles

print FileList
#--------------------------------------------------------------------------------
openFileList = []
ID = []
h_i = []
obj_i = []
canv_i = []

for fi in FileList:
	if "Test" in fi:
		openFileList.append(ROOT.TFile(path2+"/"+fi, "READ"))
	if "Unparticles" in fi:
		openFileList.append(ROOT.TFile(path+"/"+fi, "READ"))
		#print fi
	h_i.append([])
	obj_i.append([])
	canv_i.append([])

#print obj_i
#print openFileList
# Timer
sw = ROOT.TStopwatch()
sw.Start()

gStyle.SetOptStat(0)
#CMS_lumi( TPad* pad, int iPeriod=3, int iPosX=10 )
# Arrays for file objects
ROOT.gROOT.SetBatch(True)

# Get obj and Keys
# Create Histograms for each
i = 0
for fi in openFileList:
	LoopObjKeys(fi, obj_i[i], canv_i[i], h_i[i], i)
	i = i + 1

print obj_i
#print canv_i
#obj[0], canv_i[0], should be identical to others
LoopOverHistogramsPerFile(study, obj_i[0], h_i, FileList, canv_i[0], outName)


sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")
