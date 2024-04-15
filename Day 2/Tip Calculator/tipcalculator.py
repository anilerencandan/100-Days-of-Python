print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total = total_bill + (tip_percentage / 100) * total_bill
total_per_person = total / people
print(f"Each person should pay: ${total_per_person:.2f}")
