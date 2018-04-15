import math
fp = open('sinus.txt','w')
half = 50

Phi  = [x * 2* math.pi / 100 for x in range (0,101)]
Y = [int(70 * math.cos(i) * math.e**(-i/math.pi) ) for i in Phi]

for k in Y:
	if(k==0):
		fp.write(' ' * half + '0' + '\n')
	elif(k > 0):
		fp.write(' ' * half)
		for j in range(k):
			fp.write('+')
		fp.write('\n')	
	else:
		fp.write(' ' * (half - abs(k)))
		for j in range(abs(k)):
			fp.write('-')
		fp.write('\n')		

fp.close()		