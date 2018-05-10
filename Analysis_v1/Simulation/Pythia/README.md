# Pythia CMSSW Test

```bash
## select cmssw environment
## 2018 (bash syntax

export SCRAM_ARCH=slc6_amd64_gcc630  
export CMSSW_VERSION=CMSSW_9_3_8

# setup cmssw release
cmsrel $CMSSW_VERSION  
cd $CMSSW_VERSION/src  
cmsenv  

# Source: https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGenIntro
# for Sample 

curl -s https://raw.githubusercontent.com/cms-sw/genproductions/master/python/ThirteenTeV/RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_cfi.py --retry 2 --create-dirs -o Configuration/GenProduction/python/ThirteenTeV/RSGravitonToZZ_kMpl01_M_1000_TuneCUETP8M1_13TeV_pythia8_cfi.py

# fetch ADDDiPhoton (Steven’s) and ADDDilepton generator fragments
cd Configuration/GenProduction/python/ThirteenTeV/
wget https://raw.githubusercontent.com/cms-sw/genproductions/458358f7dd6400b69c440c03113ad50875cf3d65/python/ThirteenTeV/ADDDiLepton_LambdaT7000_M-1700_13TeV-pythia8_MASTER_cff.py

wget https://raw.githubusercontent.com/cms-sw/genproductions/62b0ace0af365166fc335eed41bd02e65c844d9a/python/ThirteenTeV/ADDdiPhoton_LambdaT-2500_PtHat-150to500_TuneCUETP8M1_13TeV-pythia8_cfi.py

# ADD cmsDriver.py - generate configuration file
# Source: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchool2018GeneratorExerciseatFNAL#Using_GeneratorInterface

cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/ADDDiLepton_LambdaT7000_M-1700_13TeV-pythia8_MASTER_cff.py -s GEN --mc --no_exec --conditions auto:mc -n 10

# cmsRun
# to print output to .txt file cmsRun ADDDiLepton_LambdaT7000_M-1700_13TeV-pythia8_MASTER_cff_py_GEN.py > <outfile>.txt

cmsRun ADDDiLepton_LambdaT7000_M-1700_13TeV-pythia8_MASTER_cff_py_GEN.py 

# this will generate a root file for plotting. ADDDiLepton_LambdaT7000_M-1700_13TeV-pythia8_MASTER_cff_py_GEN.root 
# edmDumpEventContent to root file is still needed after cmsRun

edmDump ADDDiLepton_LambdaT7000_M-1700_13TeV-pythia8_MASTER_cff_py_GEN.root 

# output of edmDump

Type                                  Module               Label      Process   
--------------------------------------------------------------------------------
GenEventInfoProduct                   "generator"          ""         "GEN"     
ROOT::Math::PositionVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag>    "genParticles"       "xyz0"     "GEN"     
double                                "ak4GenJets"         "rho"      "GEN"     
double                                "ak4GenJetsNoNu"     "rho"      "GEN"     
double                                "ak8GenJets"         "rho"      "GEN"     
double                                "ak8GenJetsNoNu"     "rho"      "GEN"     
double                                "ak4GenJets"         "sigma"    "GEN"     
double                                "ak4GenJetsNoNu"     "sigma"    "GEN"     
double                                "ak8GenJets"         "sigma"    "GEN"     
double                                "ak8GenJetsNoNu"     "sigma"    "GEN"     
edm::HepMCProduct                     "generatorSmeared"   ""         "GEN"     
edm::TriggerResults                   "TriggerResults"     ""         "GEN"     
float                                 "genParticles"       "t0"       "GEN"     
vector<double>                        "ak4GenJets"         "rhos"     "GEN"     
vector<double>                        "ak4GenJetsNoNu"     "rhos"     "GEN"     
vector<double>                        "ak8GenJets"         "rhos"     "GEN"     
vector<double>                        "ak8GenJetsNoNu"     "rhos"     "GEN"     
vector<double>                        "ak4GenJets"         "sigmas"   "GEN"     
vector<double>                        "ak4GenJetsNoNu"     "sigmas"   "GEN"     
vector<double>                        "ak8GenJets"         "sigmas"   "GEN"     
vector<double>                        "ak8GenJetsNoNu"     "sigmas"   "GEN"     
vector<int>                           "genParticles"       ""         "GEN"     
vector<reco::GenJet>                  "ak4GenJets"         ""         "GEN"     
vector<reco::GenJet>                  "ak4GenJetsNoNu"     ""         "GEN"     
vector<reco::GenJet>                  "ak8GenJets"         ""         "GEN"     
vector<reco::GenJet>                  "ak8GenJetsNoNu"     ""         "GEN"     
vector<reco::GenMET>                  "genMetCalo"         ""         "GEN"     
vector<reco::GenMET>                  "genMetTrue"         ""         "GEN"     
vector<reco::GenParticle>             "genParticles"       ""         "GEN"     

# Examine the root file 
root -l ADDDiLepton_LambdaT7000_M-1700_13TeV-pythia8_MASTER_cff_py_GEN.root 
TBrowser b

# When the Browser appears, perform the following clicks with the mouse:
# ROOTFILE -> Events -> GenEventInfoProduct_generator__GEN -> GenEventInfoProduct_generator__GEN.obj -> qScale()

# or just do in root prompt
Events->Draw("GenEventInfoProduct_generator__GEN.obj.qScale_")

# Now let’s test for Steven’s ADDDiPhoton generator fragment with more events
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/ADDdiPhoton_LambdaT-2500_PtHat-150to500_TuneCUETP8M1_13TeV-pythia8_cfi.py -s GEN --mc --no_exec --conditions auto:mc -n 5000

cmsRun ADDdiPhoton_LambdaT-2500_PtHat-150to500_TuneCUETP8M1_13TeV-pythia8_cfi.py

edmDumpEventContent ADDdiPhoton_LambdaT-2500_PtHat-150to500_TuneCUETP8M1_13TeV-pythia8_cfi_py_GEN.root 

Type                                  Module               Label      Process   
--------------------------------------------------------------------------------
GenEventInfoProduct                   "generator"          ""         "GEN"     
ROOT::Math::PositionVector3D<ROOT::Math::Cartesian3D<float>,ROOT::Math::DefaultCoordinateSystemTag>    "genParticles"       "xyz0"     "GEN"     
double                                "ak4GenJets"         "rho"      "GEN"     
double                                "ak4GenJetsNoNu"     "rho"      "GEN"     
double                                "ak8GenJets"         "rho"      "GEN"     
double                                "ak8GenJetsNoNu"     "rho"      "GEN"     
double                                "ak4GenJets"         "sigma"    "GEN"     
double                                "ak4GenJetsNoNu"     "sigma"    "GEN"     
double                                "ak8GenJets"         "sigma"    "GEN"     
double                                "ak8GenJetsNoNu"     "sigma"    "GEN"     
edm::HepMCProduct                     "generatorSmeared"   ""         "GEN"     
edm::TriggerResults                   "TriggerResults"     ""         "GEN"     
float                                 "genParticles"       "t0"       "GEN"     
vector<double>                        "ak4GenJets"         "rhos"     "GEN"     
vector<double>                        "ak4GenJetsNoNu"     "rhos"     "GEN"     
vector<double>                        "ak8GenJets"         "rhos"     "GEN"     
vector<double>                        "ak8GenJetsNoNu"     "rhos"     "GEN"     
vector<double>                        "ak4GenJets"         "sigmas"   "GEN"     
vector<double>                        "ak4GenJetsNoNu"     "sigmas"   "GEN"     
vector<double>                        "ak8GenJets"         "sigmas"   "GEN"     
vector<double>                        "ak8GenJetsNoNu"     "sigmas"   "GEN"     
vector<int>                           "genParticles"       ""         "GEN"     
vector<reco::GenJet>                  "ak4GenJets"         ""         "GEN"     
vector<reco::GenJet>                  "ak4GenJetsNoNu"     ""         "GEN"     
vector<reco::GenJet>                  "ak8GenJets"         ""         "GEN"     
vector<reco::GenJet>                  "ak8GenJetsNoNu"     ""         "GEN"     
vector<reco::GenMET>                  "genMetCalo"         ""         "GEN"     
vector<reco::GenMET>                  "genMetTrue"         ""         "GEN"     
vector<reco::GenParticle>             "genParticles"       ""         "GEN"    }

```
