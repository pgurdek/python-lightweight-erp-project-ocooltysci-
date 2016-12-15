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

    data = data_manager.get_table_from_file('sales/sales.csv')
    sales_options = ["Show Table", "Add", "Remove", "Update", "Lowest Price Item ID", "Items Sorted Between Date"]
    while True:
        ui.print_menu('Sales Main Menu', sales_options, 'Back To Menu')
        try:
            data = choose_sale(data)
        except KeyError as err:
            ui.print_error_message(err)
        if not data[0]:
            data_manager.write_table_to_file('sales/sales.csv', data[1])
            return True


def header_info():
    """Headers for all Sales"""
    header = ['Id', 'Title', 'Price', 'Month', 'Day', 'Year']
    return header


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    # your code

    ui.print_table(table, header_info())

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
    headers = header_info()
    numbers_of_values = len(headers)
    temp_list = []
    for index, header_title in enumerate(headers):
        if index == 0:
            temp_list.append(common.generate_random(table))

        else:
            values = value_checker(header_title)
            temp_list.extend(values)
            # temp_list.append()

    table.append(temp_list)
    return table


def value_checker(title):
    """Checks Values for Specials Titles"""

    keep_checking = True

    while keep_checking:
        value = ui.get_inputs([title], '')

        if title == "Price":
            if common.is_number(value[0]):
                return value

        elif title == "Day":
            if common.is_number(value[0]):
                number = int(value[0])
                if number > 0 and number < 32:
                    return value

        elif title == "Month":
            if common.is_number(value[0]):
                number = int(value[0])
                if number > 0 and number <= 12:
                    return value

        elif title == "Year":
            if common.is_number(value[0]):
                number = int(value[0])
                if number > 1990 and number <= 2100:
                    return value
        else:
            return value


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
    for index, line in enumerate(table):
        if line[0] == id_[0]:
            table.pop(index)
            break
        else:
            ui.print_error_message('Wrong Index, Try again')
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
    for index, elements in enumerate(table):
        if elements[0] in id_:
            table[index] = ui.get_inputs(elements, 'Please Speciy Data for this elements: ')
            break

    return table


# My Functions

def choose_sale(data):
    """Choose  menu item """
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    if option == "1":
        show_table(data)
        return data
    elif option == "2":
        return add(data)
    elif option == "3":
        show_table(data)
        return remove(data, ui.get_inputs(["Please enter ID"], "Delete ID"))
    elif option == "4":
        show_table(data)
        return update(data, ui.get_inputs(["Please enter ID"], "Pick the ID to update"))
    elif option == "5":
        get_lowest_price_item_id(data)
        return data
    elif option == "6":
        get_items_sold_between(data, ui.get_inputs(["Month From"], ""), ui.get_inputs(["Day From"], ""),
                               ui.get_inputs(["Year From"], ""), ui.get_inputs(["Month To"], ""),
                               ui.get_inputs(["Day To"], ""), ui.get_inputs(["Year to"], ""))
        return data
    elif option == "0":
        return False, data
    else:
        raise KeyError("There is no such option.")


# special functions:
# ------------------

# the question: What is the id of the item that was sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first by descending alphabetical order
def get_lowest_price_item_id(table):
    """Get Lowest Price for Item"""
    min = int(table[0][2])
    for index, value in enumerate(table):
        if min >= int(value[2]):
            min = int(value[2])

    list_to_sort = []
    for index, value in enumerate(table):
        if int(value[2]) == min:
            list_to_sort.append(value[0])

    sorted_list = common.sort_list(list_to_sort)
    ui.print_result(sorted_list[-1], 'Name of the ID with the lower Price DESC')
    return sorted_list[-1]


# the question: Which items are sold between two given dates ? (from_date < sale_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """Get items sold beetween for givens dates"""

    try:
        data_from = (int(year_from[0]), int(month_from[0]), int(day_from[0]))
        data_to = (int(year_to[0]), int(month_to[0]), int(day_to[0]))
    except:
        data_from = (year_from, month_from, day_from)
        data_to = (year_to, month_to, day_to)

    list_temp = []

    for index, row in enumerate(table):
        data_checked = (int(row[5]), int(row[3]), int(row[4]))
        if common.date_comapre(row, data_from, data_to, data_checked):
            list_temp.append([row[0], row[1], int(row[2]), int(row[3]), int(row[4]), int(row[5])])
    ui.print_table(list_temp, 'Wniki:')

    return list_temp
