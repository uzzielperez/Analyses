#define ClassRSG_cxx
#include "ClassRSG.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void ClassRSG::Loop()
{

   if (fChain == 0) return;
   Long64_t nentries = fChain->GetEntriesFast();
   //counters
 	int Ntotal      = 0;
 	int nDiphMinv   = 0;
 	int netaCut     = 0;
  int numevents   = 10000;


    //histograms
  	TH1D* gendiphotonMinv = new TH1D("gendiphotonMinv", "", 1000, 0., 10000.);// 100, 0, 10000
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

    //TString fileout_name = "RSG_kMpl02_M_750_py_GEN.root"; double xsec = 20.89;
    //TString fileout_name = "RSG_kMpl02_M_1000_py_GEN.root"; double xsec = 4.892;
    //TString fileout_name = "RSG_kMpl02_M_1250_py_GEN.root"; double xsec = 1.452;
    //TString fileout_name = "RSG_kMpl02_M_1500_py_GEN.root"; double xsec = 0.5167;
    //TString fileout_name = "RSG_kMpl02_M_1750_py_GEN.root"; double xsec = 0.2042;
    //TString fileout_name = "RSG_kMpl02_M_2000_py_GEN.root"; double xsec = 0.08850;
    //TString fileout_name = "RSG_kMpl02_M_2250_py_GEN.root"; double xsec = 0.04038;
    //TString fileout_name = "RSG_kMpl02_M_2500_py_GEN.root"; double xsec = 0.01957;
    //TString fileout_name = "RSG_kMpl02_M_3000_py_GEN.root"; double xsec = 0.005003;
    //TString fileout_name = "RSG_kMpl02_M_3500_py_GEN.root"; double xsec = 0.001413;
    //TString fileout_name = "RSG_kMpl02_M_4000_py_GEN.root"; double xsec = 0.0004246;
    //TString fileout_name = "RSG_kMpl02_M_4500_py_GEN.root"; double xsec = 0.0001356;
    //TString fileout_name = "RSG_kMpl02_M_4750_py_GEN.root"; double xsec = 0.00007651;
    //TString fileout_name = "RSG_kMpl02_M_5000_py_GEN.root"; double xsec = 0.0000444;
    //TString fileout_name = "RSG_kMpl02_M_5250_py_GEN.root"; double xsec = 0.00002617;
    //TString fileout_name = "RSG_kMpl02_M_5500_py_GEN.root"; double xsec = 0.00001577;
    //TString fileout_name = "RSG_kMpl02_M_5750_py_GEN.root"; double xsec = 0.000009680;
    //TString fileout_name = "RSG_kMpl02_M_6000_py_GEN.root"; double xsec = 0.000006005;
    //TString fileout_name = "RSG_kMpl02_M_6500_py_GEN.root"; double xsec = 0.000002464;
    //TString fileout_name = "RSG_kMpl02_M_7000_py_GEN.root"; double xsec = 0.000001082;
    TString fileout_name = "RSG_kMpl02_M_8000_py_GEN.root"; double xsec = 0.0000002359;

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      Ntotal++;

      //double weight = 20.5*1000/10000;//xsec*nEvents/10000; xsec = 2.050e-08
      //double weight = 1.000;
      double weight = xsec*1000/numevents;
      // if (Cut(ientry) < 0) continue;
    //  if (GenDiPhoton_Minv > 500.){ // && GenDiPhoton_Minv < 4000.){
    		  nDiphMinv++;
    //	if (GenPhoton1_pt >75. && GenPhoton2_pt > 75.){
    			gendiphotonMinv->Fill(GenDiPhoton_Minv, weight);
    			genphoton1Pt->Fill(GenPhoton1_pt, weight);
    			genphoton2Pt->Fill(GenPhoton2_pt, weight);
    			genphoton1Eta->Fill(GenPhoton1_eta, weight);
    			genphoton2Eta->Fill(GenPhoton2_eta, weight);
    			genphoton1Phi->Fill(GenPhoton1_phi, weight);
    			genphoton2Phi->Fill(GenPhoton2_phi, weight);
          gendiphotoncosthetastar->Fill(GenDiPhoton_cosThetaStar, weight);
    //		}//pT cut
//      }//end minv
   }//end for loop over events

   cout << endl;
   cout << "Total entries            : " << Ntotal    << " " << nentries << endl;
   cout << "Passed DiphMinv cut      : " << nDiphMinv << endl;
   cout << "Passed etaCut            : " << netaCut   << endl;
   cout << endl;

   std::cout << "Creating root file: " << fileout_name << std::endl;
   TFile file_out(fileout_name, "RECREATE");
   gendiphotonMinv->Write();
   genphoton1Pt->Write();
   genphoton2Pt->Write();
   genphoton1Eta->Write();
   genphoton2Eta->Write();
   genphoton1Phi->Write();
   genphoton2Phi->Write();
   gendiphotoncosthetastar->Write();
}
