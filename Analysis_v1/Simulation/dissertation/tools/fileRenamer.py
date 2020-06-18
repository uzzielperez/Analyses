import os

# -----
strname  = "AAA_2j_15_15_15_13TeV"
dsetname = "GGGJets_Pt-15toInf_13TeV_15-15-15sym_sherpa"
path = "."
# ------
for fname in os.listdir(path):
	if strname in fname:
		print fname
		os.rename(os.path.join(path, fname), os.path.join(path, fname.replace(strname, dsetname)))
