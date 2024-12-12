from helpers import *
from grid import *

def join(g: Grid, x, y, parent):
    kind, _ = g.get(x, y)
    g.set(x, y, (kind, parent))

    search = [(x + dx, y + dy) for dx, dy in CARDINAL_DIRS]
    for i, j in search:
        found = g.get(i, j)

        if found:
            found_kind, found_parent = found

            if found_parent is None and found_kind == kind:
                join(g, i, j, parent)

def join_plots(g: Grid):
    for x, y in g.iterate_xy():
        if g.get(x, y)[1] is None:
            join(g, x, y, (x, y))

def get_area(g: Grid, x, y):
    return sum(g.get(i, j)[1] == (x, y) for i, j in g.iterate_xy())

def get_perimeter(g: Grid, x, y):
    perim = 0

    for i, j in g.iterate_xy():
        if g.get(i, j)[1] == (x, y):
            search = [(i + dx, j + dy) for dx, dy in CARDINAL_DIRS]
            perim += len(CARDINAL_DIRS) - sum(p[1] == (x, y) for p in g.get_many(search) if p)

    return perim

def get_sides(g: Grid, x, y):
    # num corners == num sides
    corners = 0

    for i, j in g.iterate_xy():
        if g.get(i, j)[1] == (x, y):
            search = [(i + dx, j + dy) for dx, dy in ALL_DIRS]
            same = [ (a, b) for a, b in search if g.get(a, b) is not None and g.get(a, b)[1] == (x, y) ]

            # outer corners
            corners += (i + 1, j) not in same and (i, j + 1) not in same
            corners += (i + 1, j) not in same and (i, j - 1) not in same
            corners += (i - 1, j) not in same and (i, j + 1) not in same
            corners += (i - 1, j) not in same and (i, j - 1) not in same

            # inner corners
            corners += (i + 1, j) in same and (i, j + 1) in same and (i + 1, j + 1) not in same
            corners += (i - 1, j) in same and (i, j + 1) in same and (i - 1, j + 1) not in same
            corners += (i + 1, j) in same and (i, j - 1) in same and (i + 1, j - 1) not in same
            corners += (i - 1, j) in same and (i, j - 1) in same and (i - 1, j - 1) not in same

    return corners


def task1(g: Grid):
    join_plots(g)
    price = 0

    for x, y in g.iterate_xy():
        _, origin = g.get(x, y)

        if origin == (x, y):
            area = get_area(g, x, y)
            perim = get_perimeter(g, x, y)
            price += area * perim

    return price

def task2(g: Grid):
    join_plots(g)
    price = 0

    for x, y in g.iterate_xy():
        _, origin = g.get(x, y)

        if origin == (x, y):
            area = get_area(g, x, y)
            sides = get_sides(g, x, y)
            price += area * sides

    return price

if __name__ == "__main__":
    lines = get_input("sample-12-01")
    # lines = get_input("sample-12-02")
    # lines = get_input("sample-12-03")
    lines = get_input("12")
    lines = [l.strip() for l in lines]

    g = Grid(lines, sep="  ")
    g = g.map(lambda c: (c, None))
    
    print(task1(g.copy()))
    print(task2(g.copy()))
