#!/usr/bin/env python3


def multiple_returns(sentence:str):
    length = len(sentence)
    if length ==0:
        first = None
    else:
        first = sentence[0]
    return length, first

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))