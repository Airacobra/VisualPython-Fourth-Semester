import matplotlib.pyplot as plt
from random import randint

xlist = []
ylist = []

x0 = 0
y0 = 0

xlist.append(x0)
ylist.append(y0)

while(len(xlist) <= 10**6 + 1):
	number = randint(1,100)
	if number <= 85:
		x = 0.85 * x0 + 0.04 * y0
		y = -0.04 * x + 0.85 * y0 + 1.6
	if (number > 85 and number <= 92):
		x = 0.2 * x0 - 0.26 * y0
		y = 0.23 * x0 + 0.22 * y0 + 1.6
	if (number > 92 and number <= 99):
		x = -0.15 * x0 + 0.28 * y0
		y = 0.26 * x0 + 0.24 * y0 + 0.44
	if number == 100:
		x = 0 * x0
		y = 0.16 * y0

	x0 = x
	y0 = y	

	if( 0.5<x<1.5 and 1<y<2):
		xlist.append(x0)
		ylist.append(y0)

xshape = [0,5, 1.5, 1.5, 0.5, 0.5]
yshape = [1, 1, 2, 2, 1]

plt.axis([0.5, 1.5, 1, 2])
plt.plot(xlist, ylist, ',', color = 'g' )	
plt.show()