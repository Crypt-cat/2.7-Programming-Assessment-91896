import os, time, sys, random

os.system("clear")

user_money = 0
star_rating = 0
MAX_RATING = 5
MONEY_BOOST = 1.5
BREWSTER_BURGER = 25
PROFIT_MULTIPLIER = 100
money_upgrade = False

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
        user_input = get_int("Welcome to Brewster's Burgers!\n\n1. Take an order\n2. Show ingredients list\n3. Upgrades and money\n4. Show star rating\n5. Exit\n\n> ")
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
        show_rating()
    elif user_input == 5:
        exit()


def ingredients_list():
    """This function shows the user the ingredients needed for specific burgers. It lays it out in a way that is easy to understand."""
    print(f"Memorise the burger's ingredients to earn money from your orders!\n\n| {'Burger Type:':16s}| Ingredients:\n|-----------------|-----------------------------------------------------------------------------------")
    for burger in current_burgers:
        print(f"| {burger.burger_type:16s}| {burger.ingredients}\n|-----------------|-----------------------------------------------------------------------------------")
    print("\n")


def show_rating():
    """This function allows the user to see their star rating. It will tell them a message depending on what it is and this is useful to check for the requirement for the Brewster Burger."""
    reveal_text("Searching through reviews...")
    time.sleep(2)
    os.system("clear")
    print(f"Your restaurant has a star rating of {star_rating} out of 5 on Google.\nTake customer orders correctly to improve your rating (unless it's at 5).\nRemember that getting an order wrong will hurt your rating!")
    if star_rating < 3:
        print("\nYou might have to step up your game...")
    elif star_rating == 3:
        print("\nYou're doing okay.")
    else:
        print("\nYou're doing a great job at running this place!")
    print("\n")


def upgrades():
    """This function allows the user to access upgrades where the user can unlock the new Brewster Burger or multiply their overall profit. It tell them how much money they need and if they already have it
    The Brewster Burger also has a star rating requirement, which depends on how well the user takes orders. It also shows you how much money you have and a message depending on that"""
    global user_money
    global money_upgrade
    reveal_text("Counting up money...")
    time.sleep(2)
    os.system("clear")
    if user_money <= 30:
        print("\nYou might need to go make some more money...")
    elif user_money < 100:
        print("\nThat's not bad.")
    else:
        print("\nYou're rich!")
    while True:
        user_input = get_int(f"You currently have {user_money} dollars.\n\n1. Unlock Brewster Burger (${BREWSTER_BURGER}) \n2. Overall 1.5x profit multiplier (${PROFIT_MULTIPLIER})\n3. Go Back\n\n> ")
        if not user_input in [1, 2, 3]:
            print("Invalid option.")
            time.sleep(2)
            os.system("clear")
            continue
        else:
            break
    if user_input == 1:
        if len(current_burgers) == 7:
            print("You've already bought this.")
        elif star_rating < MAX_RATING:
            print(f"Sorry, you need a star rating of {MAX_RATING} out of 5 to unlock this.")
        elif user_money < BREWSTER_BURGER:
            print(f"You don't have enough money for this, you need {BREWSTER_BURGER - user_money} more dollars.")
        else:
            print("Successfully bought.")
            user_money = user_money - 25
            current_burgers.append(brewster_burger)
    elif user_input == 2:
        if money_upgrade == True:
            print("You've already bought this.")
        elif user_money < PROFIT_MULTIPLIER:
            print(f"You don't have enough money for this, you need {PROFIT_MULTIPLIER - user_money} more dollars.")
        else:
            print("Successfully bought.")
            user_money = user_money - 100
            money_upgrade = True
    else:
        menu()
    print("\n")


def take_order():
    """This function allows the user to take orders from customers and make money. This money allows them to buy upgrades. You also gain star rating depending on how you do.
    The program will tell you if you got their order right or not."""
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
        if money_upgrade == True:
            user_money = user_money + (customer_order.price*MONEY_BOOST)
        else:
            user_money = user_money + customer_order.price
        if star_rating < MAX_RATING:
            star_rating = star_rating + 1
    else:
        reveal_text("This isn't what I ordered!")
        time.sleep(3)
        os.system("clear")
        if star_rating > 0:
            star_rating = star_rating - 1


while True:
    menu()
