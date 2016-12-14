

def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table: list of lists - table to display
        title_list: list containing table headers

    Returns:
        This function doesn't return anything it only prints to console.
    """

    # your goes code

    zip_table = [list(x) for x in zip(*table)]  # create transposited list with data

    len_list = []  # list witch will store width of columns
    for line in zip_table:
        length_line = []
        for item in line:  # check length of items in column from file
            length_line.append(len(item))

        len_list.append(max(length_line))  # append length of longest strin in column

    i = 0
    for title in (title_list):  # if header is longed than items, length of header is added to width list
        if len(title) > len_list[i]:
            len_list[i] = len(title)
        i+=1


    i = 0
    for title in title_list:
        print('{:>{}}'.format(title, len_list[i] + 1), end= '|')
        i += 1

    print()

    for line in table:
        i = 0
        for item in line:
            print('{:>{}}'.format(item, len_list[i]+ 1), end= '|')
            i+=1
        print("")

    return

def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: string, list or dictionary - result of the special function
        label: label of the result

    Returns:
        This function doesn't return anything it only prints to console.
    """

    # your code

    pass


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        This function doesn't return anything it only prints to console.
    """
    # your code
    print('{}:'.format(title))
    for index, option in enumerate(list_options):
        print('   ({index}) {option}'.format(index=index+1,option = option))

    print('   (0) {exit}'.format(exit = exit_message))

    pass


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels: list of strings - labels of inputs
        title: title of the "input section"

    Returns:
        List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    # your code
    print(title)
    inputs = []
    for user_name_input in list_labels:
        user_input = input('{} : '.format(user_name_input))
        inputs.append(user_input)

    return inputs


# This function displays an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):
    """
    Displays an error message

    Args:
        message(str): error message to be displayed

    Returns:
        This function doesn't return anything it only prints to console.
    """

    # your code

    pass
