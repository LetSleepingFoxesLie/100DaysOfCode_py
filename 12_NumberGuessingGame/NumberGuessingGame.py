import random

def set_difficulty():
    attempts = 0
    difficulty = input("How difficult should this game be? Type 'easy' (5 attempts) or 'hard' (10 attempts): ")
    
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Unknown difficulty, placing the game on hard because... yeah, why not? Suffer.")
        attempts = 5
    return attempts

def guess_number_game():
    number = random.randint(0, 100)
    
    attempts = set_difficulty()
    
    while(attempts > 0):
        print(f"You only have {attempts} attempts remaining!")
        guess = int(input("Guess a number: "))
        
        if guess > number:
            print("- Too high!")
        elif guess < number:
            print("- Too low!")
        else:
            print(f"- Congratulations! The number was {number}")
            return
        
        attempts -= 1
    
    print(f"You lost! The number was {number} :/")

guess_number_game()