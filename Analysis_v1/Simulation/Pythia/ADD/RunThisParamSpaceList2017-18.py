import sys
import os 
import subprocess as sp 
import math

GRW = False 
HLZ = True

if GRW:
	ned         = 4 
	negInt      = 1 
        LambdaT_lst  = [4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 10000, 11000, 13000] 
if HLZ:
	ned 	    = 2
	negInt      = 0 
	conversionfactor = pow(math.pi/2, 0.25) 
       
        Ms = [4000, 5000, 6000, 6500, 7000, 7500, 8000, 9000, 10000, 11000, 13000]
	#LambdaT_lst = [x * conversionfactor for x in Ms] #we will convert back to Ms when comparing with 2016 results  
	LambdaT_lst = [4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 9000, 10000, 11000, 13000]

pTcut = 70.0
COM   = 13

for value in LambdaT_lst:
	lambdaT = value
	rangeIndex = 0

        if lambdaT < 5500:
		minMasslist = [500.0, 1000.0, 2000.0, 3000.0]
		maxMasslist = [1000.0, 2000.0, 3000.0, lambdaT*1.0]
	else:
		minMasslist = [500.0, 1000.0, 2000.0, 4000.0]
		maxMasslist = [1000.0, 2000.0, 4000.0, lambdaT*1.0]

	while rangeIndex < len(minMasslist):
		minMass = minMasslist[rangeIndex]
		maxMass = maxMasslist[rangeIndex]
		rangeIndex = rangeIndex + 1
		
		#print "Writing generator fragment with the following parameters: "
		#print "NED: ",ned, "; LambdaT: ",lambdaT, "; MinMass: ",minMass, "; MaxMass: ",maxMass, "; pTcut: ",pTcut
	       	command       = 'python runCardGenADD.py -n %d -l %d -min %d -max %d -p %d -i %d' %(ned, lambdaT, minMass, maxMass, pTcut, negInt) 
		#process       = sp.Popen(command.split(), stdout=sp.PIPE)
                #output, error = process.communicate()
		os.system(command)
	        
		dataset = 'ADDGravToGG_NegInt-%d_LambdaT-%d_M-%dTo%d_TuneCP5_%dTeV-pythia8_cfi.py' %(negInt, int(lambdaT), minMass, maxMass, COM)
	        #dataset = 'ADDGravToGG_NegInt-%d_NED-%d_LambdaT-%d_M-%dTo%d_TuneCUEP8M1_%dTeV-pythia8' %(negInt, ned, int(lambdaT), minMass, maxMass, COM)	
	        genfragname = 'ADDGravToGG_NegInt-%d_LambdaT-%d_M-%dTo%d_TuneCP5_%dTeV-pythia8' %(negInt, int(lambdaT), minMass, maxMass, COM)
	        #genfragname = 'ADDGravToGG_NegInt-%d_NED-%d_LambdaT-%d_M-%dTo%d_TuneCUEP8M1_%dTeV-pythia8_cfi.py' %(negInt, ned, int(lambdaT), maxMass, maxMass, COM)
	        
		print 'Generated ', genfragname, '\n'
		f = open("datasetlist2017-18.txt", "a")
		f.write('%s\n'%(dataset))
		fi = open("generatorFragmentList2017-18.txt", "a")
		fi.write('%s\n'%(genfragname))
