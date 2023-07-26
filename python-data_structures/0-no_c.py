#!/usr/bin/env python3
# Check for c took me days to figure out but is ok


def no_c(my_str):
    word_list = []
    for new_word in my_str:
        if new_word == 'c':
            new_word = ""
        if new_word == 'C':
            new_word = ""
        word_list.append(new_word)
    return ''.join(word_list)
