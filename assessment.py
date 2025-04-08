import os, time, sys

os.system("clear")


class Burger:
    """Represents a burger."""
    def __init__(self, burger_type, ingredients, price):
        """Initialise burger with given arguemnts."""
        self.burger_type = burger_type
        self.ingredients = ingredients
        self.price = price


"""Each burger has a list of ingredients, the order of ingredients in the list is [Beef Patty, Chicken Patty, Veggie Patty, Bacon, Cheese, Lettuce, Tomato, Onion, Ketchup, Aioli, Brewster Sauce]
yes/no represents if the ingredient is required for that specific burger or not.
"""
cheeseburger = Burger("Cheeseburger", ["yes", "no", "no", "no", "yes", "no", "no", "yes", "yes", "no", "no"], 7)
bacon_burger = Burger("Bacon Burger", ["yes", "no", "no", "yes", "no", "no", "no", "yes", "yes", "no", "no"], 9)
chicken_burger = Burger("Chicken Burger", ["no", "yes", "no", "no", "no", "yes", "no", "no", "no", "yes", "no"], 8)
veggie_burger = Burger("Veggie Burger", ["no", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes","no"], 10)
classic_burger = Burger("Classic Burger", ["yes", "no", "no", "no", "yes", "yes", "yes", "yes", "yes", "no", "no"], 11)
blt_burger = Burger("BLT Burger", ["no", "no", "no", "yes", "no", "yes", "yes", "no", "no", "yes", "no"], 8.5)
brewster_burger = Burger("Brewster Burger", ["yes", "no", "no", "yes", "yes", "yes", "yes", "yes", "yes", "no", "yes"], 13.5)
all_burgers = [cheeseburger, bacon_burger, chicken_burger, veggie_burger, classic_burger, blt_burger, brewster_burger]


def reveal_text(range):
    """"""
    for c in range:
        sys.stdout.write(c)
        time.sleep(0.10)
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
        temp_ingredient = get_int("1. Yes\n2. No\n\n> ")
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
        user_input = get_int("\n\nWelcome to Brewster's Burgers:\n\n1. Take an order\n2. Show ingredients list\n3. Upgrades\n4. Evaluate star rating\n5. Exit\n\n> ")
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
    print(f"Memorise the burger's ingredients to earn money from your orders!\n\n| {'Burger Type':16s}| B. Patty | C. Patty | V. Patty | Bacon | Cheese | Lettuce | Tomato | Onion | Ketchup | Aioli | Brewster Sauce |\n|-----------------|----------|----------|----------|-------|--------|---------|--------|-------|---------|-------|----------------|")
    for burger in all_burgers:
        print(f"| {burger.burger_type:16s}| {burger.ingredients[0]:8s} | {burger.ingredients[1]:8s} | {burger.ingredients[2]:8s} | {burger.ingredients[3]:5s} | {burger.ingredients[4]:6s} | {burger.ingredients[5]:7s} | {burger.ingredients[6]:6s} | {burger.ingredients[7]:5s} | {burger.ingredients[8]:7s} | {burger.ingredients[9]:5s} | {burger.ingredients[10]:15s}|\n|-----------------|----------|----------|----------|-------|--------|---------|--------|-------|---------|-------|----------------|")


while True:
    menu()
    