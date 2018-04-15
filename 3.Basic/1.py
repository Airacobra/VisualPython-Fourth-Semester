from time import sleep
from random import choice

n = 10
i = 0
L = [-1,0,1]

print(' '*25  + '|' + ' '*(n-2) + 'START'+ ' '*(n-3) + '|'+ str(i))

while(i > (-n) and i < n-1):
	sleep(0.1)
	if(choice(L) == 1):
		i+=1
	elif(choice(L) == -1):
		i-=1

	if(i>0):
		print(' '*25  + '|' + ' '*(n+i) + '*' + ' '*(n-i-1) + '|' + str(i) )	
	else:
		print(' '*25  + '|' + ' '*(n-abs(i)) + '*' + ' '*(n+abs(i)-1) + '|' + str(i) )		