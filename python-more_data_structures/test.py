#!/usr/bin/python3
# update dictionary if key exist otherwirse add to dicationatry

def print_sorted_dictionary(my_dict):
    """ Print sorted dictionary """
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))

def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) == 0:
       a_dictionary[key] = value
       print_sorted_dictionary(a_dictionary)
    else: 
        for k, v in a_dictionary.items():
            if key in k == True:
                a_dictionary[key] = value
            else:
                a_dictionary[key] = value        
            # return a_dictionary
    return a_dictionary

my_dict = { }
key = "a"
value = "a"
new_dict = update_dictionary(my_dict, key, value)
print(new_dict)
print(print_sorted_dictionary(new_dict))
# print("xx")
# print_sorted_dictionary(my_dict)