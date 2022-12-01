import pygame

pygame.init

#Screen creation
width = 500
height = int(width * 0.8)
screen = pygame.display.set_mode((width, height))

#frame control
clock = pygame.time.Clock()
FPS = 30

#movement start 
moving_right = False
moving_left = False

#Any colors 
BG = (0, 255, 255)

def bg_fill():#Background fill and image stuff
  screen.fill(BG)

  
class Player(pygame.sprite.Sprite):
  def __init__(self, x, y, speed):
    pygame.sprite.Sprite.__init__(self)    
    self.speed = speed
    self.image = pygame.image.load('Mario.webp')
    self.image = pygame.transform.scale(self.image, (50,50))
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)  

  def movement(self, moving_right, moving_left):
    dy = 0
    #Vertical for jumps
    dx = 0
    #horizontal

    if moving_right:
      dx = self.speed

    if moving_left:
      dx = -self.speed

    self.rect.x += dx
    self.rect.y += dy
  
  def display(self):
    screen.blit(self.image, self.rect)
      
    
avatar = Player(200, 200, 2)


run = True
while run:
  clock.tick(FPS)
  
  bg_fill()
  
  avatar.display()
  
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

      if event.key == pygame.K_ESCAPE:
        run = False
    #key releases
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_a:
        moving_left = False

      if pygame.key == pygame.K_d:
        moving_right = False

  pygame.display.update()

pygame.quit()