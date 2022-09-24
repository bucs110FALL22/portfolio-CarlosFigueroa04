import turtle #1. import modules
import random
import math 
import pygame
#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
  michelangelo.forward(random.randrange(1,11))
  leonardo.forward(random.randrange(1,11))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()
# PART B - complete part B here


pygame.init()

window = pygame.display.set_mode((300,100))
def shape_points(num_sides):
  coords = []
  num_sides = num_sides
  side_length = 20
  offset = 50
for i in(num_sides):
  theta = (2.0 * math.pi * (i)) / num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append([x,y])

return coords

pygame.draw.polygon(window,"red", shape_points(3))
pygame.display.flip()
pygame.time.delay(300)
window.fill("red")

	

window.exitonclick()
