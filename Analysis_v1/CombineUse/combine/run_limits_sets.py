import os 

for item in os.listdir('.'):
	if "unpar_spin" in item: 
		print "Entering %s directory." %(item) 
		os.chdir(item)
		cmd = 'python run_combine_plotter.py'
		os.system(cmd)
		os.chdir("..")
