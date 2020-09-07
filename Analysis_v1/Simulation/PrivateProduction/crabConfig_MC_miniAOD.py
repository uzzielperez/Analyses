from WMCore.Configuration import Configuration
config = Configuration()
#from CRABClient.UserUtilities import config, getUsernameFromSiteDB

EVTCONT = 'MINIAODSIM'
PU = 'noPU'
PACK = 'sherpa_GGGJets_Pt-15toInf_13TeV_15-15-15sym_sherpa_MASTER.tgz'

#--- sherpa_GGGJets_Pt-15toInf_13TeV_15-15-15sym_sherpa_MASTER_RAWSIM_noPU_step1_cfg.py
CFG = 'GGGJets_Pt-15toInf_13TeV_15-15-15sym_sherpa'


config.section_("General")
config.General.requestName = 'sherpa_%s_%s_%s_TEST_ev'%(CFG,PU,EVTCONT)
config.General.workArea = 'outcrab_MC'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'sherpa_GGGJets_Pt-15toInf_13TeV_15-15-15sym_sherpa_MASTER_AODSIM_step2_cfg.py'
config.JobType.psetName = 'miniAOD-prod_PAT.py'
config.JobType.maxMemoryMB = 2800
config.JobType.inputFiles = [PACK]


config.section_("Data")
config.Data.outputPrimaryDataset = EVTCONT
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 480
config.Data.totalUnits = 480
config.Data.publication = False
#config.Data.userInputFiles = ['/store/user/cuperez/triphoton/PrivateProd/RAWSIM/step1.root']
config.Data.userInputFiles = open('LISTS/step2_files.txt').readlines()
config.Data.outputDatasetTag = '%s_%s_%s_Sherpa'%(CFG,PU,EVTCONT)
config.Data.outLFNDirBase = '/store/user/ciperez/triphoton/PrivateProduction/EventBased'

config.section_("Site")
config.Site.storageSite = 'T3_US_FNALLPC'
