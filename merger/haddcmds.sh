#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-1000To2000_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/crab_GGJets_M-1000To2000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203147/0000 | grep \.root`
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-2000To4000_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-2000To4000_Pt-50_13TeV-sherpa/crab_GGJets_M-2000To4000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203156/0000 | grep \.root`
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-200To500_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-200To500_Pt-50_13TeV-sherpa/crab_GGJets_M-200To500_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203125/0000 | grep \.root`
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-4000To6000_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/crab_GGJets_M-4000To6000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203212/0000 | grep \.root`
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-500To1000_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-500To1000_Pt-50_13TeV-sherpa/crab_GGJets_M-500To1000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203137/0000 | grep \.root`
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-6000To8000_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-6000To8000_Pt-50_13TeV-sherpa/crab_GGJets_M-6000To8000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203224/0000 | grep \.root`
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-60To200_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-60To200_Pt-50_13TeV-sherpa/crab_GGJets_M-60To200_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203112/0000 | grep \.root`
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-8000To13000_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/GGJets_M-8000To13000_Pt-50_13TeV-sherpa/crab_GGJets_M-8000To13000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180202_203237/0000 | grep \.root`