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
  TH1D* gendiphotonMinv = new TH1D("gendiphotonMinv", "", 100, 500., 4000.);// 100, 0, 10000
  TH1D* genphoton1Pt    = new TH1D("genphoton1Pt", "", 1000, 0., 4000.);//
  TH1D* genphoton2Pt    = new TH1D("genphoton2Pt", "", 1000, 0., 4000.);
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

  //TString fileout_name = "Unparticles_SM_TuneCUEP8M1_13TeV.root"; double xsec = 0.1205;
  //TString fileout_name = "Unparticles_du1p5_LambdaU-1000_TuneCUEP8M1_13TeV.root"; double xsec = 0.1457;
  //TString fileout_name = "Unparticles_du1p5_LambdaU-800_TuneCUEP8M1_13TeV.root"; double xsec = 0.1457;
  //TString fileout_name = "Unparticles_du1p5_LambdaU-2000_TuneCUEP8M1_13TeV.root"; double xsec = 0.1457;


  //TString fileout_name = "Unparticles_du1p5_LambdaU-500_TuneCUEP8M1_13TeV.root"; double xsec = 2.285;
  //TString fileout_name = "Unparticles_du1p5_LambdaU-5000_TuneCUEP8M1_13TeV.root"; double xsec = 0.1146;
  //TString fileout_name = "Unparticles_du1p5_Lambda-U0p1_TuneCUEP8M1_13TeV.root"; double xsec = 34510;
  //TString fileout_name = "Unparticles_du1p5_LambdaU-10000_TuneCUEP8M1_13TeV.root"; double xsec = 0.1146;

  //TString fileout_name =  "Unparticles_du2p0_LambdaU-10p0_TuneCUEP8M1_13TeV.root"; int xsec =  28680;
  //TString fileout_name = "Unparticles_du2p0_LambdaU-1p0_TuneCUEP8M1_13TeV.root"; int xsec =  28680;
  //TString fileout_name = "Unparticles_du1p4_LambdaU-1p0_TuneCUEP8M1_13TeV.root"; int xsec =  54950;
  //TString fileout_name = "Unparticles_du1p4_LambdaU-10p0_TuneCUEP8M1_13TeV.root"; int xsec =  54950;

  //TString fileout_name = "TestUnparticles_du0p5_LambdaU-10p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 28680;
   //TString fileout_name = "TestUnparticles_du0p5_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 28680;
  //TString fileout_name = "TestUnparticles_du1p02_LambdaU-10p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 59420;
   //TString fileout_name = "TestUnparticles_du1p02_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 59420;
   //TString fileout_name = "TestUnparticles_du1p04_LambdaU-10p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 58750;
  //TString fileout_name = "TestUnparticles_du1p04_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 58750;
  // TString fileout_name = "TestUnparticles_du1p06_LambdaU-10p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 53850;
  // TString fileout_name = "TestUnparticles_du1p06_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 53850;
   //TString fileout_name = "TestUnparticles_du1p0_LambdaU-10p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 28680;
  //TString fileout_name = "TestUnparticles_du1p0_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = 28680;

  //TString fileout_name = "Unparticles_du2p0_LambdaU-1p0_TuneCUEP8M1_13TeV.root"; double xsec = 0.1126;
  //TString fileout_name = "Unparticles_du2p2_LambdaU-1p0_TuneCUEP8M1_13TeV.root"; double xsec = 0.1126;
  //TString fileout_name = "Unparticles_du2p0_LambdaU-15000p0_TuneCUEP8M1_13TeV.root"; double xsec = 0.1126;
  //TString fileout_name = "Unparticles_du2p2_LambdaU-15000p0_TuneCUEP8M1_13TeV.root"; double xsec = 0.1126;

  //TString fileout_name = "TestUnparticles_du2p0_LambdaU-10p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = ;
  //TString fileout_name = "TestUnparticles_du2p0_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8.root"; int xsec = ;


   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      Ntotal++;
      //double weight = 1.00;
      //double weight = 53050*1000/10000; ///du1.06, lambda1,4, 0.4
      //double weight = 28950*1000/10000; //du 1.06, 1.09 lambda 15000, 100000
      //double weight = 53030*1000/10000; //du 1.09 lambda 0.4, 1, 4
      //double weight = 28680*1000/10000; //du 2.p1 all
      double weight = xsec*1000/10000;

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

   TFile file_out(fileout_name, "RECREATE");
   //TFile file_out("Unparticles106.root", "RECREATE");
   //TFile file_out("Unparticles109.root", "RECREATE");
   //TFile file_out("Unparticles2x1.root", "RECREATE");
   //TFile file_out("Unparticles106_LambdaU-1000.root", "RECREATE");
   //TFile file_out("Unparticles10_LambdaU-1000.root", "RECREATE");
   //TFile file_out("Unparticles2x1_LambdaU-1000.root", "RECREATE");

   //--------------------------
   //TFile file_out("TestUnparticles_du1p06_LambdaU-0p4_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p06_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p06_LambdaU-4p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p06_LambdaU-15000p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p06_LambdaU-100000p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");

   //TFile file_out("TestUnparticles_du1p09_LambdaU-0p4_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p09_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p09_LambdaU-4p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p09_LambdaU-15000p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du1p09_LambdaU-100000p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");

   //TFile file_out("TestUnparticles_du2p1_LambdaU-0p4_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du2p1_LambdaU-1p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du2p1_LambdaU-4p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du2p1_LambdaU-15000p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
   //TFile file_out("TestUnparticles_du2p1_LambdaU-100000p0_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");

   //------------
    //TFile file_out("TestUnparticles_du1p06_LambdaU-4p0Weighted_TuneCUEP8M1_13TeV_pythia8_py_GEN.root","RECREATE");
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
