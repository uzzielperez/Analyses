import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP2SettingsBlock,
        processParameters = cms.vstring(
            'ExtraDimensionsUnpart:ffbar2gammagamma = on',
            'ExtraDimensionsUnpart:gg2gammagamma = on',
            'PromptPhoton:gg2gammagamma = on',
            #'PromptPhoton:ffbar2gammagamma = on',
	    'ExtraDimensionsUnpart:LambdaU = ${LambdaU}',
            'ExtraDimensionsUnpart:lambda = 1.0',
            'ExtraDimensionsUnpart:dU = ${du}',
            'ExtraDimensionsUnpart:spinU = 2',
            'PhaseSpace:pTHatMin = ${pTcut}',
            'PhaseSpace:mHatMin = ${minMass}',
            'PhaseSpace:mHatMax = ${maxMass}',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP2Settings',
                                    'processParameters',
                                    )
        )
)

ProductionFilterSequence = cms.Sequence(generator)
