from helpers import *
from grid import *
from functools import cache
from math import floor, ceil, log10

def get_ranges(s):
    return int(s.split("-")[0]), int(s.split("-")[1])

def task1(lines):
    invalid = 0

    for l in lines.split(","):
        # print()
        start, stop = get_ranges(l)

        for i in range(start, stop + 1):
            digits = floor(log10(i) / 2) + 1

            # print(f"{i} {digits} -> ({pow(10, digits)}) {i // (pow(10, digits))} {i % (pow(10, digits))}")
            first =  i // (pow(10, digits))
            second = i % (pow(10, digits))

            if first == second and int(f"{first}{second}") == i:
                # print(i)
                invalid += i

    return invalid

def task2(lines):
    invalid = 0

    for l in lines.split(","):
        # print()
        start, stop = get_ranges(l)
        print()
        found = {}

        for i in range(start, stop + 1):
            s = str(i)
            length = len(s)

            for j in range(1, length // 2 + 1):
                digits = s[0:j]
                if length % j == 0:
                    new_i = digits * (length // j)
                    if int(new_i) == i:
                        invalid += i
                        break

    return invalid

if __name__ == "__main__":
    # lines = get_input("sample-02")
    lines = get_input("02")
    lines = [l.strip() for l in lines]
    
    print(task1(lines[0]))
    print(task2(lines[0]))
