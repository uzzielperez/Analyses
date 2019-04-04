#define Class_ADDGravToGG_NegInt_1_LambdaT_5500_M_1000To2000_cxx
#include "Class_ADDGravToGG_NegInt_1_LambdaT_5500_M_1000To2000.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void Class_ADDGravToGG_NegInt_1_LambdaT_5500_M_1000To2000::Loop()
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
   TH1D* gendiphotonMinv = new TH1D("gendiphotonMinv", "", 130, 0., 13000.);// 100, 0, 10000
   TH1D* genphoton1Pt    = new TH1D("genphoton1Pt", "", 100, 0., 10000.);//
   TH1D* genphoton2Pt    = new TH1D("genphoton2Pt", "", 100, 0., 10000.);
   TH1D* genphoton1Eta   = new TH1D("genphoton1Eta", "", 70, -3.5, 3.5);
   TH1D* genphoton2Eta   = new TH1D("genphoton2Eta", "", 70, -3.5, 3.5);
   TH1D* genphoton1Phi   = new TH1D("genphoton1Phi", "", 70, -3.5, 3.5);
   TH1D* genphoton2Phi   = new TH1D("genphoton2Phi", "", 70, -3.5, 3.5);
   TH1D* gendiphotoncosthetastar = new TH1D("gendiphotoncosthetastar", "", 100, -1.0, 1.0);
   TH1D* genchidiphoton  = new TH1D("genchidiphoton", "", 70, 0, 280);

   TH1D* gendiphotonMinvisEBEB = new TH1D("gendiphotonMinvisEBEB", "", 130, 0., 13000.);// 100, 0, 10000
   TH1D* genphoton1PtisEBEB = new TH1D("genphoton1PtisEBEB", "", 100, 0., 10000.);//
   TH1D* genphoton2PtisEBEB = new TH1D("genphoton2PtisEBEB", "", 100, 0., 10000.);
   TH1D* genphoton1EtaisEBEB = new TH1D("genphoton1EtaisEBEB", "", 70, -3.5, 3.5);
   TH1D* genphoton2EtaisEBEB = new TH1D("genphoton2EtaisEBEB", "", 70, -3.5, 3.5);
   TH1D* genphoton1PhiisEBEB = new TH1D("genphoton1PhiisEBEB", "", 70, -3.5, 3.5);
   TH1D* genphoton2PhiisEBEB = new TH1D("genphoton2PhiisEBEB", "", 70, -3.5, 3.5);
   TH1D* gendiphotoncosthetastarisEBEB = new TH1D("gendiphotoncosthetastarisEBEB", "", 100, -1.0, 1.0);
   TH1D* genchidiphotonisEBEB  = new TH1D("genchidiphotonisEBEB", "", 70, 0, 280);

   TH1D* gendiphotonMinvisEBEB_M2000 = new TH1D("gendiphotonMinvisEBEB_M2000", "", 130, 0., 13000.);// 100, 0, 10000
   TH1D* genphoton1PtisEBEB_M2000 = new TH1D("genphoton1PtisEBEB_M2000", "", 100, 0., 10000.);//
   TH1D* genphoton2PtisEBEB_M2000 = new TH1D("genphoton2PtisEBEB_M2000", "", 100, 0., 10000.);
   TH1D* genphoton1EtaisEBEB_M2000 = new TH1D("genphoton1EtaisEBEB_M2000", "", 70, -3.5, 3.5);
   TH1D* genphoton2EtaisEBEB_M2000 = new TH1D("genphoton2EtaisEBEB_M2000", "", 70, -3.5, 3.5);
   TH1D* genphoton1PhiisEBEB_M2000 = new TH1D("genphoton1PhiisEBEB_M2000", "", 70, -3.5, 3.5);
   TH1D* genphoton2PhiisEBEB_M2000 = new TH1D("genphoton2PhiisEBEB_M2000", "", 70, -3.5, 3.5);
   TH1D* gendiphotoncosthetastarisEBEB_M2000 = new TH1D("gendiphotoncosthetastarisEBEB_M2000", "", 100, -1.0, 1.0);
   TH1D* genchidiphotonisEBEB_M2000  = new TH1D("genchidiphotonisEBEB_M2000", "", 70, 0, 280);

   gendiphotonMinv->Sumw2();
   genphoton1Pt->Sumw2();
   genphoton2Pt->Sumw2();
   genphoton1Eta->Sumw2();
   genphoton2Eta->Sumw2();
   genphoton1Phi->Sumw2();
   genphoton2Phi->Sumw2();
   gendiphotoncosthetastar->Sumw2();
   genchidiphoton->Sumw2();

   gendiphotonMinvisEBEB->Sumw2();
   genphoton1PtisEBEB->Sumw2();
   genphoton2PtisEBEB->Sumw2();
   genphoton1EtaisEBEB->Sumw2();
   genphoton2EtaisEBEB->Sumw2();
   genphoton1PhiisEBEB->Sumw2();
   genphoton2PhiisEBEB->Sumw2();
   gendiphotoncosthetastarisEBEB->Sumw2();
   genchidiphotonisEBEB->Sumw2();

   gendiphotonMinvisEBEB_M2000->Sumw2();
   genphoton1PtisEBEB_M2000->Sumw2();
   genphoton2PtisEBEB_M2000->Sumw2();
   genphoton1EtaisEBEB_M2000->Sumw2();
   genphoton2EtaisEBEB_M2000->Sumw2();
   genphoton1PhiisEBEB_M2000->Sumw2();
   genphoton2PhiisEBEB_M2000->Sumw2();
   gendiphotoncosthetastarisEBEB_M2000->Sumw2();
   genchidiphotonisEBEB_M2000->Sumw2();

   TString fileout_name = "OUTADDGravToGG_NegInt_1_LambdaT_5500_M_1000To2000.root";
   TString logfile = "LOG.txt";

   std::vector<double> wt;

   // Event Loop
   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      //if (Cut(ientry) < 0) continue;

      Ntotal++;

      double weight = Event_weightAll;
