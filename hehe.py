from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)
g = Turtle()
g.shape("turtle")
begin_fill()
distance = 2
#angle = 90
g.up()
#g.color("white")
for i in range(10):
    g.forward(50)
    g.stamp()
    g.forward(-50)
    g.right(36)
   #angle += 10
for j in range(20):
    g.forward(100)
    g.stamp()
    g.forward(-100)
    g.right(18)

for k in range(40):
    g.forward(150)
    g.stamp()
    g.forward(-150)
    g.right(9)
done()

