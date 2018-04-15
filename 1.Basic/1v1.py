def funkcja(list):
	suma_i_iloczyn = [0,1]
	for i in list:
		suma_i_iloczyn[0] += i
		suma_i_iloczyn[1] *= i
	return suma_i_iloczyn	

L = [5,2,3]
print(funkcja(L))
		