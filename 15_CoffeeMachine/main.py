MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# Prompts the user
def get_prompt():
    allowed_commands = ["off", "report"]
    
    while True:
        prompt = input("What would you like? (espresso, latte, or cappuccino): ")
        
        if prompt not in MENU and prompt not in allowed_commands:
            print("- Sorry, I didn't understand.")
            continue
        else:
            break

    return prompt

# Print a report with the machine's resources
def print_report(machine):
    print(f"MACHINE REPORT")
    print(f"- Water: {machine['water']}ml")
    print(f"- Milk: {machine['milk']}ml")
    print(f"- Coffee: {machine['coffee']}g")
    print(f"- Money: ${machine['money']:.2f}")

# Checks whether the machine has enough resources to make a brew
def can_make_brew(machine, drink):
    has_resources = True

    if machine['water'] < MENU[drink]['ingredients']['water']:
        print("- Sorry, there is not enough water!")
        has_resources = False
        
    if machine['milk'] < MENU[drink]['ingredients']['milk']:
        print("- Sorry, there is not enough milk!")
        has_resources = False
        
    if machine['coffee'] < MENU[drink]['ingredients']['coffee']:
        print("- Sorry, there is not enough coffee!")
        has_resources = False
    
    return has_resources

# Actually makes the brew! And gives some change, too.
def make_brew(machine, drink, money):
    machine['water'] -= MENU[drink]['ingredients']['water']
    machine['milk'] -= MENU[drink]['ingredients']['milk']
    machine['coffee'] -= MENU[drink]['ingredients']['coffee']
    
    if money > MENU[drink]['cost']:
        change = money - MENU[drink]['cost']
        print(f"+ Here's ${change:.2f} in change!")
    
    print(f"Here's your {drink}, enjoy!")
    machine['money'] += MENU[drink]['cost']
    return machine

# Collects the user's coins
def request_coins():
    
    # Some values to make the code better to read down below. I hope so.
    coin_values = [0.25, 0.10, 0.05, 0.01]
    coin_names = ["quarters", "dimes", "nickels", "pennies"]
    tally = 0
    
    # Adding some input validation.
    for i in range(len(coin_values)):
        while True:
            try:
                tally += int(input(f">> How many {coin_names[i]}? ")) * coin_values[i]
            except ValueError:
                print(">> Please, input a number.")
                continue
            break
    
    print(f"+ Your money: ${tally:.2f}")
    return tally
    
# Parses the user's input. Kind of, I hate parsing stuff.
def coffee_machine_loop():
    machine = resources
    
    # As the machine will continually run, we need a loop
    while True:    
        user_input = get_prompt().lower()
        
        if user_input == "off":
            print("+ Turning coffee machine off")
            break
        elif user_input == "report":
            print_report(machine)
            continue
        else:
            
            if can_make_brew(machine, user_input):
                coins = request_coins()
                if coins < MENU[user_input]['cost']:
                    print(f"- Sorry, that's not enough money for a {user_input} (${MENU[user_input]['cost']:.2f}). Refunded all coins.")
                    continue
                else:
                    machine = make_brew(machine, user_input, coins)

coffee_machine_loop()
