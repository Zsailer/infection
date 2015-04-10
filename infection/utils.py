# --------------------------------------------------
# Useful utilities for randomly generating names
# --------------------------------------------------

import names

def random_names(n):
    """ Generate a random list of `n` names. """
    people = list()
    for i in range(n):
        in_list = True
        while in_list is True:
            # Generate random name
            name = names.get_first_name()
            # Check for repeats
            try:
                people.index(name)
            except:
                in_list = False
        # If this name is not a repeat, append to list of names. 
        people.append(name)
    return people