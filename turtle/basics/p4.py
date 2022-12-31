# pyramid program

import turtle
# getting tutle window
wn= turtle.Screen()
wn.bgcolor('light green')
wn.title('Simple Drawing')

# creating turtle
t= turtle.Turtle()
# outside to inside
def square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)
        size-=5
# inside to outside
def sqrfunc(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size = size + 5

square(146)
square(126)
square(106)
square(86)
square(66)
square(46)
square(26)

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)
turtle.done()
