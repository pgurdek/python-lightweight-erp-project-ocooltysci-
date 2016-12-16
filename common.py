# implement commonly used functions here

import random
import string
import ui
from datetime import date


# generate and return a unique and random string
# other expectation
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)
def generate_random(table):
    """Generates random and unique string. Used for id/key generation.
    Args:table: list containing keys. Generated string should be different then all of them
    Returns: Random and unique string """
    letters = string.ascii_lowercase
    special_characters = (string.punctuation).replace(';', '')
    id_table = [list(x) for x in zip(*table)][0]
    not_unique = True
    new_id = []
    while not_unique:
        for i in range(2):
            new_id.append(random.choice(letters))
            new_id.append(random.choice(letters.upper()))
            new_id.append(random.choice(special_characters))
            new_id.append(str(random.randint(0, 9)))
        random.shuffle(new_id)
        new_id = ''.join(new_id)
        if new_id not in id_table:
            not_unique = False
    return new_id


def list_to_choose(table, kolumn, title):
    """Generates a list of one specific data from table, printed when user want
    to choose one item from it, for egzemple one manufacturer.
    Args:table and index -number- of kolumn we want to extract from table, and title
    - what kind of data list will contain. Returns: Simple list of strings """

    specyfic_data = list(set(list(zip(*table))[kolumn]))
    ui.print_result(sort_list(specyfic_data), title)
    return specyfic_data


def average(list_of_amount):
    """Counts average of number in list"""
    return sum_of(list_of_amount) / len(list_of_amount)


def sum_of(list_of_amount):
    """Counts sum of number in list"""
    amount = 0
    for number in list_of_amount:
        amount += number
    return amount


def sort_list(data_to_sort):
    """Sorts list"""
    change = True
    counter = 1
    while change:
        change = False
        for n in range(len(data_to_sort)):
            if n == (len(data_to_sort) - counter):
                break
            if data_to_sort[n] > data_to_sort[n + 1]:
                data_to_sort[n], data_to_sort[n + 1] = data_to_sort[n + 1], data_to_sort[n]
                change = True
        counter += 1
    return data_to_sort


def check_id(table):
    """
    Checks if typed id is in list with all ids, return typed id if it correct
    :param table: table created by datamenager from .csv file
    :return: id as string
    """

    table_rev = [list(x) for x in zip(*table)]

    while True:
        c_id = ui.get_inputs(['ABCDEFGHI format'], 'Type id, or something else to exit')

        if c_id[0] in table_rev[0]:
            return c_id[0]
        else:
            ui.print_error_message('Wrong id')
            break



def is_number(value):
    """Check is number is Float"""
    try:
        float(value)
        return True
    except ValueError:
        return False

def date_comapre(list, data_from, data_to, data_checked):
    """Compare Dates"""
    data_from = date(data_from[0], data_from[1], data_from[2])
    data_checked = date(data_checked[0], data_checked[1],data_checked[2])
    data_to = date(data_to[0], data_to[1],data_to[2])


    if data_from < data_checked < data_to:
        return True
    else:
        return False

