import pygame 
import random
import math


#Dart board creation
pygame.init()
Window = pygame.display.set_mode((400, 400))
Red = pygame.Color(255, 0, 0)
Blue = pygame.Color(0, 0, 255)
Black = pygame.Color(0, 0, 0)
White = pygame.Color(255, 255, 255)
Green = pygame.Color(0, 255, 0)
Pos = [200, 200]
Window.fill(Blue)
pygame.display.flip()
pygame.draw.circle(Window, 'Red', Pos, 200, 0 )
pygame.draw.line(Window, Black, (0, 200), (400, 200))
pygame.draw.line(Window, Black, (200,0), (200,400))
pygame.display.update()

#Part B 
dart1 = random.randrange(400)
dart2 = random.randrange(400)
distance_from_center = math.hypot(200 - dart1, 200 - dart2)
is_in_circle = distance_from_center <= 200

for i in range (0, 10):
  dart1 = random.randrange(400)
  dart2 = random.randrange(400)
  distance_from_center = math.hypot(200 - dart1, 200 - 
  dart2)
  is_in_circle = distance_from_center <= 200
  if is_in_circle == True:
    dart_color = Green
  else: 
    dart_color = Red
  pygame.draw.circle(Window, dart_color, (dart1, 
  dart2), 7)
  pygame.display.update()
  pygame.time.wait(500)
pygame.time.wait(500)

#The actual game or Part C
window = pygame.display.set_mode((400,400))
window.fill(Blue) 
pygame.draw.rect(window, Green, pygame.Rect(50,150,100,100))   
pygame.draw.rect(window, White, pygame.Rect(250,150,100,100))  
pygame.display.update()

print("Who will win the dart game?")
print("The green player or the white player?")
print("Click on the rectangle of your choice!")

exit_event = False
while not exit_event:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1:
                
                if (event.pos[0] >= 50 and event.pos[0] <= 150 and event.pos[1] >= 150 and event.pos[1] <= 250) or (event.pos[0] >= 250 and event.pos[0] <= 350 and event.pos[1] >= 150 and event.pos[1] <= 250): 
                    exit_event = True
mouse_pos = event.pos
#mouse_pos not defined not sure why
pick_team = False
while not pick_team:
    if mouse_pos[0] >= 50 and mouse_pos[0] <= 150 and mouse_pos[1] >= 150 and mouse_pos[1] <= 250:
        print("Green player selected")
        pick_team = 1
    elif mouse_pos[0] >= 250 and mouse_pos[0] <= 350 and mouse_pos[1] >= 150 and mouse_pos[1] <= 250:
        print("White player selected")
        pick_team = 2


pygame.draw.circle(window, 'Red',(200,200),200)   
pygame.draw.line(window,Black,(0,200),(400,200)) 
pygame.draw.line(window,Black,(200,0),(200,400)) 



pygame.display.update()
green_score = 0
white_score = 0


for i in range (0, 10):
    dart1 = random.randrange(400)  
    dart2 = random.randrange(400)
    distance_from_center = math.hypot(200 - dart1, 200 - dart2)
    is_in_circle = distance_from_center <= 200
    if is_in_circle == True:
        dart_color = Green
        green_score +=1
    else:
        dart_color = Red
    pygame.draw.circle(window, dart_color,(dart1,dart2),6)
    pygame.display.update()
    pygame.time.wait(500)

    dart1 = random.randrange(400)  
    dart2 = random.randrange(400)
    distance_from_center = math.hypot(200 - dart1, 200 - dart2)
    is_in_circle = distance_from_center <= 200
    if is_in_circle == True:
        dart_color = White
        white_score +=1
    else:
        dart_color = Black
    pygame.draw.circle(window, dart_color,(dart1,dart2),6)
    pygame.display.update()
    pygame.time.wait(500)



print("")
print(" Final score ")
print("Green player: ", green_score)
print("White player: ", white_score)
print("")



if green_score > white_score:
    print("The green player has won")
    if pick_team == 1:       
        print("Congratulation! Your player won!")
    else:
        print("Your player didn't win.  Be Better!")
elif white_score > green_score:
    print("The white player has won")
    if pick_team == 2:       
        print("Congratulation! Your player won!")
    else:
            print("Your player didn't win.  Be Better!")
else:
    print("Its surprisingly a tie!")


pygame.time.wait(10000)
