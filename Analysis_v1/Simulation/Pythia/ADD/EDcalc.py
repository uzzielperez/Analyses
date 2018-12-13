M_D = 1e+12
M_4 = 2.4e+27

ned = [1.0, 2.0, 3.0, 4.0]

for d in ned:
	V = (M_4**2)/(M_D**(2+d))
	L = V**(1/d) 
	Linv = 1/L #ev
        LinvCm = (1/L)*8065.5
	Lcm = L*(8065.5)	
	print "ned: ", d, "; V: ", V, "; L (ev): ", L, ";1/L (ev): ", Linv, "; L(cm): ", Lcm 
 
