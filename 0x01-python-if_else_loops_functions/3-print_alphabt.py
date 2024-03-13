#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    alphabet = chr(i)
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(alphabet), end='')
