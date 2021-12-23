#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_list = sys.argv
    number_of_arg = len(arg_list)-1
    if number_of_arg == 0:
        arg_text = "arguments."
    elif number_of_arg == 1:
        arg_text = "argument:"
    else:
        arg_text = "arguments:"
    print("{} {}".format(number_of_arg, arg_text))
    for arg in range(1, len(arg_list)):
        print("{}: {}".format(arg, arg_list[arg]))
