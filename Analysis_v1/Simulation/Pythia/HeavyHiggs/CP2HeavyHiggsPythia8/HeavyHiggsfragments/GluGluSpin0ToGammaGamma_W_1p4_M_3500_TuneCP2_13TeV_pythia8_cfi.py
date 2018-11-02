import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(1.095e-3),
        filterEfficiency = cms.untracked.double(1),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
	pythia8CP2SettingsBlock,
        processParameters = cms.vstring(
            'HiggsSM:gg2H = on',
            '25:m0 = 3500.0',
            '25:mWidth = 49.0',
            '25:onMode = off',
            '25:OnIfMatch = 22 22',
            '25:doForceWidth = on',
            'Higgs:clipWings = on',
            'Higgs:clipWings = 10',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
				    'pythia8CP2Settings', 
                                    'processParameters',
                                    )
        )
)

ProductionFilterSequence = cms.Sequence(generator)

