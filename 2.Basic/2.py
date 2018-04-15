#!/usr/bin/env python3 
from random import random
import math

def func2(x):
	No = 0
	Nk = 0
	for i in range(x):
		x = random()
		y = random()
		result = math.sqrt(x**2+y**2)
		if result > 1:
			Nk = Nk + 1
		else: 	
			Nk = Nk + 1
			No = No + 1
		piNumber = 4 * No / Nk
	return piNumber

fp = open('dane.dat', 'w')
for i in range(1,101):
	result = func2(i)
	fp.write(str(i) + ' ' +  str(result) + ' ' + str(result/i) + '\n')

for i in range(3,8):
	result = func2(i)
	fp.write(str(10**i) + ' '+ str(result)+ ' ' + str(result/i) + '\n')

fp.close()
