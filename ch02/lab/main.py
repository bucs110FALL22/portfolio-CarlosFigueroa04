import random 
#Part A
weeks = 16
print(weeks, type(weeks))
classes = 5
print(classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 4
print(classes_per_week, type(classes_per_week))

cost_per_class= cost_per_week/classes_per_week
print("Your total cost per class is", cost_per_class)

#Part B
my_numbers= (1, 100, 201, "hug", "jungle")
my_list = random.choice(my_numbers)
print(my_list)