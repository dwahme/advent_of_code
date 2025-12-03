from helpers import *
from grid import *
from functools import cache

@cache
def joltage(s, remaining):
    if remaining == 1: return max(s)
    return max(d + joltage(s[idx + 1:], remaining - 1) for idx, d in enumerate(s[:-remaining + 1]))

def task1(lines):
    return sum(int(joltage(l, 2)) for l in lines)

def task2(lines):
    return sum(int(joltage(l, 12)) for l in lines)

if __name__ == "__main__":
    # lines = get_input("sample-03")
    lines = get_input("03")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
 