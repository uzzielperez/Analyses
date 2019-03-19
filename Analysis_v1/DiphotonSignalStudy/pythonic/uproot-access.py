import uproot 

tfile = uproot.open('sm.root')
ttree = tfile.get('demo/fgenTree')
branches = ttree.keys()

GenDiPhoton_Minv = ttree['GenDiPhoton'].array()["Minv"]

