#a = np.array([1,1,1])
#while a[2] < 100:
#	if a[0]**2 + a[1]**2 == a[2]**2:
#		print(a)

for a in range (1,100):
	for b in range (1,100):
		for c in range (1,100):
			if a**2 + b**2 == c**2:
				print(a,b,c)

print('\n')

for a in range (1,100):
	for b in range (1,100):
		for c in range (1,100):
			if a**3 + b**3 == c**3:
				print(a,b,c)

print('\n')				

for a in range (1,100):
	for b in range (1,100):
		for c in range (1,100):
			if a**4 + b**4 == c**4:
				print(a,b,c)				