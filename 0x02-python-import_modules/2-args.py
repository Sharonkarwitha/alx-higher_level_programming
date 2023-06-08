#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_vector = len(sys.argv)
    if (args_vector <= 1):
        print("{} arguements.".format(args_vector - 1))
    elif (args_vector == 2):
        print("{} arguement:".format(args_vector - 1))
    else:
        ("{} arguements:".format(args_vector - 1))
    for arg_c in range(1, args_vector):
        print("{}: {}".format(arg_c, sys.argv[arg_c]))
