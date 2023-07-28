#!/usr/bin/python3
# return the look through a dictionary ad return the maximum number in the dictionary


def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        best_score = None
    else:
        for k,v in a_dictionary.items():
            if v == max(list(a_dictionary.values())):
                best_score = k
        return best_score
