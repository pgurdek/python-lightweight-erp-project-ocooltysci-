# implement commonly used functions here

import random
import string
import ui


# generate and return a unique and random string
# other expectation:
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

    specyfic_data = list(list(zip(*table))[kolumn])
    print(specyfic_data)
    ui.print_result(specyfic_data, title)
    return specyfic_data


def average(list_of_amount):
    """Counts average of number in list"""
    return sum_of(list_of_amount)/len(list_of_amount)


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
            if n == (len(data_to_sort)-counter):
                break
            if data_to_sort[n] > data_to_sort[n+1]:
                data_to_sort[n], data_to_sort[n+1] = data_to_sort[n+1], data_to_sort[n]
                change = True
        counter += 1
    print(data_to_sort)
    return data_to_sort
