import ROOT
from ROOT import TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend, TRatioPlot
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import sys

def createHist(file_typ, color, obj_type):
    hDiphoton_Minv = file_typ.Get(obj_type)
    hDiphoton_Minv.SetLineColor(color) # kOrange + 7 for MC 
    hDiphoton_Minv.SetLineWidth(2)
    hDiphoton_Minv.GetYaxis().SetTitleSize(20)
    hDiphoton_Minv.GetYaxis().SetTitleFont(43)
    hDiphoton_Minv.GetYaxis().SetTitleOffset(1.55)
    hDiphoton_Minv.SetStats(0)
    #hDiphoton_MinvRight.SetAxisRange(450, 1050)
    return hDiphoton_Minv

def createRatio(h1, h2):
    #NEW
    gStyle.SetOptStat(0);
    
    #OLD
    h3 = h1.Clone("h3")
    h3.SetLineColor(kBlack)
    h3.SetMarkerStyle(21)
    h3.SetTitle(r"m_{#gamma#gamma}")
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
    #x.SetUserRange(250, 1000)
    x.SetTitleSize(40)
    x.SetTitleFont(43)
    x.SetTitleOffset(10.0)
    x.SetLabelFont(43)
    x.SetLabelSize(15)
    #OLD 
    
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
    #pad2.SetGridx()
    pad2.SetGridy()
    pad2.Draw()
    
    return c, pad1, pad2


