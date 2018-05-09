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

             
     }//end loop over GenParticleCollection
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
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DiPhotonAnalyzer::endJob() 
{
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
