from helpers import *
from grid import *

def check_string(g, x, y, dx, dy, string):
    return g.get_many([(x + dx * i, y + dy * i) for i in range(len(string))]) == list(string)

def task1(lines):
    g = Grid(lines, sep="")
    return sum(check_string(g, x, y, dx, dy, "XMAS") for x, y in g.iterate_xy() for dx, dy in ALL_DIRS)

def check_cross(g, x, y):
    if g.get(x, y) != "A":
        return False

    return set(g.get_many([(x+1, y+1), (x-1, y-1)])) == set("MS") and set(g.get_many([(x-1, y+1), (x+1, y-1)])) == set("MS")

def task2(lines):
    g = Grid(lines)
    return sum([check_cross(g, x, y) for x, y in g.iterate_xy()])

if __name__ == "__main__":
    lines = get_input("04")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
