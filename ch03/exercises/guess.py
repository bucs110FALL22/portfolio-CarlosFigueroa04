import random
guess_num = random.rand(1,11)
num_guess = 0 

for i in range(3):
  guess_num = int(input("Guess a number please:"))
  num_guesses += 1 
  if guess_num > num:
    print("Your number is too high")
  elif guess_num < num: 
 
   print("Your number is too low")
else:
  print("correcto")
  correct_guess = True 
break
print("It took you", num_guesses, "to get it right")


  