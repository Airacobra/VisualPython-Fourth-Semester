from visual import *

scene = display(width = 1000, height = 500)

leftWall = box(pos = (-40,0,0), size = (1, 2, 2), color = color.white)
rightWall = box(pos = (40,0,0), size = (1, 2, 2), color = color.white)

sphere1 = sphere(pos=(-24,0,0), radius = 1, color = color.white, vel=vector(5,0,18))
sphere2 = sphere(pos=(-8,0,0), radius = 1, color = color.white, vel=vector(0,16,0))
sphere3 = sphere(pos=(8,0,0), radius = 1, color = color.white, vel=vector(20,1,22))
sphere4 = sphere(pos=(24,0,0), radius = 1, color = color.white, vel=vector(0,4,33))

helix1 = helix(pos = leftWall.pos, axis = sphere1.pos - leftWall.pos, radius = 1, coils = 20, thickness = 0.03, color = color.cyan) 
helix2 = helix(pos = sphere1.pos, axis = sphere2.pos - sphere1.pos, radius = 1, coils = 20, thickness = 0.03, color = color.cyan) 
helix3 = helix(pos = sphere2.pos, axis = sphere3.pos - sphere2.pos, radius = 1, coils = 20, thickness = 0.03, color = color.cyan) 
helix4 = helix(pos = sphere3.pos, axis = sphere4.pos - sphere3.pos, radius = 1, coils = 20, thickness = 0.03, color = color.cyan) 
helix5 = helix(pos = sphere4.pos, axis = rightWall.pos - sphere4.pos, radius = 1, coils = 20, thickness = 0.03, color = color.cyan) 

m = 1
k = 1
dt = 0.001

while True:
	rate(1000)
	F1 = k * (leftWall.pos - 2 * sphere1.pos + sphere2.pos)
	F2 = k * (sphere1.pos - 2 * sphere2.pos + sphere3.pos)
	F3 = k * (sphere2.pos - 2 * sphere3.pos + sphere4.pos)
	F4 = k * (sphere3.pos - 2 * sphere4.pos + rightWall.pos)

	a1 = F1 / m
	a2 = F2 / m
	a3 = F3 / m
	a4 = F4 / m

	sphere1.vel = sphere1.vel + a1 * dt
	sphere2.vel = sphere2.vel + a2 * dt
	sphere3.vel = sphere3.vel + a3 * dt
	sphere4.vel = sphere4.vel + a4 * dt

	sphere1.pos = sphere1.pos + sphere1.vel * dt
	sphere2.pos = sphere2.pos + sphere2.vel * dt
	sphere3.pos = sphere3.pos + sphere3.vel * dt
	sphere4.pos = sphere4.pos + sphere4.vel * dt

	helix1.pos = leftWall.pos
	helix2.pos = sphere1.pos
	helix3.pos = sphere2.pos
	helix4.pos = sphere3.pos
	helix5.pos = sphere4.pos

	helix1.axis = sphere1.pos - leftWall.pos
	helix2.axis = sphere2.pos - sphere1.pos
	helix3.axis = sphere3.pos - sphere2.pos
	helix4.axis = sphere4.pos - sphere3.pos
	helix5.axis = rightWall.pos - sphere4.pos

