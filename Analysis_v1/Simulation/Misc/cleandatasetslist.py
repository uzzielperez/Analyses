import subprocess
import os

origlist = "datasetlist.txt"
cleanlist = open("cleanedlist.txt", "w+")

# Write out code  
with open(origlist, 'r') as f:
	datasetlist = f.readlines()
	#AN.write(code)

#print datasetlist
for dataset in datasetlist:
	if "RunIISummer16MiniAODv2" in dataset:
		cleanlist.write(dataset) 

cleanlist.close()
