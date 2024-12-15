from helpers import *
from grid import *

MOVES = "v^<>"
DIRS = [UP, DOWN, LEFT, RIGHT]

def get_move(m):
    return DIRS[MOVES.index(m)]

def extra_dir(target):
    return RIGHT if target == "[" else LEFT

def scale(c):
    if c == "#": return "##"
    if c == "O": return "[]"
    if c == ".": return ".."
    if c == "@": return "@."
    return None

def check_push_r(g: Grid, pos, dir):
    
    target = g.get(*ADD(pos, dir))

    if target == "#": return False
    if target == ".": return True
    
    extra = True
    if dir in {UP, DOWN} and target in "[]":
        extra = check_push_r(g, ADD(ADD(pos, extra_dir(target)), dir), dir)

    return check_push_r(g, ADD(pos, dir), dir) and extra

def push_r(g: Grid, pos, dir):

    me = g.get(*pos)
    target = g.get(*ADD(pos, dir))

    # Check if we need to push an extra side of a box
    if dir in {UP, DOWN} and target in "[]":
        push_r(g, ADD(ADD(pos, extra_dir(target)), dir), dir)

    if target in "[]O":
        push_r(g, ADD(pos, dir), dir)

    g.set(*ADD(pos, dir), me)
    g.set(*pos, ".")

def sim(g: Grid, moves):
    pos = [p for p in g.iterate_xy() if g.get(*p) == "@"][0]

    for m in moves:
        d = get_move(m)
        can_push = check_push_r(g, pos, d)

        if can_push:
            push_r(g, pos, d)
            pos = ADD(pos, d)

    return sum(x+y*100 for x, y in g.iterate_xy() if g.get(x, y) in "O[")

def task1(g: Grid, moves):
    return sim(g, moves)

def task2(g: Grid, moves):
    g = g.map(scale)
    g.grid = [flatten(l) for l in g.grid]

    return sim(g, moves)

if __name__ == "__main__":
    lines = get_input("sample-15-01")
    # lines = get_input("sample-15-02")
    lines = get_input("sample-15-03")
    lines = get_input("15")
    lines = [l.strip() for l in lines]

    moves = "".join([l for l in lines if l.strip() and "#" not in l])

    grid_lines = [l for l in lines if "#" in l]
    g = Grid(grid_lines)

    print(task1(g.copy(), moves))
    print(task2(g.copy(), moves))
