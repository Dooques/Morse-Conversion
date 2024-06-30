import pandas as pd
import csv

print('Welcome to the Morse Converter')
to_convert = input("Please enter a word or phrase you wish to convert: ")
with open('files/morse.csv', newline='') as csv_file:
    morse = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in morse:
        print(', '.join(row))

print(morse)

morse_alphabet = pd.DataFrame(morse, columns=['alphabet', 'morse'])
print(morse_alphabet)

unconverted = []
morse_string = []

for char in to_convert:
    if char in morse_alphabet.index:
        morse_string.append(morse_alphabet.columns[char])

print(f'Your converted phrase is: {morse_string}')

