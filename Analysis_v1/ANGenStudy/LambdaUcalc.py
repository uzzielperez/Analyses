#du, y = 1.5, 0.3
#du, y = 1.1, 0.09
#du, y = 2.0, 1.4

#du, y = 1.8, 0.7 # Exclude LU<1.56 TeV
du, y = 1.1, 0.1  # Exclude LU<10000000000.0 TeV
du, y = 1.6, 0.4  # Exclude LU<4.6 TeV
du, y = 1.01, 0.05 
du, y = 1.1, 0.1  # Exclude LU<55 TeV

def L(du, y):
	return (1/y)**(1/(du-1))

def xsec(du, LU):
	return (1/LU)**(2*(du-1))

print "L(1.9, 1)", L(1.9, 1)
print "xsec(1.9, 4500.0)", xsec(1.9, 4500.0)
print "xsec(1.9, 2500)", xsec(1.9, 2500.0)

print xsec(1.9, 4500.0)/xsec(1.9, 2500.0)
print xsec(1.9, 2500.0)/xsec(1.9, 4500.0)
