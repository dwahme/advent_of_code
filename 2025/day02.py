from helpers import *
from grid import *
from functools import cache

def get_range(s):
    return int(s.split("-")[0]), int(s.split("-")[1])

def is_twopeat(s):
    return s[0:len(s) // 2] * 2 == s

def is_repeat(s):
    return any(s[0:sublen] * (len(s) // sublen) == s for sublen in range(1, len(s) // 2 + 1))

def search_repeats(start, stop, check_func):
    return sum(i for i in range(start, stop + 1) if check_func(str(i)))

def task1(lines):
    return sum(search_repeats(*get_range(l), is_twopeat) for l in lines.split(","))

def task2(lines):
    return sum(search_repeats(*get_range(l), is_repeat) for l in lines.split(","))

if __name__ == "__main__":
    # lines = get_input("sample-02")
    lines = get_input("02")
    lines = [l.strip() for l in lines]
    
    print(task1(lines[0]))
    print(task2(lines[0]))
