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

study = "Pythia-Sherpa-NED-4_Ms_4000"
#--------------------------------------------------------------------------------
path1 = "/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/ADDGravToGGSherpaStudy"
path2 = '/uscms_data/d3/cuperez/CMSSW_8_0_25/src/scripts/Analysis_v1/ADDGravToGGPythiaStudy'
File1 = "ADDGravToGGSherpa_histo_M-200-4000.root"
File2 = "wADDGravToGGPythia_histo_M-200-4000.root" #This is a test file on weights
#File2 = "ADDGravToGGPythia_histo_M-200-4000.root"
#File2 =  "CADDGravToGGPythia_histo_M-200-4000-etaCut.root"

fileDescription1 = "Sherpa-Ms-4000-4ED-GRW"
#fileDescription2 = "Pythia-Ms-4000-4ED-GRW-EtaCut"
fileDescription2 = "Pythia-Ms-4000-4ED-GRW"
#--------------------------------------------------------------------------------
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

f_f1 = ROOT.TFile(path1+"/"+File1, "READ")
f_f2 = ROOT.TFile(path2+"/"+File2, "READ")
 
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
    pad2.SetGridy()
    #pad2.SetGridx()
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

# Arrays for file objects
ROOT.gROOT.SetBatch(True)
hf1 = []
c_f1 = []
obj_f1 = []

hf2 = []
c_f2 = []
obj_f2 = []

# get obj and keys
for k, o in getall(f_f1):
    print "h_%s" %(k[1:]) 
    obj_f1.append(k[1:])
    c_f1.append("c_%s"%(k[1:]))
    h_F1 = createHist(f_f1, kBlue+1, k[1:])
    hf1.append(h_F1)
  
for kdata, odata in getall(f_f2):
    print "h_%s" %(kdata[1:]) 
    obj_f2.append(kdata[1:])
    c_f2.append("c_%s"%(kdata[1:]))
    h_F2 = createHist(f_f2, kBlack, kdata[1:])
    hf2.append(h_F2)
print "obj_f2", obj_f2
print "obj_f1", obj_f1

# Looping over the root files 
i = 0
while i<len(obj_f1):
	ytitle = "Events"	
	# Create Histograms
	#hf1 = createHist(f_f1, kBlue+1, obj_f1[i])
	#hf2 = createHist(f_f2, kBlack, obj_f2[i])
	c, pad1, pad2 = createCanvasPads()
#	c = ROOT.TCanvas()
	scale = 1.00 # already reweighted to 35.92
	#--------------- String Finder	
	if obj_f1[i].find("Minv") != -1:
		xtitle =   r"m_{#gamma#gamma}#scale[0.8]{(GeV)}" # r"#scale[0.8]{m_{#gamma#gamma}(GeV)}"
		xmin = 500
		xmax = 4000
		#scale = 35.9 
	        c.SetLogy()				
		xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .72, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
	elif obj_f1[i].find("Pt") != -1:
		xtitle = "#scale[0.8]{p_{T}(GeV)}"
		xmin = 75
		xmax = 4000
		#scale = 35.9
		c.SetLogy()	
		xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85 
	elif obj_f1[i].find("Eta") != -1:
		xtitle = r"#eta"
		if obj_f1[i].find("sc") != -1:
			xtitle = r"#scale[0.7]{sc} " + xtitle 
		if obj_f1[i].find("det") != -1:
			xtitle = r"#scale[0.7]{det} " + xtitle
		xmin = -3.0
		xmax = 3.0
		#scale = 35.9		
		xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
	elif obj_f1[i].find("Phi") != -1:
		xtitle = r"#phi"
		if obj_f1[i].find("sc") != -1:
			xtitle = r"#scale[0.7]{sc} " + xtitle
		if obj_f1[i].find("det") != -1:
			xtitle = r"#scale[0.7]{det} " + xtitle
		xmin = -3.5
		xmax = 3.5
		#scale = 35.9	
		xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .60, 0.65, 1.0, .85
		#xpos1, ypos1, xpos2, ypos2 = .45, 0.20, .85, .38
	else:
		continue
	
	if obj_f1[i].find("diphoton") != -1:
		legentry = r"SM #gamma#gamma"
	elif (obj_f1[i].find("photon1")) != -1: 
		legentry = r"#gamma_{1}"
	elif (obj_f1[i].find("photon2")) != -1:
		legentry = r"#gamma_{2}"
	else:
		legentry = obj_f1[i]

	# EBEE or EBEB 
	if obj_f1[i].find("EBEE") != -1:
		xtitle = xtitle + r" #scale[0.45]{(EBEE)}"
	if obj_f1[i].find("EBEB") != -1:
		xtitle = xtitle + r" #scale[0.45]{(EBEB)}"
	# Photon1 or Photon2
	if obj_f1[i].find("photon1") != -1:	
		xtitle = r"#scale[0.80]{#gamma_{1}: }" + xtitle 
	if obj_f1[i].find("photon2") != -1:	
		xtitle = r"#scale[0.80]{#gamma_{2}: }" + xtitle 

        # Draw histos & additional Settings
	pad1.cd()
	hf1[i].Scale(scale) # rescale to 35.9 fb^-1
	hf1[i].SetFillColor(kBlue -3)
	hf1[i].SetTitle(obj_f1[i])
	#hf1[i].GetYaxis().SetTitle("weighted Events")
	hf1[i].GetYaxis().SetTitleOffset(1.4)
	hf1[i].GetXaxis().SetRangeUser(xmin, xmax)
	hf2[i].GetXaxis().SetRangeUser(xmin, xmax)	
	hf2[i].GetYaxis().SetTitle("Events") 
	hf2[i].SetMarkerStyle(20)
	
	hf2[i].Draw(s2)  # Draw this to set max y
	hf1[i].Draw(s1)
	hf2[i].Draw(s2) # To draw over filled MC

#	hf2[i].Draw("esamex0")  # Draw this to set max y
#	hf1[i].Draw("hist same")
#	hf2[i].Draw("esamex0") # To draw over filled MC
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
	leg.AddEntry(hf1[i], "%s" %(fileDescription1), "f")
	leg.AddEntry(hf2[i], "%s" %(fileDescription2), "l")
	leg.Draw()

 	hRatio = createRatio(hf2[i], hf1[i])
        # RATIO  
	pad2.cd()
	hf1[i].GetYaxis().SetTitle("ratio %s/%s" %(fileDescription1, fileDescription2))
	#hRatio.GetXaxis().SetRangeUser(xmin, xmax)
	x = hRatio.GetXaxis()
	x.SetRangeUser(xmin, xmax)
	x.SetTitleOffset(2.5)
	x.SetTitleSize(35)
	x.SetTitle(xtitle) 
	y = hRatio.GetYaxis()
	y.SetTitle("Ratio")
	y.SetTitleSize(20)
	y.SetTitleFont(43)
	hRatio.Draw("ep")
	      
	#place_legend(c[i], None, None, None, None, header="", option="LP")
	CMS_lumi(c, 4, 11, False) 
	
	#c.Update()
	#c.Draw()
	#c.Print("BKGPlots.pdf[", "minv")
	#c.Print("BKGPlotsminv.pdf")		

	#Draw All canvases
	#from ROOT import gROOT 
	#gROOT.GetListOfCanvases().Draw() 		 
	#gROOT.GetListOfCanvases().Print("ratioplots/ratio%s/png" %(obj_f1[i]))		
	c.Print("%s/%sratio_%s.png" %("ratioplots",study, obj_f1[i]))

	# move to next object in root file
	i = i + 1
#-------------------------------------------

sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"

raw_input("Press enter to continue...")

