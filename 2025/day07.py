from helpers import *
from grid import *
from interval import *
from functools import cache

def task1(lines):
    g = Grid(lines)

    locs = set(g.find("S"))
    splits = 0

    while locs:
        x, y = locs.pop()

        if g.get(x, y + 1) == "^":
            locs |= {(x - 1, y + 1), ((x + 1), y + 1)}
            splits += 1

        elif (g.get(x, y + 1)) == ".":
            locs |= { (x, y + 1) }

        g.set(x, y, "|")
        
    return splits

@cache
def get_paths(g, x, y):
    if g.get(x, y) == "^":
        return get_paths(g, x - 1, y + 1) + get_paths(g, x + 1, y + 1)
    elif g.get(x, y) == "." or g.get(x, y) == "S":
        return get_paths(g, x, y + 1)
    
    return 1

def task2(lines):
    g = Grid(lines)

    locs = g.find("S")
    return get_paths(g, *locs[0])

if __name__ == "__main__":
    # lines = get_input("sample-07")
    lines = get_input("07")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
