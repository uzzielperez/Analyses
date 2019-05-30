import os
from glob import glob
import re
import argparse

parser = argparse.ArgumentParser(description='List files')
parser.add_argument('-p','--pattern', required=True, help='GluGluSpin0ToGammaGamma_W_1p4 for example',type=str)
args = parser.parse_args()

eosDir='/eos/uscms/store/user/cuperez'
xrootd='root://cmsxrootd.fnal.gov' # FNAL

pattern=args.pattern
print 'Analyzing %s' %(pattern)

cmssw_base = os.getenv("CMSSW_BASE")
cfg= cmssw_base + '/src/MLAnalyzer/RecHitAnalyzer/python/ConfFile_cfg.py'


#inputFiles_ = ['%s/%s'%(xrootd,path) for path in glob('%s/DiPhotonAnalysis/ExoANDiphoton/*/*/*root'%(eosDir,pattern))]
inputFiles_ = ['%s/%s'%(xrootd,path) for path in glob('%s/DiPhotonAnalysis/ExoANDiphoton/%s*/*/*/*'%(eosDir,pattern))]

listname = 'list_%s.txt'%pattern
with open(listname, 'w') as list_file:
    for inputFile in inputFiles_:
        list_file.write("%s\n" % inputFile)
	print inputFile

