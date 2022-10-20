def mult(num):
  result= 0 
  for i in range(num):
   
    result = num + num
  return result
def exp(nums):
  result = 0
  for i in range(nums):
    result = nums * nums
  return result

def main():
  num = int(input("Please enter a number: "))
  vars = mult(num)
  print(vars)
  part_2 = exp(num)
  print(part_2)



main()