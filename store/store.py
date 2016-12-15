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
        ui.print_menu(title, list_options, "Back to main menu")
        user_input = ui.get_inputs(["of action"], 'Choose number')[0]

        if user_input == "1":  # show_table
            show_table(table)
        elif user_input == "2":  # add
            add(table)
        elif user_input == "3":  # remove
            show_table(table)
            choose_id = ui.get_inputs(["ID: "], 'Choose ID to remove or 0 to exit')
            remove(table, choose_id)
        elif user_input == "4":  # update
            show_table(table)
            id_ = ui.get_inputs(["ID: "], 'Choose Id to change')[0]
            update(table, id_)
        elif user_input == "5":
            get_counts_by_manufacturers(table)
        elif user_input == "6":
            common.list_to_choose(table, 2, "Manufacturers you can choose from:")
            manufacturer = ui.get_inputs(["manufacturer"], 'Choose your')[0]
            get_average_by_manufacturer(table, manufacturer)
        elif user_input == "0":
            stay_in = False
        else:
            ui.print_error_message("There is no such option.")


def show_table(table):
    """ Display a table. Args: table: list of lists to be displayed.
    Returns: None """
    header = ['Id', 'Title', 'Manufacturer', 'Price', 'In stock']
    ui.print_table(table, header)


def add(table):
    """ Asks user for input and adds it into the table. Args: table:
    table to add new record to. Returns: Table with a new record"""

    header = ['Title', 'Manufacturer']
    new_line = [common.generate_random(table)] + ui.get_inputs(header, "Add your data: ")

    for data in ['Price', 'In stock']:
        check = True
        while check:
            date_to_check = ui.get_inputs([data], "Add your data: ")
            check = foolproofnes(date_to_check)
        new_line += date_to_check

    table.append(new_line)
    file_name = 'store/games.csv'
    data_manager.write_table_to_file(file_name, table)

    return table


def foolproofnes(values_to_check):
    """ Ckeks if given values are numbers"""
    try:
        b = 2/int(values_to_check[-1])
        if b > 0:
            return False
        else:
            ui.print_error_message("Data must be a number >0: ")
    except:
        ui.print_error_message("Data must be a number >0: ")
        return True

    return True


def remove(table, id_):
    """Remove a record with a given id from the table. Args: table: table to
    remove a record from id_ (str): id of a record to be removed. Returns:
    Table without specified record. """

    show_table(table)

    for n in table:
        if id_[0] in n:
            table.remove(n)
            return table
        elif id_[0] == '0':
            return table
    else:
         ui.print_error_message("No such ID")


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
        if data[0] in ["1", '2']:
            line_to_update[int(data[0])] = ui.get_inputs(["New data"], '')[0]
            table[line_index] = line_to_update
            data_manager.write_table_to_file(file_name, table)
        elif data[0] in ['3', '4']:
            check = True
            while check:
                date_to_check = ui.get_inputs(['Must be number > 0'], "New data: ")[0]
                check = foolproofnes(date_to_check)
            line_to_update[int(data[0])] = date_to_check
            table[line_index] = line_to_update
            data_manager.write_table_to_file(file_name, table)
        elif data[0] == "0":
            return table
        else:
            ui.print_error_message("No such option. ")
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """Answer the question: the question: How many different kinds of game
    are available of each manufacturer? Args: table with all games.
    Returns: a dictionary with this structure: { [manufacturer] : [count]."""

    label = ['Manufacturer', 'Amount of games']
    manufacturer_games = {}
    for game in table:
        if game[2] in list(manufacturer_games.keys()):
            manufacturer_games[game[2]] += 1
        else:
            manufacturer_games[game[2]] = 1
    ui.print_result(manufacturer_games, label)
    return manufacturer_games


def get_average_by_manufacturer(table, manufacturer):
    """Answer the question: What is the average amount of games in stock of
    a given manufacturer?? Args: table with all games. Returns: number of games"""

    stock_amount = [int(game[4]) for game in table if game[2] == manufacturer]
    stock = common.average(stock_amount)
    return stock
