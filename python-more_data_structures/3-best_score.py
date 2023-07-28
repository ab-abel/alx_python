#!/usr/bin/python3
# return the look through a dictionary ad return the maximum number in the dictionary


def best_score(a_dictionary):
    for k,v in a_dictionary.items():
        if v == max(list(a_dictionary.values())):
            print("Best score: {}".format(k))
