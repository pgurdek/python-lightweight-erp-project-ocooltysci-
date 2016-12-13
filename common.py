# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of lists
# @generated: string - randomly generated string (unique in the @table)


def generate_random():
    import random
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
        # print(generated)
    return generated
