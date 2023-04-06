import matplotlib as plt
import pandas as pd
import math

def get_info() -> dict:
    attacks_per_second, skill_cost, indigon_roll = 0, 0, 0
    
    while True:
        try:
            attacks_per_second = float(input("Attacks per second: "))
            break
        except ValueError:
            print("> This is not a number!")
            
    while True:
        try:
            skill_cost = float(input("Skill cost: "))
            break
        except ValueError:
            print("> This is not a number!")
            
    while True:
        try:
            indigon_roll = float(input("Indigon roll: "))
            indigon_roll = 1 + 0.01 * indigon_roll
            
            if 1.5 <= indigon_roll and indigon_roll <= 1.6:
                break
            else:
                print("> Indigon roll out of bounds, try again.")
        except ValueError:
            print("> This is not a number!")
    
    return {
        "roll": indigon_roll,
        "aps": attacks_per_second,
        "base_cost": skill_cost
    }

def calculate_mana(mana_cost: float, spent_mana: float, indigon_roll: float) -> int:
    INDIGON_THRESHOLD = 200
    
    times_indigon = 1 + math.floor(spent_mana / INDIGON_THRESHOLD)
    print(times_indigon)
    return math.ceil(mana_cost * times_indigon * indigon_roll)

def indigon(data: dict):
    # This assumes you're attacking non stop
    total_mana_spent = 0.0
    skill_mana_cost = 0.0
    
    for attack in range(math.floor(4 * data["aps"])):
        skill_mana_cost = 0
        total_mana_spent += calculate_mana(data["base_cost"], total_mana_spent, data["roll"])
        
        print(f"Attack #{attack + 1}: {skill_mana_cost} mana (total: {total_mana_spent})")

indigon(get_info())