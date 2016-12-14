# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

    title = "\nAccounting manager"
    exit_statement = "Back to main menu"
    options = ["Show table", "Add item", "Remove item", "Update table", "Which year has the highest profit?", "What is the average (per item) profit in a given year?"]

    module = os.path.dirname(__file__)
    data_file = "items.csv"
    data_file_path = os.path.join(module, data_file)
    table = data_manager.get_table_from_file(data_file_path)

    while True:
            ui.print_menu(title, options, exit_statement)
            choice = ui.get_inputs(["Choose your module: "], "")
            choice = choice[0]

            if choice == "1":
                show_table(table)
            elif choice == "2":
                add(table)
            elif choice == "3":
                show_table(table)
                id_input = common.check_id(table)

                remove(table, id_input)
                show_table(table)
            elif choice == "4":
                show_table(table)
                id_input = common.check_id(table)
                update(table, id_input)
                show_table(table)

            elif choice =="5":
                max_year = which_year_max(table)
                ui.print_result(max_year, 'Year with highest profit')

            elif choice =="6":
                year_input = ui.get_inputs(["YYYY format"], "Type year")
                avg_amount(table, year_input)

            elif choice == "0":
                break
            else:
                ui.print_error_message("Wrong input")


def show_table(table):
    """
    Display a table

    Args:
        table: list of lists to be displayed.

    Returns:
        None
    """

    header = ['Id', 'Month', 'Day', 'Year', 'Type', 'Amount']
    ui.print_table(table, header)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    title = "Add a new record"
    list_labels = ['Month', 'Day', 'Year', 'Type', 'Amount']
    record = [common.generate_random()]

    inputs = input_record()


    for things in inputs:
        record.append(things)
    table.append(record)
    data_manager.write_table_to_file("accounting/items.csv", table)
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


    for n in table:
        if id_ in n:
            table.remove(n)


    data_manager.write_table_to_file("accounting/items.csv", table)

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

    title = 'Update'
    list_labels = ['Month', 'Day', 'Year', 'Type', 'Amount']
    for data in range(len(table)):
        if table[data][0] == id_:
            inputs = input_record()
            table[data][1] = inputs[0]
            table[data][2] = inputs[1]
            table[data][3] = inputs[2]
            table[data][4] = inputs[3]
            table[data][5] = inputs[4]

    data_manager.write_table_to_file("accounting/items.csv", table)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    income = {}
    loss = {}
    profit = {}
    for record in table:
        income[record[3]] = 0
        loss[record[3]] = 0
    for record in table:
        if record[4] == 'in':
            income[record[3]] += int(record[5])

    for record in table:
        if record[4] == 'out':
            loss[record[3]] += int(record[5])


    for item in income:
        profit_year = income[item] - loss[item]

        profit[item]=profit_year

    year_max = int(max(profit, key=profit.get))
    return year_max



# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):


    # your code

    pass


def input_record():
    inputs = []
    while True:
        month = ui.get_inputs(['number without 0'], 'Type month')

        if month[0].isdigit():
            if int(month[0]) < 13 and int(month[0]) > 0:
                inputs.append(month[0])
                break

    while True:
        day = ui.get_inputs(['number without 0'], 'Type day')

        if day[0].isdigit():
            if int(day[0]) < 32:
                inputs.append(day[0])
                break

    while True:
        year = ui.get_inputs(['YYYY format'], 'Type year')

        if year[0].isdigit():
            if len(year[0]) == 4:
                inputs.append(year[0])
                break

    while True:
        type_inp = ui.get_inputs(["'in' or 'out'"], 'Type type of item')

        if type_inp[0] in ['in', 'out']:
            inputs.append(type_inp[0])
            break

    while True:
        amount = ui.get_inputs(['Amount as number'], 'Type amount')

        if amount[0].isdigit():
            inputs.append(amount[0])
            break

    return inputs

def check_id(table):
    table_rev = [list(x) for x in zip(*table)]

    while True:
        type_id = ui.get_inputs(['ABCDEFGHI format'], 'Type id')

        if type_id[0] in table_rev[0]:
            return type_id[0]
