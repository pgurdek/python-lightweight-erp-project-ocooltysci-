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

    title = "Customer Relationship Management (CRM)\n"
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
                id_input = ui.get_inputs(["type ID of the line, to remove it: "], "")
                id_ = id_input[0]
                remove(table, id_)
                show_table(table)
            elif choice == "4":
                show_table(table)
                id_input = ui.get_inputs(["type ID of the line, to update it: "], "")
                id_ = id_input[0]
                update(table, id_)
                show_table(table)
            elif choice == "5":
                get_longest_name_id(table)
            elif choice == "6":
                get_subscribed_emails(table)
            elif choice == "9":
                id_generator()
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

    inputs = ["Name: ", "Email: ", "Newsletter, press 'y' or 'n': "]
    user_input = ui.get_inputs(inputs, "")
    # while user_input[2] != 'y' or user_input[2] != 'n':
    ID = id_generator()
    user_input.insert(0, ID)

    table.append(user_input)
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
    inputs = ui.get_inputs(["Name: ", "Email: ", "Newsletter: "], "Update your data: ")
    counter = 0
    for line in table:
        if id_ in line[0]:
            # inputs = ui.get_inputs("Update: ")
            table[counter][1] = inputs[0]  # update name
            table[counter][2] = inputs[1]  # update email
            table[counter][3] = inputs[2]  # update newsletter
        counter += 1
    data_manager.write_table_to_file("crm/customers.csv", table)  # save updates
    return table


def id_generator():
    import random
    """
    Generates random ID.
    Args:
        table: list containing keys. Generated string should be different then all of them
    Returns:
        Random and unique string
    """
    special_chars = ['!', '@', '#', '$', '%', '&']
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    table = [[special_chars], [digits], [letters]]

    generated = ''
    is_unique = False
    new_id = []
    for row in table:
        new_id.append(row[0])

    while not is_unique:
        is_unique = True
        for i in range(2):
            generated += str(special_chars[random.randint(0, len(special_chars)-1)])
            generated += str(digits[random.randint(0, len(digits)-1)])
            generated += str(letters[random.randint(0, len(letters)-1)])
            generated += str(letters[random.randint(0, len(letters)-1)].upper())
        if generated in new_id:
            is_unique = False
        print(generated)
    return generated




# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first by descending alphabetical order
def get_longest_name_id(table):

    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
