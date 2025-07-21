"""
Python app for calculate Tip.
"""


print("Welcome to tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How mch tip would you like to give? 10, 12, 15 "))
num_people = int(input("How many people to split the bill? "))

total = bill * (tip / 100 + 1)

bill_per_person = total / num_people


print(f"Each person should pay: ${round(bill_per_person, 2)}")
