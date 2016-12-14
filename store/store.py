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
    """ Starts this module and displays its menu. User can access default special
    features from here. User can go back to main menu from here. Returns: None """

    file_name = 'store/games.csv'
    table = data_manager.get_table_from_file(file_name)

    title = "Store manager menu"
    list_options = ["Show Table", "Add", "Remove", "Update", "Kinds of game of each manufacturer",
                    "Average amount of games in stock by manufacturer"]
    stay_in = True

    while stay_in:
        print('Kupa')
        ui.print_menu(title, list_options, "Back to main menu")
        user_input = ui.get_inputs(["of module"], 'Choose number')[0]

        if user_input == "1":  # show_table
            print('Kuuuuupa')
            show_table(table)
        elif user_input == "2":  # add
            add(table)
        elif user_input == "3":  # remove
            show_table(table)
            choose_id = ui.get_inputs(["ID: "], 'Choose ID to remove')
            remove(table, choose_id)
        elif user_input == "4":  # update
            show_table(table)
            id_ = ui.get_inputs(["ID: "], 'Choose Id to change')[0]
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
    """ Display a table. Args: table: list of lists to be displayed.
    Returns: None """
    print('Duuuupaaa')
    header = ['Id', 'Title', 'Manufacturer', 'Price', 'In stock']
    ui.print_table(table, header)


def add(table):
    """ Asks user for input and adds it into the table. Args: table:
    table to add new record to. Returns: Table with a new record"""

    header = ['Title', 'Manufacturer', 'Price', 'In stock']
    new_line = [common.generate_random(table)] + ui.get_inputs(header, "Add your data: ")
    table.append(new_line)
    file_name = 'store/games.csv'
    data_manager.write_table_to_file(file_name, table)

    return table


def remove(table, id_):
    """Remove a record with a given id from the table. Args: table: table to
    remove a record from id_ (str): id of a record to be removed. Returns:
    Table without specified record. """

    show_table(table)
    for n in table:
        if id_[0] in n:
            table.remove(n)
    file_name = 'store/games.csv'
    data_manager.write_table_to_file(file_name, table)
    return table


def update(table, id_):
    """Updates specified record in the table. Ask users for new data. Args:
    table: list in which record should be updated, id_ (str): id of a record
    to update. Returns: table with updated record."""

    #  line_to_update = [line for line in table if line[0] == id_][0]
    file_name = 'store/games.csv'

    for n, line in enumerate(table):
        if line[0] == id_:
            line_to_update = line
            line_index = n
            break
    change = True

    while change:
        data = ui.get_inputs(["To update: "],
                             'Choose data to update: 1-Title, 2-Manufacturer, 3-Price, 4-In stock, 0-End of edditing')
        if data[0] in ["1", '2', '3', '4']:
            line_to_update[int(data[0])] = ui.get_inputs(["New data"],'')[0]
            table[line_index] = line_to_update

            data_manager.write_table_to_file(file_name, table)
        elif data[0] == "0":
            return table
        else:
            raise KeyError("There is no such data.")
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    label = ['Manufacturer', 'Amount of games']
    manufacturer_games = {}
    for game in table:
        if game[2] in list(manufacturer_games.keys()):
            manufacturer_games[game[2]] += 1
        else:
            manufacturer_games[game[2]] = 1
    ui.print_result(manufacturer_games, label)
    return manufacturer_games


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
