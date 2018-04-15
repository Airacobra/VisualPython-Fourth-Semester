def fun(lista, lista2):
	ta_sama = 0;
	L = []
	for i in lista:
		for j in lista2:
			if i == j and i not in L:
					L.append(i)
	return L					


L1 = [1,5,2,4,8]
L2 = [1,5,3,7,2]

print(fun(L1,L2))