# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'),
#     2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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

    sales_options = ["Show Table","Add","Remove","Update","Get oldest person","Get persons closest to average"]
    keep_menu = True
    while keep_menu:
        ui.print_menu('Sales Main Menu',sales_options,'Back To Menu')
        try:
            keep_menu = choose_hr()
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

    inputs = ui.get_inputs(["\n1. ID (Unique and random generated (at least 2 special char()\
 expect: ';'), 2 number, 2 lower and 2 upper case letter))", "Name", "Birth date"], "\nPlease add a worker.")

    one_input = inputs[0], inputs[1], inputs[2]
    one_input_list = list(one_input) # we must do it
    table = data_manager.get_table_from_file('hr/persons.csv')
    table.append(one_input_list)
    data_manager.write_table_to_file('hr/persons.csv', table)
    print("\n Added. \n \n")
    #print(table)

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

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass

def choose_hr():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    data = data_manager.get_table_from_file('hr/persons.csv')
    if option == "1":
        show_table(data)
        return True
    elif option == "2":
        add(data_manager.get_table_from_file('hr/persons.csv'))
        return True
    elif option == "4":
        update(data,ui.get_inputs(["Please enter ID"],"Pick the ID to update"))
        return True
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
