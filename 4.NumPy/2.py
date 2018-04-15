import numpy as np

f = open('wynik.dat','w')

for people in range(1,366):
	howMany = 0
	for _ in range(1000):
		VectorX = np.random.random_integers(1, 365, people)
		VectorY = VectorX[:, np.newaxis]

		TrueFalseMatrix = VectorX == VectorY
		ifTrueButNotOnDiagonal = (TrueFalseMatrix != np.identity(people))

		if True in ifTrueButNotOnDiagonal:
			howMany += 1

	f.write(str(people) + ':  ' + str(howMany/1000) + '\n')
	print(people,':  ',howMany/1000)		

