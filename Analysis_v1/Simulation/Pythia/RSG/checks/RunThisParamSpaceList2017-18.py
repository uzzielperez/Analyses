import sys
import os 
import subprocess as sp 
import math


#k = [0.01, 0.1, 0.2]
k = 0.2
#M = [[750,1000,1250,1500,1750,2000, 2250, 2500, 2750, 3000, 3250,3500,4000,5000],
#     [750,1000,1250,1500,1750,2000,2250, 2500,3000,3500,4000,4250,4500,4750,5000,5250,5500,5750,6000, 6500, 7000, 8000],   
#     [750,1000,1250,1500,1750,2000,2250,2500,3000,3500,4000,4500,4750,5000,5250,5500,5750,6000, 6500, 7000, 8000]]

M = [750,1000,1250,1500,1750,2000,2250,2500,3000,3500,4000,4500,4750,5000,5250,5500,5750,6000, 6500, 7000, 8000]

print "Writiting generator fragments... "
for m in M:
	command = 'python runCardGenRSG.py -k %f -m %d' %(k, m)		
	os.system(command)

	coupling        = str(k)
	coupling        = coupling.replace('.', '')
	genfrag = 'RSG_kMpl%s_M_%s.py' %(coupling, m)	
		
	print genfrag 


