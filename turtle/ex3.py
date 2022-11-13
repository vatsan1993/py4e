import turtle
t= turtle.Turtle()
r= 10
n=100
for i in range(n):
    #t.circle(radius , angle) creates and arc
    t.circle(r+i,45)
turtle.done()