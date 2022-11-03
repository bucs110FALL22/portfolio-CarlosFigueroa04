import time

class Animal:
  def __init__(self, name, type):  
    self.id = time.strftime("%d/%m/%M/%S")
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%M/%S")
    self.adoted = None

  def set_adopted(self):
    self.adopted = time.strftime("%d/%m/%M/%S")

  def __str__(self):
        result_str = f"{self.name}[{self.type}]"
        result_str += f"\narrived: {self.arrived}"
        result_str += f"\nadopted:{self.adopted}"
        return result_str

def main():
  fido = Animal("Fido", "cat")
  fido.set_adopted()
  print(fido)

  
main()
  
