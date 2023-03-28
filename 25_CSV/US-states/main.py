from turtle import Screen, Turtle
import pandas as pd

def main():
    screen = Screen()
    screen.title("Please no!")
    
    image = r"25_CSV\US-states\blank_states_img.gif"
    screen.addshape(image)
    Turtle().shape(image)
    
    data = get_states()
    
    correct_guesses = list()
    maximum_guesses = len(data.state)
    print(maximum_guesses)
    number_of_guesses = 0
    
    while True:
        player_answer = screen.textinput(f"{len(correct_guesses)}/{maximum_guesses}", "Do know the other states in the US??").title()
        number_of_guesses += 1
        
        if data.state.eq(player_answer).any() and player_answer not in correct_guesses:
            draw_turtle_on_correct_guess(
                state = player_answer,
                coordinates = get_coordinates(
                    data = data,
                    guess = player_answer
                )
            )
            correct_guesses.append(player_answer)

            if len(correct_guesses) == maximum_guesses:
                screen.textinput(f"You won!")
                break
        elif player_answer == "Break":
            generate_csv_with_other_answers(
                correct_guesses = correct_guesses,
                all_states = data.state.to_list()
            )
            break
        else:
            continue
            # print("Não")
        
    screen.mainloop()

def generate_csv_with_other_answers(correct_guesses: list, all_states: list):
    
    # Holy shit
    other_states = [state for state in all_states if state not in correct_guesses]
    
    # for state in all_states:
    #     if state not in correct_guesses:
    #         other_states.append(state)

            
    data = pd.DataFrame(data = other_states)
    data.to_csv("25_CSV\US-states\other_states.csv")

def get_states() -> pd.DataFrame:
    data = pd.read_csv(r"25_CSV\US-states\50_states.csv")
    return data

# Imagine not being intuitive :(
def get_coordinates(data: pd.DataFrame, guess: str):
    
    # Hacky way to extract an actual int instead of a fucking pd.Series
    return (data[data.state == guess].x.squeeze(), data[data.state == guess].y.squeeze())

# Whenever we get a state right, create a turtle
def draw_turtle_on_correct_guess(state: str, coordinates = tuple) -> None:
    text = Turtle()
    text.color("black")
    text.penup()
    text.hideturtle()
    text.setpos(coordinates)
    text.write(
        arg = state,
        move = False,
        align = "center",
        font = (
            "Bahnschrift",
            12,
            "normal"
        )
    )

main()