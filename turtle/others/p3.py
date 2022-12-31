# https://www.geeksforgeeks.org/turtle-programming-python/
import turtle
# getting tutle window
wn= turtle.Screen()
wn.bgcolor('light green')
wn.title('Simple Drawing')

# creating turtle
t= turtle.Turtle()

sides=6
length=70
angle = 360/sides

for i in range(sides):
    t.forward(length)
    t.right(angle)

turtle.done()