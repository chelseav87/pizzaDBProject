# this is the main file with UI
import database
import time

MENU_PROMPT = """

        --- Coffee Bean App ---

Please choose one of these options:

1) Add a new bean.
2) Find bean by name.
3) See all beans.
4) Search beans by rating.
5) See which preparation method is best for a bean.
6) Delete bean by name.
7) Exit.

Your selection: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_find_bean(connection)
        elif user_input == "3":
            prompt_see_all_beans(connection)
        elif user_input == "4":
            prompt_search_bean_rating(connection)
        elif user_input == "5":
            prompt_find_best_method(connection)
        elif user_input == "6":
            prompt_delete_bean(connection)
        else:
            print("   Invalid input, please try again!")
            time.sleep(1)


def prompt_add_new_bean(connection):
    name = input("\nEnter bean name: ").title()
    if not name:
        print("   Please enter a name!")
        time.sleep(1)
        return
    method = input("Enter how you've prepared it: ").title()
    if not method:
        print("   Please enter a method!")
        time.sleep(1)
        return
    rating = int(input("Enter your rating score (0-10): "))
    if rating < 0 or rating > 10:
        print("   Invalid rating, please try again!")
        time.sleep(1)
        return
    else:
        database.add_bean(connection, name, method, rating)
        print(f"   Added: {name} ({method}) - {rating}/10")
        time.sleep(2)

def prompt_find_bean(connection):
    name = input("Enter bean name to find: ").title()
    beans = database.get_beans_by_name(connection, name)
    if not beans:
        print("   Cannot find bean name!")
        time.sleep(1)
    else:
        for bean in beans:
            print(f"   {bean[1]} ({bean[2]}) - {bean[3]}/10")
        time.sleep(2)


def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)
    if not beans:
        print("   No beans found!")
        time.sleep(1)
    else:
        for bean in beans:
            print(f"   {bean[1]} ({bean[2]}) - {bean[3]}/10")
        time.sleep(2)


def prompt_search_bean_rating(connection):
    min_rating = int(input("Enter minimum range (0-10): "))
    max_rating = int(input("Enter maximum range (0-10): "))
    if min_rating < 0 or max_rating > 10 or min_rating > max_rating:
        print("    Invalid rating range, please try again!")
        time.sleep(1)
        return
    else:
        beans = database.get_beans_by_rating(connection, min_rating, max_rating)
        if not beans:
            print("   No bean ratings within that range!")
            time.sleep(1)
        else:
            for bean in beans:
                print(f"   {bean[1]} ({bean[2]}) - {bean[3]}/10")
            time.sleep(2)


def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ").title()
    try:
        best_method = database.get_best_preparation_for_bean(connection, name)
        print(f"   The best preparation method for {name} is: {best_method[2]}")
        time.sleep(2)
    except TypeError:
        print("   Cannot find bean name!")
        time.sleep(1)


def prompt_delete_bean(connection):
    name = input("Enter bean name to delete: ").title()
    beans = database.get_beans_by_name(connection, name)
    if not beans:
        print("   Cannot find bean name!")
        time.sleep(1)
    else:
        for bean in beans:
            print(f"   ID {bean[0]}: {bean[1]} ({bean[2]}) - {bean[3]}/10")
        try:
            ID = int(input("\nEnter the ID of the bean you want to delete: "))
            valid_ID = [bean[0] for bean in beans]
            if ID not in valid_ID:
                print("   Invalid ID, please try again!")
                time.sleep(1)
            else:
                database.get_delete_bean(connection, name, ID)
                print(f"   ID {ID}: {name} deleted.")
                time.sleep(2)
        except ValueError:
            print("   Invalid ID, please try again!")
            time.sleep(1)


menu()
