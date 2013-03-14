
    
# Polygon excercise from Week 0
    
Mark Levi



from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)


def polygon(t, n, length):
	angle = 360.0/n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

import math

def circle(t, r)
circumference = 2 * math.pi * r
n = (circumference/3) +1
length = circumference / n
polygon (t, n, length)

bob.delay = 0.01

/////////////////

def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)

def circle(t, r):
	arc(t, r, 360)


bob.delay = 0.01

arc(bob, 50, 180)




wait_for_user()




wait_for_user()					
