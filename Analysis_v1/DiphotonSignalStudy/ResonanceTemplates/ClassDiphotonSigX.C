#define ${ClassDiphotonSignal}_cxx
#include "${ClassDiphotonSignal}.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void ${ClassDiphotonSignal}::Loop()
{
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();
   //counters
   int Ntotal      = 0;
   int nDiphMinv   = 0;
   int netaCut     = 0;
   int isEBEB = 0;
   int isEBEEorEEEB = 0;
   int isEEEB = 0;
   int isEEEE = 0;

   //histograms
   TH1D* diphotonMinv = new TH1D("diphotonMinv", "", 1000, 0., 13000.);// 100, 0, 10000
   TH1D* photon1Pt    = new TH1D("photon1Pt", "", 1000, 0., 10000.);//
   TH1D* photon2Pt    = new TH1D("photon2Pt", "", 1000, 0., 10000.);
   TH1D* photon1Eta   = new TH1D("photon1Eta", "", 80, -4.0, 4.0);
   TH1D* photon2Eta   = new TH1D("photon2Eta", "", 80, -4.0, 4.0);
   TH1D* photon1Phi   = new TH1D("photon1Phi", "", 80, -4.0, 4.5);
   TH1D* photon2Phi   = new TH1D("photon2Phi", "", 80, -4.0, 4.5);
   TH1D* diphotoncosthetastar = new TH1D("diphotoncosthetastar", "", 100, -1.0, 1.0);
   //TH1D* chidiphoton  = new TH1D("chidiphoton", "", 100, 0, 50);

   TH1D* diphotonMinvisEBEB = new TH1D("diphotonMinvisEBEB", "", 1000, 0., 13000.);// 100, 0, 10000
   TH1D* photon1PtisEBEB = new TH1D("photon1PtisEBEB", "", 1000, 0., 10000.);//
   TH1D* photon2PtisEBEB = new TH1D("photon2PtisEBEB", "", 1000, 0., 10000.);
   TH1D* photon1EtaisEBEB = new TH1D("photon1EtaisEBEB", "", 80, -4.0, 4.0);
   TH1D* photon2EtaisEBEB = new TH1D("photon2EtaisEBEB", "", 80, -4.0, 4.0);
   TH1D* photon1PhiisEBEB = new TH1D("photon1PhiisEBEB", "", 80, -4.0, 4.5);
   TH1D* photon2PhiisEBEB = new TH1D("photon2PhiisEBEB", "", 80, -4.0, 4.5);
   TH1D* diphotoncosthetastarisEBEB = new TH1D("diphotoncosthetastarisEBEB", "", 100, -1.0, 1.0);
   //TH1D* chidiphotonisEBEB  = new TH1D("chidiphoton", "", 100, 0, 50);

   diphotonMinv->Sumw2();
   photon1Pt->Sumw2();
   photon2Pt->Sumw2();
   photon1Eta->Sumw2();
   photon2Eta->Sumw2();
   photon1Phi->Sumw2();
   photon2Phi->Sumw2();
   diphotoncosthetastar->Sumw2();
   //chidiphoton->Sumw2();

   diphotonMinvisEBEB->Sumw2();
   photon1PtisEBEB->Sumw2();
   photon2PtisEBEB->Sumw2();
   photon1EtaisEBEB->Sumw2();
   photon2EtaisEBEB->Sumw2();
   photon1PhiisEBEB->Sumw2();
   photon2PhiisEBEB->Sumw2();
   diphotoncosthetastarisEBEB->Sumw2();
   //chidiphotonisEBEB->Sumw2();

   TString fileout_name = "OUT${outputfile}.root";
   TString logfile = "LOG.txt";

   // Event Loop
   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      //if (Cut(ientry) < 0) continue;
      Ntotal++;
      double weight = Event_weightAll;
      if(jentry%10000 == 0) cout << "Number of processed events: " << jentry << endl;
      // Only look at eventw with two true photons
      if (isGood)
      {
        diphotonMinv->Fill(Diphoton_Minv, weight);
        photon1Pt->Fill(Photon1_pt, weight);
        photon2Pt->Fill(Photon2_pt, weight);
        photon1Eta->Fill(Photon1_eta, weight);
        photon2Eta->Fill(Photon2_eta, weight);
        photon1Phi->Fill(Photon1_phi, weight);
        photon2Phi->Fill(Photon2_phi, weight);
        diphotoncosthetastar->Fill(Diphoton_cosThetaStar, weight);
        //chidiphoton->Fill(Diphoton_chiDiphoton, weight);

        if (((std::abs(Photon1_eta)<1.442) && (1.566 < std::abs(Photon2_eta) && std::abs(Photon2_eta) < 2.5)) || ((1.566 < std::abs(Photon1_eta) && std::abs(Photon1_eta) < 2.5) && (std::abs(Photon2_eta) < 1.4442))) isEBEEorEEEB = isEBEEorEEEB + 1;
        if ((1.566 < std::abs(Photon1_eta) && std::abs(Photon1_eta) < 2.5) && (1.566 < std::abs(Photon2_eta) && std::abs(Photon2_eta) < 2.5)) isEEEE = isEEEE + 1;
        if  ((std::abs(Photon1_eta)<1.442) && (std::abs(Photon2_eta)<1.442))
        {
          isEBEB = isEBEB + 1; //
          diphotonMinvisEBEB->Fill(Diphoton_Minv, weight);
          photon1PtisEBEB->Fill(Photon1_pt, weight);
          photon2PtisEBEB->Fill(Photon2_pt, weight);
          photon1EtaisEBEB->Fill(Photon1_eta, weight);
          photon2EtaisEBEB->Fill(Photon2_eta, weight);
          photon1PhiisEBEB->Fill(Photon1_phi, weight);
          photon2PhiisEBEB->Fill(Photon2_phi, weight);
          diphotoncosthetastarisEBEB->Fill(Diphoton_cosThetaStar, weight);
          //chidiphotonisEBEB->Fill(Diphoton_chiDiphoton, weight);
        }
      }
   }
   cout << endl;
   cout << "File: " << fileout_name << endl;
   cout << "Total entries            : " << Ntotal    << " " << nentries << endl;
   cout << "isEBEB  : " << isEBEB << endl;
   cout << "isEBEEorEEEB: " << isEBEEorEEEB << endl;
   cout << "isEEEE: " << isEEEE << endl;
   cout << endl;
   ofstream outfile;
   outfile.open(logfile, ios::app);
   outfile << fileout_name << ", " << Ntotal << ", " << isEBEB << ", " << isEBEEorEEEB <<  ", " << isEEEE << endl;
   outfile.close();

   TFile file_out(fileout_name, "RECREATE");
   diphotonMinv->Write();
   photon1Pt->Write();
   photon2Pt->Write();
   photon1Eta->Write();
   photon2Eta->Write();
   photon1Phi->Write();
   photon2Phi->Write();
   diphotoncosthetastar->Write();
   //chidiphoton->Write();

   diphotonMinvisEBEB->Write();
   photon1PtisEBEB->Write();
   photon2PtisEBEB->Write();
   photon1EtaisEBEB->Write();
   photon2EtaisEBEB->Write();
   photon1PhiisEBEB->Write();
   photon2PhiisEBEB->Write();
   diphotoncosthetastarisEBEB->Write();
   //chidiphotonisEBEB->Write();

}
