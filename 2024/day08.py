import helpers
from grid import *

def task1(lines):
    g = Grid(lines, sep="")
    out = g.map(lambda _: ".")

    for x, y in g.iterate_xy():
        if g.get(x, y) != ".":
            for new_x, new_y in g.iterate_xy():
                if (x, y) != (new_x, new_y) and g.get(x, y) == g.get(new_x, new_y):
                    dx = abs(x - new_x) * (-1 if new_x > x else 1)
                    dy = abs(y - new_y) * (-1 if new_y > y else 1)
                    out.set(x + dx, y + dy, "#")

    return sum(out.get(x, y) == "#" for x, y in out.iterate_xy())

def task2(lines):
    g = Grid(lines, sep="")
    out = g.map(lambda _: ".")

    for x, y in g.iterate_xy():
        if g.get(x, y) != ".":
            for new_x, new_y in g.iterate_xy():
                if (x, y) != (new_x, new_y) and g.get(x, y) == g.get(new_x, new_y):
                    dx = abs(x - new_x) * (-1 if new_x > x else 1)
                    dy = abs(y - new_y) * (-1 if new_y > y else 1)

                    i = 0
                    while g.get(x + dx * i, y + dy * i):
                        out.set(x + dx * i, y + dy * i, "#")
                        i += 1

    return sum(out.get(x, y) == "#" for x, y in out.iterate_xy())

if __name__ == "__main__":
    lines = helpers.get_input("08")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
