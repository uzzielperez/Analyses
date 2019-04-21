import ROOT

M = [5750, 2500, 4250, 1250, 1500, 3000, 4750, 5000, 6500]
isGood_frac = [0.908, 0.887, 0.898, 0.879, 0.880, 0.892, 0.904, 0.904, 0.910]
Ntotal = [81181, 73804, 79273, 66793, 67054, 76326, 80211, 77228, 81650]
NisEBEB = [70211, 53424, 64944, 39251, 41677, 57731, 67287, 65380, 71575]
NisbEorEb = [2790, 10435, 5205, 17424, 15396, 8715, 4267, 3550, 1978]
MC_total = [100000, 99000, 100000, 98000, 96000, 100000, 100000, 96000, 100000]

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

c1 = ROOT.TCanvas("c1", "Efficiency vs M", 200, 10, 700, 500)
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

umin, umax = 0, 0.8

gr = ROOT.TGraph(n, mass, e_barrel)
gr.SetLineColor( 2 )
gr.SetLineWidth( 2 )
gr.SetMarkerColor( 4 )
#gr.SetMarkerStyle( 21 )
gr.SetMinimum(0.2)
gr.SetTitle(r' CMS Simulation')
gr.GetXaxis().SetTitle( r'm_X (GeV)' )
gr.GetYaxis().SetTitle( r'#epsilon #times A' )
#gr.SetMinimum(0.2)
gr.GetYaxis().SetRangeUser(umin, umax) 

gr_eb = ROOT.TGraph(n, mass, e_EBorBE)
gr_eb.SetLineColor( 3 )
gr_eb.SetLineWidth( 2 )
gr_eb.SetLineStyle( 2 )
gr_eb.SetMarkerColor( 4 )
#gr_eb.SetMarkerStyle( 21 )
gr_eb.GetYaxis().SetRangeUser(umin, umax)
gr_eb.SetTitle(r' CMS Simulation')

gr_t = ROOT.TGraph(n, mass, etotal)
gr_t.SetLineColor( 1 )
gr_t.SetLineWidth( 2 )
gr_t.SetLineStyle( 2 )
gr_t.SetMarkerColor( 4 )
#gr_t.SetMarkerStyle( 21 )
gr_t.GetYaxis().SetRangeUser(umin, umax)
gr_t.SetTitle(r' CMS Simulation')

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
leg.SetHeader(r"RSG #tilde{#kappa} = 0.01")
leg.AddEntry(gr, "EBEB", "l")
leg.AddEntry(gr_eb, "EBEE", "l")
leg.AddEntry(gr_t, "Total", "l")
leg.Draw() 

# Multigraph solution
#gr.GetYaxis.SetRangeUser(0,1)
#gr_eb.GetYaxis.SetRangeUser(0,1)
#mg.Add(gr, "AP")
#mg.Add(gr_eb, "AP")


c1.Update()
#c1.GetFrame().SetFillColor(21)
#c1.GetFrame().SetBorderSize(12)
c1.Modified()
c1.Update()
c1.Draw()
c1.SaveAs("rsg_eff.pdf")
