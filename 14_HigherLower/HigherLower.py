from Data import data
from random import randint

# Display two people at random - cannot be the same
# Make the player choose between both
# Show whether player has won or not
# Swap the "loser" of the previous round with a new entry
# Keep going

# Self-explanatory: get a random subject from data
def fetch_from_data():
    index = randint(0, len(data) - 1)
    return data[index]

# Reads and prints relevant data from subject
def display_info(subject):
    return f"{subject['name']}, a {subject['description']} from {subject['country']} || {subject['follower_count']}"
    # For debugging purposes:
    # return f"{subject['name']}, a {subject['description']} from {subject['country']}"

# Gets the player input
def get_player_input(a_person, b_person):
    print("Who has more followers on Instagram?")
    print(f"[A] {display_info(a_person)}")
    print("--- VS ---")
    print(f"[B] {display_info(b_person)}")
    
    player_input = input("Your guess (A/B): ")
    
    return player_input

# Checks whether the player input is correct or not. Returns a boolean value
def is_player_input_correct(a, b, i):
    # First condition: A's follower count is HIGHER than B's
    if a["follower_count"] > b["follower_count"] and i.lower() == "a":
        # Win
        # Alternative: return i.lower() == "a"
        return True
    # Second condition: A's follower count is LOWER than B's
    elif a["follower_count"] < b["follower_count"] and i.lower() == "b":
        # Also win!
        # Alternative: return i.lower() == "b"
        return True
    else:
        # Lose!
        return False

# The game itself!
def higher_lower_game():
    
    # Get two people at random
    a_person = fetch_from_data()
    b_person = fetch_from_data()
    
    score = 0
    
    while(a_person == b_person):
        b_person = fetch_from_data()
    
    # Who has more followers on Instagram?
    while(True):
        player_input = get_player_input(a_person, b_person)
        if is_player_input_correct(a_person, b_person, player_input):
            score += 1
            print(f"Congratulations! Score: {score}")
            
            # Generate new person
            a_person = b_person
            b_person = fetch_from_data()
            while(a_person == b_person):
                b_person = fetch_from_data()
        else:
            break
    
    print(f"Game over! Total score: {score}")
            
    
higher_lower_game()