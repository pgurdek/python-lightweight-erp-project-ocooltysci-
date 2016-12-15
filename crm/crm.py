# data structure:
# id: string
#     Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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

    title = "\nCustomer Relationship Management (CRM)"
    exit_statement = "Back to main menu"
    options = ["Show table", "Add item", "Remove item", "Update table",
    "What is the id of the customer with the longest name?",
    "Which customers has subscribed to the newsletter?"]

    module = os.path.dirname(__file__)
    data_file = "customers.csv"
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
                id_input = ui.get_inputs(["type ID of the line, to remove: "], "")
                id_ = id_input[0]
                remove(table, id_)
                show_table(table)
            elif choice == "4":
                show_table(table)
                id_input = ui.get_inputs(["type ID of the line, to update: "], "")
                id_ = id_input[0]
                update(table, id_)
                show_table(table)
            elif choice == "5":
                longest_id = get_longest_name_id(table)
                print(longest_id)
                ui.print_result(longest_id, 'longest name ID')
            elif choice == "6":
                nice_list = get_subscribed_emails(table)
                show_nicelist(nice_list)
                # ui.print_result('Newsletter Customers list: ', nice_list)  # result, label
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

    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.
    Args:
        table: table to add new record to
    Returns:
        Table with a new record
    """
    title = "Add a new record"
    list_labels = ['Name', 'Email', 'Subscribed']
    record = [common.generate_random()]
    inputs = ui.get_inputs(list_labels, title)
    allowed = ['y', 'n', '1', '0']
    while True:
        if len(inputs[0]) > 2:
            break
        else:
            new_in = ui.get_inputs(['Name'], title)
            inputs[0] = new_in[0]
    while True:
        if inputs[2] in allowed:
            break
        else:
            new_in = ui.get_inputs(['Subscribed'], title)
            inputs[2] = new_in[0]
    if inputs[2] == 'y':
        inputs[2] = '1'
    elif inputs[2] == 'n':
        inputs[2] = '0'
    while True:
        if '@' in inputs[1]:
            break
        else:
            new_in = ui.get_inputs(['Email'], title)
            inputs[1] = new_in[0]
    inputs.insert(0, record[0])
    table.append(inputs)
    data_manager.write_table_to_file("crm/customers.csv", table)
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
    for n in table:
        if id_ in n:
            table.remove(n)
    show_table(table)
    file_name = 'customers.csv'
    data_manager.write_table_to_file("crm/customers.csv", table)

    return table


def update(table, id_):
    """Updates specified record in the table. Ask users for new data.
    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
    Returns:
        table with updated record """

    title = 'Update'
    list_labels = ['Name', 'Email', 'Subscribed']
    for data in range(len(table)):
        if table[data][0] == id_:
            inputs = ui.get_inputs(list_labels, title)
            table[data][1] = inputs[0]
            table[data][2] = inputs[1]
            check(inputs, table, data)
            data_manager.write_table_to_file("crm/customers.csv", table)
            break
    return table


def check(inputs, table, data):
    title = 'Update'
    if inputs[2] == 'y' or inputs[2] == '1':
        table[data][3] = '1'
    elif inputs[2] == 'n' or inputs[2] == '0':
        table[data][3] = '0'
    else:
        while True:
            subscribed = ui.get_inputs(['Subscribed'], title)
            subscribed = subscribed[0]
            if subscribed == 'y' or subscribed == '1':
                table[data][3] = '1'
                break
            elif subscribed == 'n' or subscribed == '0':
                table[data][3] = '0'
                break
    return inputs


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):
    names = [[row[0], row[1]] for row in table]
    longest = bubble(names)[0][0]
    return longest


def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1, i, -1):
            if lst[j][1] < lst[j - 1][1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst

# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):
    subscribed_list = []
    for row in range(len(table)):
        if table[row][3] == '1':
            subscribed_list.append(table[row][2] + ';' + table[row][1])
    return subscribed_list


def show_nicelist(nice_list):
        to_print_list = []
        for item in nice_list:
            item = str(item).split(';')
            item[0], item[1] = item[1], item[0]
            to_print_list.append(item)

        header = ['Name', 'email']
        ui.print_table(to_print_list, header)
