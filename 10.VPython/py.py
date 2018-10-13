from visual import *

p = -100
m = 1
M = 10
n = 20
step = 0.01
spheres = []

scene = display(width = 550, height = 580)
scene.range = 250
circle = ring(pos = (0,0,0), radius = 200, axis = (0,0,1), thickness = 0.5, color = color.cyan)

ball = sphere(pos=(50,-50,0), radius = 30, color = color.white, vel=vector(random.randint(-5,5),random.randint(-5,5),0))
for i in range(n):
	spheres.append(sphere(pos=(p,p,0),radius = 5, color = color.red, vel=vector(random.randint(-10,10),random.randint(-10,10),0)))
	p += 11


while True:
	rate(10000000)
	
	for sphere in spheres:
		sphere.pos += sphere.vel * step
		if mag(sphere.pos) > circle.radius - sphere.radius:	#(abs(ball.pos.x) > 100 - ball.radius) or (abs(ball.pos.y) > 100 - ball.radius):
			Vr = sphere.pos / mag(sphere.pos) * dot(sphere.pos / mag(sphere.pos), sphere.vel)
			sphere.vel = sphere.vel - 2*Vr			

	ball.pos += ball.vel * step
	if mag(ball.pos) > circle.radius - ball.radius - circle.thickness:
		Vr = ball.pos / mag(ball.pos) * dot(ball.pos / mag(ball.pos), ball.vel)
		ball.vel = ball.vel - 2*Vr

	# for i in spheres:
	# 	if (mag(ball.pos) > mag(i.pos) + i.radius):
	# 		v1 = i.vel - 2 * M/(M+m) * dot(ball.vel - i.vel, ((ball.pos+ball.vel*step-i.pos+i.vel*step)/mag(ball.pos+ball.vel*step-i.pos+i.vel*step))) * (ball.pos+ball.vel*step-i.pos+i.vel*step)/mag(ball.pos+ball.vel*step-i.pos+i.vel*step)
	# 		v2 = ball.pos + 2 *m/(M+m) * dot(ball.vel - i.vel, ((ball.pos+ball.vel*step-i.pos+i.vel*step)/mag(ball.pos+ball.vel*step-i.pos+i.vel*step))) * (ball.pos+ball.vel*step-i.pos+i.vel*step)/mag(ball.pos+ball.vel*step-i.pos+i.vel*step)
	# 		ball.vel = v2
	# 		i.vel = v1


