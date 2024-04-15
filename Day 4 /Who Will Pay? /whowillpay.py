names_string = input("Please enter the names separated by commas: ")
names = names_string.split(", ")

import random
names_choice = len(names)
pay = random.randint(0, names_choice - 1)

who_is_paying = names[pay]

print("The person who is paying is:", who_is_paying)
