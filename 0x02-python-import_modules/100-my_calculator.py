#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    arg_list = sys.argv
    number_of_arg = len(sys.argv)-1
    if (number_of_arg != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(arg_list[1])
    operator = arg_list[2]
    b = int(arg_list[3])
    if operator == "+":
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif operator == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
