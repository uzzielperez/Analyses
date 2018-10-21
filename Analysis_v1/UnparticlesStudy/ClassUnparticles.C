#define ClassUnparticles_cxx
#include "ClassUnparticles.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void ClassUnparticles::Loop()
{
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();
   //counters
 	int Ntotal      = 0;
 	int nDiphMinv   = 0;
 	int netaCut     = 0;

  //histograms
  TH1D* gendiphotonMinv = new TH1D("gendiphotonMinv", "", 50, 0., 250.);// 100, 0, 10000
  TH1D* genphoton1Pt    = new TH1D("genphoton1Pt", "", 1000, 0., 10000.);//
  TH1D* genphoton2Pt    = new TH1D("genphoton2Pt", "", 1000, 0., 10000.);
  TH1D* genphoton1Eta   = new TH1D("genphoton1Eta", "", 80, -3.0, 3.0);
  TH1D* genphoton2Eta   = new TH1D("genphoton2Eta", "", 80, -3.0, 3.0);
  TH1D* genphoton1Phi   = new TH1D("genphoton1Phi", "", 80, -3.5, 3.5);
  TH1D* genphoton2Phi   = new TH1D("genphoton2Phi", "", 80, -3.5, 3.5);
  TH1D* gendiphotoncosthetastar = new TH1D("gendiphotoncosthetastar", "", 100, -1.0, 1.0);

  gendiphotonMinv->Sumw2();
  genphoton1Pt->Sumw2();
  genphoton2Pt->Sumw2();
  genphoton1Eta->Sumw2();
  genphoton2Eta->Sumw2();
  genphoton1Phi->Sumw2();
  genphoton2Phi->Sumw2();
  gendiphotoncosthetastar->Sumw2();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      Ntotal++;
      double weight = 1.00;
      gendiphotonMinv->Fill(GenDiPhoton_Minv, weight);
    	genphoton1Pt->Fill(GenPhoton1_pt, weight);
    	genphoton2Pt->Fill(GenPhoton2_pt, weight);
    	genphoton1Eta->Fill(GenPhoton1_eta, weight);
    	genphoton2Eta->Fill(GenPhoton2_eta, weight);
    	genphoton1Phi->Fill(GenPhoton1_phi, weight);
    	genphoton2Phi->Fill(GenPhoton2_phi, weight);
      gendiphotoncosthetastar->Fill(GenDiPhoton_cosThetaStar, weight);
   }
   cout << endl;
   cout << "Total entries            : " << Ntotal    << " " << nentries << endl;
   //cout << "Passed DiphMinv cut      : " << nDiphMinv << endl;
   //cout << "Passed etaCut            : " << netaCut   << endl;
   cout << endl;

   //TFile file_out("Unparticles106.root", "RECREATE");
   //TFile file_out("Unparticles109.root", "RECREATE");
   //TFile file_out("Unparticles2x1.root", "RECREATE");
   TFile file_out("Unparticles106_LambdaU-1000.root", "RECREATE");
   //TFile file_out("Unparticles10_LambdaU-1000.root", "RECREATE");
   //TFile file_out("Unparticles2x1_LambdaU-1000.root", "RECREATE");
   cout << "Writing file.." << endl;
   gendiphotonMinv->Write();
   genphoton1Pt->Write();
   genphoton2Pt->Write();
   genphoton1Eta->Write();
   genphoton2Eta->Write();
   genphoton1Phi->Write();
   genphoton2Phi->Write();
   gendiphotoncosthetastar->Write();
}
