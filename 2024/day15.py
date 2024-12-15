from helpers import *
from grid import *

MOVES = "v^<>"
DIRS = [UP, DOWN, LEFT, RIGHT]

def get_move(m):
    return DIRS[MOVES.index(m)]

def scale(c):
    if c == "#": return "##"
    if c == "O": return "[]"
    if c == ".": return ".."
    if c == "@": return "@."
    return None

def check_push_r(g: Grid, pos, dir):
    
    target = g.get(*ADD(pos, dir))

    if target == "#":
        return False
    
    if target == ".":
        return True

    if dir in {LEFT, RIGHT} or target == "O":
        return check_push_r(g, ADD(pos, dir), dir)

    else:
        # moving up or down, make sure that we account for boxes
        assert(target in "[]")
        extra_check = RIGHT if target == "[" else LEFT
        return check_push_r(g, ADD(pos, dir), dir) and check_push_r(g, ADD(ADD(pos, extra_check), dir), dir)

def push_r(g: Grid, pos, dir):

    me = g.get(*pos)
    target = g.get(*ADD(pos, dir))

    assert(target in "[]O.")
    assert(me in "[]O@")
    
    # Check if we need to push an extra side of a box
    if dir in {UP, DOWN} and target in "[]":
        extra_push = RIGHT if target == "[" else LEFT
        push_r(g, ADD(ADD(pos, extra_push), dir), dir)

    if target in "[]O":
        push_r(g, ADD(pos, dir), dir)

    g.set(*ADD(pos, dir), me)
    g.set(*pos, ".")


def task1(g: Grid, moves):
    
    pos = [p for p in g.iterate_xy() if g.get(*p) == "@"][0]

    for m in moves:
        d = get_move(m)
        can_push = check_push_r(g, pos, d)

        if can_push:
            push_r(g, pos, d)
            g.set(*pos, ".")
            pos = ADD(pos, d)

    return sum(x+y*100 for x, y in g.iterate_xy() if g.get(x, y) == "O")

def task2(g: Grid, moves):

    g = g.map(scale)
    g.grid = [flatten(l) for l in g.grid]
    
    pos = [p for p in g.iterate_xy() if g.get(*p) == "@"][0]
    
    for m in moves:
        d = get_move(m)
        can_push = check_push_r(g, pos, d)

        if can_push:
            push_r(g, pos, d)
            g.set(*pos, ".")
            pos = ADD(pos, d)
        
    return sum(x+y*100 for x, y in g.iterate_xy() if g.get(x, y) == "[")

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
