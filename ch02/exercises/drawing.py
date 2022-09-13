import turtle

my_turtle = turtle.Turtle()



sides = int(input("How many sides are in your shape?"))
length = int(input("How long is each side?"))


my_turtle.shape("turtle")
my_turtle.color("red")

for i in range(sides):
  my_turtle.forward(length)
  my_turtle.left(360/sides)
  


turtle.done()