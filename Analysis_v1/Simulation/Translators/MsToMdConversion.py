import math
from math import gamma
import numpy as np

GRW_Mslst = np.array([4, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 11, 13])
HLZ_Mslst = np.array([4, 5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 13])
Hewett_Mslst = np.array([4, 5, 6, 6.5, 7, 7.5, 8, 9, 10, 11, 13])


GRW_NED = 4
HLZ_NED = 2
Hewett_NED = 2 #Doesn't really matter. Independent

def Gamma_function_part(NED):
	return gamma(NED/2) 

def M_d(NED, M_s): 
	factor1 = 1/(2*math.sqrt(math.pi)) 
        factor2 = math.pow(Gamma_function_part(NED),-1/(NED + 2))
	return factor1*factor2*M_s 

#Check should both be 1.0  
print "gamma(4)= ", Gamma_function_part(GRW_NED)
print "gamma(2)= ", Gamma_function_part(HLZ_NED)

# GRW M_d
print "GRW: ", M_d(GRW_NED, GRW_Mslst) 
# HLZ M_d 
print "HLZ: ", M_d(HLZ_NED, HLZ_Mslst)
# Hewett M_d
print "Hewett_NED: ", M_d(Hewett_NED, Hewett_Mslst)




	 
