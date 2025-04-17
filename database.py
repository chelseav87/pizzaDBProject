import sqlite3

CREATE_PIZZA_TABLE = "CREATE TABLE IF NOT EXISTS pizza (ID INTEGER PRIMARY KEY, Style TEXT, Toppings TEXT, Rating INTEGER);"

INSERT_PIZZA = "INSERT INTO pizza (style, toppings, rating) VALUES (?, ?, ?);"
GET_PIZZAS_BY_STYLE = "SELECT * FROM pizza WHERE style = ?;"
GET_ALL_PIZZAS = "SELECT * FROM pizza;"
GET_PIZZAS_BY_RATING = "SELECT * FROM pizza WHERE rating BETWEEN ? AND ?;"
GET_BEST_TOPPINGS_FOR_PIZZA = """
SELECT * FROM pizza
WHERE style = ?
ORDER by rating DESC
LIMIT 1;"""
GET_DELETE_PIZZA = "DELETE FROM pizza WHERE style = ? AND ID = ?;"


def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_PIZZA_TABLE)


def add_pizza(connection, style, toppings, rating):
    with connection:
        connection.execute(INSERT_PIZZA, (style, toppings, rating))


def get_pizzas_by_style(connection, style):
    with connection:
        return connection.execute(GET_PIZZAS_BY_STYLE, (style,)).fetchall()


def get_all_pizzas(connection):
    with connection:
        return connection.execute(GET_ALL_PIZZAS).fetchall()


def get_pizzas_by_rating(connection, min_rating, max_rating):
    with connection:
        return connection.execute(GET_PIZZAS_BY_RATING, (min_rating, max_rating,)).fetchall()


def get_best_toppings_for_pizza(connection, style):
    with connection:
        return connection.execute(GET_BEST_TOPPINGS_FOR_PIZZA, (style,)).fetchone()


def get_delete_pizza(connection, style, ID):
    with connection:
        connection.execute(GET_DELETE_PIZZA, (style, ID))
