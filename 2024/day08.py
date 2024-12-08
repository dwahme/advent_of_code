import helpers
from grid import *

def task1(lines):
    g = Grid(lines, sep="")
    out = g.copy()
    
    for y in out.grid:
        for x in range(len(y)):
            y[x] = "."
    
    # print(g)
    # print()
    # print(out)

    for y in range(len(g.grid)):
        for x in range(len(g.grid[y])):
            if g.grid[y][x] != ".":

                # prob can start at y here
                for new_y in range(len(g.grid)):
                    for new_x in range(len(g.grid[y])):
                        if g.grid[y][x] == g.grid[new_y][new_x] and y != new_y and x != new_x:

                            set_y = y + (abs(y - new_y) * (-1 if new_y > y else 1))
                            set_x = x + (abs(x - new_x) * (-1 if new_x > x else 1))

                            if g.get(set_x, set_y):
                                out.grid[set_y][set_x] = "#"


    # print()
    # print(out)
    return sum(out.grid[y][x] == "#" for y in range(len(out.grid)) for x in range(len(out.grid[y])))

def task2(lines):
    g = Grid(lines, sep="")
    out = g.copy()
    
    for y in out.grid:
        for x in range(len(y)):
            y[x] = "."
    
    # print(g)
    # print()
    # print(out)

    for y in range(len(g.grid)):
        for x in range(len(g.grid[y])):
            if g.grid[y][x] != ".":
                print(x, y)

                # prob can start at y here
                for new_y in range(len(g.grid)):
                    for new_x in range(len(g.grid[y])):
                        if g.grid[y][x] == g.grid[new_y][new_x] and y != new_y and x != new_x:

                            dy = (abs(y - new_y) * (-1 if new_y > y else 1))
                            dx = (abs(x - new_x) * (-1 if new_x > x else 1))

                            for i in range(0, len(g.grid)):
                                if g.get(x + dx * i, y + dy * i):
                                    out.grid[y + dy * i][x + dx * i] = "#"
                                else:
                                    break


    print()
    print(out)
    return sum(out.grid[y][x] == "#" for y in range(len(out.grid)) for x in range(len(out.grid[y])))

if __name__ == "__main__":
    lines = helpers.get_input("08")
    # lines = helpers.get_input("sample-08-02")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
