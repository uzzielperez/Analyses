#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend, TLine
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
from plotsHelper import *

import sys
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)
from CMSlumi import CMS_lumi, set_CMS_lumi
import argparse

#filename = 'HEM15-16.root'
#filename = 'HEM15-16_data.root'
filename = 'Chris_HEM15-16_data.root'
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
#
## Basic Plotting Template
#i = 0
#while i<len(histos):
#	c = ROOT.TCanvas()
#
#	if "HEM" in obj[i]:
#		Region = "HEM"
#	elif "HEP" in obj[i]:
#		Region = "HEP"
#	if obj[i].find("Eta") != -1:
#		xtitle = r"#eta"
#		xmin = -3.0
#		xmax = 3.0
#		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
#		if "Post" in obj[i]:
#			legentry = "Post%s-Eta" %(Region)
#			lumival = 6.612
#		elif "Pre" in obj[i]:
#			legentry = "Pre%s-Eta" %(Region)
#			lumival = 20.315
##		etamax_line = TLine(-1.392,0,-1.392, 20)
##		etamax_line.SetLineColor(kRed)
##		etamax_line.Draw()
##		etamin_line = TLine(-3,0,-3,20)
##		etamin_line.SetLineColor(kRed)
##		etamin_line.Draw()
#	elif obj[i].find("Phi") != -1:
#		xtitle = r"#phi"
#		xmin = -3.5
#		xmax = 3.5
#		xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
#		if "Post" in obj[i]:
#			legentry = "Post%s-Phi" %(Region)
#			lumival = 6.612
#		elif "Pre" in obj[i]:
#			legentry = "Pre%s-Phi" %(Region)
#	 		lumival = 20.315
#	# Histogram Name and Draw
#	histos[i] = f.Get(obj[i])
#	histos[i].GetXaxis().SetTitleOffset(1.2)
#	histos[i].GetYaxis().SetTitleOffset(1.2)
#
#	ytitle = "weighted events"
#	histos[i].GetYaxis().SetTitle(ytitle)
#
#	histos[i].GetXaxis().SetTitle(xtitle)
#	histos[i].SetAxisRange(xmin, xmax)
#
#	if DrawAsHist:
#		histos[i].Draw("hist")
#	else:
#		histos[i].Draw()
#
#	leg = TLegend(xpos1, ypos1, xpos2, ypos2)
#	leg.SetBorderSize(0)
#	leg.SetFillColor(0)
#	leg.SetFillStyle(0)
#	leg.SetTextFont(42)
#	leg.SetTextSize(0.035)
#	leg.AddEntry(histos[i], legentry ,"l")
#	leg.Draw()
#
#        set_CMS_lumi(c, 4, 11, lumival)
#
#	c.Update()
#	c.Draw()
#
#	if DrawAsHist:
#		c.Print("HEM15-16_h%s.png" %(obj[i]))
#	else:
#		c.Print("HEM15-16%s.png" %(obj[i]))
#
#	i = i + 1

#Special Plots

def compare_hist(f, obj1, obj2, angle):
	canvas = ROOT.TCanvas()
	h1 = f.Get(obj1)
	h2 = f.Get(obj2)
        xtitle, minx, maxx, SetLogy, xpos1, ypos1, xpos2, ypos2 =  objSettings(obj1)

	if "Eta" in angle:
		xmin, xmax = -4, 4
	elif "Phi" in angle:
		xmin, xmax = -3.5, 3.5
        h1.GetYaxis().SetTitle("Events")
        h1.GetXaxis().SetTitle(xtitle)
	h1.SetAxisRange(xmin, xmax)
	h1.SetLineColor(kBlue)
	#h2.SetLineColor(kRed)
	h1.SetMarkerStyle(3)
	h2.SetMarkerStyle(2)
	h1.SetFillColor(7)
	h2.SetFillColor(42)
	h2.SetFillStyle(3013)
	h1.Draw("hist, e")
    	h2.Draw("hist, e, same")

	#xpos1, ypos1, xpos2, ypos2 = .30, 0.20, .70, .38

	leg = TLegend(xpos1, ypos1, xpos2, ypos2)
	leg.SetBorderSize(0)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	leg.SetTextSize(0.035)
	leg.AddEntry(h1, obj1 ,"l")
	leg.AddEntry(h2, obj2, "l")
	leg.Draw()

	set_CMS_lumi(canvas, 4, 11, "1")
	canvas.Update()
	canvas.Draw()
	canvas.Print("HEM15-16_%s.png" %(angle))

compare_hist(f, "photonsEta_PreHEM", "photonsEta_PostHEM", "Eta_PrevsPost")
#compare_hist(f, "photon1Eta_PreHEM", "photon1Eta_PostHEM", "Eta1_PrevsPost")
#compare_hist(f, "photon2Eta_PreHEM", "photon2Eta_PostHEM", "Eta2_PrevsPost")

#compare_hist(f, "photon1Phi_PreHEM", "photon1Phi_PostHEM", "Phi1_PrevsPost")
#compare_hist(f, "photon2Phi_PreHEM", "photon2Phi_PostHEM", "Phi2_PrevsPost")
compare_hist(f, "photonsPhi_PreHEM", "photonsPhi_PostHEM", "Phi_PrevsPost")


#compare_hist(f, "photon1Phi_PostHEM", "photon1Phi_PostHEP", "Phi1_HEMvsHEP")
#compare_hist(f, "photon2Phi_PostHEM", "photon2Phi_PostHEP", "Phi2_HEMvsHEP")
compare_hist(f, "photonsPhi_PostHEM", "photonsPhi_PostHEP", "Phi_HEMvsHEP")

compare_hist(f, "photons_scPhi_PreHEM", "photons_scPhi_PostHEM", "scPhi_PrevsPost")
compare_hist(f, "photons_scPhi_PostHEM", "photons_scPhi_PostHEP", "scPhi_HEMvsHEP")


sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")
