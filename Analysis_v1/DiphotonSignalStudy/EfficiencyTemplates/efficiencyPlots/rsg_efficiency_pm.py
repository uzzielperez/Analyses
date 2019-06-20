from __future__ import division
import ROOT
from hep_plt.CMSlumi import CMS_lumi, set_CMS_lumi, CMS_Energy
from ROOT import *
import re
from array import array
from math import sin, sqrt

import csv

# --- FUNCTION DEFINITIONS
# have to use a dict for the MC_total
MC_total_dict = {750: 100000,
                 1250: 98000,
                 1500: 96000,
                 2500: 99000,
                 3000: 100000,
                 4250: 100000,
                 4500: 99026,
                 4750: 100000,
                 5000: 96000,
                 5750: 100000,
                 6000: 100000,
                 6500: 100000,
                 7000: 95002,
                 }

def readCSV_eff(inputfile):
	M, isGood_frac, Ntotal, NisEBEB, NisbEorEb, MC_total = [], [], [], [], [], []
	with open(inputfile, mode='r') as infile:
	    csv_file = csv.DictReader(infile)
	    row_num = 0
 	    for line in csv_file:
        	dset, ntotal,= line['Sample'], line['Ntotal']
		NisGood, isGoodfrac = line['NisGood'], line['isGoodfrac']
		nEBEB = line['nEBEB']
		nEBEEorEEEB = line['nEBEEorEEEB']
		nEEEE = line['nEEEE']
		npTcut = line['npTcut']
		#pattern = "GluGluSpin0ToGammaGamma_W_1p4_M_([^(]*)"
	        pattern = "RSGravitonToGammaGamma_kMpl01_M_([^(]*)"

		match = re.findall(pattern, dset)
		mass = int(match[0])
		M.append(mass)
		isGood_frac.append(double(isGoodfrac))
		Ntotal.append(int(ntotal))
		NisEBEB.append(int(nEBEB))
		NisbEorEb.append(int(nEBEEorEEEB))
		MC_total.append(MC_total_dict[mass])

	efficiency_isEBEB = array( 'd' )
	efficiency_isbEorEb = array( 'd')
	efficiency_tot = array('d')


	for ntotal, nb, neBoreB, e, mctotal in zip(Ntotal, NisEBEB, NisbEorEb, isGood_frac, MC_total):
		barrel_eff = nb*e/mctotal
    		endcap_barrel_eff = neBoreB*e/mctotal
   		total_eff = barrel_eff + endcap_barrel_eff
    		#print neBoreB, e, mctotal, neBoreB*e/mctotal, barrel_eff, endcap_barrel_eff
  	        efficiency_isEBEB.append(barrel_eff)
	        efficiency_isbEorEb.append(endcap_barrel_eff)
    		efficiency_tot.append(total_eff)

	gROOT.SetBatch()
	e_barrel_dict = {}
	e_EBorBE_dict = {}
	e_total_dict = {}

	for m, e1, e2, et in zip(M, efficiency_isEBEB, efficiency_isbEorEb, efficiency_tot):
   		#print e2
		e_barrel_dict[m] = e1
    		e_EBorBE_dict[m] = e2
    		e_total_dict[m] = et

	n = len(M)

	mass, e_barrel, e_EBorBE, etotal = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )
	M.sort()
	for mpt in M:
	    #print e_barrel_dict[mpt]
	    #print e_EBorBE_dict[mpt]
	    e_barrel.append(e_barrel_dict[mpt])
	    e_EBorBE.append(e_EBorBE_dict[mpt])
	    etotal.append(e_total_dict[mpt])
	    mass.append(mpt)

	return mass, e_barrel, e_EBorBE, etotal

