import ROOT
from ROOT import TClass,TKey, TIter,TCanvas, TPad, TFile, TPaveText, TColor, TGaxis, TH1F, TPad, TH1D, TLegend
from ROOT import kBlack, kBlue, kRed
from ROOT import gBenchmark, gStyle, gROOT, gDirectory
import re
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

def makeList(ListName):
    ListName = []
    return ListName

def LoopObjKeys(fileAssign, obj_i, canvas_i, hist_i, index):
    for k, o in getall(fileAssign):
        print "h_%s" %(k[1:])
        obj_i.append(k[1:])
        canvas_i.append("c_%s"%(k[1:]))
        histFi = createHist(fileAssign, index+1 , k[1:])
        hist_i.append(histFi)
        #print "obj: %s" %(String(index)), obj_i[index]

#def regexHelper(expTarget, WholeExpression, sec):

#     regex = (r'%s\s+(.*)'%(expTarget))
#     match = re.findall(regex, WholeExpression)
#
#     #match = match[0].split(" ")
#     #print regex, WholeExpression

#def diphotonAnalysisStringFinder(objEL):

def LoopOverHistogramsPerFile(study, obj_f1, h, listofFiles, canv, outName, isMD):
    i = 0
    while i<len(obj_f1):
    	ytitle = "Events"
        canv[i] = ROOT.TCanvas()
    	#c, pad1, pad2 = createCanvasPads()
    	scale = 1.00
	countMinv = 0
	countpt = 0
	countEta = 0
	countPhi = 0  
	#c.cd()
    	#--------------- String Finder
    	if obj_f1[i].find("Minv") != -1:
    		xtitle =   r"m_{#gamma#gamma}#scale[0.8]{(GeV)}" # r"#scale[0.8]{m_{#gamma#gamma}(GeV)}"
           	xmin = 0
           	xmax = 11000
    		#scale = 35.9
                SetLogy = True
    	    	#c.SetLogy()
    		xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
		countMinv = countMinv +1 
	#if obj[i].find("photon1") or obj[i].find("photon2") !=1:   
 	elif obj_f1[i].find("Pt") != -1:
    		xtitle = "#scale[0.8]{p_{T}(GeV)}"
    		xmin = 75
    		xmax = 4000
    		#scale = 35.9
                SetLogy = True
    		#c.SetLogy()
		#countpt = countpt +1
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
                SetLogy = False
    		xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
		#countEta = countEta+1
    	elif obj_f1[i].find("Phi") != -1:
    		xtitle = r"#phi"
    		if obj_f1[i].find("sc") != -1:
    			xtitle = r"#scale[0.7]{sc} " + xtitle
    		if obj_f1[i].find("det") != -1:
    			xtitle = r"#scale[0.7]{det} " + xtitle
    		xmin = -3.5
    		xmax = 3.5
    		#scale = 35.9
                SetLogy = False
		#countPhi = countPhi + 1 
    		xpos1, ypos1, xpos2, ypos2 = .40, 0.75, 1.0, .85
    	else:
    		continue

    	if obj_f1[i].find("diphoton") != -1:
		#ocount = ocount + 1
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

         # Draw All the Histograms in the List of Files
        FileNum = 0
        #h[FileNum][i].Scale(scale)
        h[FileNum][i].SetTitle(obj_f1[i])
        h[FileNum][i].GetYaxis().SetTitle("Weighted Events")
        h[FileNum][i].GetYaxis().SetTitleOffset(1.1)
        h[FileNum][i].GetXaxis().SetRangeUser(xmin, xmax)
	leg = TLegend(xpos1, ypos1, xpos2, ypos2)
	leg.SetBorderSize(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	leg.SetTextSize(0.035)	
        
	while FileNum < len(listofFiles):
		canv[i].cd()
		if SetLogy:
			canv[i].SetLogy()		
		h[FileNum][i].SetLineColor(FileNum+2)
		h[FileNum][i].Draw("hist same")
        	if isMD:
			pattern = r'MD/(.*)'	
			match = re.findall(pattern, listofFiles[FileNum])
        		leg.AddEntry(h[FileNum][i], "LambdaT-%s" %(match[0]), "l")
		else:
			pattern = r'LambdaT-([^(]*)\_M-500'		
			match = re.findall(pattern, listofFiles[FileNum])
        		leg.AddEntry(h[FileNum][i], "LambdaT-%s" %(match[0]), "l")	
		#hf2[i].SetMarkerStyle(20)
		leg.Draw()
		leg.SetEntrySeparation(0.3)
		canv[i].Update()
          
	        FileNum = FileNum + 1
		print "filenum: ", FileNum	
	#CMS_lumi(c, 4, 11, False)
	leg.SetEntrySeparation(0.3)
	#leg.Draw() 
   	canv[i].Print("%s/%s%sratio_%s.png" %("ratioplots",outName, study, obj_f1[i]))

    	# move to next object in root file
    	i = i + 1
