from helpers import *
from grid import *
from range import *
from functools import cache

def task1(ranges, ingredients):
    return sum(any(i in r for r in ranges) for i in ingredients)

def task2(ranges):
    return sum(r.hi - r.lo for r in Range.merge_all(ranges))

if __name__ == "__main__":
    # lines = get_input("sample-05")
    lines = get_input("05")
    lines = [l.strip() for l in lines]

    split = lines.index("")
    ranges = [ Range(int(l.split("-")[0]), int(l.split("-")[1]) + 1) for l in lines[:split] ]
    ingredients = [ int(l) for l in lines[split + 1:] ]
    
    print(task1(ranges, ingredients))
    print(task2(ranges))
