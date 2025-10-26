import random
import string

print("Welcome to the PyPassword Generator")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbol = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^",
           "&", "*", "(", ")", "_", "-", "+", "="]

# rand_letters = random.choices(letters, k=num_letters)
rand_chars = []
for _ in range(num_letters):
    rand_chars.append(random.choice(letters))

# rand_symbols = random.choices(symbols, k=num_symbol)
for _ in range(num_symbol):
    rand_chars.append(random.choice(symbols))

# rand_numbers = random.choices(numbers, k=num_numbers)
for _ in range(num_numbers):
    rand_chars.append(random.choice(numbers))

random.shuffle(rand_chars)

password = "".join(rand_chars)

print(f"Your password is: {password}")
