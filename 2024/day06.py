from helpers import *
from grid import *

DIRS = [DOWN, RIGHT, UP, LEFT]

def run_sim(g: Grid, pos):
    dir_idx = 0
    move_list = set()

    while True:
        new_pos = ADD(pos, DIRS[dir_idx])

        # infinite loop
        move = (pos, new_pos)
        if move in move_list:
            return g, True

        # guard walked off grid
        if not g.in_bounds(*new_pos):
            g.set(*pos, "X")
            return g, False
        
        # rotate the guard
        if g.get(*new_pos) in "#O":
            dir_idx = (dir_idx + 1) % len(DIRS)

        # move the guard
        else:
            g.set(*pos, "X")
            move_list.add(move)
            pos = new_pos

def task1(g: Grid, start):
    return sum([g.get(*pos) == "X" for pos in run_sim(g, start)[0].iterate_xy()])

def task2(g: Grid, start):
    solved = run_sim(g.copy(), start)[0]
    return sum(run_sim(g.copy().set(*pos, "O"), start)[1] for pos in g.iterate_xy() if g.get(*pos) not in "^#" and solved.get(*pos) == "X")

if __name__ == "__main__":
    lines = get_input("sample-06")
    lines = get_input("06")
    lines = [l.strip() for l in lines]

    g = Grid(lines, sep="")
    start = [pos for pos in g.iterate_xy() if g.get(*pos) == "^"][0]
    
    print(task1(g.copy(), start))
    print(task2(g.copy(), start))
