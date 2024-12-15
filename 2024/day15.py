from helpers import *
from grid import *

DIR_MAP = { "^": UP, "v": DOWN, "<": LEFT, ">": RIGHT }
SCALEUP = { "#": "##", "O": "[]", ".": "..", "@": "@." }

def extra_dir(target):
    return RIGHT if target == "[" else LEFT

def can_push(g: Grid, pos, dir):
    target = g.get(*ADD(pos, dir))

    if target == "#": return False
    if target == ".": return True
    
    extra = True
    if dir in {UP, DOWN} and target in "[]":
        extra = can_push(g, ADD(pos, dir, extra_dir(target)), dir)

    return can_push(g, ADD(pos, dir), dir) and extra

def push(g: Grid, pos, dir):
    target = g.get(*ADD(pos, dir))

    if dir in {UP, DOWN} and target in "[]":
        push(g, ADD(pos, dir, extra_dir(target)), dir)

    if target in "[]O":
        push(g, ADD(pos, dir), dir)

    g.set(*ADD(pos, dir), g.get(*pos))
    g.set(*pos, ".")

def sim(g: Grid, moves):
    pos = [p for p in g.iterate_xy() if g.get(*p) == "@"][0]

    for m in moves:
        d = DIR_MAP[m]

        if can_push(g, pos, d):
            push(g, pos, d)
            pos = ADD(pos, d)

    return sum(x+y*100 for x, y in g.iterate_xy() if g.get(x, y) in "O[")

def task1(g: Grid, moves):
    return sim(g, moves)

def task2(g: Grid, moves):
    g = g.map(lambda x: SCALEUP[x])
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
