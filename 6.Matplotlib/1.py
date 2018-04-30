import matplotlib.pyplot as plt
import numpy as np

colours = ['LawnGreen', 'BlueViolet', 'Cornsilk', 'DarkKhaki', 'FireBrick' ]

for j in range(5):
	x = 0
	y = 0
	xList = []
	yList = []
	xList.append(x)
	yList.append(y)
	for i in range(10**4):
		angle = np.random.uniform(0, 2 * np.pi)
		x += np.cos(angle)
		y += np.sin(angle)
		xList.append(x)
		yList.append(y)
		if i == (10**4 - 1):
			plt.plot(x, y, 'o', color = colours[j], lw = 2, zorder = 2)	

	plt.plot(xList, yList, '-', color = colours[j], lw = 0.3, zorder = 1)

plt.show()