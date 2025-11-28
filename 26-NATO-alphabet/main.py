import pandas as pd

# Read csv data
df = pd.read_csv("./nato_phonetic_alphabet.csv")
# Create data dictionary
data_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# Get word from user
word = input("Enter a word: ").upper()
# Generate nato list
nato_list = [data_dict[char] for char in word]

# print nato list
print(nato_list)