def createTGraphError(N, m, e, ex, ey, color, linestyl):
	umin, umax = 0, 0.70
	xmin, xmax = 750, 7000

	gr = ROOT.TGraphErrors(n, mass, e, ex, ey)
	gr.SetLineColor( color )
	gr.SetLineWidth( 2 )
	gr.SetMarkerColor( color )
	gr.SetMarkerStyle(2)
	gr.SetLineStyle( linestyl )
	#gr.SetMarkerStyle( 21 )
	gr.SetMinimum(0.2)
	gr.SetTitle(r' ')
	# gr.GetXaxis().SetTitle( r'GluGluSpin0 m_X (GeV)' )
	gr.GetXaxis().SetTitle( r'RSGraviton m_X (GeV)' )

	#gr.GetYaxis().SetTitle( r'#epsilon #times A' )
        gr.GetYaxis().SetTitle( r'#epsilon #times A' )
	#gr.SetMinimum(0.2)
	gr.GetYaxis().SetRangeUser(umin, umax)
	gr.GetXaxis().SetRangeUser(xmin, xmax)

	return gr

def stddev(lst):
	mean = float(sum(lst)) / len(lst)
	return sqrt(sum((x - mean)**2 for x in lst) / len(lst))

def calcerror(data, mlist):
	Nlist = array('d', [MC_total_dict[n] for n in mlist] )
	err = array('d', [sqrt( e *(1-e)/n ) for e, n in zip(data, Nlist)] )
	#error = array('d', [s/sqrt(N) for s, N in zip(err, Nlist) ] )
	print err
	return err

# --- PROGRAM START ---

#in1 = 'rsg_75.csv'
#in2 = 'rsg_125.csv'
#in2 = 'LOG.csv'

in1, in2 = 'rsgE_ALOGpt75.csv', 'rsg_125.csv'
in0 = 'rsgE_ALOGpt0.csv'

mass, e_barrel, e_EBorBE, etotal = readCSV_eff( in1 )
mass125, e125_barrel, e125_EBorBE, e125total = readCSV_eff( in2 )
mass, e0_barrel, e0_EBorBE, e0total = readCSV_eff(in0)

print e_barrel
print e125_barrel

c1 = ROOT.TCanvas("c1", "Efficiency vs M", 200, 10, 550, 500)
#c1.SetFillColor( 42 )
#c1.SetGrid()
c1.cd()
pad1 = ROOT.TPad("pad1", "", 0, 0, 1, 1)
pad2 = ROOT.TPad("pad2", "", 0, 0, 1, 1)
pad3 = ROOT.TPad("pad3", "", 0, 0, 1, 1)
pad1_b = ROOT.TPad("pad1_b", "", 0, 0, 1, 1)
pad2_b = ROOT.TPad("pad2_b", "", 0, 0, 1, 1)
pad3_b = ROOT.TPad("pad3_b", "", 0, 0, 1, 1)
pad1_c = ROOT.TPad("pad1_c", "", 0, 0, 1, 1)
pad2_c = ROOT.TPad("pad2_c", "", 0, 0, 1, 1)
pad3_c = ROOT.TPad("pad3_c", "", 0, 0, 1, 1)
pad2.SetFillStyle(4000) # Make Transparent pad
pad2.SetFrameFillStyle(0)
pad3.SetFillStyle(4000) # Make Transparent pad
pad3.SetFrameFillStyle(0)
pad1_b.SetFillStyle(4000) # Make Transparent pad
pad1_b.SetFrameFillStyle(0)
pad2_b.SetFillStyle(4000) # Make Transparent pad
pad2_b.SetFrameFillStyle(0)
pad3_b.SetFillStyle(4000) # Make Transparent pad
pad3_b.SetFrameFillStyle(0)
pad1_c.SetFillStyle(4000) # Make Transparent pad
pad1_c.SetFrameFillStyle(0)
pad2_c.SetFillStyle(4000) # Make Transparent pad
pad2_c.SetFrameFillStyle(0)
pad3_c.SetFillStyle(4000) # Make Transparent pad
pad3_c.SetFrameFillStyle(0)

