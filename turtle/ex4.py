import  turtle
t = turtle.Turtle()
r=10
for i in range(10):
    t.circle(r*i)
    t.up()
    t.sety((r*i) * (-1))
    t.down()
turtle.done()
