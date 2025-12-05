from helpers import *
from grid import *
from functools import cache

def task1(ranges, ingredients):
    return sum(any(lo <= ingredient <= hi for lo, hi in ranges) for ingredient in ingredients)

def task2(ranges):
    fresh_count = 0
    max_hi = -1

    for lo, hi in sorted(ranges, key=lambda r: r[0]):
        # no overlap
        if max_hi < lo:
            fresh_count += hi - lo + 1
        # partial overlap
        elif max_hi <= hi:
            fresh_count += hi - max_hi

        max_hi = max(max_hi, hi)

    return fresh_count

if __name__ == "__main__":
    # lines = get_input("sample-05")
    lines = get_input("05")
    lines = [l.strip() for l in lines]

    split = lines.index("")
    ranges = [ (int(l.split("-")[0]), int(l.split("-")[1])) for l in lines[:split] ]
    ingredients = [ int(l) for l in lines[split + 1:] ]
    
    print(task1(ranges, ingredients))
    print(task2(ranges))
