def L(du, y):
	return (1/y)**(1/(du-1))

def xsec(du, LU):
	return (1/LU)**(2*(du-1))

print "L(1.9, 1)", L(1.9, 1)
print "xsec(1.9, 4500.0)", xsec(1.9, 4500.0)
print "xsec(1.9, 2500)", xsec(1.9, 2500.0)

print xsec(1.9, 4500.0)/xsec(1.9, 2500.0)
print xsec(1.9, 2500.0)/xsec(1.9, 4500.0)


print "L(1.9, 1)", L(1.9, 1)
print "L(1.8, 0.7)", L(1.8, 0.7)
print "L(1.7, 0.5)", L(1.7, 0.5)
print "L(1.6, 0.4)", L(1.6, 0.4)
print "L(1.5, 0.3)", L(1.5, 0.3)
print "L(1.4, 0.2)", L(1.4, 0.2)


