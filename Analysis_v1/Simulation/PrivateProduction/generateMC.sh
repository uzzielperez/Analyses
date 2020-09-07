#!/bin/bash

# Script to generate CMSSW full-sim cfg files
# from GEN cfgs (aka Pythia8 or RandomGun cfg files)

#### After checking out a CMSSW release, put the GEN cfg in
#### Configuration/GenProduction/python/
#CFGPATH=Configuration/GenProduction/python/Guns
#CFGPATH=Configuration/GenProduction/python/ThirteenTeV
CFGPATH=MY/PROJECT/python

#### Specify the filename of the GEN cfg
#CFG=Py8PtGun_bb_cfi.py
#CFG=ADDGravToGG_NegInt-1_LambdaT-9000_M-2000To4000_TuneCP2_13TeV-pythia8_cfi.py
#CFG=GG_M-2000To4000_Pt70_TuneCP2_13TeV-pythia8_cfi.py
#CFG=GG_M-4000To13000_Pt70_TuneCP2_13TeV-pythia8_cfi.py
#CFG=sherpa_AA_3j_13TeV_MASTER_cff.py
#CFG=sherpa_EEA_0j_pT20_13TeV_MASTER_cff.py
#CFG=sherpa_AAA_0j_pT20_13TeV_MASTER_cff.py
#CFG=sherpa_AAA_2j_pT20_13TeV_MASTER_cff.py
#CFG=sherpa_EEA_2j_pT20_13TeV_MASTER_cff.py
CFG=sherpa_GGGJets_Pt-15toInf_13TeV_15-15-15sym_sherpa_MASTER_cff.py

#### Global tag
#COND=80X_mcRun2_asymptotic_2016_TrancheIV_v6
COND=94X_mc2017_realistic_v10

#### Event content: determines which collections are stored
#EVTCONT=FEVTDEBUG
EVTCONT=AODSIM

#### PU scenario: see https://github.com/cms-sw/cmssw/blob/master/Configuration/StandardSequences/python/Mixing.py
PU=2016_25ns_Moriond17MC_PoissonOOTPU
PU_INPUT="dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-MCRUN2_71_V1-v2/GEN-SIM"

NEVTS=20 # will be overwritten in crabMC 

#ERA=Run2_2016
ERA=Run2_2017

# RAW - energy deposits per channel 
# Run RECO on raw
# GEN collisions 
# SIM - follows collision particles as they interact with detector
# read more on 'underlying event' - soft proton-proton collisions.. vs hard interaction vs parton shower

# hard collisions e.g. 3 photons + jet (quark/gluon) 

# HLT - Triphoton triggers... for accuracy..
# pileup fake rate
# madgraph ---> 

#https://gitlab.cern.ch/cms-sw/cmssw/blob/ab8b5a9a563286db65023d041f64e1e4fb7eb256/Configuration/HLT/python/autoHLT.py

#FNAME=Pythia8_noPU_AODSIM_allsteps_cfg.py
#FNAME=Pythia8_noPU_AODSIM_allsteps_BKG_cfg.py
#FNAME=noPU_${EVTCONT}_allsteps_EEA_cfg.py
#FNAME=noPU_${EVTCONT}_allsteps_EEA_cfg.py
#FNAME=Pythia8_noPU_AODSIM_allsteps_AAA_cfg.py
FNAME=noPU_${EVTCONT}_allsteps_GGGJetsPt15_SherpaRun2_2017_cfg.py

OUTFILE=noPU_${EVTCONT}_allsteps_GGGJetsPt15_SherpaRun2_2017.root
#OUTFILE=noPU_AODSIM_allsteps_GGGJetsPt15_Sherpa_cfg.py
#OUTFILE=noPU_${EVTCONT}_allsteps_EEA_2j_cfg.root

#__________ Commands to generate the CMSSW full-sim cfg __________#
# These were generated using the runTheMatrix.py script
# with suitable change of parameters

#### All Steps ####
#cmsDriver.py $CFGPATH/$CFG --mc --conditions $COND -n $NEVTS --era Run2_2017 --geometry DB:Extended --eventcontent $EVTCONT --runUnscheduled -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@fake,RAW2DIGI,L1Reco,RECO,EI --datatier $EVTCONT --beamspot Realistic25ns13TeVEarly2017Collision --fileout file:$OUTFILE --python_filename $FNAME --no_exec

