import pandas

# List, dictionary, and dataframe comprehension practice
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("8. Nato Phonetic Alphabet/nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
list = [alphabet_dict[letter] for letter in user_input]
print(list)
