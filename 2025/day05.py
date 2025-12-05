from helpers import *
from grid import *
from functools import cache

def task1(lines):
    split = lines.index("")
    ranges = [ (int(l.split("-")[0]), int(l.split("-")[1])) for l in lines[:split] ]
    ingredients = [ int(l) for l in lines[split + 1:] ]

    fresh_count = 0
    for ingredient in ingredients:
        fresh_count += any(lo <= ingredient <= hi for lo,hi in ranges)

    return fresh_count

def task2(lines):
    split = lines.index("")
    ranges = [ (int(l.split("-")[0]), int(l.split("-")[1])) for l in lines[:split] ]

    fresh_count = 0
    ranges.sort(key=lambda r: r[0])
    max_hi = -1

    for lo, hi in ranges:

        # no overlap
        if max_hi < lo:
            fresh_count += hi - lo + 1
            max_hi = hi
        # partial overlap
        elif max_hi <= hi:
            fresh_count += hi - max_hi
            max_hi = hi

    return fresh_count

if __name__ == "__main__":
    # lines = get_input("sample-05")
    lines = get_input("05")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
