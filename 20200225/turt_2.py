from random import *
from turtle import *
shape("turtle")
speed(0)
pensize(3)
penup()
goto(300,300)
pendown()
for i in range(4):
	right(90)
	fd(600)
penup()
goto(300,420)
pendown()
for i in range(4):
	circle(-120,90)
	fd(600)
penup()
goto(0,0)
pendown()
deg = 0
while True:
	coord = pos()
	if abs(coord[0]) >= 300 or abs(coord[1]) >= 300:
		circle(deg, 23)
		continue
	color(random(), random(), random())
	deg = randrange(-60,60)
	circle(deg, randrange(200))
