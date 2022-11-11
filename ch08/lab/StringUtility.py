class StringUtility:
  def __init__(self, string):
    self.string = string
    
  def __str__(self):
    return self.string

  def vowels(self):
    list = self.string.lower()
    count = 0
    for i in list:
      if i == "a":
        count += 1
      elif i == "e":
        count += 1 
      elif i == "i":
        count += 1
      elif i == "o":
        count += 1
      elif i == "u":
        count += 1
      if count >= 5:
        count = "many"
        break
    return(str(count))

  def bothEnds(self):
    if len(self.string) > 2:
      return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
    else:
      return ""

  def fixStart(self):
    if len(self.string) == 0:
      return(self.string)
    firstlet = self.string[0]
    string = self.string
    
    for i in self.string:
      if i == firstlet:
        string = string.replace(i,"*")
    string = string.replace("*",firstlet,1)


    return(string)
    
  def asciiSum(self):
    sum = 0 
    for i in self.string:
      sum = sum + ord(i)
    return (sum)
    
  def cipher(self):
    crypt = ""
    Upperalpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    Loweralpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(0, len(self.string)):
      letternumber = ord(self.string[i])
      length = len(self.string)
      if length + letternumber>90 and (self.string[i]) in Upperalpha:
         new = letternumber + length -26 
         ztoa = chr(new)
         crypt+=(ztoa)
      elif 123 < (length + letternumber) <= 148 and (self.string[i]) in Loweralpha: 
         new = letternumber + length -26 
         ztoa = chr(new)
         crypt+=(ztoa)
      elif  (length + letternumber) > 148 and (self.string[i]) in Loweralpha: 
         new = letternumber + length - 52
         ztoa = chr(new)
         crypt+=(ztoa)
      elif " " == self.string[i]:
         new = letternumber 
         ztoa = chr(new)
         crypt+=(ztoa)

      else:
        crypt+=chr(letternumber+length)
    return crypt
    
    
    
        
    