inputfile = 'cleandis.txt'
#inputfile = 'outfile.txt'
#inputfile = 'datasetlist.txt'

f = open(inputfile)
lines = f.read().split('\n')

outfile = 'processdis.txt'
out = open(outfile, "w+")

for line in lines:
	if 'json_Run2018Dv2_324209-324420' in line:
	#if 'json_Run2018Dv2_324420' in line:
	#if 'crab_EGamma__Run2018D-PromptReco-v2__MINIAOD_json_323775-324209' in line:
	#if 'json_Run2018Dv2_324209' in line:
	#if 'json_toRun2018Dv2_323775' in line:
	#if 'json_toRun2018Dv2_323775' in line and 'skimmed' in line:
		print line 
		out.write(line+"\n")	

