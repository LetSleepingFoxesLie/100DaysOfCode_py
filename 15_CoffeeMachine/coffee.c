#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Brew{
    int water;
    int milk;
    int coffee;

    float cost;
} Brew;

typedef struct Machine{
    int water;
    int milk;
    int coffee;

    float money;
} Machine;

char* get_input(){
    // Shortcut because I can't be arsed
    char command[31];

    printf("What would you like? (espresso, latte, or cappuccino): ");
    scanf("%s", command);

    char *this_sucks = (char*) malloc (strlen(command) * (sizeof(char)));
    strcpy(this_sucks, command);
    
    return this_sucks;
}

Machine* initialize_machine(){
    Machine *machine = malloc (sizeof(Machine));

    machine->water = 300;
    machine->milk = 200;
    machine->coffee = 100;
    machine->money = 0.0;

    return machine;
}

void print_machine_report(Machine machine){
    printf("MACHINE REPORT!\n");
    printf("- Water: %dml\n", machine.water);
    printf("- Milk: %dml\n", machine.milk);
    printf("- Coffee: %dml\n", machine.coffee);
    printf("- Money: $%.2f\n", machine.money);
}

int can_make_brew(Machine machine, Brew brew){
    int has_resources = 1;

    if(machine.water < brew.water){
        printf("> Sorry, there is not enough water\n");
        has_resources = 0;
    }

    if(machine.milk < brew.milk){
        printf("> Sorry, there is not enough milk\n");
        has_resources = 0;
    }

    if(machine.coffee < brew.coffee){
        printf("> Sorry, there is not enough coffee\n");
        has_resources = 0;
    }

    return has_resources;
}

Machine* brew_drink(Machine* machine, Brew brew, float money, char* brew_name){
    machine->water -= brew.water;
    machine->milk -= brew.milk;
    machine->coffee -= brew.coffee;

    if(money > brew.cost){
        float change = money - brew.cost;
        printf("+ Here's $%.2f in change!\n", change);
    }

    printf("+ Here's your freshly brewed %s, enjoy!\n", brew_name);
    machine->money += brew.cost;
    return machine;
}

float request_coins(){
    float coin_values[4] = {0.25, 0.10, 0.05, 0.01};
    char coin_names[4][10] = {
        "quarters",
        "dimes",
        "nickels",
        "pennies"
    };

    float tally = 0.0;

    for(int i = 0; i < 4; i++){
        int number;
        printf(">> How many %s? ", coin_names[i]);
        scanf("%d", &number);

        printf("%d\n", number);
        tally += (float) number * coin_values[i];
    }

    printf("\n>> Your money: %.2f\n", tally);
    return tally;
}

int main(){
    Machine *machine = initialize_machine();
    Brew espresso;
    espresso.water = 50;
    espresso.milk = 0;
    espresso.coffee = 0;
    espresso.cost = 1.5;

    Brew latte;
    latte.water = 200;
    latte.milk = 150;
    latte.coffee = 24;
    latte.cost = 2.5;

    Brew cappuccino;
    cappuccino.water = 250;
    cappuccino.milk = 100;
    cappuccino.coffee = 24;
    cappuccino.cost = 3.0;


    while(1){
        char *user_input = get_input();
        
        if(strcmp(user_input, "off") == 0){
            printf("- Turning coffee machine off...\n");
            break;
        } else if(strcmp(user_input, "report") == 0){
            print_machine_report(*machine);
        } else {
            // Espresso
            if(strcmp(user_input, "espresso") == 0){
                if(can_make_brew(*machine, espresso)){
                    float pay = request_coins();

                    if(pay < espresso.cost){
                        printf("- Sorry, you are very pobre, and you can't afford %.2f for a(n) %s\n", espresso.cost, user_input);
                        continue;
                    }

                    brew_drink(machine, espresso, pay, user_input);
                }
            }

            // Latte
            if(strcmp(user_input, "latte") == 0){
                if(can_make_brew(*machine, latte)){
                    float pay = request_coins();

                    if(pay < latte.cost){
                        printf("- Sorry, you are very pobre, and you can't afford %.2f for a(n) %s\n", latte.cost, user_input);
                        continue;
                    }

                    brew_drink(machine, latte, pay, user_input);
                }
            }

            // Cappuccino
            if(strcmp(user_input, "cappuccino") == 0){
                if(can_make_brew(*machine, cappuccino)){
                    float pay = request_coins();

                    if(pay < cappuccino.cost){
                        printf("- Sorry, you are very pobre, and you can't afford %.2f for a(n) %s\n", cappuccino.cost, user_input);
                        continue;
                    }

                    brew_drink(machine, cappuccino, pay, user_input);
                }
            }            
        }
    }
    return 0;
}