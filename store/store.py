# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollars)
# in_stock: number

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """
    file_name = 'store/games.csv'
    table = data_manager.get_table_from_file(file_name)

    title = "Store manager menu"
    list_options = ["Show Table", "Add", "Remove", "Update", "Kinds of game of each manufacturer",
                    "Average amount of games in stock by manufacturer"]
    stay_in = True
    while stay_in:
        ui.print_menu(title, list_options, "Back to main menu")
        user_input = input('Choose your option: ')
        if user_input == "1":
            show_table(table)
        elif user_input == "2":
            add(table)
        elif user_input == "3":
            remove(table, id_)
        elif user_input == "4":
            update(table, id_)
        elif user_input == "5":
            get_counts_by_manufacturers(table)
        elif user_input == "6":
            get_average_by_manufacturer(table, manufacturer)
        elif user_input == "0":
            stay_in = False
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    print(table)

    pass


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.
    Args:
        table: table to remove a record from
        id_ (str): id of a record to be removed
    Returns:
        Table without specified record.
    """
    show_table(table)
    choose_id = input('Choose ID to remove: ')
    if idd in [table[n][0] for n in table]:
        print(idd)

    write_table_to_file(file_name, table)

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
