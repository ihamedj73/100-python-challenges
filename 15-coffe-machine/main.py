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

coins = {
    "penny": 0.01,
    "nickles": 0.00,
    "dimes": 0.10,
    "quarter": 0.25,
}


def report_resources():
    print("The current resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources_sufficient(order):
    error_message = "Sorry there is not enough"
    order_ingredients = order['ingredients']
    if order_ingredients['water'] > resources['water']:
        print(f"{error_message} water")
        return False
    elif order_ingredients.get("milk", None) and order_ingredients['milk'] > resources['milk']:
        print(f"{error_message} Milk")
        return False
    elif order_ingredients['coffee'] > resources['coffee']:
        print(f"{error_message} Coffee")
        return False
    else:
        return True


def get_money():
    """Get coins from a person and return inserted money"""
    penny = int(input("How many Penny: "))
    nickles = int(input("How many nickles: "))
    dimes = int(input("How many dimes: "))
    quarter = int(input("How many quarter: "))

    inserted_money = (penny * coins['penny']) + (nickles * coins['nickles']) + (
        dimes * coins['dimes']) + (quarter * coins['quarter'])

    return inserted_money


def make_coffee(order):
    """Generate order and decrease resources"""
    ingredients = order['ingredients']
    resources['coffee'] -= ingredients['coffee']
    resources["water"] -= ingredients['water']

    if ingredients.get("milk", None):
        resources["milk"] -= ingredients['milk']


is_on = True
while is_on:
    order = input(
        "What would you like? (espresso / latte / cappuccino ): ").lower()

    if order == "report":
        report_resources()
    elif order == "off":
        is_on = False
    else:
        ordered_coffee = MENU[order]

        if check_resources_sufficient(ordered_coffee):
            inserted_money = get_money()
            order_cost = ordered_coffee['cost']

            if inserted_money < order_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                make_coffee(ordered_coffee)
                money += order_cost
                report_resources()
                if inserted_money > order_cost:
                    money_to_refund = inserted_money - order_cost
                    print(
                        f"Here is ${round(money_to_refund, 2)} dollars in change")
                print(f"Here is your {order}. Enjoy!”.")
