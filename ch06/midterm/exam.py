import turtle
def player_select():
  selection = int(input("Enter 1 or 2 or 3 "))
  return selection
  
def star():
  
  Turtle = turtle.Turtle()
  screen = turtle.Screen()
  Turtle.color('Yellow')
  angle = 252
  angle_2 = 36
  for i in range(5):
    Turtle.forward(50)
    Turtle.right(angle)
    Turtle.forward(50)
    Turtle.right(angle_2)
  screen.exitonclick()
  #This is the star


  
def coin():
  Pen = turtle.Turtle()
  screen = turtle.Screen()  
  Pen.color('Black')
  for i in range(4):
    Pen.forward(40)
    Pen.right(45)
    Pen.forward(20)
    Pen.right(45)
  Pen.up()
  Pen.forward(20)
  Pen.right(90)
  Pen.forward(20)
  
  Pen.down()
  Pen.left(90)
  Pen.forward(10)
  for i in range(2):
    Pen.right(90)
    Pen.forward(30)
    Pen.right(90)
    Pen.forward(15)
    
  screen.exitonclick()  
  #meant to resemble a coin

  
def poke():
  Pen = turtle.Turtle()
  screen = turtle.Screen()  
  Pen.color('Red')
  Pen.left(90)
  Pen.forward(20)
  for i in range(2):  
    Pen.right(90)
    Pen.forward(10)
    Pen.left(90)
    Pen.forward(20)
    Pen.right(90)
    Pen.forward(20)
    Pen.left(90)
    Pen.forward(10)
    Pen.right(90)
    Pen.forward(40)
  for i in range(2):  
    Pen.color('Black')
    Pen.right(90)
    Pen.forward(10)
    Pen.left(90)
    Pen.forward(20)
    Pen.right(90)
    Pen.forward(20)
    Pen.left(90)
    Pen.forward(10)
    Pen.right(90)
    Pen.forward(40) 
    #Outer shell
  Pen.back(20)
  Pen.right(90)
  Pen.forward(10)
  Pen.right(90)
  Pen.forward(10)
  Pen.left(90)
  Pen.forward(20)
  Pen.left(90)
  Pen.color('grey')
  for i in range(6):
    Pen.forward(20)
    Pen.right(90)
    Pen.forward(10)
    Pen.left(90)
    Pen.forward(10)
    Pen.right(90)
    #Middle circle for the pokeball  
  Pen.forward(20)
  Pen.left(90)
  Pen.color('black')
  Pen.forward(20)
  Pen.left(90)
  Pen.forward(10)
  Pen.right(90)
  Pen.forward(10)
  
  
    
  screen.exitonclick()
def main():
  num = player_select()
  if num == 1:
    star()
  elif num == 2:
    coin()
  elif num == 3:
    poke()
    
  
  
main()