
def percentage_to_letter(score=0):
  if score >= 90:
    print("A")
  elif score >= 80:
    print("B")
  elif score >= 70:
    print("C")
  elif score >= 60:
    print("D")
  elif score < 60:
    print("F")
  return score
    

  
score = int(input("WHat is the grade: "))
letter_grade = percentage_to_letter(score)

def is_passing(letter = None):
  if letter_grade >= 60:
    print("True")
  elif letter_grade < 60:
    print(False)
  return letter_grade
is_passing()  