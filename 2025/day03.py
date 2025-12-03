from helpers import *
from grid import *
from functools import cache

@cache
def max_joltage(s, remaining_digits):

    ns = [int(s) for s in s]

    if remaining_digits == 1:
        return max(ns)
    
    best = -1
    for idx, n in enumerate(ns[:-remaining_digits + 1]):
        best = max(best, n * 10 ** (remaining_digits - 1) + max_joltage(s[idx + 1:], remaining_digits - 1))
    
    return best

def task1(lines):
    total = 0

    for l in lines:
        ns = [int(s) for s in l]
        jolt = max_joltage(l, 2)

        total += jolt

    return total



def task2(lines):
    total = 0

    for l in lines:
        ns = [int(s) for s in l]
        jolt = max_joltage(l, 12)

        total += jolt

    return total

if __name__ == "__main__":
    # lines = get_input("sample-03")
    lines = get_input("03")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
