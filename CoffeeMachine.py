MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

money = 0


def resource_checker(choice: str, items=resources) -> bool:
    string = "Money refunded."
    if MENU[choice]['ingredients']['water'] > items['water']:
        print("Not enough water in the machine. " + string)
        return False
    elif choice != 'espresso' and \
            MENU[choice]['ingredients']['milk'] > items['milk']:
        print("Not enough milk in the machine. " + string)
        return False
    elif MENU[choice]['ingredients']['coffee'] > items['coffee']:
        print("Not enough coffee in the machine. " + string)
        return False
    return True


def resource_remover(choice: str):
    resources['water'] -= MENU[choice]['ingredients']['water']
    if choice != 'espresso':
        resources['milk'] -= MENU[choice]['ingredients']['milk']
    resources['coffee'] -= MENU[choice]['ingredients']['coffee']


def choice_checker_admin(choice: str) -> bool:
    if choice == 'report':
        for key, value in resources.items():
            print(f"{key} : {value}".title())
        print(f"money: {money}".title())
        return False
    elif choice == 'off':
        return True


def choice_checker_items(choice: str) -> bool:
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if resource_checker(choice):
            resource_remover(choice)
            return True
    return False


def coin_counter() -> float:
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return_value = quarters + dimes + nickles + pennies
    return return_value


end = False
while not end:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice != 'report' and choice != 'off':
        print("Please insert coins.")
        total = coin_counter()
        if total < MENU[choice]['cost']:
            print("Sorry, that's not enough money. Money refunded.")
        elif choice_checker_items(choice):
            money += MENU[choice]['cost']
            change = round(total - MENU[choice]['cost'], 2)
            if change != 0:
                print(f"Here is your ${change} change.")
            print(f"Enjoy your {choice}")
    else:
        end = choice_checker_admin(choice)
