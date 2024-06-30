import csv
import pandas as pd


class Morse:
    def __init__(self):
        self.alphabet = []
        self.morse_code = []

    def convert_string(self, to_convert):
        print('Welcome to the Morse Converter')
        to_convert = input("Please enter a word or phrase you wish to convert: ")
        with open('files/morse.csv', newline='') as csv_file:
            morse = csv.reader(csv_file, delimiter=' ', quotechar='|')
            for row in morse:
                entry = ', '.join(row).split(',')
                self.alphabet.append(entry[0])
                self.morse_code.append(entry[1])

        morse_alphabet = pd.DataFrame({'alphabet': self.alphabet, 'morse_code': self.morse_code})

        morse_string = []
        for char in to_convert:
            char_entry = morse_alphabet.loc[morse_alphabet.alphabet == char.capitalize()]
            morse_string.append(char.capitalize() + ': ' + char_entry.morse_code.values[0])

        print(f'Your converted phrase is: {", ".join(morse_string)}')
