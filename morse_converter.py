import csv
import pandas as pd


class Morse:
    def __init__(self):
        self.alphabet = []
        self.morse_code = []
        with open('files/morse.csv', newline='') as csv_file:
            morse = csv.reader(csv_file, delimiter=' ', quotechar='|')
            for row in morse:
                entry = ', '.join(row).split(',')
                self.alphabet.append(entry[0])
                self.morse_code.append(entry[1])
        self.morse_alphabet = pd.DataFrame({'alphabet': self.alphabet, 'morse_code': self.morse_code})

    def convert_string(self, to_convert):
        print("String received")
        morse_string = []
        for char in to_convert:
            char_cap = char.capitalize()
            print(char_cap)
            if char_cap in self.morse_alphabet.alphabet.values:
                print(f' Searching DF {char}')
                print("char found")
                char_entry = self.morse_alphabet.loc[self.morse_alphabet.alphabet == char_cap]
                print(char_entry.morse_code.values)
                morse_string.append(char_entry.morse_code.values[0])
        print(morse_string)
        result = " ".join(morse_string)
        print(result)
        return result
