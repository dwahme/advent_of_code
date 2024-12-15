from helpers import *
from grid import *

def check_string(g, pos, dir, string):
    return g.get_many([ADD(pos, SCALE(dir, i)) for i in range(len(string))]) == list(string)

def task1(g):
    return sum(check_string(g, pos, dir, "XMAS") for pos in g.iterate_xy() for dir in ALL_DIRS)

def check_cross(g: Grid, pos):
    return g.get(*pos) == "A" and set("MS") == set(g.get_many([ADD(pos, UP_L), ADD(pos, DOWN_R)])) == set(g.get_many([ADD(pos, UP_R), ADD(pos, DOWN_L)]))

def task2(g):
    return sum([check_cross(g, pos) for pos in g.iterate_xy()])

if __name__ == "__main__":
    lines = get_input("04")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    
    print(task1(g))
    print(task2(g))
