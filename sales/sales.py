# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made

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

    # your code
    sales_options = ["Show Table","Add","Remove","Update","Lowest Price Item ID","Items Sorted Between Date"]
    keep_menu = True
    while keep_menu:
        ui.print_menu('Sales Main Menu',sales_options,'Back To Menu')
        try:
            keep_menu = choose_sale()
        except KeyError as err:
            ui.print_error_message(err)



def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

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

    # your code

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
    for index,elements in enumerate(table):
        if elements[0] in id_:
            table[index] = ui.get_inputs(elements,'Please Speciy Data for this elements: ')
            break

    return table
# My Functions

def choose_sale():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    data = data_manager.get_table_from_file('sales/sales.csv')
    if option == "1":
        show_table(data)
        return True
    elif option == "4":
        update(data,ui.get_inputs(["Please enter ID"],"Pick the ID to update"))
        return True
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")



# data = data_manager.get_table_from_file('sales.csv')
#
#
# print(data)


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):

    # your code

    pass


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):

    # your code

    pass

