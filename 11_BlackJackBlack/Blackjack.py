import random
import os

def blackjack_loop():
    while(True):
        os.system("cls||clear")
        blackjack_game()
        user_input = input("Do you want to play another game? (y/n) ")
        if user_input.lower() == "y":
            continue
        else:
            break

# Where the game really happens
def blackjack_game():
    #     = [A,  2, 3, 4, 5, 6, 7, 8, 9, 10, J,  Q,  K ]
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand_player, hand_dealer = draw_start(cards), draw_start(cards)
    
    print(f"P: {hand_player} -> {calculate_hand(hand_player)}")
    print(f"D: {print_veiled_hand(hand_dealer)} -> ?")
    
    # If dealer outright gets a blackjack, he wins:
    if calculate_hand(hand_dealer) == 21:
        print("Dealer wins!")
        return False
    
    # If dealer doesn't, then, if the player does, they win
    if calculate_hand(hand_player) == 21:
        print("Player wins!")
        return True
    
    # Otherwise, make them play the game:
    while(True):
        if player_wants_another_card():
            hand_player.append(generate_card(cards))
            hand_dealer.append(generate_card(cards))
            
            print(f"P: {hand_player} -> {calculate_hand(hand_player)}")
            print(f"D: {print_veiled_hand(hand_dealer)} -> ?")
            
            # Then check his score with every drawn card
            if calculate_hand(hand_player) == 21:
                print("Player wins!")
                print(f"D: {hand_dealer} -> {calculate_hand(hand_dealer)}")
                return True
            
            if calculate_hand(hand_player) > 21:
                print("Player loses!")
                print(f"D: {hand_dealer} -> {calculate_hand(hand_dealer)}")
                return False
            
        else:
            # Let the computer play by breaking this while
            break
    
    # And so it does until it either wins, busts, or its hand's value > 16
    while(calculate_hand(hand_dealer) < 17):
        hand_dealer.append(generate_card(cards))
        print(f"D: {hand_dealer} -> {calculate_hand(hand_dealer)}")
        
        if calculate_hand(hand_dealer) == 21:
            print("Dealer wins!")
            return False
        
        if calculate_hand(hand_dealer) > 21:
            print("Player wins!")
            return True
    
    # Calculating scores if neither party won or busted
    score_player = calculate_hand(hand_player)
    score_dealer = calculate_hand(hand_dealer)
    print(f"D: {hand_dealer} -> {calculate_hand(hand_dealer)}")
    
    if is_bust(hand_dealer):
        print("Player wins!")
        return True

    if score_player == score_dealer:
        print("It's a draw!")
        return False
    elif score_player > score_dealer:
        print("Player wins!")
        return True
    else:
        print("Player loses!")
        return False

# Generates a random card. What else are you expecting?
def generate_card(cards):
    return cards[random.randint(0, len(cards) - 1)]

# Checks whether player wants another card
def player_wants_another_card():
    user_input = input("Do you want another card? (y/n) ")
    if user_input.lower() == "y":
        return True
    elif user_input.lower() == "n":
        return False
    else:
        print("Input error, assuming 'n'")
        return False
    
# Generates the two starting cards by implementing generate_cards()
def draw_start(cards):
    drawn_cards = []
    for card in range(2):
        drawn_cards.append(generate_card(cards))
    return drawn_cards

# Prints the dealer's veiled hand. Apparently, only the first card is shown to the player, so we must comply. Bummer
def print_veiled_hand(hand):
    return_string = "["
    index = 0
    for card in hand:
        if index == 0:
            return_string += f"{card}, "
        else:
            return_string += "_, "
        index += 1
    return_string = return_string[:-2]
    return_string += "]"
    return return_string

# And in the end I didn't even use these two:
def is_winning_hand(hand):
    score = calculate_hand(hand)
    if score == 21:
        return True
    else:
        return False

def is_bust(hand):
    score = calculate_hand(hand)
    if score > 21:
        return True
    else:
        return False

# Because calculating the hand's score and then returning it felt better. Not the most practical thing all things considered, but, if it works, it works
def calculate_hand(hand):
    if len(hand) == 0:
        return "Error: hand is empty"
    
    tally, ace_counter = 0, 0
    
    for card in hand:
        tally += int(card)
        if int(card) == 11:
            ace_counter += 1
        
    for ace in range(ace_counter):
        if tally > 21:
            tally -= 10
            
    return tally

# Calling the game itself. We gotta run it, bois
blackjack_loop()