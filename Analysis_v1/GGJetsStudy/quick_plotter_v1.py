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

#--------------------------------------------------------------------------------
path = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/GGJetsStudy'
filename = 'GGJets_histograms.root' 
#--------------------------------------------------------------------------------

# Draw Options 
h = True       # Draw histograms as "hist"
overlay = False # Overlay some histograms. See second loop below   
fit = True

#--------------------------------------------------------------------------------
# Timer 
sw = ROOT.TStopwatch()
sw.Start()

##########################################
# Extra Cosmetics
gStyle.SetOptStat(0)

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

#Overlay canvases
samePt = ROOT.TCanvas()
sameFullDetPt = ROOT.TCanvas()
samepTEBEE = ROOT.TCanvas()
samepTEBEB = ROOT.TCanvas()

sameEtaAll = ROOT.TCanvas()
sameDetEta = ROOT.TCanvas()
sameEta = ROOT.TCanvas()

samePhiAll = ROOT.TCanvas()
samePhi = ROOT.TCanvas()
sameDetEta = ROOT.TCanvas()


# Basic Plotting Template
i = 0
while i<len(histos):

       
	 # Canvas
	#c[i] = ROOT.TCanvas("canvas%s"%(i),"canvas%s"%(i), 600, 600) # Modify size
	c = ROOT.TCanvas()
	#c[i].SetGrid()
	
	#--------------- String Finder	
	if obj[i].find("Minv") != -1:
		xtitle = r"m_{#gamma#gamma} #scale[0.8]{(GeV)}"
		xmin = 200
		xmax = 1600 
	        c.SetLogy()	
		xpos1, ypos1, xpos2, ypos2 = .60, 0.75, 1.0, .85
	elif obj[i].find("Pt") != -1:
		xtitle = "p_{T} (GeV)"
		xmin = 200
		xmax = 1600
		c.SetLogy()	
		xpos1, ypos1, xpos2, ypos2 = .60, 0.75, 1.0, .85 
	elif obj[i].find("Eta") != -1:
		xtitle = r"#eta" 
		xmin = -3.0
		xmax = 3.0
		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .28
	elif obj[i].find("Phi") != -1:
		xtitle = r"#phi"
		xmin = -3.5
		xmax = 3.5	
		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .28
	else:
		continue
	
	if obj[i].find("diphoton") != -1:
		legentry = r"SM #gamma#gamma"
	elif (obj[i].find("photon1")) != -1: 
		legentry = r"#gamma_{1}"
	elif (obj[i].find("photon2")) != -1:
		legentry = r"#gamma_{2}"
	else:
		legentry = obj[i]

	#i = i + 1

	# Overlay Legend Settings
	legpT = TLegend(xpos1, ypos1, xpos2, ypos2)
	legpT.SetBorderSize(0)
	legpT.SetFillColor(0)
	legpT.SetFillStyle(0)
	legpT.SetTextFont(42)
	legpT.SetTextSize(0.035)

	legEtaAll = TLegend(xpos1, ypos1, xpos2, ypos2)
	legEtaAll.SetBorderSize(0)
	legEtaAll.SetFillColor(0)
	legEtaAll.SetFillStyle(0)
	legEtaAll.SetTextFont(42)
	legEtaAll.SetTextSize(0.035)

	legPhiAll = TLegend(xpos1, ypos1, xpos2, ypos2)
	legPhiAll.SetBorderSize(0)
	legPhiAll.SetFillColor(0)
	legPhiAll.SetFillStyle(0)
	legPhiAll.SetTextFont(42)
	legPhiAll.SetTextSize(0.035)

#i=0
#while i<len(histos):
		 
	# Histogram Name and Draw
	histos[i] = f.Get(obj[i])
	histos[i].GetXaxis().SetTitleOffset(1.2)
	histos[i].GetYaxis().SetTitleOffset(1.2)

	ytitle = "weighted events"
	histos[i].GetYaxis().SetTitle(ytitle)
	
	histos[i].GetXaxis().SetTitle(xtitle) 
	histos[i].SetAxisRange(xmin, xmax)
	#-----------------------
	
	if fit:
		if obj[i].find("Phi") != -1:
			histos[i].Fit("pol0")
			histos[i].GetFunction("pol0").SetLineColor(kRed)

	#------------------------------
	# Overlay (Set to True to run this)
	# refer to lines 74-85 for list of canvases

	if overlay:
		if obj[i].find("photon1") or obj[i].find("photon2") !=1:
			histos[i].SetLineColor(i)
			if obj[i].find("Pt") != -1:
				samePt.cd()
				samePt.SetLogy()
				if h:
					histos[i].Draw("hist same")
				else:
					histos[i].Draw("same")
		
				legpT.AddEntry(histos[i], obj[i] ,"l")
				legpT.Draw()
				samePt.Update()
			
			if obj[i].find("Eta") != -1:
				sameEtaAll.cd()
				if h:
					histos[i].Draw("hist same")
				else:
					histos[i].Draw("same")			
				legEtaAll.AddEntry(histos[i], obj[i] ,"l")
				legEtaAll.Draw()
				sameEtaAll.Update()
			if obj[i].find("Phi") != -1:
				samePhiAll.cd()
				if h:
					histos[i].Draw("hist same")
				else:
					histos[i].Draw("same")
		
				legPhiAll.AddEntry(histos[i], obj[i] ,"l")
				legPhiAll.Draw()				
				samePhiAll.Update()
	else:	
		#------------------	
		# Going to default canvas (no overlay)
		#------------------
		c.cd()
		#-----------------------
		# --Draw option
			
		if h:
			histos[i].Draw("hist")
		else:
			histos[i].Draw()
		
		#Legend
		leg = TLegend(xpos1, ypos1, xpos2, ypos2)
		leg.SetBorderSize(0)
		leg.SetFillColor(0)
		leg.SetFillStyle(0)
		leg.SetTextFont(42)
		leg.SetTextSize(0.035)
		leg.AddEntry(histos[i], legentry ,"l")
		leg.Draw()

	      
		#place_legend(c[i], None, None, None, None, header="", option="LP")
		CMS_lumi(c, 4, 11, True) 
		
		c.Update()
		c.Draw()
		#c.Print("BKGPlots.pdf[", "minv")
		#c.Print("BKGPlotsminv.pdf")
		
		if h:
			c.Print("%s/v1h%s.png" %(path,obj[i]))
		else:
			c.Print("%s/v1%s.png" %(path,obj[i]))

	i = i+1

#-------------------------------------------

#-------------------------------------------
# Overlay Draw
if overlay:
	samePt.Draw()
	sameEtaAll.Draw()
	samePhiAll.Draw()
	if h:		
		samePt.Print("%s/hsamePt.png" %(path))
		sameEtaAll.Print("%s/hsameEtaAll.png" %(path))
		samePhiAll.Print("%s/hsamePhiAll.png" %(path))
	else:
		samePt.Print("%s/samePt.png" %(path))
		sameEtaAll.Print("%s/sameEtaAll.png" %(path))
		samePhiAll.Print("%s/samePhiAll.png" %(path))

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")

