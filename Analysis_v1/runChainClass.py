import ROOT 
import time
import subprocess
import os

inputfile = 'ainput.txt'
f = open(inputfile)
lines = f.read().split('\n') #list containing each line
lines = lines[:-1] #to exclude last slot in lines which is white space
print len(lines)
cwd = os.getcwd()

# Timer
sw = ROOT.TStopwatch()
sw.Start()


#------------------------------------------

#chain.Print()
study = "GGJets"
classname = "Class%s" %(study)

#------------------------------------------

#create empty rootfile for plots
#rootfile = "%s.root" %(study)
#outFile = ROOT.TFile(rootfile, "RECREATE")
#outDir = outFile.mkdir("%sStudy" %(study))
#outDir.cd()

newfolder = '%sStudy' %(study)
os.mkdir(newfolder)
os.chdir(newfolder)

print "Moving to %sStudy/" %(study)

#-----------------------------------------

tree = "diphoton/fTree"
#tree = "diphoton/fGenTrees" 

#-----------------------------------------

# Adding files to TChain
chain = ROOT.TChain(tree)
print "Adding files to %s" %(tree)
for e in lines:
	print e
	chain.Add(e) 
print " >> Input evts:",chain.GetEntries()
chain.MakeClass(classname)
f.close()

#------------------------------------------
AN_template = "%s/aAN_template.C" %(cwd)
AN_file = "analyze%s.C" %(classname)
AN = open(AN_file, "w+")
AN.write('#include "%s.C" \n' %(classname))

# Write out code  
with open(AN_template, 'r') as f2:
	code = f2.read().replace('ClassNameHere', classname)
	AN.write(code)

print "Created %s to run over files" %(AN_file)
print code
AN.close()

#------------------------------------------

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"
