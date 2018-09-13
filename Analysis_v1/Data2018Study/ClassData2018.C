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
std::string data_year("");
std::string region;
bool endcap = (region=="endcap");

//SET THIS
endcap = "endcap";

std::string kfactor = kfactorString("BB", "R1F1");
if(endcap) kfactor = kfactorString("BE", "R1F1");

std::string cut("Photon1.pt>125&&Photon2.pt>125 && abs(Photon1.eta)<1.4442 && abs(Photon2.eta)<1.4442 && Diphoton.Minv > 500 && Diphoton.Minv < 1000 && isGood");
if(endcap) cut = "Photon1.pt>125&&Photon2.pt>125 && Diphoton.Minv > 500 && Diphoton.Minv < 1000 && isGood && ( !(abs(Photon1.eta)<1.4442 && abs(Photon2.eta)<1.4442) && ((abs(Photon1.eta)<1.4442 && (abs(Photon2.eta)>1.56&&abs(Photon2.eta)<2.5)) || (abs(Photon2.eta)<1.4442 && (abs(Photon1.eta)>1.56&&abs(Photon1.eta)<2.5))))";

int nbins=100;
double xmin=0.0; // GeV
double xmax=2000; // GeV

   if (fChain == 0) return;
   init();
   Long64_t nentries = fChain->GetEntriesFast();
   //Define Samples
   sample data("data_" + data_year, "Data");
   sample gg("gg", "#gamma#gamma", kfactor);
   sample gj("gj", "#gamma + jets");
   //sample vg("vg", "V#gamma");
   //sample w("w", "W");
   //sample dy("dy", "DY");
   //sample ttg("ttg", "t#bar{t}#gamma");
   std::vector<sample> samples;
   samples.push_back(data);
   //samples.push_back(ttg);
   //samples.push_back(w);
   //samples.push_back(vg);
   //samples.push_back(dy);
   samples.push_back(gj);
   samples.push_back(gg);

   //Define Variables and cuts
   plot p0(samples, "Minv", cut, 40, 0, 2000);
   plot p1(samples, "Photon1.pt", cut, 40, xmin, xmax/2);
   plot p2(samples, "Photon2.pt", cut, 40, xmin, xmax/2);
   // plot p3(samples, "Diphoton.qt", cut, nbins/2, xmin, xmax/2);
   // plot p4(samples, "Diphoton.deltaPhi", cut, nbins/2, -TMath::Pi(), TMath::Pi());
   // plot p5(samples, "Diphoton.deltaEta", cut, nbins/2, -5, 5);
   // plot p6(samples, "abs(Diphoton.cosThetaStar)", cut, 20, 0, 1);
   // plot p7(samples, "nPV", cut, 80, 0, 80);
   // plot p8(samples, "Diphoton.deltaR", cut, 60, 0, 6);
   plot p9(samples, "Photon1.eta", cut, nbins/2, -5, 5);
   plot p10(samples, "Photon2.eta", cut, nbins/2, -5, 5);
   plot p11(samples, "Photon1.phi", cut, nbins/2, -TMath::Pi(), TMath::Pi());
   plot p12(samples, "Photon2.phi", cut, nbins/2, -TMath::Pi(), TMath::Pi());
   // plot p13(samples, "abs(Diphoton.deltaPhi)", cut, nbins/4, 0, TMath::Pi());

   //Create a bunch of histograms for each sample
   std::vector<vector<TH1D*>> vhists; //vector of a vector
   vhists.push_back(p0.hist());
   vhists.push_back(p1.hist());
   vhists.push_back(p2.hist());
   // vhists.push_back(p3.hist());
   // vhists.push_back(p4.hist());
   // vhists.push_back(p5.hist());
   // vhists.push_back(p6.hist());
   // vhists.push_back(p7.hist());
   // vhists.push_back(p8.hist());
   vhists.push_back(p9.hist());
   vhists.push_back(p10.hist());
   vhists.push_back(p11.hist());
   vhists.push_back(p12.hist());
   //vhists.push_back(p13.hist());

   //Special histograms for HEM (Transfer this later)
   TH1D* photon1Eta_B4HEM      = new TH1D("photon1Eta_B4HEM", "", nbins/2, -5, 5);
	 TH1D* photon2Eta_B4HEM      = new TH1D("photon2Eta_B4HEM", "", nbins/2, -5, 5);
   TH1D* photon1Phi_B4HEM      = new TH1D("photon1Phi_B4HEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2Phi_B4HEM      = new TH1D("photon2Phi_B4HEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon1Eta_AfterHEM   = new TH1D("photon1Eta_AfterHEM", "", nbins/2, -5, 5);
   TH1D* photon2Eta_AfterHEM   = new TH1D("photon2Eta_AfterHEM", "", nbins/2, -5, 5);
   TH1D* photon1Phi_AfterHEM   = new TH1D("photon1Phi_AfterHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photon2Phi_AfterHEM   = new TH1D("photon2Phi_AfterHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());

   TH1D* photonsEta_B4HEM      = new TH1D("photonsEta_B4HEM", "", nbins/2, -5,5);
   TH1D* photonsEta_AfterHEM   = new TH1D("photonsEta_AfterHEM", "", nbins/2, -5,5);
   TH1D* photonsPhi_B4HEM      = new TH1D("photonsPhi_B4HEM", "", nbins/2, -TMath::Pi(), TMath::Pi());
   TH1D* photonsPhi_AfterHEM   = new TH1D("photonsPhi_AfterHEM", "", nbins/2, -TMath::Pi(), TMath::Pi());

   photon1Eta_B4HEM->Sumw2();
   photon2Eta_B4HEM->Sumw2();
   photon1Phi_B4HEM->Sumw2();
   photon2Phi_B4HEM->Sumw2();
   photon1Eta_AfterHEM->Sumw2();
   photon2Eta_AfterHEM->Sumw2();
   photon1Phi_AfterHEM->Sumw2();
   photon2Phi_AfterHEM->Sumw2();

   photonsEta_B4HEM->Sumw2();
   photonsEta_AfterHEM->Sumw2();
   photonsPhi_B4HEM->Sumw2();
   photonsPhi_AfterHEM->Sumw2();

   for(auto ivarhist : vhists){
     //for(unsigned i = 0; i < ivarhist.size(); ++i){
     for(auto isamplehist : ivarhist){
      cout << "Variable for sample: " << isamplehist->GetName() << endl;
    }//end loop over vector of vector
  }//loop over vector of vector of hists samples for each variable

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
      if(Photon1_pt>125&&Photon2_pt>125 && Diphoton_Minv > 500 && Diphoton_Minv < 1000 && isGood){
        if(Photon1_isEE){
          //cout << "Fill Photon1 here." << endl;
          if(Event_run < 319077){
            //Put here HEM- Condition
                photon1Eta_B4HEM->Fill(Photon1_eta);
                photon1Phi_B4HEM->Fill(Photon1_phi);
                photonsEta_B4HEM->Fill(Photon1_eta);
                photonsPhi_B4HEM->Fill(Photon1_phi);

            //cout << "Fill HEM-B4" << endl;
          }
          else{
                photon1Eta_AfterHEM->Fill(Photon1_eta);
                photon1Phi_AfterHEM->Fill(Photon1_phi);
                photonsEta_AfterHEM->Fill(Photon1_eta);
                photonsPhi_AfterHEM->Fill(Photon1_phi);
          }
        }

        if(Photon2_isEE){
          //cout << "Fill Photon2 here." << endl;
          if(Event_run < 319077){
            //Put here HEM- Condition
         	      photon2Eta_B4HEM->Fill(Photon2_eta);
                photon2Phi_B4HEM->Fill(Photon2_phi);
                photonsEta_B4HEM->Fill(Photon1_eta);
                photonsPhi_B4HEM->Fill(Photon1_phi);

          }
          else{
            //Put here HEM- Condition
                photon2Eta_AfterHEM->Fill(Photon2_eta);
                photon2Phi_AfterHEM->Fill(Photon2_phi);
                photonsEta_AfterHEM->Fill(Photon1_eta);
                photonsPhi_AfterHEM->Fill(Photon1_phi);
          }
        }
      }
      //kinematic conditions
   }//end loop over events

   TFile file_out("HEM15-16_data.root", "RECREATE");
   photon1Eta_B4HEM->Write();
   photon2Eta_B4HEM->Write();
   photon1Phi_B4HEM->Write();
   photon2Phi_B4HEM->Write();
   photon1Eta_AfterHEM->Write();
   photon2Eta_AfterHEM->Write();
   photon1Phi_AfterHEM->Write();
   photon2Phi_AfterHEM->Write();

}//end ClassData2018::Loop()
