from visual import *
from random import randint

n = 10
m = 1
k = 1
dt = 0.001

scene = display(width = 1000, height = 500)

leftWall = box(pos = (-40,0,0), size = (1, 2, 2), color = color.white)
rightWall = box(pos = (40,0,0), size = (1, 2, 2), color = color.white)

spheres = []
spheres.append(leftWall)
for _ in range(n):
	spheres.append(sphere(pos=(random.randint(-40,40),0,0),radius = 1, color = color.white, vel=vector(random.randint(1,40),random.randint(1,40),random.randint(1,40))))
spheres.append(rightWall)

helixes = []
for i in range(n+1):
	helixes.append(helix(pos = spheres[i].pos, axis = spheres[i+1].pos - spheres[i].pos, radius = 1, coils = 20, thickness = 0.03, color = color.cyan))

F = []
a = []
v = []

for i in range(len(helixes)-1):
	F.append(0)
	a.append(0)
	v.append(0)

while True:
	rate(1000)	

	for i in range(len(helixes)-1):
		F[i] = k * (spheres[i].pos - 2 * spheres[i+2].pos + spheres[i+1].pos)
		a[i] = F[i] / m

	for i in range(len(helixes)-2):	
		spheres[i+1].vel = spheres[i+1].vel + a[i-1] * dt 

	for i in range(len(helixes)-2):
		spheres[i+1].pos = spheres[i+1].pos + spheres[i+1].vel * dt 

	for i in range(len(helixes)+1):
		helixes[i-1].pos = spheres[i-1].pos			

	for i in range(1,len(helixes)+1):
		helixes[i-1].axis = spheres[i].pos - spheres[i-1].pos	

