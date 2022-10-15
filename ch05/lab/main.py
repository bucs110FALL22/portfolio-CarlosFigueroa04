import pygame

pygame.init()
window = pygame.display.set_mode()
window.fill('white')
upper_limit = 20
iters = {}
scale = 15
#Part A
def thing(n):
  count = 0
  while n != 1:
    if n % 2 == 0:
      n = n//2
    elif n % 2 != 0:
      n = n * 3 + 1
    count = count + 1
   
  return(count)
thing(101)


# Part B and C
max_val = 0
max_so_far = 0 
font = pygame.font.Font(None, 20)
scale = 15

for i in range(2, upper_limit + 1): 
  count = 0
  n = i
  while n != 1:
    if n%2 == 0:
      n = n//2
    elif n%2 != 0:
      n = n*3 + 1
    count = count + 1
    iters[i] = count
    iters.items()
    coords = list(iters.items())
  if max_so_far < count:
    max_so_far = count
    max_val = max_so_far
    for p in range(len(coords) - 1):
      pygame.draw.lines(window, "red", False, (coords * scale))
      pygame.display.flip()
      new_display = pygame.transform.flip(window, False, True)
      pygame.display.flip()
      window.blit(new_display, (0, 0))
      pygame.display.flip()
  #msg= font.render(, True, "black")
  
pygame.time.wait(500)    

     
     
  