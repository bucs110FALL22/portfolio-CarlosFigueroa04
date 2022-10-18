import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')
def drawEQshape(num_sides , side_length):
  for i in range(num_sides):
    turtle.forward(side_length)
    turtle.left(angle)
  

num_sides = int(input("How many sides are in your shape?"))
side_length = int(input("How long are the shapes sides?"))
angle = 360/num_sides

drawEQshape(num_sides, side_length)