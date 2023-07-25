#!/usr/bin/python3
# raise an exception with a message 


def raise_exception_msg():
    try:
        raise NameError("C is fun")
    except NameError as ne:
        print(ne)
