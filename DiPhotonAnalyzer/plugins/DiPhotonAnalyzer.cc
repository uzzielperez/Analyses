// -*- C++ -*-
//
// Package:    Analyses/DiPhotonAnalyzer
// Class:      DiPhotonAnalyzer
// 
/**\class DiPhotonAnalyzer DiPhotonAnalyzer.cc Analyses/DiPhotonAnalyzer/plugins/DiPhotonAnalyzer.cc

 Description: Based on Steve K's Diphoton analyzer: https://github.com/skaplanhex/DiphotonAnalysis/blob/master/src/DiphotonAnalyzer.cc

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cilicia Uzziel Perez
//         Created:  Tue, 08 May 2018 00:41:08 GMT
//
//


// system include files
#include <memory>

using namespace std; 

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// Misc.
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

//TFileService
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

//for reco::Candidate
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"

//for the GenParticleCollection and GenParticles
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include <vector>
#include "TLorentzVector.h"
#include "TH2D.h"
#include "TTree.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class DiPhotonAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit DiPhotonAnalyzer(const edm::ParameterSet&);
      ~DiPhotonAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      
      // the handle which will be holding the genParticles from the event
      // reco::GenParticleCollection is just a typedef for std::vector<reco::GenParticle>
      edm::Handle< reco::GenParticleCollection > particles;
      // InputTag -> passed to analyzer in configuration file
      edm::InputTag particles_;

      TH1D* hNumPhotons;
      TH1D* hggMass;
      TH1D* hggMass_varBinning;
      TH1D* hleadingPhoPt;
      TH1D* hleadingPhoEta;
      TH1D* hleadingPhoPhi;
      TH1D* hsubleadingPhoPt;
      TH1D* hsubleadingPhoEta;
      TH1D* hsubleadingPhoPhi;
      TH1D* hggDPhi;

      TH1D* allPhotonPt;
      TH1D* allPhotonEta;
      TH1D* allPhotonPhi;

      bool makeTree;
      double leadingPtCut;
      double subleadingPtCut;

      int numTotalEvents = 0;
      int numEventsPassingCuts = 0;

      string eventSource;      

      // tree stuff
      TTree* tree;
      vector<double> PhotonPt;
      vector<double> PhotonEta;
      vector<double> PhotonPhi;
      vector<double> PhotonEnergy;
      vector<int> pdgId;
      vector<int> mother1;
      vector<int> mother2;
      vector<double> GenPt;
      vector<double> GenEta;
      vector<double> GenPhi;
      vector<double> GenEnergy;
      Double_t massHolder;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DiPhotonAnalyzer::DiPhotonAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   usesResource("TFileService");
   edm::Service<TFileService> fs;

   //Tree Name
   fPythiaGenTree = fs->make<TTree>("fTree","DiPhotonTree");

   // Branches 
     
   //---
   // Paramater set that is passed to the analyzer via the config file.  
   particles_ = iConfig.getParameter<edm::InputTag>("particles");
   leadingPtCut = iConfig.getParameter<double>("leadingPtCut");
   subleadingPtCut = iConfig.getParameter<double>("subleadingPtCut");   
   eventSource = iConfig.getParameter<string>("eventSource");
   makeTree = iConfig.getParameter<bool>("makeTree");
   
   cout<< "eventSource: " << eventSource << endl;
}


DiPhotonAnalyzer::~DiPhotonAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
DiPhotonAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;

   iEvent.getByLabel(particles_,particles);
   
    //Initialize
    double leadingPhotonPt = -99999.99;
    double leadingPhotonEta = -99999.99.;
    double leadingPhotonPhi = -99999.99;
    double leadingPhotonE = -99999.99;
    double subleadingPhotonPt = -99999.99;
    double subleadingPhotonEta = -99999.99;
    double subleadingPhotonPhi = -99999.99;
    double subleadingPhotonE = -99999.99;
    int    numPhotons = 0;
    int    numFinalState = 0;     

    numTotalEvents++;

     for (reco::GenParticleCollection::const_iterator iParticle = particles->begin(); iParticle != particles->end(); ++iParticle){
          int pdgIdNum = iParticle->pdgId();
          double pt = iParticle->pt();
          double eta = iParticle->eta();
          double phi = iParticle->phi();
          double energy = iParticle->energy();
          int status = iParticle->status();
          
          //if Particle is Photon, pdgIdNum==22
           if (status == 1 && pdgIdNum==22){
              allPhotonPt->Fill(pt);
              allPhotonEta->Fill(eta);
              allPhotonPhi->Fill(phi);
            }//end photon condition
            
            if (pdgIdNum==22) numPhotons++;
            
            //Sorting 
            if (pt > leadingPhotonPt){
                subleadingPhotonPt = leadingPhotonPt;
                subleadingPhotonEta = leadingPhotonEta;
                subleadingPhotonPhi = leadingPhotonPhi;
                subleadingPhotonE = leadingPhotonE;

                leadingPhotonPt = pt;
                leadingPhotonEta = eta;
                leadingPhotonPhi = phi;
                leadingPhotonE = energy;
            }

            else if ( (pt < leadingPhotonPt) && (pt > subleadingPhotonPt) ){
                subleadingPhotonPt = pt;
                subleadingPhotonEta = eta;
                subleadingPhotonPhi = phi;
                subleadingPhotonE = energy;
            }
              
     }//end loop over GenParticleCollection

     hNumPhotons->Fill(numPhotons);
     bool passedAllCuts = true; // no cuts for now, do offline

      if( passedAllCuts ){
            numEventsPassingCuts++;
            //fill histograms
            hleadingPhoPt->Fill(leadingPhotonPt);
            hleadingPhoEta->Fill(leadingPhotonEta);
            hleadingPhoPhi->Fill(leadingPhotonPhi);
            
            hsubleadingPhoPt->Fill(subleadingPhotonPt);
            hsubleadingPhoEta->Fill(subleadingPhotonEta);
            hsubleadingPhoPhi->Fill(subleadingPhotonPhi);
            subleadingPt_leadingPt->Fill(leadingPhotonPt,subleadingPhotonPt);
     
            //fill a mass plot
            TLorentzVector leadingPhoton,subleadingPhoton;
            leadingPhoton.SetPtEtaPhiE(leadingPhotonPt,leadingPhotonEta,leadingPhotonPhi,leadingPhotonE);
            subleadingPhoton.SetPtEtaPhiE(subleadingPhotonPt,subleadingPhotonEta,subleadingPhotonPhi,subleadingPhotonE);
            
            TLorentzVector total = leadingPhoton + subleadingPhoton; // I think this works
            double ggmass = total.M();
            hggMass->Fill( ggmass );
            hggMass_varBinning->Fill( ggmass );   
            
            if(makeTree){
              PhotonPt.push_back(leadingPhotonPt);
              PhotonPt.push_back(subleadingPhotonPt);
              PhotonEta.push_back(leadingPhotonEta);
              PhotonEta.push_back(subleadingPhotonEta);
              PhotonPhi.push_back(leadingPhotonPhi);
              PhotonPhi.push_back(subleadingPhotonPhi);
              PhotonEnergy.push_back(leadingPhotonE);
              PhotonEnergy.push_back(subleadingPhotonE);
              massHolder = ggmass;

              tree->Fill();

              PhotonPt.clear();
              PhotonEta.clear();
              PhotonPhi.clear();
              PhotonEnergy.clear();
              pdgId.clear();
              GenPt.clear();
              GenEta.clear();
              GenPhi.clear();
              GenEnergy.clear();
              massHolder = -1.; 
            }//makeTree
  }//passedCuts
#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
DiPhotonAnalyzer::beginJob()
{
    hNumPhotons = fs->make<TH1D>("hNumPhotons","Photon Multiplicity (|#eta|<1.4442)",11,-0.5,10.5);
    hggMass = fs->make<TH1D>("hggMass","",199,0,3000.);
    Double_t bins[7] = {0.,650.,1150.,1800.,2600.,3500.,13000.};
    hggMass_varBinning = fs->make<TH1D>("hggMass_varBinning","",6,bins);
    hggDPhi = fs->make<TH1D>("hggDPhi","",300,-3.141593,3.141593);
    hleadingPhoPt = fs->make<TH1D>("hleadingPhoPt","Leading Photon pT",1800.,0,1800.);
    hleadingPhoEta = fs->make<TH1D>("hleadingPhoEta","Leading Photon #eta",100,-1.5,1.5);
    hleadingPhoPhi = fs->make<TH1D>("hleadingPhoPhi","Leading Photon #varphi",100,-3.1416,3.1416);
    hsubleadingPhoPt = fs->make<TH1D>("hsubleadingPhoPt","Subleading Photon pT",1800.,0,1800.);
    hsubleadingPhoEta = fs->make<TH1D>("hsubleadingPhoEta","Subleading Photon #eta",100,-1.5,1.5);
    hsubleadingPhoPhi = fs->make<TH1D>("hsubleadingPhoPhi","Subleading Photon #varphi",100,-3.1416,3.1416);
    
    allPhotonPt = fs->make<TH1D>("allPhotonPt","",1800,0,1800.);
    allPhotonEta = fs->make<TH1D>("allPhotonEta","",100,-6.,6.);
    allPhotonPhi = fs->make<TH1D>("allPhotonPhi","",100,-3.1416,3.1416);
    
    //tree stuff
    if( makeTree ){
      tree = fs->make<TTree>("tree","tree");
      tree->Branch("PhotonPt",&PhotonPt);
      tree->Branch("PhotonEta",&PhotonEta);
      tree->Branch("PhotonPhi",&PhotonPhi);
      tree->Branch("PhotonEnergy",&PhotonEnergy);
      tree->Branch("pdgId",&pdgId);
      // tree->Branch("mother1",&mother1);
      // tree->Branch("mother2",&mother2);
      tree->Branch("GenPt",&GenPt);
      tree->Branch("GenEta",&GenEta);
      tree->Branch("GenPhi",&GenPhi);
      tree->Branch("GenEnergy",&GenEnergy);
      tree->Branch("ggMass",&massHolder,"ggMass/D");
    }
     
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DiPhotonAnalyzer::endJob() 
{
    hggMass->GetXaxis()->SetTitle("M_{#gamma#gamma} (GeV/c^{2})");
    cout << "Number of Events Passing Cuts: " << numEventsPassingCuts << endl;
    cout << "Number of Total Events: " << numTotalEvents << endl;
    
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DiPhotonAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DiPhotonAnalyzer);
