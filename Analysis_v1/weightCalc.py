import ROOT
import argparse

# Command Line Options 
parser = argparse.ArgumentParser(description='Calculates weight, number of events of given root files.')
parser.add_argument('-i', '--input', help='Input file/s.', required=True, type=str)
#parser.add_argument('-i', '--input', nargs= '+', help='Input file/s.', required=True, type=str)
args = parser.parse_args()
  
#-----------------------------------------
# Reading input

inputfile = args.input
#inputfile = 'aInputMerged.txt'
#inputfile = 'ainput.txt'

f = open(inputfile)
lines = f.read().split('\n') #list containing each line
lines = lines[:-1] #to exclude last slot in lines which is white space
print len(lines)
#cwd = os.getcwd()

#-----------------------------------------

def weightCalc(xsec, Lumi, N_0): 
	return xsec*Lumi/N_0

#------------------------------------------

# Timer
sw = ROOT.TStopwatch()
sw.Start()

#------------------------------------------

tree = "diphoton/fTree"
#tree = "diphoton/fGenTrees" 

#-----------------------------------------
# Luminosity

#L = 1 #fb^(-1)
#L =  0.0007209 #Event_weightLumi 
L = 1000

# Normalization Lumi

normL = 1000

#-----------------------------------------

def xsecF(sample):
	if(sample.find("GGJets_M-60To200_Pt-50_13TeV-sherpa")  != -1): 
		xsec = 5.785e+00;
	elif(sample.find("GGJets_M-200To500_Pt-50_13TeV-sherpa") != -1): 
		xsec = 2.244e+00;
	elif(sample.find("GGJets_M-500To1000_Pt-50_13TeV-sherpa")!= -1): 
		xsec = 1.510e-01;
	elif(sample.find("GGJets_M-1000To2000_Pt-50_13TeV-sherpa")!= -1): 
		xsec = 1.084e-02;
	elif(sample.find("GGJets_M-2000To4000_Pt-50_13TeV-sherpa")!= -1): 
		xsec = 3.690e-04;
	elif(sample.find("GGJets_M-4000To6000_Pt-50_13TeV-sherpa")!= -1): 
		xsec = 2.451e-06;
	elif(sample.find("GGJets_M-6000To8000_Pt-50_13TeV-sherpa")!= -1): 
		xsec = 1.753e-08;
	elif(sample.find("GGJets_M-8000To13000_Pt-50_13TeV-sherpa")!= -1):
		xsec = 7.053e-11;
	return xsec

#-----------------------------------------

def averageWeight(sample):
       if(sample.find("GGJets_M-60To200_Pt-50_13TeV-sherpa")):
		 average = 3.895719e-01
       if(sample.find("GGJets_M-200To500_Pt-50_13TeV-sherpa")):
		 average = 2.818643e-01
       if(sample.find("GGJets_M-500To1000_Pt-50_13TeV-sherpa")):
		 average = 2.094533e-01
       if(sample.find("GGJets_M-1000To2000_Pt-50_13TeV-sherpa")):
		 average = 1.749053e-01
       if(sample.find("GGJets_M-2000To4000_Pt-50_13TeV-sherpa")):
		 average = 1.638999e-01
       if(sample.find("GGJets_M-4000To6000_Pt-50_13TeV-sherpa")):
		 average = 1.673106e-01
       if(sample.find("GGJets_M-6000To8000_Pt-50_13TeV-sherpa")):
		 average = 1.816810e-01
       if(sample.find("GGJets_M-8000To13000_Pt-50_13TeV-sherpa")):
		 average = 1.972643e-01

       return average
#----------------------------------------

def weightLumiCalc(sample,normLumi,nEventsSample):
	return xsecF(sample)*normLumi/(nEventsSample*averageWeight(sample))

#------------------------------------------


# loop over all input 
# print out xsec  

#print "Checking files..."
#for b in lines: 
#	print b
fullchain = ROOT.TChain(tree)

for e in lines:
	 chain = ROOT.TChain(tree)
	 chain.Add(e,0) #second argument to add num_entries 
	 fullchain.Add(e,0)	
         print e 
	 W = chain.GetWeight()
	 N = chain.GetEntries()
	 #sigma = xsecF(e) 
	 #calcW = weightCalc(sigma, L, N)  
	 #LW = weightLumiCalc(e, normL, N)
	 print "Entries: ", N 
       	 #print "xsec: ", sigma, ", Lumi: ", L, ", Entries: ", N, "CalcWeight: ", calcW, "Weight: ", W, "Lumiweight: ", LW, "\n"       	 

Nt = fullchain.GetEntries()
print "Weight: ", fullchain.GetWeight()
print "Total Entries: ", Nt


f.close()

sw.Stop()
print "Real time: " + str(sw.RealTime() / 60.0) + " minutes"
print "CPU time:  " + str(sw.CpuTime() / 60.0) + " minutes"

