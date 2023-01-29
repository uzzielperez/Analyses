import sys
import os 
import subprocess as sp 
import math

du = [1.1, 1.5, 1.9]


LambdaU = [0.4, 1, 4, 15000, 100000]

       
print "Writiting generator fragments... "
idu = 0 
while idu < len(du):
	for ilambdau in LambdaU:
		#print "du: ", du[idu], "; LambdaU: ", ilambdau
		command = 'python runCardGenUnparticles.py -d %f -l %f' %(du[idu], ilambdau)		
		#print command
		#os.system(command) 
		#process = sp.Popen(command.split(), stdout=sp.PIPE)
		#output, error = process.communicate()

		du_label        = str(du[idu])
		du_label        = du_label.replace('.', 'p')
		
		ilambdau_label  = str(ilambdau)
		ilambdau_label 	= ilambdau_label.replace('.', 'p')

		#RunCard_outName = 'Unparticles_du%d_LambdaU-%d_TuneCUEP8M1_13TeV_pythia8.py' %(du, LambdaU)
		dataset = 'Unparticles_du%s_LambdaU-%s_TuneCUEP8M1_13TeV_pythia8' %(du_label, ilambdau_label)	
		genfrag = 'Unparticles_du%s_LambdaU-%s_TuneCUEP8M1_13TeV_pythia8_cfi.py' %(du_label, ilambdau_label)	
		
		print genfrag 
		f = open("datasetUnparticles.txt", "a")
		f.write('%s\n'%(dataset))
                fi = open("generatorFragmentListUnparticles.txt", "a")
                fi.write('%s\n'%(genfrag))                                                    
	idu = idu+1


