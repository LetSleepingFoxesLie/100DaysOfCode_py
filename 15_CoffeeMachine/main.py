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
    prompt = input("What would you like? (espresso, latte, or cappuccino): ")
    return prompt

# Print a report with the machine's resources
def print_report(machine):
    print(f"MACHINE REPORT")
    print(f"- Water: {machine['water']}ml")
    print(f"- Milk: {machine['milk']}ml")
    print(f"- Coffee: {machine['coffee']}g")
    print(f"- Money: ${machine['money']:.2f}")

def can_make_brew(machine, drink, money):
    
    if money < MENU[drink]['cost']:
        print(f"- Sorry, that's not enough money for a {drink} (${MENU[drink]['cost']:.2f}). Refunded all coins.")
        return False
    
    has_resources = True

    if machine['water'] < MENU[drink]['ingredients']['water']:
        print("- Sorry, there is not enough water!")
        has_resources = False
        
    if machine['milk'] < MENU[drink]['ingredients']['milk']:
        print("- Sorry, there is not enough milk!")
        has_resources = False
        
    if machine['coffee'] < MENU[drink]['ingredients']['coffee']:
        print("- Sorry, there is not enough coffee!")
        has_resource = False
    
    return has_resources

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

def request_coins():
    # Quarters, dimes, nickles, pennies
    coin_values = [0.25, 0.10, 0.05, 0.01]
    coin_names = ["quarters", "dimes", "nickles", "pennies"]
    tally = 0
    
    for i in range(len(coin_values)):
        tally += int(input(f">> How many {coin_names[i]}? ")) * coin_values[i]
    
    print((f"+ Your money: ${tally:.2f}"))
    return tally
    

# Parses the user's input
def coffee_machine_loop():
    machine = resources
    
    while(True):    
        user_input = get_prompt().lower()
        if user_input == "off":
            print("+ Turning coffee machine off")
            break
        elif user_input == "report":
            print_report(machine)
            continue
        else:
            coins = request_coins()
            if can_make_brew(machine, user_input, coins):
                print(f"+ Success! Making {user_input}")
                machine = make_brew(machine, user_input, coins)
            else:
                continue

coffee_machine_loop()
