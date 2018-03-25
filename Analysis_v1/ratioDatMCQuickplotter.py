#!/usr/bin/python

import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory

from legend import *

import sys  
CMSlumiPath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/pyroot'
sys.path.append(CMSlumiPath)  
from CMSlumi_ratio import CMS_lumi

#--------------------------------------------------------------------------------
MCpath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/GGJetsStudy'
DATApath = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/DoubleEGDataStudy'
mcfile = 'GGJets_histograms300-2000.root' 
datafile = 'DoubleEG_histograms300-2000.root'
#--------------------------------------------------------------------------------
# Timer 
sw = ROOT.TStopwatch()
sw.Start()

##########################################
# Extra Cosmetics
gStyle.SetOptStat(0)

#CMS_lumi( TPad* pad, int iPeriod=3, int iPosX=10 )
##########################################

f_mc = ROOT.TFile(MCpath+"/"+mcfile, "READ")
f_data = ROOT.TFile(DATApath+"/"+datafile, "READ")
 
#-----------------------------------------
# Plotting functions 
def createHist(file_typ, color, objtype): 
    hist = file_typ.Get(objtype) # e.g. DiphotonMinv
    hist.SetLineColor(color) # kOrange + 7 for MC 
    hist.SetLineWidth(2)
    hist.GetYaxis().SetTitleSize(20)
    hist.GetYaxis().SetTitleFont(43)
    hist.GetYaxis().SetTitleOffset(1.55)
    hist.SetStats(0)
    #hist.SetAxisRange(450, 1050)
    return hist

def createRatio(h1, h2):
    h3 = h1.Clone("h3")
    h3.SetLineColor(kBlack)
    h3.SetMarkerStyle(21)
    h3.SetTitle("RATIO")
    #h3.SetMinimum(0.8)
    #h3.SetMaximum(2.5)
    # Set up plot for markers and errors
    h3.Sumw2()
    h3.SetStats(0)
    h3.Divide(h2)

    # Adjust y-axis settings
    y = h3.GetYaxis()
    y.SetTitle("ratio %s/%s" %(h1, h2))
    #y.SetTitleOffset(4.55)
    #y = h3.GetYaxis()
    #y.SetTitle("ratio h1/h2 ")
    y.SetNdivisions(505)
    y.SetTitleSize(20)
    y.SetTitleFont(43)
    y.SetTitleOffset(1.55)
    y.SetLabelFont(43)
    y.SetLabelSize(15)

    # Adjust x-axis settings
    x = h3.GetXaxis()
    x.SetTitleSize(40)
    x.SetTitleFont(43)
    x.SetTitleOffset(10.0)
    x.SetLabelFont(43)
    x.SetLabelSize(15)

    return h3

def createCanvasPads():
    c = TCanvas("c", "canvas", 800, 800)
    # Upper histogram plot is pad1
    pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1.0)
    pad1.SetBottomMargin(0)  # joins upper and lower plot
    #pad1.SetGridx()
    pad1.SetLogy()
    pad1.Draw()
    # Lower ratio plot is pad2
    c.cd()  # returns to main canvas before defining pad2
    pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
    pad2.SetTopMargin(0)  # joins upper and lower plot
    pad2.SetBottomMargin(0.2)
    pad2.SetGridx()
    pad2.Draw()
    
    return c, pad1, pad2

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
# Arrays for Data and MC objects
ROOT.gROOT.SetBatch(True)
hMC = []
cMC = []
objMC = []

hDATA = []
cData = []
objData = []

# get obj and keys
for k, o in getall(f_mc):
    print "h_%s" %(k[1:]) 
    objMC.append(k[1:])
    cMC.append("c_%s"%(k[1:]))
    hmc = createHist(f_mc, kBlue+1, k[1:])
    hMC.append(hmc)
  
for kdata, odata in getall(f_data):
    print "h_%s" %(kdata[1:]) 
    objData.append(kdata[1:])
    cData.append("c_%s"%(kdata[1:]))
    hdata = createHist(f_data, kBlack, kdata[1:])
    hDATA.append(hdata)
print "objData", objData
print "objMC", objMC

# Looping over the root files 
i = 0
while i<len(objMC):
	
	# Create Histograms
	#hMC = createHist(f_mc, kBlue+1, objMC[i])
	#hDATA = createHist(f_data, kBlack, objData[i])
 	hRatio = createRatio(hDATA[i], hMC[i])
	c, pad1, pad2 = createCanvasPads()
