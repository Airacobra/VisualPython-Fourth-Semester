import matplotlib.pyplot as plt
import numpy as np

average = 0
List10 = [x for x in range(10)]
Nmax = [10, 100, 400, 1000, 2500]
dList = []

for n in range(len(Nmax)):
	for _ in range(10 ** 4):
		d = 0
		for maxn in Nmax:
			for i in range(0, maxn):
				step = np.random.random_integers(0,1)
				if step:
					d += 1
				else:
					d -= 1

			d = d**2
			average += d
		
	average = average / (10 ** 4)
	dList[n] = np.sqrt(average)


plt.plot(Nmax, dList, 's')
plt.show()	

