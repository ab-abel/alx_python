#!/usr/bin/python3
from add_0 import add


def main():
    a = 1
    b = 2
    answer = "{} + {} = {}".format(a, b, add(a, b))
    print(answer)

if __name__ == "__main__":
    main()
