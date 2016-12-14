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

    hr_options = ["Show Table","Add","Remove","Update","Get oldest person","Get persons closest to average"]
    keep_menu = True
    while keep_menu:
        ui.print_menu('HR Main Menu',hr_options,'Back To Menu')
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
    print("")
    header = ['Id', 'Name', 'Birth date']

    ui.print_table(table, header)
    print("")



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code

    inputs = ui.get_inputs(["Name", "Birth date"], "\nPlease add a worker.")
    random_id = common.generate_random()
    one_input = random_id, inputs[0], inputs[1]
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
    table = data_manager.get_table_from_file('hr/persons.csv')

    for n in table:
        if id_ in n:
            table.remove(n)
    data_manager.write_table_to_file("hr/persons.csv", table)
    print("\nRemoved.\n\n")
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

    def change_name(id_):
        list_labels2 = ['Name']
        title2 = ''
        counter = 0
        for data in range(len(table)):
            if table[data][0] == id_:
                not_proper_input = True
                inputs = None
                while not_proper_input:
                    inputs = ui.get_inputs(list_labels2, title2)
                    if not any(char.isalpha() for char in inputs[0]):
                        if inputs[0] == "":
                            print("Please type something.\n")
                            not_proper_input = True
                            continue
                        not_proper_input = True
                        print("Wrong type input.\n")
                    else:
                        not_proper_input = False
                table[data][1] = inputs[0]
                counter += 1
        return counter

    def change_birth_date(id_):
        title2 = ''
        counter = 0
        list_labels2 = ['Birth date']
        for data in range(len(table)):
            if table[data][0] == id_:
                not_proper_input = True
                inputs = None
                while not_proper_input: # Makes users input contains something
                    inputs = ui.get_inputs(list_labels2, title2)
                    try:
                        is_int = int(inputs[0])
                    except:
                        if inputs[0] == "":
                            print("Please type something")
                            not_proper_input = True
                        else:
                            print("Wrong type input.\n")
                            not_proper_input = True
                        continue
                    else:
                        not_proper_input = False
                table[data][2] = inputs[0]
                counter += 1
        return counter

    def change_name_and_birth_date(id_):
        change_name(id_)
        change_birth_date(id_)
        counter = 0
        counter += 1
        return counter

    table = data_manager.get_table_from_file('hr/persons.csv')
    title = 'Name, birth date' # was "update"
    list_labels = ['Name', 'Birth date']
    is_id_ok = True
    dupa = 0
    for data in range(len(table)):
        if table[data][0] == id_:
            what_change = input("\nSelect what do you want to change:\n1 - name\n\
2 - birth date \n3 - change name and birth date\n")
            if what_change == str(1):
                is_id_ok = True
                change_name_checker = 0
                change_birth_date_checker = 0
                change_name_and_birth_date_checker = 0
                change_name_checker = change_name(id_)
            elif what_change == str(2):
                is_id_ok = True
                change_name_checker = 0
                change_birth_date_checker = 0
                change_name_and_birth_date_checker = 0
                change_birth_date_checker = change_birth_date(id_)
            elif what_change == str(3):
                is_id_ok = True
                change_name_checker = 0
                change_birth_date_checker = 0
                change_name_and_birth_date_checker = 0
                change_name_and_birth_date_checker = change_name_and_birth_date(id_)
            else:
                print("\nThere is no such option.\n")
        else:
            is_id_ok = False

    if is_id_ok == False:
        print("\nThere is no such ID.")
        change_name_checker = 0
        change_birth_date_checker = 0
        change_name_and_birth_date_checker = 0

    data_manager.write_table_to_file("hr/persons.csv", table)
    if change_name_checker or change_birth_date_checker or change_name_and_birth_date_checker:
        print("\nDone\n")
    else:
        print("\nNo changes have been done.\n")

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
    elif option == "3":
        id_ = input("\nSelect ID to remove: ")
        remove(data_manager.get_table_from_file('hr/persons.csv'), id_)
        return True
    elif option == "4":
        id_ = input("\nSelect ID to update: ")
        update(data, id_)
        return True
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
