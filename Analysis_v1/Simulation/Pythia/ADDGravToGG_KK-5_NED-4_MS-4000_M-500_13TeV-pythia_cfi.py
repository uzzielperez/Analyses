import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1.),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'ExtraDimensionsLED:ffbar2gammagamma = on', 
            'ExtraDimensionsLED:gg2gammagamma = on',
            'ExtraDimensionsLED:MD = 1128.3791671',
	    'ExtraDimensionsLED:n = 4', 
	    'ExtraDimensionsLED:LambdaT = 4000.',
            'ExtraDimensionsLED:CutoffMode = 2',
	    'PhaseSpace:pTHatMin = 70.',
	    'PhaseSpace:mHatMin = 500.0'
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters'
        )
    )
)


~                             
