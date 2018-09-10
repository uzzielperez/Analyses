import FWCore.ParameterSet.Config as cms 

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'ExtraDimensionsLED:LambdaT = 13000.0',
            'ExtraDimensionsLED:n = 2',
            'ExtraDimensionsLED:ffbar2gammagamma = on',
            'ExtraDimensionsLED:gg2gammagamma = on',
            'ExtraDimensionsLED:CutOffmode = 2', 
            'ExtraDimensionsLED:NegInt= 0',
            'PhaseSpace:pTHatMin = 70.0',
	    'PhaseSpace:mHatMin = 2000.0',
	    'PhaseSpace:mHatMax = 1000.0'
      


  ),  
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )   
    )   
)

