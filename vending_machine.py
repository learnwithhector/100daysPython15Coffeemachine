import sys
import time

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


def get_integer(prompt):
    while True:
        number = input(prompt)
        if number.isnumeric():
            return int(number)


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


def sufficient_resources(drink):
    if drink == "e" or drink == "espresso":
        if resources["water"] < 50:
            print("Sorry, there is not enough water")
        if resources["coffee"] < 18:
            print("Sorry, there is not enough coffee")
        return resources["water"] >= 50 and resources["coffee"] >= 18
    elif drink == "l" or drink == "latte":
        if resources["water"] < 200:
            print("Sorry, there is not enough water")
        if resources["milk"] < 150:
            print("Sorry, there is not enough milk")
        if resources["coffee"] < 24:
            print("Sorry, there is not enough coffee")
        return resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24
    else:
        if resources["water"] < 250:
            print("Sorry, there is not enough water")
        if resources["milk"] < 100:
            print("Sorry, there is not enough milk")
        if resources["coffee"] < 24:
            print("Sorry, there is not enough coffee")
        return resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24


def process_coins(price):
    money = 0
    num_quarters = get_integer("How many quarters? ")
    num_dimes = get_integer("How many dimes? ")
    num_nickels = get_integer("How many nickels? ")
    num_pennies = get_integer("How many pennies? ")

    money = (num_quarters * 0.25) + (num_dimes * 0.1) + (num_nickels * 0.05) + (num_pennies * 0.01)
    if money == price:
        print("Exact money. Thank you")
        return True
    elif money > price:
        change = money - price
        print(f"You have given me ${money:.2f}. Your drink costs ${price:.2f} Here is your ${change:.2f} change.")
        return True
    else:
        print(f"You have given me ${money:.2f} but the drink costs ${price:.2f}. Money refunded")
        return False


def make_drink(drink):
    print(f"Here is your {drink} ☕. Please enjoy")
    if drink == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


valid_choices = ["e", "espresso", "l", "latte", "c", "cappuccino", "off" "report"]

while True:
    order = ""
    while order not in valid_choices:
        order = input("What would you like? ").casefold()
        if order == "off":
            print("Powering off...")
            sys.exit()
        elif order == "report":
            print_resources()
        elif order == "e" or order == "espresso" or order == "l" or order == "latte" or order == "c" or order == "cappuccino":
            can_make = sufficient_resources(order)
            if can_make:
                print("We can make this")
                if order == "e" or order == "espresso":
                    order = "espresso"
                    cost = MENU["espresso"]["cost"]
                elif order == "l" or order == "latte":
                    order = "latte"
                    cost = MENU["latte"]["cost"]
                else:
                    order = "cappuccino"
                    cost = MENU["cappuccino"]["cost"]
                print(f"This drink costs ${MENU[order]['cost']:.2f}")
                successful_purchase = process_coins(cost)
                if successful_purchase:
                    print(f"making {order}...")
                    time.sleep(2)
                    make_drink(order)

            else:
                print("The machine does not have the resources")
