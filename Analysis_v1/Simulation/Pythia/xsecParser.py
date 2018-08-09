import re

filename = 'outCO-2.txt'

# Cross-section Information Sample 
"""
*-------  PYTHIA Event and Cross Section Statistics  -------------------------------------------------------------*
 |                                                                                                                 |
 | Subprocess                                    Code |            Number of events       |      sigma +- delta    |
 |                                                    |       Tried   Selected   Accepted |     (estimated) (mb)   |
 |                                                    |                                   |                        |
 |-----------------------------------------------------------------------------------------------------------------|
 |                                                    |                                   |                        |
 | f fbar -> (LED G*) -> gamma gamma             5026 |        3743        775        775 |   8.458e-12  1.373e-13 |
 | g g -> (LED G*) -> gamma gamma                5027 |        2896        225        225 |   2.249e-12  7.391e-14 |
 |                                                    |                                   |                        |
 | sum                                                |        6639       1000       1000 |   1.071e-11  1.560e-13 |
 |                                                                                                                 |
 *-------  End PYTHIA Event and Cross Section Statistics ----------------------------------------------------------*
 """

pattern = (r'sum\s+(.*)')
new_file = []

# Make sure file gets closed after being iterated
with open(filename, 'r') as f:
   lines = f.readlines()

for line in lines:
	match = re.findall(pattern, line)
	if match:
		match[0].split(" ")
		matchstring = str(match[0])
		matchstring = matchstring.split(" ")
		#print match
		print matchstring
		error = matchstring[-2]
		xsec = matchstring[-4]

print xsec,"+-", error	
