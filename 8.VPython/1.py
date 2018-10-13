from visual import *

M = 2 * 10**30
G = 6.7 * 10 **(-11)
dt = 3600

scene = display(width = 550, height = 580)
sun = sphere(pos=(0,0,0),radius = 3*10**10,color=color.yellow)
p1 = sphere(pos=(70*10**9,0,0), radius=6*10**9, color=color.magenta, vel=vector(0,47*10**3,0))
p2 = sphere(pos=(110*10**9,0,0), radius=9*10**9, color=color.orange, vel=vector(0,35*10**3,0))
p3 = sphere(pos=(150*10**9,0,0), radius=7*10**9, color=color.blue, vel=vector(0,30*10**3,0))
p4 = sphere(pos=(250*10**9,0,0), radius=8*10**9, color=color.red, vel=vector(0,24*10**3,0))

pAll = [p1,p2,p3,p4]
trails = [curve(pos=(70*10**9,0,0), color=color.magenta),
		  curve(pos=(110*10**9,0,0), color=color.orange),
		  curve(pos=(150*10**9,0,0), color=color.blue),
		  curve(pos=(250*10**9,0,0), color=color.red)]

while True:
	rate(800)
	for current, p in enumerate(pAll):
		a = - G * M * p.pos/(mag(p.pos)**3)
		p.vel += a * dt
		p.pos += p.vel * dt
		trails[current].append(p.pos)

