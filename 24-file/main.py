PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read()


names_list = names.split("\n")

for name in names_list:
    new_letter = letter.replace(PLACEHOLDER, name)
    with open(f"./Output/letter_for_{name}.docx", mode="w") as new_letter_file:
        new_letter_file.write(new_letter)
