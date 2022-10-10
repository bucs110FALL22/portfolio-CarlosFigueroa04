def star_pyramid():
  num_row = int(input("How many rows would you like?"))
  for i in range(num_row):
    for j in range(i+1):
      print("* ", end = "")
    print(" ")
star_pyramid()

def rstar_pyramid():
  num_row = int(input("How many rows would you like?:"))
  for i in range(num_row, 0, -1):
    for j in range(0, i):
      print("* ", end = "")
    print(" ")
rstar_pyramid()