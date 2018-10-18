inputfile = 'datasetlist.txt'
f = open(inputfile)
lines = f.read().split('\n')

outfile = 'cleaneddatasetlist.txt'
out = open(outfile, "w+")

for line in lines:
	if 'json_toRun2018Dv2_323775' in line:
		print line 
		out.write(line)	

