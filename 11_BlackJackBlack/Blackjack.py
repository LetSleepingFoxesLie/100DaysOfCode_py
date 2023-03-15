import random

def blackjack_loop():
    while(True):
        blackjack_game()
        
def blackjack_game():
    #     = [A,  2, 3, 4, 5, 6, 7, 8, 9, 10, J,  Q,  K ]
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand_player, hand_dealer = draw_start(cards), draw_start(cards)
    print(hand_player)
    print(hand_dealer)

def draw_card(cards):
    return cards[random.randint(0, len(cards) - 1)]

def draw_start(cards):
    drawn_cards = []
    for card in range(2):
        drawn_cards.append(
            draw_card(cards)
        )
    return drawn_cards

def card_prints(hand):
    if len(hand) == 0:
        return "Error: hand is empty"
    
    return_string = "["
    for card in hand:
        return_string += f"{card}, "
    return_string += "]"
    return return_string

blackjack_game()