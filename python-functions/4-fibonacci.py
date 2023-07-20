#!/usr/bin/env python3
# fibonacci sequence
# 0 1 1 2 3 5 8 13 21...

def fibonacci_sequence(n):
    a = []
    a.append(0)
    a.append(1)  
    for i in range(2, n):
        a.append(a[i-1] + a[i-2])
    print(a)


def fib2(n):
    c,d = 0,1
    while (d<n):
        print(d, end=', ')
        c,d=d, c+d

# fib2(20)
