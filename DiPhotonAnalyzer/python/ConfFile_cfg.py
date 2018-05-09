import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')


options.register('leadingPtCut',
                 60.,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "leading photon pt cut"
)

options.register('subleadingPtCut',
                 60.,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "subleading photon pt cut"
)

options.register('makeTree',
                True,
                VarParsing.multiplicity.singleton,
                VarParsing.varType.bool,
                "whether or not to include a tree in the output file")

options.setDefault('maxEvents', -1)
options.parseArguments()

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )


process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:myfile.root'
         'file:/afs/cern.ch/user/c/ciperez/Generation/CMSSW_9_3_8/src/ADDGravToGG_NED-4_LambdaT-4000_M-500_13TeV-pythia8_cff_py_GEN.root'
    )
)

process.TFileService = cms.Service("TFileService",
                fileName = cms.string("TestADDPythia.root")
                            )


process.demo = cms.EDAnalyzer('DiPhotonAnalyzer',
          
  particles = cms.InputTag("genParticles"),
  leadingPtCut = cms.double(options.leadingPtCut),
  subleadingPtCut = cms.double(options.subleadingPtCut),
  makeTree = cms.bool(options.makeTree)
)


process.p = cms.Path(process.demo)
