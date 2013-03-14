# Flower excercise (4.2) from Week 0

Mark Levi


from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01

import math
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

def petal(t, r, angle):
    for i in range(2):
   		arc(t, r, angle)
        lt(t, 180-angle)

def flower(t, n, r, angle):
	for i in range(n):
		petal(t, r, angle)
		lt(t, 360.0/n)

def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)


move(bob, -100)
flower(bob, 7, 60, 60)

move(bob, 100)
flower(bob, 10, 40, 80)

move(bob, 100)
flower(bob, 20, 200, 20)

die(bob)









wait_for_user()

