from helpers import *
from grid import *
from interval import *
from functools import cache

def get_splits(g, pos):
    val = g.get(*pos)
    g.set(*pos, "|")

    if val == "^":
        return get_splits(g, ADD(pos, DOWN_L)) + get_splits(g, ADD(pos, DOWN_R))
    elif val == "." or val == "S":
        return get_splits(g, ADD(pos, DOWN))
    return 1

def task1(lines):
    g = Grid(lines)
    return get_splits(g, g.find("S")[0])

@cache
def get_paths(g, pos):
    val = g.get(*pos)

    if val == "^":
        return get_paths(g, ADD(pos, DOWN_L)) + get_paths(g, ADD(pos, DOWN_R))
    elif val == "." or val == "S":
        return get_paths(g, ADD(pos, DOWN))
    return 1

def task2(lines):
    g = Grid(lines)
    return get_paths(g, g.find("S")[0])

if __name__ == "__main__":
    # lines = get_input("sample-07")
    lines = get_input("07")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
