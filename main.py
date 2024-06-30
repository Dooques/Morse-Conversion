import pandas as pd
import csv

print('Welcome to the Morse Converter')
# to_convert = input("Please enter a word or phrase you wish to convert: ")
to_convert = "hello"
alphabet = []
morse_code = []
with open('files/morse.csv', newline='') as csv_file:
    morse = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in morse:
        entry = ', '.join(row).split(',')
        alphabet.append(entry[0])
        morse_code.append(entry[1])

morse_alphabet = pd.DataFrame({'alphabet': alphabet, 'morse_code': morse_code})

unconverted = []
morse_string = []
for char in to_convert:
    char_entry = morse_alphabet.loc[morse_alphabet.alphabet == char.capitalize()]
    morse_string.append(char.capitalize() + ': ' + char_entry.morse_code.values[0])

print(f'Your converted phrase is: {morse_string}')

