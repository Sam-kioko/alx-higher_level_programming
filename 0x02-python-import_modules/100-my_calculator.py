#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main(argv):
    num_args = len(argv) - 1
    if num_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        addition = add(a, b)
        print("{} + {} = {}".format(a, b, addition))
    elif operator == '-':
        subtract = sub(a, b)
        print("{} - {} = {}".format(a, b, subtract))
    elif operator == '*':
        multiply = mul(a, b)
        print("{} * {} = {}".format(a, b, multiply))
    elif operator == '/':
        division = div(a, b)
        print("{} / {} = {}".format(a, b, division))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
