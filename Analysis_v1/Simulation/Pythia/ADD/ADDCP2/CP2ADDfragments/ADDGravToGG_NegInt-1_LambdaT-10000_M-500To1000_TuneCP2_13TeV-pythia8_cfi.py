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
            'ExtraDimensionsLED:LambdaT = 10000.0',
            'ExtraDimensionsLED:n = 4',
            'ExtraDimensionsLED:ffbar2gammagamma = on',
            'ExtraDimensionsLED:gg2gammagamma = on',
            'ExtraDimensionsLED:CutOffmode = 2', 
            'ExtraDimensionsLED:NegInt= 1',
            'PhaseSpace:pTHatMin = 70.0',
	    'PhaseSpace:mHatMin = 500.0',	    
	    'PhaseSpace:mHatMax = 1000.0', 
            ),  
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP2Settings', 
				    'processParameters',
                                    )   
        )   
)


