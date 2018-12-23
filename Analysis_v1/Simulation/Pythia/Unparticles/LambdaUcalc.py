def L(du, y):
	return (1/y)**(1/(du-1))

def xsec(du, LU):
	return (1/LU)**(2*(du-1))

print "L(1.9, 1)", L(1.9, 1)
print "xsec(1.9, 4500.0)", xsec(1.9, 4500.0)
print "xsec(1.9, 2500)", xsec(1.9, 2500.0)

print xsec(1.9, 4500.0)/xsec(1.9, 2500.0)
print xsec(1.9, 2500.0)/xsec(1.9, 4500.0)