#cmsDriver.py $CFGPATH/$CFG --mc --conditions $COND -n $NEVTS --era Run2_2017 --eventcontent $EVTCONT --runUnscheduled --relval 9000,3000 -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@fake,RAW2DIGI,L1Reco,RECO,EI --datatier GEN-SIM-DIGI-RAW-RECO --beamspot Realistic25ns13TeVEarly2017Collision --fileout file:step_all_nopu.root --python_filename Pythia8_noPU_AODSIM_allsteps_cfg.py --no_exec


#NoPileup
#cmsDriver.py $CFGPATH/$CFG --mc --conditions $COND -n $NEVTS --era $ERA --eventcontent $EVTCONT --relval 9000,3000 -s GEN,SIM,DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2016,RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-DIGI-RAW-RECO --beamspot Realistic25ns13TeV2017Collision --fileout file:step_${EVTCONT}.root --python_filename ${CFG%_*}_noPU_${EVTCONT}_cfg.py  --no_exec

#Pileup
#cmsDriver.py $CFGPATH/$CFG --mc --conditions $COND -n $NEVTS --era Run2_2017 --eventcontent $EVTCONT -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@fake,RAW2DIGI,L1Reco,RECO --pileup_input $PU_INPUT --pileup $PU --datatier GEN-SIM-DIGI-RAW-RECO --beamspot Realistic25ns13TeVEarly2017Collision --fileout file:step_full.root --python_filename ${CFG%_*}_${PU}_${EVTCONT}_cfg.py --no_exec

#cmsDriver.py $CFGPATH/$CFG --mc --conditions $COND -n $NEVTS --era Run2_2017 --eventcontent $EVTCONT -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@fake,RAW2DIGI,L1Reco,RECO --pileup_input $PU_INPUT --pileup $PU --datatier GEN-SIM-DIGI-RAW-RECO --beamspot Realistic25ns13TeV2017Collision --fileout file:$OUTFILE --python_filename ${CFG%_*}_${PU}_${EVTCONT}_cfg.py --no_exec

#### Stepped ####

# GEN-SIM-RAW
#cmsDriver.py $CFGPATH/$CFG --conditions $COND -n $NEVTS --era Run2_2016 --eventcontent RAWSIM -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@fake --pileup_input $PU_INPUT --pileup $PU --datatier GEN-SIM-RAW --beamspot Realistic25ns13TeV2016Collision --fileout file:step1.root --python_filename ${CFG%_*}_RAWSIM_${PU}_step1_cfg.py --no_exec

# DIGI-RECO
#cmsDriver.py step2 --filein file:step1.root --fileout file:step2.root --mc --eventcontent AODSIM --conditions $COND -n $NEVTS --era Run2_2016 --datatier AODSIM --step RAW2DIGI,L1Reco,RECO --python_filename ${CFG%_*}_AODSIM_${PU}_step2_cfg.py --no_exec --runUnscheduled

# MINIAOD
#cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --conditions $COND --era Run2_2016 --no_exec --filein step2.root

### Stepped Triphoton" 
#https://cmssdt.cern.ch/lxr/source/Configuration/StandardSequences/python/VtxSmeared.py?v=CMSSW_9_4_0
# GEN-SIM-RAW
cmsDriver.py $CFGPATH/$CFG --mc --conditions $COND -n $NEVTS --era Run2_2017 --eventcontent RAWSIM -s GEN,SIM,DIGI,L1,DIGI2RAW,HLT:@relval2017 --datatier GEN-SIM-RAW --beamspot Realistic25ns13TeVEarly2017Collision --fileout file:step1.root --python_filename ${CFG%_*}_RAWSIM_noPU_step1_cfg.py --no_exec

# DIGI-RECO
#cmsDriver.py step2 --filein file:step1.root --fileout file:step2.root --mc --eventcontent AODSIM --conditions $COND -n $NEVTS --era Run2_2017 --datatier AODSIM --step RAW2DIGI,L1Reco,RECO --python_filename ${CFG%_*}_AODSIM_step2_cfg.py --no_exec --runUnscheduled

# MINIAOD
#cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --conditions $COND --era Run2_2017 --no_exec --filein file:step2.root -n $NEVTS
