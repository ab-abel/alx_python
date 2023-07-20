#!/usr/bin/env python3
# fibonacci sequence


def fibonacci_sequence(n):
    c,d = 0,1
    while (d<n):
        print(d, end=', ')
        c,d=d, c+d
