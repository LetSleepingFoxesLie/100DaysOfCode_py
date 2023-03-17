from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    
    while True:
        order = input(f"Which drink will you want? ({menu.get_items()}): ")
        
        if order == "off":
            print(f"[Log] Turning machine off...")
            break
        elif order == "report":
            coffee_machine.report()
            money_machine.report()
            continue
        else:
            brew = menu.find_drink(order)

            if brew is None:
                continue
            
            if coffee_machine.is_resource_sufficient(brew): # I would have put an "and" statement...
                if money_machine.make_payment(brew.cost): # but doing it like this wastes less time
                    coffee_machine.make_coffee(brew)    # as you won't ask for payment if you can't make the drink
        
main()