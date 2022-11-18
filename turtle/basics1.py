# https://www.geeksforgeeks.org/turtle-programming-python/
# pythonturtle.org

import turtle
# getting tutle window
wn= turtle.Screen()
wn.bgcolor('light green')
wn.title('Simple Drawing')

# creating turtle
t= turtle.Turtle()
for i in range(4):
    t.forward(100)
    t.right(90)
turtle.done()