#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory

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
	
	# Histogram Name and Draw
	histos[i] = f.Get(obj[i])
	histos[i].GetXaxis().SetTitleOffset(1.4)
	histos[i].GetYaxis().SetTitleOffset(1.4)
	
	ytitle = "weighted events/ 80 GeV"
	histos[i].GetYaxis().SetTitle(ytitle)
	
	# ------for Minv
	#histos[i].GetXaxis().SetTitle(r"m_{#gamma#gamma} #scale[0.8]{(GeV)}") #problem here
	#histos[i].SetAxisRange(200, 1600)
	histos[i].Draw("hist")
	
	#Legend
	leg = TLegend(.60, 0.75, .97, .85) ###### NEEDS TO BE MODIFIED
	leg.SetBorderSize(0)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	leg.SetTextSize(0.035)
	leg.AddEntry(histos[i], obj[i] ,"l")
	leg.Draw()

	CMS_lumi(c[i], 4, 11, True) 

	c[i].SetLogy()
	c[i].Draw()
	#c[i].Print("BKGPlots.pdf[", "minv")
	#c[i].Print("BKGPlotsminv.pdf")
	c[i].Print("%s.png" %(obj[i]))

	i = i+1

#-------------------------------------------

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")
