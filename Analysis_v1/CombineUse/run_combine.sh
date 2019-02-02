#combine -m 10 -M AsymptoticLimits distrack_10_datacard_input.txt > ctau10_limit.txt
#combine -m 30 -M AsymptoticLimits distrack_30_datacard_input.txt > ctau30_limit.txt
#combine -m 50 -M AsymptoticLimits distrack_50_datacard_input.txt > ctau50_limit.txt
#combine -m 100 -M AsymptoticLimits distrack_100_datacard_input.txt > ctau100_limit.txt
#combine -m 1000 -M AsymptoticLimits distrack_1000_datacard_input.txt > ctau1000_limit.txt
combine -m 3000 -M AsymptoticLimits unpar_du1p9_LU2000.txt > Limit_Unpar_du1p9_LU2000.txt
combine -m 2500 -M AsymptoticLimits unpar_du1p9_LU2500.txt > Limit_Unpar_du1p9_LU2500.txt
combine -m 2000 -M AsymptoticLimits unpar_du1p9_LU3000.txt > Limit_Unpar_du1p9_LU3000.txt
