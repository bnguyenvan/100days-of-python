from menu import MENU, resources
from coffee import coffee_icon
money = 0


# TODO: print report of resources if user type report
def print_resource(resource):
    """Print water, milk, coffee and money left in machine"""
    for i in resource:
        print(f"{i}: {resource[i]}")
    print(f"Money: : {money}")


# TODO: Check if resource is sufficient with the coffee type that user chose
def check_enough_resource(coffee, resource):
    coffee_require = coffee["ingredients"]
    for j in coffee_require:
        if coffee_require[j] > resource[j]:
            return False
    return True


def insert_coins():
    print("Please insert coins.")
    quarters_coins = 0.25 * int(input("how many quarters?: "))
    dimes_coins = 0.1 * int(input("how many dimes?: "))
    nickles_coins = 0.05 * int(input("how many nickles?: "))
    pennies_coins = 0.01 * int(input("how many pennies?: "))
    total_coins = quarters_coins + dimes_coins + nickles_coins + pennies_coins
    return total_coins


# TODO: Check transaction successful
def transaction_check(money_input, cost):
    change = round(money_input - cost, 2)
    if change < 0:
        print(f"Sorry that's not enough money. Money refunded.")
        return False
    elif change > 0:
        print(f"Here is ${change} in change.")
        return True
    else:
        return True


# TODO: Make Coffee
def make_coffee(coffee):
    coffee_ingredient = coffee['ingredients']
    for i in coffee_ingredient:
        resources[i] -= coffee_ingredient[i]


machine_on = True


# TODO: Repeat the process
while machine_on:
    # TODO: ask user choose coffee type
    # print("Here is our Menu:")
    # for i in MENU:
    #     print(f"{i}: ${MENU[i]['cost']}")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print_resource(resources)
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        # TODO: Ask user insert coins if there are sufficient resources
        coffee_type = MENU[user_choice]
        if check_enough_resource(coffee_type, resources):
            total_money = insert_coins()
            if transaction_check(total_money, coffee_type["cost"]):
                make_coffee(coffee_type)
                money += coffee_type["cost"]
                print(f"here is your {user_choice} {coffee_icon}. Enjoy!")
    else:
        print("We only serve: espresso/latte/cappuccino. Please make a right choice.")
