from visual import *
from math import *

L = 1
g1 = 9.8
g2 = 9.8000000000001
m = 1
dt = 0.0001

phi1 = pi
theta1 = pi-0.1
df1 = 0
dt1 = 0
ddf1 = 0
ddt1 = 0

phi2 = pi
theta2 = pi-0.1
df2 = 0
dt2 = 0
ddf2 = 0
ddt2 = 0

scene = display(width = 550, height = 580)
wall = box(pos = (0,0,0), size = (0.1, 0.1, 0.1), color = color.white)
sphere1A = sphere(pos=(L*sin(pi),-L*cos(pi),0), radius = 0.1, color = color.cyan)
sphere1B = sphere(pos=(L*sin(pi)+L*sin(pi-0.1),-L*cos(pi)-L*cos(pi-0.1),0), radius = 0.1, color = color.cyan)
sphere2A = sphere(pos=(L*sin(pi),-L*cos(pi),0), radius = 0.1, color = color.white)
sphere2B = sphere(pos=(L*sin(pi)+L*sin(pi-0.1),-L*cos(pi)-L*cos(pi-0.1),0), radius = 0.1, color = color.white)
cy1A = cylinder(pos=wall.pos,axis=sphere1A.pos,radius=0.01,length=L,color=color.cyan)
cy1B = cylinder(pos=sphere1A.pos,axis=sphere1B.pos-sphere1A.pos,radius=0.01,length=L,color=color.cyan)
cy2A = cylinder(pos=wall.pos,axis=sphere2A.pos,radius=0.01,length=L)
cy2B = cylinder(pos=sphere2A.pos,axis=sphere2B.pos-sphere2A.pos,radius=0.01,length=L)

while True:
	rate(10000)
	ddf1 = (-g1/L*(2*sin(phi1)-sin(theta1)*cos(phi1-theta1))-1/2*pow(df1,2)*sin(2*phi1-2*theta1)-pow(dt1,2)*sin(phi1-theta1))/(1+pow(sin(phi1-theta1),2))
	ddt1 = (-g1/L*(2*sin(theta1)-2*sin(phi1)*cos(phi1-theta1))+1/2*pow(dt1,2)*sin(2*phi1-2*theta1)+2*pow(df1,2)*sin(phi1-theta1))/(1+pow(sin(phi1-theta1),2))

	ddf2 = (-g2/L*(2*sin(phi2)-sin(theta2)*cos(phi2-theta2))-1/2*pow(df2,2)*sin(2*phi2-2*theta2)-pow(dt2,2)*sin(phi2-theta2))/(1+pow(sin(phi2-theta2),2))
	ddt2 = (-g2/L*(2*sin(theta2)-2*sin(phi2)*cos(phi2-theta2))+1/2*pow(dt2,2)*sin(2*phi2-2*theta2)+2*pow(df2,2)*sin(phi2-theta2))/(1+pow(sin(phi2-theta2),2))

	df1=df1+ddf1*dt
	dt1=dt1+ddt1*dt

	df2=df2+ddf2*dt
	dt2=dt2+ddt2*dt

	phi1=phi1+df1*dt
	theta1=theta1+dt1*dt

	phi2=phi2+df2*dt
	theta2=theta2+dt2*dt

	sphere1A.pos=(L*sin(phi1),-L*cos(phi1),0)
	sphere1B.pos=(L*sin(phi1)+L*sin(theta1),-L*cos(phi1)-L*cos(theta1),0)
	cy1A.axis=sphere1A.pos
	cy1B.pos=sphere1A.pos
	cy1B.axis=sphere1B.pos-sphere1A.pos

	sphere2A.pos=(L*sin(phi2),-L*cos(phi2),0)
	sphere2B.pos=(L*sin(phi2)+L*sin(theta2),-L*cos(phi2)-L*cos(theta2),0)
	cy2A.axis=sphere2A.pos
	cy2B.pos=sphere2A.pos
	cy2B.axis=sphere2B.pos-sphere2A.pos