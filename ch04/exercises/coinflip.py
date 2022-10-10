import turtle
import random

my_turtle = turtle.Turtle()
window = turtle.Screen
my_turtle.shape("turtle")


distance = 10
angle = 90
is_in_screen = True
while is_in_screen:
  coin= random.randrange(0, 2)
  if coin:
    my_turtle.left(angle)
  else:
    my_turtle.right(angle)
  my_turtle.forward(distance)

  turtlex = my_turtle.xcor()
  turtley = my_turtle.ycor()

  x_range = window.window_width()/2
  y_range = window.window_width()/2

  if abs(turtlex) > x_range or abs(turtley) > y_range:
    is_in_range = False

window.bgcolor("yellow")
window.exitonclick()