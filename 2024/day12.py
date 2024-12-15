from helpers import *
from grid import *

def join_plots(g: Grid):

    plots = []
    
    for x, y in g.iterate_xy():

        search = [(x + dx, y + dy) for dx, dy in CARDINAL_DIRS]

        overlaps = {i for s in search for i, p in enumerate(plots) if s in p and g.get(*s) == g.get(x, y)}
        overlaps = [plots[i] for i in overlaps]

        if not overlaps:
            plots += [ {(x, y)} ]

        if overlaps:
            overlaps[0] |= {(x, y)}

            for o in overlaps[1:]:
                overlaps[0] |= o
                plots.remove(o)

    return plots

def get_area(plot):
    return len(plot)

def get_perimeter(plot):
    search = [(x + dx, y + dy) for dx, dy in CARDINAL_DIRS for x, y in plot]
    return sum(s not in plot for s in search)

def outside_corner(same, x, y, dx, dy):
    return (x + dx, y) not in same and (x, y + dy) not in same

def inside_corner(same, x, y, dx, dy):
    return (x + dx, y) in same and (x, y + dy) in same and (x + dx, y + dy) not in same

def get_sides(plot):
    # num corners == num sides
    return sum(inside_corner(plot, *p, *d) or outside_corner(plot, *p, *d) for d in DIAG_DIRS for p in plot)

def task1(plots):
    return sum(get_area(p) * get_perimeter(p) for p in plots)

def task2(plots):
    return sum(get_area(p) * get_sides(p) for p in plots)

if __name__ == "__main__":
    lines = get_input("sample-12-01")
    # lines = get_input("sample-12-02")
    # lines = get_input("sample-12-03")
    lines = get_input("12")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    plots = join_plots(g)
    
    print(task1(plots))
    print(task2(plots))
