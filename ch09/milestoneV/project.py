import pygame
import math
pygame.init()

#Screen creation
width = 500
height = int(width * 0.8)
screen = pygame.display.set_mode((width, height))

#frame control
clock = pygame.time.Clock()
FPS = 60

#game variables
Gravity = 0.75
#movement start 
moving_right = False
moving_left = False
y = 50
#Any colors 
BG = pygame.image.load('Mountains.webp')
BG = pygame.transform.scale(BG, (400,300))

def bg_fill():#Background fill and image stuff  
  pygame.draw.line(screen, 'Black', (0,250), (width,250), 20)
  
class Player(pygame.sprite.Sprite):
  def __init__(self, x, y, speed):
    pygame.sprite.Sprite.__init__(self)    
    self.speed = speed
    self.jump = False
    self.vel_y = 0
    self.animation_list = []
    self.index = 0
    #for i in range(1):      
    self.image = pygame.image.load("idle.png")
    self.image = pygame.transform.scale(self.image, (50,50))
      #self.animation_list.append(image)
    #self.image = self.animation_list[self.index]
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)  

    #------
    self.img = pygame.image.load(("Mario.webp"))
    self.img = pygame.transform.scale(self.img, (50,25 ))
    self.img = pygame. transform. rotate(self.img, 180)
    self.rects = self.img.get_rect()
    self.scale = 5
    self.counter = 0
    number_of_enemies = 1
    self.ems = pygame.sprite.Group()
    self.xpos = 0
    self.ypos = 0
    
    
    #for i in range(number_of_enemies):
        #s = Player(self.xpos, self.ypos, 2)
        #self.ems.add(s)
  #def update(self):
    #if (self.rects.x == 0):
       #self.rect.xs = width
    #else:
      #self.counter = self.counter +1
    #if (self.counter >= self.scale): 
      #self.rects.x = self.rects.x - 1 
      #self.counter = 0 
    #-------------
      
    

# enemy = Enemy(200,200)

    #----------------
  def movement(self, moving_right, moving_left):
    dy = 0
    #Vertical for jumps
    dx = 0
    #horizontal

    if moving_right:
      dx = self.speed

    if moving_left:
      dx = -self.speed
    #Jumping 
    if self.jump == True:
      self.vel_y = -11
      self.jump = False
    #Make him actually come back down
    self.vel_y += Gravity
    if self.vel_y > 10:
      self.vel_y 
    dy += self.vel_y

    if self.rect.bottom + dy > 250:
      dy = 250 - self.rect.bottom
    
    self.rect.x += dx
    self.rect.y += dy
  
  def display(self):
    screen.blit(self.image, self.rect)
      
  def EnDisplay(self):
    screen.blit(self.img, self.rect)
avatar = Player(200, 200, 2)
scroll = 0
tiles = math.ceil(width / 400) + 1 
enemy = Player(400, 200, 2)

run = True
while run:
  clock.tick(FPS)
  for i in range(0, tiles):
    screen.blit(BG, (i * 400 + scroll , 0))
  
  scroll-= 5
  if abs(scroll) > 400:
    scroll = 0
  #All drawing stuff 
  bg_fill()
  avatar.display()
  enemy.EnDisplay()
  
  
  avatar.movement(moving_right, moving_left)
  
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      run = False
     #Key presses down
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        moving_left = True
        
      if event.key == pygame.K_d:
        moving_right = True

      if event.key == pygame.K_w:
        avatar.jump = True

      if event.key == pygame.K_ESCAPE:
        run = False
        
    
    #key releases
        
    if event.type == pygame.KEYUP:
      
      if event.key == pygame.K_a:
        moving_left = False

      if event.key == pygame.K_d:
        moving_right = False

  pygame.display.update()
pygame.quit()