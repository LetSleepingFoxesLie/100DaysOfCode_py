from random import randint
import pandas as pd

def main():
    print(sequence_of_ones(5))
    print(sequence_of_letters("Alaska"))
    print(sequence_of_doubled_numbers(8))
    print(conditional_list_comprehension())
    print(sequence_of_squared_numbers())
    print(sequence_of_even_numbers())
    
    random_dict = dict_comprehension()
    print(random_dict)
    people_with_good_score = dict_scorer(random_dict)
    print(people_with_good_score)
    print(word_length_dict("Cgar bwov zmxcyu nwuesti, Vhkzo. Zdlh'a oeaz mxg zwax gg, lnp C emdg sm nqavkza cequ jourwar. WI: uwr abg sto ahc, Hktq."))
    print(dict_comp_temperature_converter())
    pandas_comprehension_what()
    
def sequence_of_ones(argument: int):
    # Apparently going to cut down on some shit!
    # new_list = [new_item for item in list]
    
    return [n for n in range(argument)]

def sequence_of_letters(word: str):
    return [letter for letter in word]

def sequence_of_doubled_numbers(amount: int):
    return [n * 2 for n in range(amount)]

def conditional_list_comprehension():
    names = ["Alaska", "Wolf", "White", "Some other random ass name", "Car-burning French"]
    return [name for name in names if len(name) <= 6]

def sequence_of_squared_numbers():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    return [n**2 for n in numbers]

def sequence_of_even_numbers():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    return [n for n in numbers if n % 2 == 0]

def dict_comprehension():
    # What
    # new_dict = {new_key:new_value for (key, value) in dict.items()}
    names = ["Alaska", "Wolf", "White", "Some other random ass name", "Car-burning French"]
    return {name:randint(1, 100) for name in names}

def dict_scorer(d: dict):
    return {name:score for (name, score) in d.items() if score >= 60 or name == "Alaska"}

def word_length_dict(p: str):
    # l = [word for word in p.split(sep = " ")]
    return {word:len(word) for word in p.split(sep = " ")}

def dict_comp_temperature_converter():
    weather_data = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    return {day:(t * 1.8 + 32) for (day, t) in weather_data.items()}

def pandas_comprehension_what():
    IQ_dict = {
        "subject": ["Alaska", "Flamm", "Some dumbass"],
        "score": [128, 67, 84]
    }
    
    pd_iq = pd.DataFrame(IQ_dict)
    # Loop through rows of a data frame:
    for (index, row) in pd_iq.iterrows():
        print(row.subject)

main()