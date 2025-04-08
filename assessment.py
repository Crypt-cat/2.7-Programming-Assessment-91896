import os, time, sys, random

os.system("clear")

user_money = 0
star_rating = 0


class Burger:
    """Represents a burger."""
    def __init__(self, burger_type, ingredients, price):
        """Initialise burger with given arguemnts."""
        self.burger_type = burger_type
        self.ingredients = ingredients
        self.price = price


"""Each burger has a list of ingredients, the order of ingredients in the list is [Beef Patty, Chicken Patty, Veggie Patty, Bacon, Cheese, Lettuce, Tomato, Onion, Ketchup, Aioli, Brewster Sauce]
if the ingredient is present in the list, it means it's part of its recipe. If the ingredient is not there, it is not needed.
"""
cheeseburger = Burger("Cheeseburger", ["Beef Patty", "Cheese", "Onion", "Ketchup"], 7)
bacon_burger = Burger("Bacon Burger", ["Beef Patty", "Bacon", "Onion", "Ketchup"], 9)
chicken_burger = Burger("Chicken Burger", ["Chicken Patty", "Lettuce", "Aioli"], 8)
veggie_burger = Burger("Veggie Burger", ["Veggie Patty", "Lettuce", "Tomato", "Aioli"], 10)
classic_burger = Burger("Classic Burger", ["Beef Patty", "Cheese", "Lettuce", "Tomato", "Onion", "Ketchup"], 11)
blt_burger = Burger("BLT Burger", ["Bacon", "Lettuce", "Tomato", "Aioli"], 8.5)
brewster_burger = Burger("Brewster Burger", ["Beef Patty", "Bacon", "Cheese", "Lettuce", "Tomato", "Onion", "Brewster Sauce"], 13.5)
current_burgers = [cheeseburger, bacon_burger, chicken_burger, veggie_burger, classic_burger, blt_burger]


def reveal_text(range):
    """"""
    for c in range:
        sys.stdout.write(c)
        time.sleep(0.06)
        sys.stdout.flush()


def get_int(question):
    while True:
        try:
            temp_int = int(input(question))
            os.system("clear")
            return temp_int
        except ValueError:
            os.system("clear")
            print("Invalid input.")
            time.sleep(2)
            os.system("clear")


def get_ingredient(question):
    while True:
        temp_ingredient = get_int(f"{question}\n\n1. Yes\n2. No\n\n> ")
        os.system("clear")
        if not temp_ingredient in [1, 2]:
            print("Invalid input.")
            time.sleep(2)
            os.system("clear")
            continue
        else:
            return temp_ingredient


def menu():
    while True:
        user_input = get_int("Welcome to Brewster's Burgers!\n\n1. Take an order\n2. Show ingredients list\n3. Upgrades\n4. Evaluate star rating\n5. Exit\n\n> ")
        if not user_input in [1, 2, 3, 4, 5]:
            print("Invalid option.")
            time.sleep(2)
            os.system("clear")
            continue
        else:
            break
    if user_input == 1:
        take_order()
    elif user_input == 2:
        ingredients_list()
    elif user_input == 3:
        upgrades()
    elif user_input == 4:
        star_rating()
    elif user_input == 5:
        exit()


def ingredients_list():
    print(f"Memorise the burger's ingredients to earn money from your orders!\n\n| {'Burger Type:':16s}| Ingredients:\n|-----------------|-----------------------------------------------------------------------------------")
    for burger in current_burgers:
        print(f"| {burger.burger_type:16s}| {burger.ingredients}\n|-----------------|-----------------------------------------------------------------------------------")
    print("\n")


def take_order():
    global user_money
    global star_rating
    customer_order = random.choice(current_burgers)
    correct_ingredients = customer_order.ingredients
    reveal_text(f"Hi, could I please get the {customer_order.burger_type}?")
    time.sleep(3)
    os.system("clear")
    ingredients = ["Beef Patty", "Chicken Patty", "Veggie Patty", "Bacon", "Cheese", "Lettuce", "Tomato", "Onion", "Ketchup", "Aioli", "Brewster Sauce"]
    user_order = []
    for ing in ingredients:
        temp_ingredient = get_ingredient(f"Does the {customer_order.burger_type} use {ing} in it?")
        if temp_ingredient == 1:
            user_order.append(ing)
    if correct_ingredients == user_order:
        reveal_text("Thank you for getting my order correct!")
        time.sleep(3)
        os.system("clear")
        user_money = user_money + customer_order.price
        if star_rating < 5:
            star_rating = star_rating + 1
    else:
        reveal_text("This isn't what I ordered!")
        time.sleep(3)
        os.system("clear")
        if star_rating > 0:
            star_rating = star_rating - 1

while True:
    print(star_rating)
    print(user_money)
    menu()
    