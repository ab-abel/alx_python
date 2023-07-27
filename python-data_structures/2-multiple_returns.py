#!/usr/bin/env python3


def multiple_returns(sentence:str):
    length = len(sentence)
    if length ==0:
        first = None
    else:
        first = sentence[0]
    return length, first
