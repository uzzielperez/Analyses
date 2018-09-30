#define ClassData2018_cxx
#include "ClassData2018.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include "interface/easyplot.hh"
#include "interface/utilities.hh"

using namespace std;

void ClassData2018::Loop()
{
//   In a ROOT session, you can do:
//      root> .L ClassData2018.C
//      root> ClassData2018 t
//      root> t.GetEntry(12); // Fill t data members with entry number 12
//      root> t.Show();       // Show values of entry 12
//      root> t.Show(16);     // Read and show values of entry 16
//      root> t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
// std::string data_year("");
std::string region;
bool endcap = (region=="endcap");

//SET THIS
endcap = "endcap";

// std::string kfactor = kfactorString("BB", "R1F1");
// if(endcap) kfactor = kfactorString("BE", "R1F1");
//
// std::string cut("Photon1.pt>125&&Photon2.pt>125 && abs(Photon1.eta)<1.4442 && abs(Photon2.eta)<1.4442 && Diphoton.Minv > 500 && Diphoton.Minv < 1000 && isGood");
// if(endcap) cut = "Photon1.pt>125&&Photon2.pt>125 && Diphoton.Minv > 500 && Diphoton.Minv < 1000 && isGood && ( !(abs(Photon1.eta)<1.4442 && abs(Photon2.eta)<1.4442) && ((abs(Photon1.eta)<1.4442 && (abs(Photon2.eta)>1.56&&abs(Photon2.eta)<2.5)) || (abs(Photon2.eta)<1.4442 && (abs(Photon1.eta)>1.56&&abs(Photon1.eta)<2.5))))";

int nbins=100;
double xmin=0.0; // GeV
double xmax=2000; // GeV

   if (fChain == 0) return;
   init();
   Long64_t nentries = fChain->GetEntriesFast();
   //Define Samples
   // sample data("data_" + data_year, "Data");
   // sample gg("gg", "#gamma#gamma", kfactor);
   // sample gj("gj", "#gamma + jets");
   // //sample vg("vg", "V#gamma");
   // //sample w("w", "W");
   // //sample dy("dy", "DY");
   // //sample ttg("ttg", "t#bar{t}#gamma");
   // std::vector<sample> samples;
   // samples.push_back(data);
   // //samples.push_back(ttg);
   // //samples.push_back(w);
   // //samples.push_back(vg);
   // //samples.push_back(dy);
   // samples.push_back(gj);
   // samples.push_back(gg);
   //
   // //Define Variables and cuts
   // plot p0(samples, "Minv", cut, 40, 0, 2000);
   // plot p1(samples, "Photon1.pt", cut, 40, xmin, xmax/2);
   // plot p2(samples, "Photon2.pt", cut, 40, xmin, xmax/2);
   // // plot p3(samples, "Diphoton.qt", cut, nbins/2, xmin, xmax/2);
   // // plot p4(samples, "Diphoton.deltaPhi", cut, nbins/2, -TMath::Pi(), TMath::Pi());
   // // plot p5(samples, "Diphoton.deltaEta", cut, nbins/2, -5, 5);
   // // plot p6(samples, "abs(Diphoton.cosThetaStar)", cut, 20, 0, 1);
   // // plot p7(samples, "nPV", cut, 80, 0, 80);
   // // plot p8(samples, "Diphoton.deltaR", cut, 60, 0, 6);
   // plot p9(samples, "Photon1.eta", cut, nbins/2, -5, 5);
   // plot p10(samples, "Photon2.eta", cut, nbins/2, -5, 5);
   // plot p11(samples, "Photon1.phi", cut, nbins/2, -TMath::Pi(), TMath::Pi());
   // plot p12(samples, "Photon2.phi", cut, nbins/2, -TMath::Pi(), TMath::Pi());
   // // plot p13(samples, "abs(Diphoton.deltaPhi)", cut, nbins/4, 0, TMath::Pi());
   //
   // //Create a bunch of histograms for each sample
   // std::vector<vector<TH1D*>> vhists; //vector of a vector
   // vhists.push_back(p0.hist());
   // vhists.push_back(p1.hist());
   // vhists.push_back(p2.hist());
   // // vhists.push_back(p3.hist());
   // // vhists.push_back(p4.hist());
   // // vhists.push_back(p5.hist());
   // // vhists.push_back(p6.hist());
   // // vhists.push_back(p7.hist());
   // // vhists.push_back(p8.hist());
   // vhists.push_back(p9.hist());
   // vhists.push_back(p10.hist());
   // vhists.push_back(p11.hist());
   // vhists.push_back(p12.hist());
   //vhists.push_back(p13.hist());

   //Special histograms for HEM (Transfer this later)
   TH1D* photon1Eta_PreHEM      = new TH1D("photon1Eta_PreHEM", "", nbins/2, -5, 5);
   TH1D* photon2Eta_PreHEM      = new TH1D("photon2Eta_PreHEM", "", nbins/2, -5, 5);
   TH1D* photon1Phi_PreHEM      = new TH1D("photon1Phi_PreHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2Phi_PreHEM      = new TH1D("photon2Phi_PreHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon1Eta_PostHEM   = new TH1D("photon1Eta_PostHEM", "", nbins/2, -5, 5);
   TH1D* photon2Eta_PostHEM   = new TH1D("photon2Eta_PostHEM", "", nbins/2, -5, 5);
   TH1D* photon1Phi_PostHEM   = new TH1D("photon1Phi_PostHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2Phi_PostHEM   = new TH1D("photon2Phi_PostHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photonsEta_PreHEM      = new TH1D("photonsEta_PreHEM", "", nbins/2, -5,5);
   TH1D* photonsEta_PostHEM   = new TH1D("photonsEta_PostHEM", "", nbins/2, -5,5);
   TH1D* photonsPhi_PreHEM      = new TH1D("photonsPhi_PreHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photonsPhi_PostHEM   = new TH1D("photonsPhi_PostHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());


   TH1D* photon1Eta_PreHEP      = new TH1D("photon1Eta_PreHEP", "", nbins/2, -5, 5);
	 TH1D* photon2Eta_PreHEP      = new TH1D("photon2Eta_PreHEP", "", nbins/2, -5, 5);
   TH1D* photon1Phi_PreHEP      = new TH1D("photon1Phi_PreHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2Phi_PreHEP      = new TH1D("photon2Phi_PreHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon1Eta_PostHEP   = new TH1D("photon1Eta_PostHEP", "", nbins/2, -5, 5);
   TH1D* photon2Eta_PostHEP   = new TH1D("photon2Eta_PostHEP", "", nbins/2, -5, 5);
   TH1D* photon1Phi_PostHEP   = new TH1D("photon1Phi_PostHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2Phi_PostHEP   = new TH1D("photon2Phi_PostHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photonsEta_PreHEP      = new TH1D("photonsEta_PreHEP", "", nbins/2, -5,5);
   TH1D* photonsEta_PostHEP   = new TH1D("photonsEta_PostHEP", "", nbins/2, -5,5);
   TH1D* photonsPhi_PreHEP      = new TH1D("photonsPhi_PreHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photonsPhi_PostHEP   = new TH1D("photonsPhi_PostHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());

//SuperCluseter
   TH1D* photon1_scPhi_PreHEM      = new TH1D("photon1_scPhi_PreHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2_scPhi_PreHEM      = new TH1D("photon2_scPhi_PreHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon1_scPhi_PostHEM   = new TH1D("photon1_scPhi_PostHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2_scPhi_PostHEM   = new TH1D("photon2_scPhi_PostHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photons_scPhi_PreHEM      = new TH1D("photons_scPhi_PreHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photons_scPhi_PostHEM   = new TH1D("photons_scPhi_PostHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon1_scPhi_PreHEP      = new TH1D("photon1_scPhi_PreHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2_scPhi_PreHEP      = new TH1D("photon2_scPhi_PreHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon1_scPhi_PostHEP   = new TH1D("photon1_scPhi_PostHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2_scPhi_PostHEP   = new TH1D("photon2_scPhi_PostHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photons_scPhi_PreHEP      = new TH1D("photons_scPhi_PreHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photons_scPhi_PostHEP   = new TH1D("photons_scPhi_PostHEP", "", nbins/2, -TMath::Pi(), TMath::Pi());

   photon1Eta_PreHEM->Sumw2();
   photon2Eta_PreHEM->Sumw2();
   photon1Phi_PreHEM->Sumw2();
   photon2Phi_PreHEM->Sumw2();
   photon1Eta_PostHEM->Sumw2();
   photon2Eta_PostHEM->Sumw2();
   photon1Phi_PostHEM->Sumw2();
   photon2Phi_PostHEM->Sumw2();
   photonsEta_PreHEM->Sumw2();
   photonsEta_PostHEM->Sumw2();
   photonsPhi_PreHEM->Sumw2();
   photonsPhi_PostHEM->Sumw2();


   photon1Eta_PreHEP->Sumw2();
   photon2Eta_PreHEP->Sumw2();
   photon1Phi_PreHEP->Sumw2();
   photon2Phi_PreHEP->Sumw2();
   photon1Eta_PostHEP->Sumw2();
   photon2Eta_PostHEP->Sumw2();
   photon1Phi_PostHEP->Sumw2();
   photon2Phi_PostHEP->Sumw2();
   photonsEta_PreHEP->Sumw2();
   photonsEta_PostHEP->Sumw2();
   photonsPhi_PreHEP->Sumw2();
   photonsPhi_PostHEP->Sumw2();


//SuperCluster
   photon1_scPhi_PreHEM->Sumw2();
   photon1_scPhi_PreHEP->Sumw2();
   photon1_scPhi_PostHEM->Sumw2();
   photon1_scPhi_PostHEP->Sumw2();
   photon2_scPhi_PreHEM->Sumw2();
   photon2_scPhi_PreHEP->Sumw2();
   photon2_scPhi_PostHEM->Sumw2();
   photon2_scPhi_PostHEP->Sumw2();
   photons_scPhi_PreHEM->Sumw2();
   photons_scPhi_PreHEP->Sumw2();
   photons_scPhi_PostHEM->Sumw2();
   photons_scPhi_PostHEP->Sumw2();

   TH2D *hPost_PhiEta      = new TH2D("hPost_PhiEta",     "hPost_PhiEta",      nbins/2,-5, 5, nbins/2, -TMath::Pi(), TMath::Pi());
   TH2D *hPre_PhiEta       = new TH2D("hPre_PhiEta",      "hPre_PhiEta",       nbins/2,-5, 5, nbins/2, -TMath::Pi(), TMath::Pi());
   TH2D *hPost_scPhiscEta  = new TH2D("hPost_scPhiscEta", "hPost_scPhiscEta",  nbins/2,-5, 5, nbins/2, -TMath::Pi(), TMath::Pi());
   TH2D *hPre_scPhiscEta   = new TH2D("hPre_scPhiscEta",  "hPre_scPhiscEta",   nbins/2,-5, 5, nbins/2, -TMath::Pi(), TMath::Pi());

//   for(auto ivarhist : vhists){
//     //for(unsigned i = 0; i < ivarhist.size(); ++i){
//     for(auto isamplehist : ivarhist){
//      cout << "Variable for sample: " << isamplehist->GetName() << endl;
//    }//end loop over vector of vector
//  }//loop over vector of vector of hists samples for each variable
//
   ////-------Loop Over Events
   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;

      if(jentry%10000 == 0) cout << "Number of processed events: " << jentry << endl;
      //Loop over all hists variables and the samples
      //Focus only on Endcap
      int HEMminStartRun = 319077;
      double weight;
      // if(Event_run<319077) weight = 1/20.315;
      // else weight = 1/(6.612+12.8+3.969);
      //weight = 1/(6.612+12.8+3.969);
      weight = 1.00;
      //HEM15/16
      //-1.57 < phi < -0.87
      //-3 < eta < -1.4
      if(Photon1_pt>125&&Photon2_pt>125 && Diphoton_Minv > 350 && Diphoton_Minv < 1000 && isGood){//Original
      //if(Photon1_pt>70&&Photon2_pt>70 && Diphoton_Minv > 350 && Diphoton_Minv < 1000 && isGood){//Loose
      //if(Photon1_pt>20&&Photon2_pt>20 && isGood){//SuperLoose DQM
      if(Event_run < 319077){
        hPre_PhiEta ->Fill(Photon1_eta, Photon1_phi);
        hPre_scPhiscEta->Fill(Photon1_eta, Photon1_phi);
        //if(Photon1_isEE){
          if(Photon1_eta > -3.0 && Photon1_eta < -1.392){// HEM{
            photon1Eta_PreHEM->Fill(Photon1_eta, weight);
            photonsEta_PreHEM->Fill(Photon1_eta, weight);
            photon1Phi_PreHEM->Fill(Photon1_phi, weight);
            photonsPhi_PreHEM->Fill(Photon1_phi, weight);
            photon1_scPhi_PreHEM->Fill(Photon1_scPhi, weight);
            photons_scPhi_PreHEM->Fill(Photon1_scPhi, weight);
          }
          else if(Photon1_eta > 1.392 && Photon1_eta < 3.0){//HEP
            photon1Phi_PreHEP->Fill(Photon1_phi, weight);
            photonsPhi_PreHEP->Fill(Photon1_phi, weight);
            photon1_scPhi_PreHEP->Fill(Photon1_scPhi, weight);
            photons_scPhi_PreHEP->Fill(Photon1_scPhi, weight);
          }
        //}//Photon1EE
        //if(Photon2_isEE){
          //Put here HEM- Condition
          // if(Photon1_phi > -1.57 && Photon1_eta < -0.87){
         //}
         if(Photon2_eta > -3.0 && Photon2_eta > -1.392){
           photon2Eta_PreHEM->Fill(Photon2_eta, weight);
           photonsEta_PreHEM->Fill(Photon2_eta, weight);
           photon2Phi_PreHEM->Fill(Photon2_phi, weight);
           photonsPhi_PreHEM->Fill(Photon2_phi, weight);
           photon2_scPhi_PreHEM->Fill(Photon2_scPhi, weight);
           photons_scPhi_PreHEM->Fill(Photon2_scPhi, weight);
         }
         else if(Photon2_eta > 1.392 && Photon2_eta < 3.0){
             //photon2Eta_PreHEP->Fill(Photon2_eta);
             photon2Phi_PreHEP->Fill(Photon2_phi, weight);
             //photonsEta_PreHEP->Fill(Photon1_eta);
             photonsPhi_PreHEP->Fill(Photon2_phi, weight);
             photon2_scPhi_PreHEP->Fill(Photon2_scPhi, weight);
             photons_scPhi_PreHEP->Fill(Photon2_scPhi, weight);
          }
        //}Photon2isEE
      }
      else if (Event_run > 319077){
        hPost_PhiEta->Fill(Photon1_eta, Photon1_phi);
        hPost_scPhiscEta->Fill(Photon1_eta, Photon1_phi);
        if(Photon1_isEE){
          photon1Eta_PostHEM->Fill(Photon1_eta, weight);
          photonsEta_PostHEM->Fill(Photon1_eta, weight);
          if(Photon1_eta > -3.0 && Photon1_eta < -1.392){//HEM
            photon1Phi_PostHEM->Fill(Photon1_phi, weight);
            photonsPhi_PostHEM->Fill(Photon1_phi, weight);
            photon1_scPhi_PostHEM->Fill(Photon1_scPhi, weight);
            photons_scPhi_PostHEM->Fill(Photon1_scPhi, weight);
          }
          else if(Photon1_eta > 1.392 && Photon1_eta < 3.0){//HEP
            //photon1Eta_PostHEP->Fill(Photon1_eta);
            photon1Phi_PostHEP->Fill(Photon1_phi, weight);
            //photonsEta_PostHEP->Fill(Photon1_eta);
            photonsPhi_PostHEP->Fill(Photon1_phi, weight);
            photon1_scPhi_PostHEP->Fill(Photon1_scPhi, weight);
            photons_scPhi_PostHEP->Fill(Photon1_scPhi, weight);
          }
          if(Photon2_isEE){
            photon2Eta_PostHEM->Fill(Photon2_eta, weight);
            photonsEta_PostHEM->Fill(Photon2_eta, weight);
            if(Photon2_eta > -3.0 && Photon2_eta > -1.392){
              photon2Phi_PostHEM->Fill(Photon2_phi, weight);
              photonsPhi_PostHEM->Fill(Photon2_phi, weight);
              photon2_scPhi_PostHEM->Fill(Photon2_scPhi, weight);
              photons_scPhi_PostHEM->Fill(Photon2_scPhi, weight);
            }
            else if(Photon2_eta > 1.392 && Photon2_eta < 3.0){
              //photon2Eta_PostHEP->Fill(Photon2_eta);
              photon2Phi_PostHEP->Fill(Photon2_phi, weight);
              //photonsEta_PostHEP->Fill(Photon1_eta);
              photonsPhi_PostHEP->Fill(Photon2_phi, weight);
              photon2_scPhi_PostHEP->Fill(Photon2_scPhi, weight);
              photons_scPhi_PostHEP->Fill(Photon2_scPhi, weight);
            }
          }
        }
      }
    }//kinematic conditions
   }//end loop over events

   TFile file_out("HEM15-16_data_pT125_M300-1000_w1.root", "RECREATE");

   photon1Eta_PreHEM->Write();
   photon2Eta_PreHEM->Write();
   photon1Phi_PreHEM->Write();
   photon2Phi_PreHEM->Write();
   photon1Eta_PostHEM->Write();
   photon2Eta_PostHEM->Write();
   photon1Phi_PostHEM->Write();
   photon2Phi_PostHEM->Write();
   photonsEta_PreHEM->Write();
   photonsEta_PostHEM->Write();
   photonsPhi_PreHEM->Write();
   photonsPhi_PostHEM->Write();

   //photon1Eta_PreHEP->Write();
   //photon2Eta_PreHEP->Write();
   photon1Phi_PreHEP->Write();
   photon2Phi_PreHEP->Write();
   //photon1Eta_PostHEP->Write();
   //photon2Eta_PostHEP->Write();
   photon1Phi_PostHEP->Write();
   photon2Phi_PostHEP->Write();
   //photonsEta_PreHEP->Write();
   //photonsEta_PostHEP->Write();
   photonsPhi_PreHEP->Write();
   photonsPhi_PostHEP->Write();

   //SuperCluster
   photon1_scPhi_PreHEM->Write();
   photon1_scPhi_PreHEP->Write();
   photon1_scPhi_PostHEM->Write();
   photon1_scPhi_PostHEP->Write();
   photon2_scPhi_PreHEM->Write();
   photon2_scPhi_PreHEP->Write();
   photon2_scPhi_PostHEM->Write();
   photon2_scPhi_PostHEP->Write();
   photons_scPhi_PreHEM->Write();
   photons_scPhi_PreHEP->Write();
   photons_scPhi_PostHEM->Write();
   photons_scPhi_PostHEP->Write();

   //TH2D
   hPre_PhiEta->Write();
   hPre_scPhiscEta->Write();
   hPost_PhiEta->Write();
   hPost_scPhiscEta->Write();

}//end ClassData2018::Loop()
