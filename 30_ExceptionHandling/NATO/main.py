import pandas as pd

def main():
    data = pd.read_csv(r"30_ExceptionHandling\NATO\nato_phonetic_alphabet.csv")
    phonetic_code = NATO_dict_builder(data)
    
    while True:
        try:
            print(word_to_NATO(
                word = input("Convert which word? "),
                dictionary = phonetic_code
            ))
            break
        except KeyError:
            print("Please, input only letters in the alphabet, please!")
    
    # Convert which word? Alaska
    # => ['Alfa', 'Lima', 'Alfa', 'Sierra', 'Kilo', 'Alfa']

def NATO_dict_builder(data: pd.DataFrame) -> dict:
    return {row.letter:row.code for (index, row) in data.iterrows()}

def word_to_NATO(word: str, dictionary: dict) -> list:
    return [dictionary[letter.upper()] for letter in word]

main()