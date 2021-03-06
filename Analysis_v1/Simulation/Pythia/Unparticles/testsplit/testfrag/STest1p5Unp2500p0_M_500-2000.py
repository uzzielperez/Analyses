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
	    'ExtraDimensionsUnpart:ffbar2gammagamma = on',
	    'ExtraDimensionsUnpart:gg2gammagamma = on', 
            'ExtraDimensionsUnpart:LambdaU =  2500.0',
            'ExtraDimensionsUnpart:lambda = 1.0', 
	    'ExtraDimensionsUnpart:dU = 1.5',
	    #'ExtraDimensionsUnpart:spinU = 2',
	    'PhaseSpace:pTHatMin = 70.0',
            'PhaseSpace:mHatMin = 500',
            'PhaseSpace:mHatMax = 2000', 
            ),  
        parameterSets = cms.vstring('pythia8CommonSettings',
				    'pythia8CUEP8M1Settings',
				    'processParameters',
                                    )   
        )   
)
ProductionFilterSequence = cms.Sequence(generator)

