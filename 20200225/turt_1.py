from random import *
from turtle import *
from math import *

def stop(x, y):
	global flg
	flg = False

flg = True
t1 = Turtle()
t1.getscreen().onclick(stop)
t1.shape("turtle")
t1.pensize(3)
t1.speed(0)
t1.penup()
t2 = t1.clone()
t2.hideturtle()
t1.pendown()
size = (window_width(), window_height())
while flg:
	deg, sec = randrange(-60,60), randrange(200)
	t2.circle(deg, sec)
	if size[0] != window_width() and size[1] != window_height() and \
	(abs(t1.pos()[0]) > window_width() or abs(t1.pos()[0]) > window_height()):
		t1.penup()
		t1.goto(0,0)
		t2.goto(0,0)
		t1.pendown()
	coord = t2.pos()
	size = (window_width(), window_height())
	if abs(coord[0]) >= window_width() / 2 or abs(coord[1]) >= window_height() / 2:
		t2.goto(t1.pos())
		t2.right(t2.heading())
		t2.left(t1.heading())
		continue
	t1.color(random(), random(), random())
	t1.circle(deg, sec)
