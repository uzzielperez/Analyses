import FWCore.ParameterSet.Config as cms 

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8aMCatNLOSettingsBlock,
        processParameters = cms.vstring(
	    'ExtraDimensionsUnpart:ffbar2gammagamma = on',
	    'ExtraDimensionsUnpart:gg2gammagamma = on', 
            'ExtraDimensionsUnpart:LambdaU =  15000',
            'ExtraDimensionsUnpart:lambda = 1.0',
	    'ExtraDimensionsUnpart:dU = 1.06', 
            ),  
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings', 
                                    'pythia8aMCatNLOSettings',
				    'processParameters',
                                    )   
        )   
)


