from visual import *
import numpy as np

scene = display(width = 550, height = 580)
scene.range = 8

wallRight = box(pos = (4,0,0), size = (0.1, 8, 8), color = color.cyan)
wallLeft = box(pos = (-4,0,0), size = (0.1, 8, 8), color = color.red)
wallUp = box(pos = (0,4,0), size = (8, 0.1, 8), color = color.magenta)
wallDown = box(pos = (0,-4,0), size = (8, 0.1, 8), color = color.blue)
wallForward = box(pos = (0,0,4), size = (8, 8, 0.1), color = color.green, opacity = 0.0)
wallBackward = box(pos = (0,0,-4), size = (8, 8, 0.1), color = color.orange)

step = 0.01
time = 0

spheres = []
position = []
for i in range(20):
	x = np.random.uniform(-0.5, 0.5)
	y = np.random.uniform(-0.5, 0.5)
	z = np.random.uniform(-0.5, 0.5)
	spheres.append(sphere(pos = (0,0,0), radius = 0.3, color = color.white))
	spheres[i].vel = vector(x,y,z)



while time < 10000:
	rate(1000)
	for ball in spheres:
		ball.pos +=ball.vel * step
		if abs(ball.pos.x) + ball.radius >= wallRight.pos.x - wallRight.size.x:
			if ball.pos.x > 0:
				temp = wallRight.color
				wallRight.color = ball.color
				ball.color = temp
			else:
				temp = wallLeft.color
				wallLeft.color = ball.color
				ball.color = temp
			ball.vel.x = -ball.vel.x	
		if abs(ball.pos.y) + ball.radius >= wallUp.pos.y - wallUp.size.y:
			if ball.pos.y > 0:
				temp = wallUp.color
				wallUp.color = ball.color
				ball.color = temp
			else:
				temp = wallDown.color
				wallDown.color = ball.color
				ball.color = temp
			ball.vel.y = -ball.vel.y	
		if abs(ball.pos.z) + ball.radius >= wallForward.pos.z - wallForward.size.z:
			if ball.pos.z > 0:
				temp = wallForward.color
				wallForward.color = ball.color
				ball.color = temp
			else:
				temp = wallBackward.color
				wallBackward.color = ball.color
				ball.color = temp
			ball.vel.z = -ball.vel.z				
		time += step		