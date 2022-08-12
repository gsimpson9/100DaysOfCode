

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas as pd
data = pd.read_csv('nato_phonetic_alphabet.csv')

#TODO 1. Create a dictionary in this format:

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
user_word = input("Please enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_word]
print(output_list)



# Shite


# #TODO 1. Create a dictionary in this format:
# with open('nato_phonetic_alphabet.csv') as phonetic_file:
#     phonetic_list = phonetic_file.readlines()
#
# letters = [letter[0] for letter in phonetic_list[1:]]
# phonetic = [letter[1:].strip().replace(',', '') for letter in phonetic_list[1:]]
#
# phonetic_dict = {
#     'Letters': letters,
#     'Words': phonetic
# }
#
# phonetic_df = pd.DataFrame(phonetic_dict)
# print(phonetic_df)