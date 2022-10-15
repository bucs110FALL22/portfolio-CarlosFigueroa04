import pygame

pygame.init()

upper_limit = 20
iters = {}

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


# Part B

max_so_far = 0 
for i in range(2, upper_limit + 1):  
  count = thing(i)
  
  iters[i] = count


print(iters)

#Part C 

window = pygame.display.set_mode()



  


