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
    ui.print_gap()
    header = ['Id', 'Name', 'Birth date']

    ui.print_table(table, header)

    ui.print_gap()



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table: table to add new record to

    Returns:
        Table with a new record
    """

    # your code




    not_proper_input = True
    inputs = None
    is_int = None
    #while not_proper_input: # wrong input handling
    inputs = ui.get_inputs(["Name", "Birth date"], "\nPlease add a worker.")
    if any(char.isalpha() for char in inputs[0]): # checks if there
#is a letter in user input. If at least 1 letter is present, input is ok.
        not_proper_input = False
        if inputs[0] == "":
            ui.print_gap()
            ui.print_error_message("Please type something in 'Name'.")
            ui.print_gap()
            not_proper_input = True
            #continue
    else:
        if inputs[0] == "":
            ui.print_gap()
            ui.print_error_message("Please type something in 'Name'.")
            ui.print_gap()
            not_proper_input = True
        else:
            ui.print_gap()
            ui.print_error_message("Wrong name type input.")
            ui.print_gap()
            not_proper_input = True
        #continue
    #else:
    #    not_proper_input = False
    try:
        is_int = int(inputs[1])
    except:
        if inputs[1] == "":
            ui.print_gap()
            ui.print_error_message("Please type something in 'Birth date'.")
            not_proper_input = True
        else:
            ui.print_gap()
            ui.print_error_message("Wrong birth date type input.")
            ui.print_gap()
            not_proper_input = True
        #continue
    #else:
    #    not_proper_input = False

    table = data_manager.get_table_from_file('hr/persons.csv')
    list_of_ids = []
    random_id = common.generate_random(table)
    one_input = random_id, inputs[0], inputs[1]
    one_input_list = list(one_input)  # we must do it
    table = data_manager.get_table_from_file('hr/persons.csv')
    if not_proper_input == False:
        table.append(one_input_list)
        ui.print_gap()
        ui.print_message("Added.")
        ui.print_gap()
    data_manager.write_table_to_file('hr/persons.csv', table)
    #ui.print_gap()
    #ui.print_message("Added.")
    #ui.print_gap()
    ui.print_gap()

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
    counter = 0
    for n in table:
        if id_[0] in n:
            counter += 1
            table.remove(n)
    data_manager.write_table_to_file("hr/persons.csv", table)
    if counter:
        ui.print_gap()
        ui.print_message("Removed.")
        ui.print_gap()
        ui.print_gap()
    else:
        ui.print_gap()
        ui.print_error_message("Can't find '{}' ID.".format(id_[0]))
        ui.print_gap()
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
        """Works if user what to change only name of a worker."""

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
                            ui.print_error_message("Please type something.")
                            ui.print_gap()
                            not_proper_input = True
                            continue
                        not_proper_input = True
                        ui.print_error_message("Wrong type input.")
                        ui.print_gap()
                    else:
                        not_proper_input = False
                table[data][1] = inputs[0]
                counter += 1
        return counter

    def change_birth_date(id_):
        """Works if user what to change only birth date of a worker."""
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
                            ui.print_error_message("Please type something")
                            not_proper_input = True
                        else:
                            ui.print_error_message("Wrong type input.")
                            ui.print_gap()
                            not_proper_input = True
                        continue
                    else:
                        not_proper_input = False
                table[data][2] = inputs[0]
                counter += 1
        return counter

    def change_name_and_birth_date(id_):
        """Works if user what to change name and birth date of a worker."""
        change_name(id_)
        change_birth_date(id_)
        counter = 0
        counter += 1
        return counter

    table = data_manager.get_table_from_file('hr/persons.csv')
    title = 'Name, birth date'
    list_labels = ['Name', 'Birth date']
    is_id_ok = True
    for data in range(len(table)):
        if table[data][0] == id_[0]:
            list_labels2 = ["Select what do you want to change:\n1 - name\n\
2 - birth date \n3 - change name and birth date"]
            ui.print_gap()
            title2 = ""
            while True:
                inputs = ui.get_inputs(list_labels2, title2)
                ui.print_gap()
                ui.print_gap()
                if inputs[0] == str(1):
                    is_id_ok = True
                    change_name_checker = 0
                    change_birth_date_checker = 0
                    change_name_and_birth_date_checker = 0
                    change_name_checker = change_name(id_[0])
                    break
                elif inputs[0] == str(2):
                    is_id_ok = True
                    change_name_checker = 0
                    change_birth_date_checker = 0
                    change_name_and_birth_date_checker = 0
                    change_birth_date_checker = change_birth_date(id_[0])
                    break
                elif inputs[0] == str(3):
                    is_id_ok = True
                    change_name_checker = 0
                    change_birth_date_checker = 0
                    change_name_and_birth_date_checker = 0
                    change_name_and_birth_date_checker = change_name_and_birth_date(id_[0])
                    break
                else:
                    ui.print_gap()
                    ui.print_error_message("There is no such option.")
                    ui.print_gap()
                    change_name_checker = 0
                    change_birth_date_checker = 0
                    change_name_and_birth_date_checker = 0
                    is_id_ok = True
                    break

        else:
            is_id_ok = False

    if is_id_ok == False:
        ui.print_gap()
        ui.print_error_message("There is no such ID.")
        change_name_checker = 0
        change_birth_date_checker = 0
        change_name_and_birth_date_checker = 0

    data_manager.write_table_to_file("hr/persons.csv", table)
    if change_name_checker or change_birth_date_checker or change_name_and_birth_date_checker:
        ui.print_gap()
        ui.print_message("Done.")
        ui.print_gap()
    else:
        ui.print_gap()
        ui.print_message("No changes have been done.")
        ui.print_gap()

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code
    oldest_people_list = []
    oldest_year = 5000  # How can I omit it by not declaring a variable? after 3000 years it will be out of date.
    for person in table:
        if int(person[2]) < oldest_year:
            oldest_people_list = []
            oldest_year = int(person[2])
            oldest_people_list.append(person[1])
        elif int(person[2]) == oldest_year:
            oldest_people_list.append(person[1])
    ui.print_gap()
    ui.print_message(oldest_people_list)
    ui.print_gap()


    return oldest_people_list

# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code
    total_age = 0
    amount_of_people = 0
    closest_to_average_people_list = []
    try:
        for person in table:
            total_age += int(person[2])
            amount_of_people += 1
        average_age = total_age / amount_of_people

        difference_init = 500
        for person in table:
            difference = abs(int(person[2]) - average_age)
            if difference < difference_init:
                closest_to_average_people_list = []
                closest_to_average_people_list.append(person[1])
                difference_init = difference

            elif difference == difference_init:
                closest_to_average_people_list.append(person[1])

        ui.print_gap()
        ui.print_message(closest_to_average_people_list)
        ui.print_gap()

        return closest_to_average_people_list
    except:
        ui.print_gap()
        ui.print_message("There must be someone in persons list.")
        ui.print_gap()





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
        id_ = ui.get_inputs(["Type an ID you want to remove: "], "")
        remove(data_manager.get_table_from_file('hr/persons.csv'), id_)
        return True
    elif option == "4":
        ui.print_gap()
        id_ = ui.get_inputs(["Select ID to update: "], "")
        update(data, id_)
        return True
    elif option == "5":
        get_oldest_person(data_manager.get_table_from_file('hr/persons.csv'))
        return True
    elif option == "6":
        get_persons_closest_to_average(data_manager.get_table_from_file('hr/persons.csv'))
        return True
    elif option == "0":
        return False
    else:
        raise KeyError("There is no such option.")
