import ROOT
from hep_plt.CMSlumi import CMS_lumi, set_CMS_lumi, CMS_Energy
from ROOT import *
import re

# RSG Original
# M = [5750, 2500, 4250, 1250, 1500, 3000, 4750, 5000, 6500, 750, 6000, 7000]
#
# Ntotal = [81181, 73804, 79273, 66793, 67054, 76326, 80211, 77228, 81650, 63565, 81285, 77175]
# isGood_frac = [0.908, 0.887, 0.898, 0.879, 0.880, 0.892, 0.904, 0.904, 0.910, 0.878, 0.909, 0.912]
# NisEBEB = [70211, 53424, 64944, 39251, 41677, 57731, 67287, 65380, 71575, 33105, 70711, 68184]
# NisbEorEb = [2790, 10435, 5205, 17424, 15396, 8715, 4267, 3550, 1978, 20314, 2466, 1529]
# MC_total = [100000, 99000, 100000, 98000, 96000, 100000, 100000, 96000, 100000, 100000, 100000, 95002]



import csv
# inputfile = 'RSG75.csv'
# inputfile = 'RSG125.csv'
inputfile = 'RSG75_AN.csv'
#inputfile = 'RSG125_AN.csv'
#inputfile = 'RSGdefault.csv'

M, isGood_frac, Ntotal, NisEBEB, NisbEorEb, MC_total = [], [], [], [], [], []

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
                 750: 100000,
                 }

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

        pattern = "RSGravitonToGammaGamma_kMpl01_M_([^(]*)"
        match = re.findall(pattern, dset)
        mass = int(match[0])
        M.append(mass)
        isGood_frac.append(double(isGoodfrac))
        Ntotal.append(int(ntotal))
        NisEBEB.append(int(nEBEB))
        NisbEorEb.append(int(nEBEEorEEEB))
        MC_total.append(MC_total_dict[mass])

        #print dset, ntotal, NisGood, isGoodfrac, nEBEB, nEBEEorEEEB, nEEEE, npTcut

#print len(M), len(MC_total)
#print M, isGood_frac
print M
print Ntotal
print isGood_frac
print NisEBEB
print NisbEorEb
print MC_total

efficiency_isEBEB = []
efficiency_isbEorEb = []
efficiency_tot = []

for ntotal, nb, neBoreB, e, mctotal in zip(Ntotal, NisEBEB, NisbEorEb, isGood_frac, MC_total):
    barrel_eff = nb*e/mctotal
    endcap_barrel_eff = neBoreB*e/mctotal
    total_eff = barrel_eff + endcap_barrel_eff
    efficiency_isEBEB.append(barrel_eff)
    efficiency_isbEorEb.append(endcap_barrel_eff)
    efficiency_tot.append(total_eff)

from array import array
from math import sin
gROOT.SetBatch()
e_barrel_dict = {}
e_EBorBE_dict = {}
e_total_dict = {}

for m, e1, e2, et in zip(M, efficiency_isEBEB, efficiency_isbEorEb, efficiency_tot):
    e_barrel_dict[m] = e1
    e_EBorBE_dict[m] = e2
    e_total_dict[m] = et

n = len(M)
mass, e_barrel, e_EBorBE, etotal = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )

M.sort()
for mpt in M:
    e_barrel.append(e_barrel_dict[mpt])
    e_EBorBE.append(e_EBorBE_dict[mpt])
    etotal.append(e_total_dict[mpt])
    mass.append(mpt)

c1 = ROOT.TCanvas("c1", "Efficiency vs M", 200, 10, 550, 500)
#c1.SetFillColor( 42 )
#c1.SetGrid()
c1.cd()
pad1 = ROOT.TPad("pad1", "", 0, 0, 1, 1)
pad2 = ROOT.TPad("pad2", "", 0, 0, 1, 1)
pad3 = ROOT.TPad("pad2", "", 0, 0, 1, 1)
pad2.SetFillStyle(4000) # Make Transparent pad
pad2.SetFrameFillStyle(0)
pad3.SetFillStyle(4000) # Make Transparent pad
pad3.SetFrameFillStyle(0)
mg = ROOT.TMultiGraph()

umin, umax = 0, 0.70
xmin, xmax = 750, 7000

gr = ROOT.TGraph(n, mass, e_barrel)
gr.SetLineColor( 2 )
gr.SetLineWidth( 2 )
gr.SetMarkerColor( 4 )
gr.SetLineStyle(2)
#gr.SetMarkerStyle( 21 )
gr.SetMinimum(0.2)
gr.SetTitle(r' ')
gr.GetXaxis().SetTitle( r'RSGraviton m_X (GeV)' )
gr.GetYaxis().SetTitle( r'#epsilon #times A' )
#gr.SetMinimum(0.2)
gr.GetYaxis().SetRangeUser(umin, umax)
gr.GetXaxis().SetRangeUser(xmin, xmax)

gr_eb = ROOT.TGraph(n, mass, e_EBorBE)
gr_eb.SetLineColor( 4 )
gr_eb.SetLineWidth( 2 )
gr_eb.SetLineStyle( 2 )
gr_eb.SetMarkerColor( 4 )
#gr_eb.SetMarkerStyle( 21 )
gr_eb.GetYaxis().SetRangeUser(umin, umax)
gr_eb.GetXaxis().SetRangeUser(xmin, xmax)
gr_eb.SetTitle(r' ')

gr_t = ROOT.TGraph(n, mass, etotal)
gr_t.SetLineColor( 1 )
gr_t.SetLineWidth( 2 )
gr_t.SetLineStyle( 2 )
gr_t.SetMarkerColor( 4 )
#gr_t.SetMarkerStyle( 21 )
gr_t.GetYaxis().SetRangeUser(umin, umax)
gr_t.GetXaxis().SetRangeUser(xmin, xmax)
gr_t.SetTitle(r' ')

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


leg = ROOT.TLegend(0.65, 0.3, 0.9, 0.6)
leg.SetBorderSize(0)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.SetTextSize(0.035)
leg.SetHeader(r"#tilde{#kappa} = 0.01")
leg.AddEntry(gr, "EBEB", "l")
leg.AddEntry(gr_eb, "EBEE", "l")
leg.AddEntry(gr_t, "Total", "l")
leg.Draw()

# set_CMS_lumi(c1, 4, 0, 137)
CMS_Energy(c1, 0, E="13 TeV")
c1.Update()
#c1.GetFrame().SetFillColor(21)
#c1.GetFrame().SetBorderSize(12)
c1.Modified()
c1.Update()
c1.Draw()
tag = inputfile[3:-4]
c1.SaveAs("rsg_eff_cms_750-7000_%s.pdf" %(tag))
