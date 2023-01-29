1: import FWCore.ParameterSet.Config as cms

2: 

3: from Configuration.Generator.Pythia8CommonSettings_cfi import *

4: from Configuration.Generator.MCTunes2017.PythiaCP2Settings_cfi import *

5: from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

6: 

7: generator = cms.EDFilter("Pythia8GeneratorFilter",

8:     maxEventsToPrint = cms.untracked.int32(1),

9:     pythiaPylistVerbosity = cms.untracked.int32(1),

10:     filterEfficiency = cms.untracked.double(1.0),

11:     pythiaHepMCVerbosity = cms.untracked.bool(False),

12:     comEnergy = cms.double(13000.),

13:     PythiaParameters = cms.PSet(

14:         pythia8CommonSettingsBlock,

15:         pythia8CP2SettingsBlock,

16:         pythia8PSweightsSettingsBlock,	

17:         processParameters = cms.vstring(

18:             'ExtraDimensionsUnpart:ffbar2gammagamma = on',

19:             'ExtraDimensionsUnpart:gg2gammagamma = on',

20:             'PromptPhoton:gg2gammagamma = on',

21:             #'PromptPhoton:ffbar2gammagamma = on',

22: 	    'ExtraDimensionsUnpart:LambdaU = 3500.0',

23:             'ExtraDimensionsUnpart:lambda = 1.0',

24:             'ExtraDimensionsUnpart:dU = 1.9',

25:             'ExtraDimensionsUnpart:spinU = 2',

26:             'PhaseSpace:pTHatMin = 70',

27:             'PhaseSpace:mHatMin = 500',

28:             'PhaseSpace:mHatMax = 1000',

29:             ),

30:         parameterSets = cms.vstring('pythia8CommonSettings',

31:                                     'pythia8CP2Settings',

32:                                     'processParameters',

33: 				    'pythia8PSweightsSettings',	

34:                                     )

35:         )

36: )

37: 

38: ProductionFilterSequence = cms.Sequence(generator)

