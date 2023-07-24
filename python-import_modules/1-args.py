#!/usr/bin/python3
import sys


def list_args(*argv):
       
    argv_lenght = len(argv[0])-1


    if argv_lenght == 1:    
        print("{} argument:".format(argv_lenght))
    elif argv_lenght == 0:
        print("{} argument.".format(argv_lenght))
    else:
        print("{}: arguments:".format(argv_lenght))
    for x in range(1, len(argv[0])):
            print("{}: {}".format(x, argv[0][x]))
        
if __name__ == "__main__":
    cmd_input = []
    for i in range(0, len(sys.argv)):
        cmd_input.append(str(sys.argv[i]))
    list_args(cmd_input)
