from helpers import *
from grid import *
from functools import cache

def remove(g, replacement):
    removed = 0

    for p in g.iterate_xy():
        if g.get(*p) != "@": continue

        accesses = g.get_many([ADD(p, d) for d in ALL_DIRS])
        if accesses.count("@") + accesses.count("x") < 4:
            g.set(*p, replacement)
            removed += 1
    
    return removed

def task1(lines):
    g = Grid(lines)
    return remove(g, "x")

def task2(lines):
    g = Grid(lines)

    total = 0
    while removed := remove(g, "."):
        total += removed

    return total

if __name__ == "__main__":
    # lines = get_input("sample-04")
    lines = get_input("04")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
