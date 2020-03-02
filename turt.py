from random import *
from turtle import *
shape("turtle")
pensize(3)
penup()
goto(300,300)
pendown()
for i in range(4):
	right(90)
	fd(600)
penup()
goto(0,0)
pendown()
while True:
	coord = pos()
	if abs(coord[0]) >= 300 or abs(coord[1]) >= 300:
		undo()
	color(random(), random(), random())
	circle(randrange(-60,60), randrange(200))
	
