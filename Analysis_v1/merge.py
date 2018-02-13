import os 
import sys
import glob
import ROOT
import re
import time
import subprocess

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
INPUTDIR = '/store/user/cuperez/DiPhotonAnalysis/Summer16GGJets/'
#INPUTDIR = '/store/user/cuperez/DiPhotonAnalysis/....'

# FinalState and Mass bin
fstate = 'GGJets_M-'
massbin = ["1000To2000", "2000To4000","200To500","4000To6000","500To1000",
	  "6000To8000","60To200","8000To13000"]  
ptcut = '_Pt-50'
energy ='_13TeV'
gen = '-sherpa'

# Version
INPUTV = '__80XMiniAODv2__MINIAODSIM'

# Subdirectories
INPUTSUB = ["/180202_203147/0000","/180202_203156/0000","/180202_203125/0000",
"/180202_203212/0000","/180202_203137/0000","/180202_203224/0000",
"/180202_203112/0000","/180202_203237/0000"]


################# OUTPUT 
# Main Output Dir
#outputdir = '/store/user/cuperez/DiPhotonAnalysis/Summer16_GGJets_Merged/'
outputdir = '/store/user/cuperez/DiPhotonAnalysis/Summer16-GGJets-Merge/'

#outputfilename = FSTATEBIN + rootext

# Timer
sw = ROOT.TStopwatch()
sw.Start()

################ MERGING
#create bash script that stitches the names together
mergerfile = 'arootmerger.sh'
chainerfile = 'ainput.txt'
fh = open(mergerfile, "w+") #w+ to create and write file
f2chain = open(chainerfile, "w+")
fh.write("#!/bin/bash")
fh.write('\n')

def substr(a, b):                              
    return "".join(a.rsplit(b))
def merge(inf, outf):
	#subprocess.call(["hadd", "-f", outf, `inf`])
	bashcmd = "hadd -f %s `%s`" %(outf, inf) 
	#process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)
	#output, error = process.communicate()
        
	#subprocess.Popen(bashcmd)	
	
	#output = subprocess.checkoutput(['bash', '-c', bashcmd])
	#print bashcmd
        #print " "
        fh.write(bashcmd) 	
	fh.write('\n')
        outfile = substr(outf_, rootpreeos)
	f2chain.write("root://cmsxrootd.fnal.gov/%s" %(outfile))
	f2chain.write('\n')
        return;


for i in range(len(massbin)):
	 FSTATEBIN = fstate + massbin[i] + ptcut + energy + gen
	 inputf = INPUTDIR + FSTATEBIN + crab + FSTATEBIN + INPUTV + INPUTSUB[i]
	 inf_ = rootxrd + inputf + greproot
	 outf_ = rootpreeos + outputdir + FSTATEBIN + rootext  
	 #print "Merging files: %s" %(inf_)
	 #print " "
	 #print "Output at %s" %(outf_)
	 #print " "
	 merge(inf_, outf_)

fh.close()
print "Created %s to merge files to %s" %(mergerfile, outputdir)
print "Created %s to chain files with common tree" %(chainerfile)
print ">> Merging the files...." 

bashcom = "chmod u+rx %s" %(mergerfile)
process = subprocess.Popen(bashcom.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

#runmerger = "bash rootmerger.sh"
#current working directory
cwd = os.getcwd()
#print "%s/rootmerger.sh" %(cwd)
#######################MERGING##########################
#bottleneck
subprocess.call("%s/rootmerger.sh" %(cwd), shell = True)
########################################################
print "Merging process finished. To check, type \n \n root -l root://cmsxrootd.fnal.gov/%s*.root " %(outputdir)
print " "
sw.Stop()
print "Processing Time:"
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time: " + str(sw.CpuTime() /60.0) + " minutes"
