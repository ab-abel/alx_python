#!/usr/bin/python3
# update dictionary if key exist otherwirse add to dicationatry


def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if key in k == True:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value        
        return a_dictionary


def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    return keys
