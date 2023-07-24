#!/usr/bin/python3

def list_args(*argv):
    argv_lenght = len(argv)
    if argv_lenght == 1:    
        print("{}: argument.".format(argv_lenght))
    else:
        print("{}: arguments.".format(argv_lenght))
    for x in range(0, argv_lenght):
            print("{}: {}".format(x+1, argv[x]))
        
if __name__ == "__main__":
    list_args("hello")

# list_args("Hello", "Holberton", "School", "98", "Battery", "street")
