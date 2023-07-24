#!/usr/bin/python3

def list_args(*argv):
    print("{}: arguments.".format(len(argv)))
    for x in range(0, len(argv)):
    # print("{}: {}".format(x, argv[x]))
        print("{}: {}".format(x+1, argv[x]))

if __name__ == "__main__":
    list_args()

# list_args("Hello", "Holberton", "School", "98", "Battery", "street")
