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
INPUTDIR = '/store/user/ciperez/DiPhotonAnalysis/ADDGravToGG/SherpaTest'

################# OUTPUT 
#outputdir = '/store/user/cuperez/ADDGravToGG/ADDGravToGG_MS-10000_NED-4_KK-1_M-500-11000/'
outputdir = '/store/user/cuperez/DiPhotonAnalysis/ADDGravToGG/SherpaTestMerged'

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


#Put Files Path here (from eoshelper) 
paths = ['/store/user/cuperez/DiPhotonAnalysis/ADDGravToGG/SherpaTest/ADDGravToGG_MS-4000_NED-4_KK-1_M-1000To2000_13TeV-sherpa/crab_ADDGravToGG_MS-4000_NED-4_KK-1_M-1000To2000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180618_033354/0000',
"/store/user/cuperez/DiPhotonAnalysis/ADDGravToGG/SherpaTest/ADDGravToGG_MS-4000_NED-4_KK-1_M-2000To4000_13TeV-sherpa/crab_ADDGravToGG_MS-4000_NED-4_KK-1_M-2000To4000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180618_033407/0000",
"/store/user/cuperez/DiPhotonAnalysis/ADDGravToGG/SherpaTest/ADDGravToGG_MS-4000_NED-4_KK-1_M-200To500_13TeV-sherpa/crab_ADDGravToGG_MS-4000_NED-4_KK-1_M-200To500_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180618_033420/0000",
"/store/user/cuperez/DiPhotonAnalysis/ADDGravToGG/SherpaTest/ADDGravToGG_MS-4000_NED-4_KK-1_M-500To1000_13TeV-sherpa/crab_ADDGravToGG_MS-4000_NED-4_KK-1_M-500To1000_13TeV-sherpa__80XMiniAODv2__MINIAODSIM/180618_033432/0000"]

for e in paths:
	#pattern = r'Ms-([^(]*)\_M'	
	pattern = r'SherpaTest/([^(]*)\/crab'
        match = re.findall(pattern, e) # will serve as root FileName 
	print match
	inf_  = rootxrd + e + greproot
	outf_ = rootpreeos + outputdir + match[0] + 'out' + rootext
	print "Output at %s" %(outf_)
	merge(inf_, outf_, floop, f2chain)

#if mergeloop:	
# Name stitching
 #for i in range(len(runormassbin)):
 #	if data:
 #		FSTATEBIN = fstate + runormassbin[i]
 #		inputf = INPUTDIR + crab + FSTATEBIN  + INPUTSUB[i]
 #	else:
 #		if signal:
 #			FSTATEBIN = fstate +runormassbin[i] + energy + gen
 #		else:
 #			FSTATEBIN = fstate + runormassbin[i] + ptcut + energy + gen
 #		inputf = INPUTDIR + FSTATEBIN + crab + FSTATEBIN + INPUTV + INPUTSUB[i]
 #	inf_ = rootxrd + inputf + greproot
 #	outf_ = rootpreeos + outputdir + FSTATEBIN + 'out' + rootext  
 #	#print "Merging files: %s" %(inf_)
 #	#print " "
 #	print ("Output at %s" %(outf_))
 #	#print " "
 #	merge(inf_, outf_,floop, f2chain)

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
