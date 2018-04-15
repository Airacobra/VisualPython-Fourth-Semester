import math

def func(x):
	piNumber = 4
	for i in range(1,x):
		if i % 2 == 0:
			piNumber += 4/((2 * i) + 1)
		else:
			piNumber -= 4/((2 * i) + 1)	
	return piNumber			




for j in range(1,101):
	number = func(j)
	print(j,  number,  number/(math.pi), "\n")

for j in range(3,8):
	number = func(10**j)	
	print(j,  number, number/(math.pi),  "\n")