#	c = ROOT.TCanvas()
	#--------------- String Finder	
	if objMC[i].find("Minv") != -1:
		xtitle = r"m_{#gamma#gamma} #scale[0.8]{(GeV)}"
		xmin = 200
		xmax = 1600
		scale = 39.5 
	        c.SetLogy()			
		xpos1, ypos1, xpos2, ypos2 = .72, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
	elif objMC[i].find("Pt") != -1:
		xtitle = "p_{T} (GeV)"
		xmin = 200
		xmax = 1600
		scale = 35.9
		c.SetLogy()	
		xpos1, ypos1, xpos2, ypos2 = .72, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85 
	elif objMC[i].find("Eta") != -1:
		xtitle = r"#eta" 
		xmin = -3.0
		xmax = 3.0
		scale = 35.9		
		xpos1, ypos1, xpos2, ypos2 = .72, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
	elif objMC[i].find("Phi") != -1:
		xtitle = r"#phi"
		xmin = -3.5
		xmax = 3.5
		scale = 35.9	
		xpos1, ypos1, xpos2, ypos2 = .72, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
	else:
		continue
	
	if objMC[i].find("diphoton") != -1:
		legentry = r"SM #gamma#gamma"
	elif (objMC[i].find("photon1")) != -1: 
		legentry = r"#gamma_{1}"
	elif (objMC[i].find("photon2")) != -1:
		legentry = r"#gamma_{2}"
	else:
		legentry = objMC[i]

        # Draw histos & additional Settings
	pad1.cd()
	hMC[i].Scale(scale) # rescale to 35.9 fb^-1
	hMC[i].SetFillColor(kBlue -3)
	hMC[i].SetTitle(objMC[i])
	hMC[i].GetYaxis().SetTitle("weighted Events")
	hMC[i].GetYaxis().SetTitleOffset(1.4)
	hDATA[i].GetXaxis().SetRangeUser(500, 1800)	

	hDATA[i].SetMarkerStyle(20)
	hDATA[i].Draw("esamex0")
	hMC[i].Draw("hist same")
	#to avoid clipping the bottom zero, redraw a small axis
	#hM.GetYaxis().SetLabelSize(0.0)
	#axis = TGaxis(-5, 20, -5, 220, 20, 220, 510, "")
	#axis.SetLabelFont(43)
	#axis.SetLabelSize(15)
	#axis.Draw()
	
	# Legend
	leg = TLegend(xpos1, ypos1, xpos2, ypos2)
	leg.SetBorderSize(0)
	leg.SetFillColor(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	leg.SetTextSize(0.035)
	leg.AddEntry(hMC[i], "MC", "f")
	leg.AddEntry(hDATA[i], "DATA", "l")
	leg.Draw()

        # RATIO  
	pad2.cd()
	hMC[i].GetYaxis().SetTitle("ratio %s/%s" %("MC", "DATA"))
	hRatio.GetXaxis().SetRangeUser(500, 1800) 
	y = hRatio.GetYaxis()
	y.SetTitle("Ratio")
	y.SetTitleSize(20)
	y.SetTitleFont(43)
	hRatio.Draw("ep")

	#Legend
	#leg = TLegend(xpos1, ypos1, xpos2, ypos2)
	#leg.SetBorderSize(0)
	#leg.SetFillColor(0)
	#leg.SetFillStyle(0)
	#leg.SetTextFont(42)
	#leg.SetTextSize(0.035)
	#leg.AddEntry(hMC, "MC", "lpf")
	#leg.AddEntry(hDATA, "DATA", "lpf")
	#leg.Draw()

	      
	#place_legend(c[i], None, None, None, None, header="", option="LP")
	CMS_lumi(c, 4, 11, False) 
	
	#c.Update()
	#c.Draw()
	#c.Print("BKGPlots.pdf[", "minv")
	#c.Print("BKGPlotsminv.pdf")		

	#Draw All canvases
	#from ROOT import gROOT 
	#gROOT.GetListOfCanvases().Draw() 		 
	#gROOT.GetListOfCanvases().Print("ratioplots/ratio%s/png" %(objMC[i]))		
	c.Print("%s/Ratio_%s.png" %("ratioplots",objMC[i]))

	# move to next object in root file
	i = i + 1
#-------------------------------------------

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")

