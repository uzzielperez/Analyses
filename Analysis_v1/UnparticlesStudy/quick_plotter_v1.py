#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory


import sys
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)
from CMSlumi import CMS_lumi
import argparse

#filename = 'RSG750.root'
#filename = 'Unparticles106.root'
#filename = 'Unparticles109.root'
filename = 'Unparticles2x1.root'

# Draw Options
h = True      # Draw histograms as "hist"
overlay = False
fit = False
SetLogy = False

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

# Overlay Legend Settings
#def legendAny(LEG,x1, y1, x2, y2):
#	LEG = TLegend(x1, y1, x2, y2)
#	LEG.SetBorderSize(0)
#	LEG.SetFillColor(0)
#	LEG.SetFillStyle(0)
#	LEG.SetTextFont(0)
#	LEG.SetTextSize(0)
#	return LEG
#
# Overlay count
countpT = 0
countEtaAll = 0
countPhiAll = 0

# Basic Plotting Template
i = 0
while i<len(histos):
	# Canvas
	#c[i] = ROOT.TCanvas("canvas%s"%(i),"canvas%s"%(i), 600, 600) # Modify size
	#c[i].SetGrid()
	c = ROOT.TCanvas()

	#--------------- String Finder
	if obj[i].find("Minv") != -1:
		xtitle = r"m_{#gamma#gamma} #scale[0.8]{(GeV)}"
		xmin = 200
		xmax = 4000 #1600
		if SetLogy:
	        	c.SetLogy()
		xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
	elif obj[i].find("Pt") != -1:
		xtitle = "p_{T} (GeV)"
		xmin = 200
		xmax = 4000 #1600
		if SetLogy:
			c.SetLogy()
		xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
	elif obj[i].find("Eta") != -1:
		xtitle = r"#eta"
		xmin = -3.0
		xmax = 3.0
		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
	elif obj[i].find("Phi") != -1:
		xtitle = r"#phi"
		xmin = -3.5
		xmax = 3.5
		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
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
			histos[i].GetFunction("pol0").SetLineColor(i+10)
			# Stats Box
			gStyle.SetOptFit(0) #set to 1 to turn on stats box for fit
			stats = histos[i].FindObject( "stats" )
			if not stats:
				#continue
				stats.__class__ = ROOT.TPaveStats
	#------------------------------
	# Overlay (Set to True to run this)
	# refer to lines 74-85 for list of canvases

	if overlay:
		if obj[i].find("photon1") or obj[i].find("photon2") !=1:
			if obj[i].find("Pt") != -1:
				countpT = countpT + 1
			        histos[i].SetLineColor(countpT)
				if countpT == 1:
					legpT = TLegend(xpos1, ypos1, xpos2, ypos2)
					legpT.SetBorderSize(0)
					legpT.SetFillColor(0)
					legpT.SetFillStyle(0)
					legpT.SetTextFont(42)
					legpT.SetTextSize(0.035)
				samePt.cd()
				if SetLogy:
					samePt.SetLogy()
				if h:
					histos[i].Draw("hist same")
				else:
					histos[i].Draw("same")

				legpT.AddEntry(histos[i], obj[i] ,"l")
				#legpT.Update()
				samePt.Update()

			if obj[i].find("Eta") != -1:
				countEtaAll = countEtaAll + 1
			        histos[i].SetLineColor(countEtaAll+1)
				if countEtaAll == 1:
					legEtaAll = TLegend(xpos1, ypos1, xpos2, ypos2)
					legEtaAll.SetBorderSize(0)
					legEtaAll.SetFillColor(0)
					legEtaAll.SetFillStyle(0)
					legEtaAll.SetTextFont(42)
					legEtaAll.SetTextSize(0.035)
				sameEtaAll.cd()
				if h:
					histos[i].Draw("hist same")
				else:
					histos[i].Draw("same")
				legEtaAll.AddEntry(histos[i], obj[i] ,"l")
				#legEtaAll.Update()
				sameEtaAll.Update()
			if obj[i].find("Phi") != -1:
				countPhiAll = countPhiAll + 1
			        histos[i].SetLineColor(countPhiAll+1)
				if countPhiAll == 1:
					legPhiAll = TLegend(xpos1, ypos1, xpos2, ypos2)
					legPhiAll.SetBorderSize(0)
					legPhiAll.SetFillColor(0)
					legPhiAll.SetFillStyle(0)
					legPhiAll.SetTextFont(42)
					legPhiAll.SetTextSize(0.035)
				samePhiAll.cd()
				if h:
					histos[i].Draw("hist same")
				else:
					histos[i].Draw("same")

				legPhiAll.AddEntry(histos[i], obj[i] ,"l")
				#legPhiAll.Update()
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
			c.Print("v1h%s.pdf" %(obj[i]))
		else:
			c.Print("v1%s.pdf" %(obj[i]))

	i = i+1

#-------------------------------------------

#-------------------------------------------
# Overlay Draw
if overlay:
	samePt.cd()
	legpT.SetEntrySeparation(0.3)
	legpT.Draw()

	sameEtaAll.cd()
	legEtaAll.SetEntrySeparation(0.3)
	legEtaAll.Draw()

	samePhiAll.cd()
	legPhiAll.SetEntrySeparation(0.3)
	legPhiAll.Draw()

	CMS_lumi(samePt, 4, 11, True)
	CMS_lumi(sameEtaAll, 4, 11, True)
	CMS_lumi(samePhiAll, 4, 11, True)
	samePt.Update()
	sameEtaAll.Update()
	samePhiAll.Update()
	samePt.Draw()
	sameEtaAll.Draw()
	samePhiAll.Draw()

	if h:
		samePt.Print("hsamePt.pdf")
		sameEtaAll.Print("hsameEtaAll.pdf")
		samePhiAll.Print("hsamePhiAll.pdf")
	else:
		samePt.Print("samePt.pdf")
		sameEtaAll.Print("sameEtaAll.pdf")
		samePhiAll.Print("samePhiAll.pdf")

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")
