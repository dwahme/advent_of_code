from helpers import *
from grid import *
from functools import cache

def is_twopeat(s):
    return s[0:len(s) // 2] * 2 == s

def is_repeat(s):
    return any(s[0:sublen] * (len(s) // sublen) == s for sublen in range(1, len(s) // 2 + 1))

def task1(ranges):
    return sum(i for r in ranges.split(",") for i in range(*map(int, r.split("-"))) if is_twopeat(str(i)))

def task2(ranges):
    return sum(i for r in ranges.split(",") for i in range(*map(int, r.split("-"))) if is_repeat(str(i)))

if __name__ == "__main__":
    # lines = get_input("sample-02")
    lines = get_input("02")
    lines = [l.strip() for l in lines]
    
    print(task1(lines[0]))
    print(task2(lines[0]))
