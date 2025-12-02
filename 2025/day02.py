from helpers import *
from grid import *
from functools import cache

def is_twopeat(s):
    return s[0:len(s) // 2] * 2 == s

def is_repeat(s):
    return any(s[0:sublen] * (len(s) // sublen) == s for sublen in range(1, len(s) // 2 + 1))

def task1(ranges):
    return sum(i for r in ranges for i in r if is_twopeat(str(i)))

def task2(ranges):
    return sum(i for r in ranges for i in r if is_repeat(str(i)))

if __name__ == "__main__":
    # lines = get_input("sample-02")
    lines = get_input("02")
    lines = [l.strip() for l in lines]

    ranges = [range(int(r.split("-")[0]), int(r.split("-")[1]) + 1) for r in lines[0].split(",")]
    
    print(task1(ranges))
    print(task2(ranges))