#mg = ROOT.TMultiGraph()

n = len(mass)
n125 = len(mass125)
n0 = n

err_t1 = calcerror(etotal, mass)
err_eb1 = calcerror(e_barrel, mass)
err_eborbe1 = calcerror(e_EBorBE, mass)
err_y1 = array('d', [0]*len(err_t1))
gr = createTGraphError(n, mass, e_barrel, err_eb1, err_y1, 2, linestyl=2)
gr_eb = createTGraphError(n, mass, e_EBorBE, err_eborbe1, err_y1, 4, linestyl=2)
gr_t = createTGraphError(n, mass, etotal, err_t1, err_y1, 1, linestyl=2)


err_t2 = calcerror(e125total, mass125)
err_eb2 = calcerror(e125_barrel, mass125)
err_eborbe2 = calcerror(e125_EBorBE, mass125)
err_y2 = array('d', [0]*len(err_t2))
gr125 = createTGraphError(n125, mass125, e125_barrel, err_eb2, err_y2, 2, linestyl=1)
gr_eb125 = createTGraphError(n125, mass125, e125_EBorBE, err_eborbe2, err_y2, 4, 1)
gr_t125 = createTGraphError(n125, mass125, e125total, err_eborbe2, err_y2, 1, 1 )

err_t0 = calcerror(e0total, mass)
err_eb0 = calcerror(e0_barrel, mass)
err_eborbe0 = calcerror(e0_EBorBE, mass)
err_y0 = array('d', [0]*len(err_t0))
gr0 = createTGraphError(n0, mass, e0_barrel, err_eb2, err_y2, 2, linestyl=3)
gr_eb0 = createTGraphError(n0, mass, e0_EBorBE, err_eborbe0, err_y0, 4, 3)
gr_t0 = createTGraphError(n0, mass, e0total, err_eborbe0, err_y0, 1, 3)


# Multipad solution
pad1.Draw()
pad1.cd()
gr.Draw(" APL ")
pad2.Draw()
pad2.cd()
gr_eb.Draw( ' APL ' )
pad3.Draw()
pad3.cd()
gr_t.Draw( ' APL ' )

pad1_b.Draw()
pad1_b.cd()
gr125.Draw( ' APL ')
pad2_b.Draw()
pad2_b.cd()
gr_eb125.Draw( ' APL ' )
pad3_b.Draw()
pad3_b.cd()
gr_t125.Draw( ' APL ' )

pad1_c.Draw()
pad1_c.cd()
gr0.Draw( ' APL ')
pad2_c.Draw()
pad2_c.cd()
gr_eb0.Draw( ' APL ' )
pad3_c.Draw()
pad3_c.cd()
gr_t0.Draw( ' APL ' )


leg = ROOT.TLegend(0.65, 0.3, 0.9, 0.6)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.SetHeader(r"#tilde{#kappa} = 0.01")
#leg.SetHeader(r"#frac{#Gamma_{x}}{m_{x}} = 0.01")

leg.AddEntry(gr, "EBEB pt75", "l")
leg.AddEntry(gr_eb, "EBEE pt75", "l")
leg.AddEntry(gr_t, "Total pt75", "l")
leg.AddEntry(gr125, "EBEB pt125", "l")
leg.AddEntry(gr_eb125, "EBEE pt125", "l")
leg.AddEntry(gr_t125, "Total pt125", "l")
leg.AddEntry(gr0, "EBEB", "l")
leg.AddEntry(gr_eb0, "EBEE", "l")
leg.AddEntry(gr_t0, "Total", "l")
leg.Draw()

# set_CMS_lumi(c1, 4, 0, 137)
CMS_Energy(c1, 0, E="13 TeV")
c1.Update()
c1.Modified()
c1.Update()
c1.Draw()

c1.SaveAs("rsg_efficiency_pm_sepAcceptance.pdf" )
