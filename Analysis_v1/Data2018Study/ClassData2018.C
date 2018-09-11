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
   sample vg("vg", "V#gamma");
   sample w("w", "W");
   sample dy("dy", "DY");
   sample ttg("ttg", "t#bar{t}#gamma");
   std::vector<sample> samples;
   samples.push_back(data);
   samples.push_back(ttg);
   samples.push_back(w);
   samples.push_back(vg);
   samples.push_back(dy);
   samples.push_back(gj);
   samples.push_back(gg);

   //Define Histograms
   vector<TH1D*> vMinv;
   vector<TH1D*> vPhoton1_pT;
   vector<TH1D*> vPhoton2_pT;
   vector<TH1D*> vDiphoton_qT;
   vector<TH1D*> vDiphoton_deltaPhi;
   vector<TH1D*> vDiphoton_deltaEta;
   vector<TH1D*> vAbsDiphooton_cosThetaStar;
   vector<TH1D*> vnPV;
   vector<TH1D*> vDiphoton_deltaR;
   vector<TH1D*> vPhoton1_eta;
   vector<TH1D*> vPhoton2_eta;
   vector<TH1D*> vPhoton1_phi;
   vector<TH1D*> vPhoton2_phi;

   for(auto isample : samples) {
     cout << isample.name() << endl;
   }

   //-------Loop Over Events
   // Long64_t nbytes = 0, nb = 0;
   // for (Long64_t jentry=0; jentry<nentries;jentry++) {
   //    Long64_t ientry = LoadTree(jentry);
   //    if (ientry < 0) break;
   //    nb = fChain->GetEntry(jentry);   nbytes += nb;
   //    // if (Cut(ientry) < 0) continue;
   //
   // }//end loop over events
}//end ClassData2018::Loop()
