liczba = input("Podaj liczbe: ")
liczba = int(liczba)
if liczba % 2 == 0:
	print("Podana liczba jest parzysta")
else: 
	print("Podana liczba jest nieparzysta")
L = []
czy_pierwsza = 0

for i in range(2,liczba):
	if liczba % i == 0:
		L.append(i)
		czy_pierwsza = 1
if liczba != 0:
	L.append(1)
if liczba > 1:	
	L.append(liczba)
L.sort()
		
if czy_pierwsza == 1:
	print("zadana liczba nie jest pierwsza") 
else:
	print("zadana liczba jest pierwsza")		
print("Dzielniki:")
print(L)	