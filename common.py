# implement commonly used functions here

import random
import ui

# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)


def generate_random():
    import random
    import string
    """
    Generates random ID.
    Args:
        table: list containing keys. Generated string should be different then all of them
    Returns:
        Random and unique string
    """
    # Unique and randomly generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
    special_chars = ['!', '@', '#', '$', '%', '&']
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = string.ascii_lowercase
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


def check_id(table):
    """
    Checks if typed id is in list with all ids, return typed id if it correct

    :param table: table created by datamenager from .csv file
    :return: id as string
    """

    table_rev = [list(x) for x in zip(*table)]

    while True:
        c_id = ui.get_inputs(['ABCDEFGHI format'], 'Type id')

        if c_id[0] in table_rev[0]:
            return c_id[0]
        else:
            ui.print_error_message('Wrong id')


def clear():
    """
    Prints empty line 50 times

    :return: nothing, only prints to console
    """

    clear = "\n" * 50
    print(clear)
