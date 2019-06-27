import os
from glob import glob
import re
import argparse

# Command line options
parser = argparse.ArgumentParser(description="cmsDriver")
parser.add_argument("-i", "--inputfile", default="parsedis.txt", help="Datasets you need.")
parser.add_argument("-d", "--delete", action="store_true", help="Clean directory and delete copied files")
parser.add_argument("-r", "--run", action="store_true", help="Run os.system(cmd) to get CRAB files.")
parser.add_argument("-v", "--verbose", help="Debugging option", action="store_true")
parser.add_argument("-p", "--parse", action="store_true", help="Parse log files.")
parser.add_argument("-a", "--average", action="store_true", help="Get average.")
#parser.add_argument("-f", "--format", action="store_true")
parser.add_argument("-s", "--sort", action="store_true", help="Sort by dataset")
parser.add_argument("-t", "--timestamped", action="store_true")
args = parser.parse_args()

eosDir='/eos/uscms/store/user/cuperez'
xrootd='root://cmsxrootd.fnal.gov' # FNAL
#xrootd='root://eoscms.cern.ch' # CERN

signal='RSGravToGG*_TuneCUEP8M1_13TeV-pythia8'
signal='GluGluSpin0ToGG*_TuneCUEP8M1_13TeV-pythia8'
inputFiles_ = ['%s/%s'%(xrootd,path) for path in glob('%s/DiPhotonAnalysis/xsec/%s/*/*/*/*/*'%(eosDir,signal))]

listname = 'xseclist.txt'
with open(listname, 'w') as list_file:
    for inputFile in inputFiles_:
	#print inputFile
	inputFile = inputFile.replace('/eos/uscms', '')	
	print inputFile
        list_file.write("%s\n" % inputFile)

	pattern = r'DiPhotonAnalysis/xsec/([^(]*)/crab'
        match = re.findall(pattern, inputFile)
        dataset = match[0]
        tagpattern = 'cmsRun_([^(]*).log.tar.gz'
        tag = re.findall(tagpattern, inputFile)
        tarredsets = ".".join((dataset+tag[0], "tar.gz"))

        # Copy the output
        cmd = 'xrdcp %s %s' %(inputFile, tarredsets)
        tarcmd = 'tar -xvf %s -C %s' %(tarredsets, dataset)

        if args.run:
                os.system(cmd)
                if not os.path.exists(dataset):
                        mkdircmd = 'mkdir %s' %(dataset)
                        os.system(mkdircmd)
                os.system(tarcmd)
        if args.delete:
                os.system("rm -rf %s*" %(dataset))
        if args.verbose:
                print cmd
                print tarcmd

