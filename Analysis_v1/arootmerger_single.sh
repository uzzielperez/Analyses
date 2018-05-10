#!/bin/bash
hadd -f root://cmseos.fnal.gov//store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/GGJets_M-500To1000_Pt-50_13TeV-sherpa.root `xrdfs root://cmseos.fnal.gov ls -u /store/user/cuperez/DiPhotonAnalysis/Summer16GGJetsResubmit/GGJets_M-500To1000_Pt-50_13TeV-sherpa/crab_GGJets_M-500To1000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180216_200831/0000/ | grep \.root`
