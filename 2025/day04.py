from helpers import *
from grid import *
from functools import cache

def task1(lines):
    g = Grid(lines)

    for p in g.iterate_xy():

        if g.get(*p) != "@": continue

        accesses = g.get_many([ADD(p, d) for d in ALL_DIRS])
        if accesses.count("@") + accesses.count("x") < 4:
            g.set(*p, "x")

    return len(g.find("x"))

def task2(lines):
    total = 0

    g = Grid(lines)

    while True:

        removed = 0

        for p in g.iterate_xy():

            if g.get(*p) != "@": continue

            accesses = g.get_many([ADD(p, d) for d in ALL_DIRS])
            if accesses.count("@") < 4:
                removed += 1
                g.set(*p, ".")

        total += removed

        if not removed:
            break

    return total

if __name__ == "__main__":
    # lines = get_input("sample-04")
    lines = get_input("04")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