//      double last_wt;
//      if (!wt.empty())
//      {
//        last_wt = wt.back();
//      	if (weight != last_wt) cout << "Weight: " << weight << endl;
//      }
      wt.push_back (weight);


      if(jentry%10000 == 0) cout << "Number of processed events: " << jentry << endl;
      // Only look at eventw with two true photons
      if (fabs(GenPhoton1_eta) < 2.8 && fabs(GenPhoton2_eta) < 2.8)
      {//fabs or TMath
        gendiphotonMinv->Fill(Gendiphoton_Minv, weight);
        genphoton1Pt->Fill(GenPhoton1_pt, weight);
        genphoton2Pt->Fill(GenPhoton2_pt, weight);
        genphoton1Eta->Fill(GenPhoton1_eta, weight);
        genphoton2Eta->Fill(GenPhoton2_eta, weight);
        genphoton1Phi->Fill(GenPhoton1_phi, weight);
        genphoton2Phi->Fill(GenPhoton2_phi, weight);
        gendiphotoncosthetastar->Fill(Gendiphoton_cosThetaStar, weight);
        genchidiphoton->Fill(Gendiphoton_chiDiphoton, weight);

        if (((std::abs(GenPhoton1_eta)<1.442) && (1.566 < std::abs(GenPhoton2_eta) && std::abs(GenPhoton2_eta) < 2.5)) || ((1.566 < std::abs(GenPhoton1_eta) && std::abs(GenPhoton1_eta) < 2.5) && (std::abs(GenPhoton2_eta) < 1.4442))) isEBEEorEEEB = isEBEEorEEEB + 1;
        if ((1.566 < std::abs(GenPhoton1_eta) && std::abs(GenPhoton1_eta) < 2.5) && (1.566 < std::abs(GenPhoton2_eta) && std::abs(GenPhoton2_eta) < 2.5)) isEEEE = isEEEE + 1;
        if  ((std::abs(GenPhoton1_eta)<1.442) && (std::abs(GenPhoton2_eta)<1.442))
        {
          isEBEB = isEBEB + 1; //

          gendiphotonMinvisEBEB->Fill(Gendiphoton_Minv, weight);
          genphoton1PtisEBEB->Fill(GenPhoton1_pt, weight);
          genphoton2PtisEBEB->Fill(GenPhoton2_pt, weight);
          genphoton1EtaisEBEB->Fill(GenPhoton1_eta, weight);
          genphoton2EtaisEBEB->Fill(GenPhoton2_eta, weight);
          genphoton1PhiisEBEB->Fill(GenPhoton1_phi, weight);
          genphoton2PhiisEBEB->Fill(GenPhoton2_phi, weight);
          gendiphotoncosthetastarisEBEB->Fill(Gendiphoton_cosThetaStar, weight);
          genchidiphotonisEBEB->Fill(Gendiphoton_chiDiphoton, weight);

          if (Gendiphoton_Minv > 2000){
            gendiphotonMinvisEBEB_M2000->Fill(Gendiphoton_Minv, weight);
            genphoton1PtisEBEB_M2000->Fill(GenPhoton1_pt, weight);
            genphoton2PtisEBEB_M2000->Fill(GenPhoton2_pt, weight);
            genphoton1EtaisEBEB_M2000->Fill(GenPhoton1_eta, weight);
            genphoton2EtaisEBEB_M2000->Fill(GenPhoton2_eta, weight);
            genphoton1PhiisEBEB_M2000->Fill(GenPhoton1_phi, weight);
            genphoton2PhiisEBEB_M2000->Fill(GenPhoton2_phi, weight);
            gendiphotoncosthetastarisEBEB_M2000->Fill(Gendiphoton_cosThetaStar, weight);
            genchidiphotonisEBEB_M2000->Fill(Gendiphoton_chiDiphoton, weight);
          }
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

   gendiphotonMinv->Write();
   genphoton1Pt->Write();
   genphoton2Pt->Write();
   genphoton1Eta->Write();
   genphoton2Eta->Write();
   genphoton1Phi->Write();
   genphoton2Phi->Write();
   gendiphotoncosthetastar->Write();
   genchidiphoton->Write();

   gendiphotonMinvisEBEB->Write();
   genphoton1PtisEBEB->Write();
   genphoton2PtisEBEB->Write();
   genphoton1EtaisEBEB->Write();
   genphoton2EtaisEBEB->Write();
   genphoton1PhiisEBEB->Write();
   genphoton2PhiisEBEB->Write();
   gendiphotoncosthetastarisEBEB->Write();
   genchidiphotonisEBEB->Write();

   gendiphotonMinvisEBEB_M2000->Write();
   genphoton1PtisEBEB_M2000->Write();
   genphoton2PtisEBEB_M2000->Write();
   genphoton1EtaisEBEB_M2000->Write();
   genphoton2EtaisEBEB_M2000->Write();
   genphoton1PhiisEBEB_M2000->Write();
   genphoton2PhiisEBEB_M2000->Write();
   gendiphotoncosthetastarisEBEB_M2000->Write();
   genchidiphotonisEBEB_M2000->Write();

   cout << "WeightAll Mbin: " << wt.back();
}
