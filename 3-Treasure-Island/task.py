print("Welcome to pizza Delivery")

size = input("What pizza size do you want? S, M , L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or, N: ")
extra_cheese = input("Do you want extra cheese? Y, N: ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

else:
    print("You typed the wrong word")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is ${bill}")
