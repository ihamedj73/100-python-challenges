import pandas as pd

# Read csv data
df = pd.read_csv("./nato_phonetic_alphabet.csv")
# Create data dictionary
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

while True:
    # Get word from user
    word = input("Enter a word: ").upper()
    try:
        # Generate nato list
        nato_list = [data_dict[char] for char in word]
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")


# print nato list
print(nato_list)
