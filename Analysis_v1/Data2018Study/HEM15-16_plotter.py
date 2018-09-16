#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend, TLine
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory


import sys  
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)  
from CMSlumi import CMS_lumi, set_CMS_lumi
import argparse

#filename = 'HEM15-16.root'
filename = 'HEM15-16_data.root'

# Draw Options 
DrawAsHist = False 
gStyle.SetOptStat(0)

# Timer 
sw = ROOT.TStopwatch()
sw.Start()


f = ROOT.TFile(filename, "READ") 

#----------------------------------------
# This part taken from andy buckley
# https://root-forum.cern.ch/t/loop-over-all-objects-in-a-root-file/10807/4

def getall(d, basepath="/"):
    "Generator function to recurse into a ROOT file/dir and yield (path, obj) pairs"
    for key in d.GetListOfKeys():
        kname = key.GetName()
        if key.IsFolder():
            for i in getall(d.Get(kname), basepath+kname+"/"):
                yield i
        else:
            yield basepath+kname, d.Get(kname)

ROOT.gROOT.SetBatch(True)
histos = []
canvas = []
obj = []

for k, o in getall(f):
    #print o.ClassName(), k
    print "h_%s" %(k[1:])
    canvas.append("c_%s"%(k[1:]))
    histos.append("h_%s"%(k[1:]))
    obj.append(k[1:])
    
#print c
#print histos
print obj

# Basic Plotting Template
i = 0
while i<len(histos):
	c = ROOT.TCanvas()

	if obj[i].find("Eta") != -1:
		xtitle = r"#eta" 
		xmin = -3.0
		xmax = 3.0
		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
		if "After" in obj[i]:
			legentry = "PostHEM-Eta"
			lumival = 6.612
		elif "B4" in obj[i]:
			legentry = "PreHEM-Eta"
			lumival = 20.315
#		etamax_line = TLine(-1.392,0,-1.392, 20)
#		etamax_line.SetLineColor(kRed)
#		etamax_line.Draw()
#		etamin_line = TLine(-3,0,-3,20)
#		etamin_line.SetLineColor(kRed)
#		etamin_line.Draw()
	elif obj[i].find("Phi") != -1:
		xtitle = r"#phi"
		xmin = -3.5
		xmax = 3.5	
		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
		if "After" in obj[i]:
			legentry = "PostHEM-Phi"
			lumival = 6.612
		elif "B4" in obj[i]:
			legentry = "PreHEM-Phi"
	 		lumival = 20.315 
	# Histogram Name and Draw
	histos[i] = f.Get(obj[i])
	histos[i].GetXaxis().SetTitleOffset(1.2)
	histos[i].GetYaxis().SetTitleOffset(1.2)

	ytitle = "weighted events"
	histos[i].GetYaxis().SetTitle(ytitle)
	
	histos[i].GetXaxis().SetTitle(xtitle) 
	histos[i].SetAxisRange(xmin, xmax)

	if DrawAsHist:
		histos[i].Draw("hist")
	else: 
		histos[i].Draw()

	leg = TLegend(xpos1, ypos1, xpos2, ypos2)
	leg.SetBorderSize(0)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	leg.SetTextSize(0.035)
	leg.AddEntry(histos[i], legentry ,"l")
	leg.Draw() 
	
        set_CMS_lumi(c, 4, 11, lumival)	
	
	c.Update()
	c.Draw()
		
	if DrawAsHist:
		c.Print("HEM15-16_h%s.png" %(obj[i]))
	else:
		c.Print("HEM15-16%s.png" %(obj[i]))
	
	i = i + 1 

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")

