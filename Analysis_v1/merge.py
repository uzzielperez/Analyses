import os 
import sys
import glob
import ROOT
import re
import time
import subprocess

########################################
# Merge Settings 

mergeloop = True     #Set to false if there is only one INPUTDIR
data =   False         # Set to false if mc 
signal = True 

############### Commands and Extensions
rootpreeos = 'root://cmseos.fnal.gov/'
rootxrd = 'xrdfs root://cmseos.fnal.gov ls -u '
#rootxrd = 'xrdfsls -u' #alias of previous
greproot = ' | grep \.root'
crab = '/crab_'
rootext = '.root'
cmsxrootd = 'root://cmsxrootd.fnal.gov/'
################### Input Directory
# Main
#INPUTDIR = '/store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/'
#INPUTDIR = '/store/user/cuperez/DiPhotonAnalysis/....'
#INPUTDIR = '/store/user/cuperez/DiPhotonAnalysis/Run2016Data/DoubleEG/'
INPUTDIR = '/store/user/cuperez/ADDGravToGGSherpa/'

# For Resubmissions
#INPATH = '/store/user/cuperez/DiPhotonAnalysis/Summer16GGJetsResubmit/GGJets_M-500To1000_Pt-50_13TeV-sherpa/crab_GGJets_M-500To1000_Pt-50_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180216_200831/0000/'

################# OUTPUT 
# Main Output Dir
#outputdir = '/store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/'
#outputdir = '/store/user/cuperez/DiPhotonAnalysis/Summer16-GGJets-Merge/'
#outputdir = '/store/user/cuperez/DiPhotonAnalysis/Run2016Data-Merged/'
outputdir = '/store/user/cuperez/ADDGravToGG/ADDGravToGG_MS-4000_NED-4_KK-1_M-200-4000/'

#ref

# FinalState and Mass bin
fstate = 'ADDGravToGG_MS-4000_NED-4_KK-1_M-'
#fstate = 'DoubleEG__'
#fstate = 'GGJets_M-'

# MassBin/Cat
#runormassbin = ['2000To4000', '500To1000']
runormassbin = ['1000To2000', '2000To4000', '200To500', '500To1000']
#runormassbin = ["1000To2000", "2000To4000","200To500","4000To6000","500To1000","6000To8000","60To200","8000To13000"]  
#runormassbin = ['Run2016B-03Feb2017_ver2-v2__MINIAOD/', 'Run2016C-03Feb2017-v1__MINIAOD/', 'Run2016D-03Feb2017-v1__MINIAOD/', 'Run2016E-03Feb2017-v1__MINIAOD/', 'Run2016F-03Feb2017-v1__MINIAOD/', 'Run2016G-03Feb2017-v1__MINIAOD/', 'Run2016H-03Feb2017_ver2-v1__MINIAOD/', 'Run2016H-03Feb2017_ver3-v1__MINIAOD/']

# Trailing Characters
#ptcut = '_Pt-50' #no ptcut with ADDGravToGGSherp
energy ='_13TeV'
gen = '-sherpa'

# Reference
#/store/user/cuperez/ADDGravToGGSherpa/ADDGravToGG_MS-4000_NED-4_KK-1_M-200To500_13TeV-sherpa/crab_ADDGravToGG_MS-4000_NED-4_KK-1_M-200To500_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180517_193448
#/store/user/cuperez/ADDGravToGGSherpa/ADDGravToGG_MS-4000_NED-4_KK-1_M-500To1000_13TeV-sherpa/crab_ADDGravToGG_MS-4000_NED-4_KK-1_M-500To1000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180517_193500


# Version
INPUTV = '__80XMiniAODv2__MINIAODSIM'
#INPUTV = 'ver2-v2__MINIAOD/'

# Subdirectories
#INPUTSUB = ["/180202_203147/0000","/180202_203156/0000","/180202_203125/0000",
#"/180202_203212/0000","/180202_203137/0000","/180202_203224/0000",
#"/180202_203112/0000","/180202_203237/0000"]
#INPUTSUB = ['180307_213615/0000','180307_213641/0000', '180307_213658/0000', '180307_213717/0000','180307_213733/0000','180307_213750/0000','180307_213819/0000','180307_213845/0000']
INPUTSUB = ['/180517_193429/0000','/180517_193438/0000', '/180517_193448/0000', '/180517_193500/0000']


