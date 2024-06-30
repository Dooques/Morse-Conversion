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
print(alphabet)
print(morse_code)
morse_alphabet = pd.DataFrame(morse, columns=['alphabet', 'morse'])

unconverted = []
morse_string = []

for char in to_convert:
    if char in morse_alphabet.index:
        morse_string.append(morse_alphabet.columns[char])

print(f'Your converted phrase is: {morse_string}')

