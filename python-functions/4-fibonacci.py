#!/usr/bin/env python3
# fibonacci sequence

def fibonacci_sequence(n):
    a = []
    a.append(0)
    a.append(1)  
    for i in range(2, n):
        a.append(a[i-1] + a[i-2])
    print(a)
