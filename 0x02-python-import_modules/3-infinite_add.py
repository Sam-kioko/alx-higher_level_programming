#!/usr/bin/python3
import sys


def main(argv):
    if len(argv) == 1:
        print("0")
    else:
        # Convert command-line arguments to integers and sum them up
        result = sum(int(arg) for arg in argv[1:])
        print(result)


if __name__ == "__main__":
    main(sys.argv)
