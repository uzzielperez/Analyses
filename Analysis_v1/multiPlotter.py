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

study = "Pythia-Sherpa-NED-4_Ms_4000"
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

else:
	File1 = 'TestADDG2gg_LambdaT-10000_M-500-pythia8.root'
	File2 = 'TestADDG2gg_LambdaT-4000_M-500-pythia8.root'
	File3 = 'TestADDG2gg_LambdaT-5000_M-500-pythia8.root'
	File4 = 'TestADDG2gg_LambdaT-7000_M-500-pythia8.root'

	fileDesc1 = 'LambdaT-10000'
	fileDesc2 = 'LambdaT-4000'
	fileDesc3 = 'LambdaT-5000'
	fileDesc4 = 'LambdaT-7000'

FileList = [File1, File2, File3, File4]
#FileList = args.inputfiles
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
	ID.append(match[0])
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

#Get obj and Keys

i = 0
for fi in openFileList:
	LoopObjKeys(fi, obj_i[i], canv_i[i], h_i[i], i)
	i = i + 1

for objFi in obj_i:
	j = 0
	while j < len(objFi):
		ytitle = 'Events'
		c = ROOT.TCanvas()
		scale = 1.00
		#--------------- String Finder
	  	if objFi[j].find("Minv") != -1:
			xtitle = r"m_{#gamma#gamma}#scale[0.8]{(GeV)}" # r"#scale[0.8]{m_{#gamma#gamma}(GeV)}"
	       		xmin = 500
	       		xmax = 4000
			#scale = 35.9
			c.SetLogy()
			xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85

			#xpos1, ypos1, xpos2, ypos2 = .72, 0.75, 1.0, .85
			#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
		elif objFi[j].find("Pt") != -1:
		#elif objFi[j].find("Pt") != -1:
			xtitle = "#scale[0.8]{p_{T}(GeV)}"
			xmin = 75
			xmax = 4000
			#scale = 35.9
			c.SetLogy()
			xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
			#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85

                elif objFi[j].find("Eta") != -1:
			xtitle = r"#eta"
			if objFi[j].find("sc") != -1:
			    xtitle = r"#scale[0.7]{sc} " + xtitle
			if objFi[j].find("det") != -1:
			    xtitle = r"#scale[0.7]{det} " + xtitle
			xmin = -3.0
			xmax = 3.0
			#scale = 35.9
			xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
			#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
			#xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38

       	        elif objFi[j].find("Phi") != -1:
			xtitle = r"#phi"
			if objFi[j].find("sc") != -1:
			    xtitle = r"#scale[0.7]{sc} " + xtitle
			if objFi[j].find("det") != -1:
			    xtitle = r"#scale[0.7]{det} " + xtitle
			xmin = -3.5
			xmax = 3.5
			#scale = 35.9
			xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
			#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
			#xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38

	        else:
	        	continue

		if objFi[j].find("diphoton") != -1:
			legentry = r"SM #gamma#gamma"
		elif (objFi[j].find("photon1")) != -1:
			legentry = r"#gamma_{1}"
		elif (objFi[j].find("photon2")) != -1:
			legentry = r"#gamma_{2}"
		else:
			legentry = objFi[j]

	   	# EBEE or EBEB
	   	if objFi[j].find("EBEE") != -1:
	        	xtitle = xtitle + r" #scale[0.45]{(EBEE)}"
	    	if objFi[j].find("EBEB") != -1:
	        	xtitle = xtitle + r" #scale[0.45]{(EBEB)}"
	    	# Photon1 or Photon2
	    	if objFi[j].find("photon1") != -1:
	        	xtitle = r"#scale[0.80]{#gamma_{1}: }" + xtitle
	    	if objFi[j].find("photon2") != -1:
	        	xtitle = r"#scale[0.80]{#gamma_{2}: }" + xtitle


		
		
		j = j + 1
#--------------------------------------
#
#         # Draw histos & additional Settings
# 	pad1.cd()
# 	hf1[i].Scale(scale) # rescale to 35.9 fb^-1
# 	hf1[i].SetFillColor(kBlue -3)
# 	hf1[i].SetTitle(obj_f1[i])
# 	#hf1[i].GetYaxis().SetTitle("weighted Events")
# 	hf1[i].GetYaxis().SetTitleOffset(1.4)
# 	hf1[i].GetXaxis().SetRangeUser(xmin, xmax)
# 	hf2[i].GetXaxis().SetRangeUser(xmin, xmax)
# 	hf2[i].GetYaxis().SetTitle("Events")
# 	hf2[i].SetMarkerStyle(20)
#
# 	hf2[i].Draw(s2)  # Draw this to set max y
# 	hf1[i].Draw(s1)
# 	hf2[i].Draw(s2) # To draw over filled MC
#
# #	hf2[i].Draw("esamex0")  # Draw this to set max y
# #	hf1[i].Draw("hist same")
# #	hf2[i].Draw("esamex0") # To draw over filled MC
# 	#to avoid clipping the bottom zero, redraw a small axis
# 	#hM.GetYaxis().SetLabelSize(0.0)
# 	#axis = TGaxis(-5, 20, -5, 220, 20, 220, 510, "")
# 	#axis.SetLabelFont(43)
# 	#axis.SetLabelSize(15)
# 	#axis.Draw()
#
# 	# Legend
# 	leg = TLegend(xpos1, ypos1, xpos2, ypos2)
# 	leg.SetBorderSize(0)
# 	leg.SetFillColor(0)
# 	leg.SetFillStyle(0)
# 	leg.SetTextFont(42)
# 	leg.SetTextSize(0.035)
# 	leg.AddEntry(hf1[i], "%s" %(fileDescription1), "f")
# 	leg.AddEntry(hf2[i], "%s" %(fileDescription2), "l")
# 	leg.Draw()
#
#  	hRatio = createRatio(hf2[i], hf1[i])
#         # RATIO
# 	pad2.cd()
# 	hf1[i].GetYaxis().SetTitle("ratio %s/%s" %(fileDescription1, fileDescription2))
# 	#hRatio.GetXaxis().SetRangeUser(xmin, xmax)
# 	x = hRatio.GetXaxis()
# 	x.SetRangeUser(xmin, xmax)
# 	x.SetTitleOffset(2.5)
# 	x.SetTitleSize(35)
# 	x.SetTitle(xtitle)
# 	y = hRatio.GetYaxis()
# 	y.SetTitle("Ratio")
# 	y.SetTitleSize(20)
# 	y.SetTitleFont(43)
# 	hRatio.Draw("ep")
#
# 	#place_legend(c[i], None, None, None, None, header="", option="LP")
# 	CMS_lumi(c, 4, 11, False)
#
# 	#c.Update()
# 	#c.Draw()
# 	#c.Print("BKGPlots.pdf[", "minv")
# 	#c.Print("BKGPlotsminv.pdf")
#
# 	#Draw All canvases
# 	#from ROOT import gROOT
# 	#gROOT.GetListOfCanvases().Draw()
# 	#gROOT.GetListOfCanvases().Print("ratioplots/ratio%s/png" %(obj_f1[i]))
# 	c.Print("%s/%sratio_%s.png" %("ratioplots",study, obj_f1[i]))
#
# 	# move to next object in root file
# 	i = i + 1
# #-------------------------------------------

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")
