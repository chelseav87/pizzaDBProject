# this is the main file with UI
import database
import time

MENU_PROMPT = """

        --- Pizza App ---

Please choose one of these options:

1) Add a new pizza.
2) Find pizza by style.
3) See all pizzas.
4) Search pizzas by rating.
5) See which toppings are best for a style of pizza.
6) Delete pizza by style.
7) Exit.

Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            prompt_add_new_pizza(connection)
        elif user_input == "2":
            prompt_find_pizza(connection)
        elif user_input == "3":
            prompt_see_all_pizzas(connection)
        elif user_input == "4":
            prompt_search_pizza_rating(connection)
        elif user_input == "5":
            prompt_find_best_toppings(connection)
        elif user_input == "6":
            prompt_delete_pizza(connection)
        else:
            print("   Invalid input, please try again!")
            time.sleep(1)


def prompt_add_new_pizza(connection):
    style = input("\nEnter pizza style: ").title()
    if not style:
        print("   Please enter a style!")
        time.sleep(1)
        return
    toppings = input("Enter the topping(s): ").title()
    if not toppings:
        print("   Please enter some toppings!")
        time.sleep(1)
        return
    rating = int(input("Enter your rating score (0-10): "))
    if rating < 0 or rating > 10:
        print("   Invalid rating, please try again!")
        time.sleep(1)
        return
    else:
        database.add_pizza(connection, style, toppings, rating)
        print(f"   Added: {style} ({toppings}) - {rating}/10")
        time.sleep(2)

def prompt_find_pizza(connection):
    style = input("Enter pizza style to find: ").title()
    pizzas = database.get_pizzas_by_style(connection, style)
    if not pizzas:
        print("   Cannot find pizza style!")
        time.sleep(1)
    else:
        for pizza in pizzas:
            print(f"   {pizza[1]} ({pizza[2]}) - {pizza[3]}/10")
        time.sleep(2)


def prompt_see_all_pizzas(connection):
    pizzas = database.get_all_pizzas(connection)
    if not pizzas:
        print("   No pizzas found!")
        time.sleep(1)
    else:
        for pizza in pizzas:
            print(f"   {pizza[1]} ({pizza[2]}) - {pizza[3]}/10")
        time.sleep(2)


def prompt_search_pizza_rating(connection):
    min_rating = int(input("Enter minimum range (0-10): "))
    max_rating = int(input("Enter maximum range (0-10): "))
    if min_rating < 0 or max_rating > 10 or min_rating > max_rating:
        print("    Invalid rating range, please try again!")
        time.sleep(1)
        return
    else:
        pizzas = database.get_pizzas_by_rating(connection, min_rating, max_rating)
        if not pizzas:
            print("   No pizza ratings within that range!")
            time.sleep(1)
        else:
            for pizza in pizzas:
                print(f"   {pizza[1]} ({pizza[2]}) - {pizza[3]}/10")
            time.sleep(2)


def prompt_find_best_toppings(connection):
    style = input("Enter pizza style to find: ").title()
    try:
        best_toppings = database.get_best_toppings_for_pizza(connection, style)
        print(f"   The best toppings for {style} is: {best_toppings[2]}")
        time.sleep(2)
    except TypeError:
        print("   Cannot find pizza style!")
        time.sleep(1)


def prompt_delete_pizza(connection):
    style = input("Enter pizza style to delete: ").title()
    pizzas = database.get_pizzas_by_style(connection, style)
    if not pizzas:
        print("   Cannot find pizza style!")
        time.sleep(1)
    else:
        for pizza in pizzas:
            print(f"   ID {pizza[0]}: {pizza[1]} ({pizza[2]}) - {pizza[3]}/10")
        try:
            ID = int(input("\nEnter the ID of the pizza you want to delete: "))
            valid_ID = [pizza[0] for pizza in pizzas]
            if ID not in valid_ID:
                print("   Invalid ID, please try again!")
                time.sleep(1)
            else:
                database.get_delete_pizza(connection, style, ID)
                print(f"   ID {ID}: {style} deleted.")
                time.sleep(2)
        except ValueError:
            print("   Invalid ID, please try again!")
            time.sleep(1)


menu()