# Timer
sw = ROOT.TStopwatch()
sw.Start()

################ MERGING

#--------------------------------------------------------
# Merge Loop
#create bash script that stitches the names together
mergerfile = 'arootmerger.sh'
amergerfile = 'arootmerger_single.sh'
chainerfile = 'aInputMerged.txt' # input to runChainClass.py
floop = open(mergerfile, "w+")   #w+ to create and write file
fsingle= open(amergerfile, "w+")
f2chain = open(chainerfile, "w+")

floop.write("#!/bin/bash")
floop.write('\n')
fsingle.write("#!/bin/bash")
fsingle.write('\n')

def substr(a, b):                              
	return "".join(a.rsplit(b))
def merge(inf, outf, mergeFile, chainFile):
	bashcmd = "hadd -f %s `%s`" %(outf, inf)  
	mergeFile.write(bashcmd)	
	mergeFile.write('\n')
	outfile = substr(outf, rootpreeos)
	chainFile.write("root://cmsxrootd.fnal.gov/%s" %(outfile))
	chainFile.write('\n')
	return;

def mergeone(inf,outf, mergeFile, chainFile):
	bashcmd = "hadd -f %s `%s`" %(outf, inf)  
	print (bashcmd)
	print (" ")
	mergeFile.write(bashcmd)	
	mergeFile.write('\n')
	outfile = substr(outf, rootpreeos)
	print ("root://cmsxrootd.fnal.gov/%s" %(outfile))
	return;


#if mergeloop:	
# Name stitching
for i in range(len(runormassbin)):
	if data:
		FSTATEBIN = fstate + runormassbin[i]
		inputf = INPUTDIR + crab + FSTATEBIN  + INPUTSUB[i]
	else:
		if signal:
			FSTATEBIN = fstate +runormassbin[i] + energy + gen
		else:
			FSTATEBIN = fstate + runormassbin[i] + ptcut + energy + gen
		inputf = INPUTDIR + FSTATEBIN + crab + FSTATEBIN + INPUTV + INPUTSUB[i]
	inf_ = rootxrd + inputf + greproot
	outf_ = rootpreeos + outputdir + FSTATEBIN + 'out' + rootext  
	#print "Merging files: %s" %(inf_)
	#print " "
	print ("Output at %s" %(outf_))
	#print " "
	merge(inf_, outf_,floop, f2chain)

	
#else:
#inputf2 = INPATH
#inf_2 = rootxrd + inputf2 + greproot
#outf_2 = rootpreeos + outputdir + fstate + runormassbin[4]+ ptcut + energy + gen + rootext
#print ("outf_2", outf_2)
#mergeone(inf_2,outf_2, fsingle, f2chain)

floop.close()
fsingle.close()

if mergeloop:
	print ("Created %s to merge files to %s" %(mergerfile, outputdir))
else:
	print ("Created %s to merge files to %s" %(amergerfile, outputdir))

print ("Created %s to chain files with common tree" %(chainerfile))
print (">> Merging the files....")

if mergeloop:
	bashcom = "chmod u+rx %s" %(mergerfile)
	process = subprocess.Popen(bashcom.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	# runmerger = "bash rootmerger.sh"
	# get current working directory
	cwd = os.getcwd()

######################MERGING##########################
#bottleneck--> bash <mergerfile>.sh
	subprocess.call("%s/%s" %(cwd, mergerfile), shell = True)
#######################################################
else:
	bashcom = "chmod u+rx %s" %(amergerfile)
	process = subprocess.Popen(bashcom.split(), stdout=subprocess.PIPE)
	output, error = process.communicate()

	# runmerger = "bash rootmerger.sh"
	# get current working directory
	cwd = os.getcwd()
	
######################MERGING##########################
	subprocess.call("%s/%s" %(cwd, amergerfile), shell = True)
#######################################################

print ("Merging process finished. To check, type \n \n root -l root://cmsxrootd.fnal.gov/%s*.root " %(outputdir))
print (" ")

sw.Stop()
print ("Processing Time:")
print ("Real time: " + str(sw.RealTime() / 60.0) + " minutes")
print ("CPU time: " + str(sw.CpuTime() /60.0) + " minutes")