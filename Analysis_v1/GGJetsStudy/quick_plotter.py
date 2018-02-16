#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory

from legend import *

import sys  
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)  
from CMSlumi import CMS_lumi

path = 'uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/GGJetsStudy' 
filename = 'GGJets_histograms.root' 

# Timer 
sw = ROOT.TStopwatch()
sw.Start()

##########################################
# Extra Cosmetics
#gStyle.SetOptStat(0)

#CMS_lumi( TPad* pad, int iPeriod=3, int iPosX=10 )
##########################################

f = ROOT.TFile(filename, "READ")
#f.ls()

#----------------------------------------
# This part taken from andy buckley
# https://root-forum.cern.ch/t/loop-over-all-objects-in-a-root-file/10807/4

def getall(d, basepath="/"):
    "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
    for key in d.GetListOfKeys():
        kname = key.GetName()
        if key.IsFolder():
            # TODO: -> "yield from" in Py3
            for i in getall(d.Get(kname), basepath+kname+"/"):
                yield i
        else:
            yield basepath+kname, d.Get(kname)
# Demo
ROOT.gROOT.SetBatch(True)
histos = []
c = []
obj = []

for k, o in getall(f):
    #print o.ClassName(), k
    print "h_%s" %(k[1:])
    c.append("c_%s"%(k[1:]))
    histos.append("h_%s"%(k[1:]))
    obj.append(k[1:])
    
#print c
#print histos
print obj

#-----------------------------------------
# Basic Plotting Template
#
#leg = []
i = 0
while i<len(histos):

       
	 # Canvas
	c[i] = ROOT.TCanvas("canvas%s"%(i),"canvas%s"%(i), 600, 600) # Modify size
	#c[i].SetGrid()
	
	#--------------- String Finder	
	if obj[i].find("Minv") != -1:
		xtitle = r"m_{#gamma#gamma} #scale[0.8]{(GeV)}"
		xmin = 200
		xmax = 1600 
	        c[i].SetLogy()
	elif obj[i].find("Pt") != -1:
		xtitle = "p_{T} (GeV)"
		xmin = 200
		xmax = 1600
		c[i].SetLogy()
	elif obj[i].find("Eta") != -1:
		xtitle = r"#eta" 
		xmin = -3.0
		xmax = 3.0
	elif obj[i].find("Phi") != -1:
		xtitle = r"#phi"
		xmin = -3.5
		xmax = 3.5
	else:
		continue
	
	if obj[i].find("diphoton") != -1:
		legentry = r"#gamma#gamma"
	elif (obj[i].find("photon1")) != -1: 
		legentry = r"#gamma_{1}"
	elif (obj[i].find("photon2")) != -1:
		legentry = r"#gamma_{2}"
	else:
		legentry = obj[i]

	#------------------	

	# Histogram Name and Draw
	histos[i] = f.Get(obj[i])
	histos[i].GetXaxis().SetTitleOffset(1.2)
	histos[i].GetYaxis().SetTitleOffset(1.2)

	ytitle = "weighted events/ 80 GeV"
	histos[i].GetYaxis().SetTitle(ytitle)
	
	histos[i].GetXaxis().SetTitle(xtitle) 
	histos[i].SetAxisRange(xmin, xmax)
	
	# --Draw option
	
	h = True
	
	if h:
		histos[i].Draw("hist")
	else:
		histos[i].Draw()
	
#	overlay = False
	
#	if overlay
#	if obj[i].find
	# ----

	#Legend
	#leg = TLegend(xlegpos1, ylegpos1, xlegpos1, ylegpos1) ###### NEEDS TO BE MODIFIED
	leg = TLegend(.60, 0.75, .97, .85)
	leg.SetBorderSize(0)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	leg.SetTextSize(0.035)
	leg.AddEntry(histos[i], legentry ,"l")
	leg.Draw()

       #c[i].PlaceLegend()
	CMS_lumi(c[i], 4, 11, True) 

	c[i].Draw()
	#c[i].Print("BKGPlots.pdf[", "minv")
	#c[i].Print("BKGPlotsminv.pdf")
	
	if h:
		c[i].Print("h%s.png" %(obj[i]))
	else:
		c[i].Print("%s.png" %(obj[i]))

	i = i+1

#-------------------------------------------

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")
