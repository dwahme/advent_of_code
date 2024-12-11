from helpers import *
from grid import *

def get_reachable(g: Grid, x, y, cur_height):
    search = [g.get(x + 1, y), g.get(x - 1, y), g.get(x, y + 1), g.get(x, y - 1)]
    search = [s for s in search if s]
    return { r for height, reachable in search for r in reachable if height - 1 == cur_height and reachable is not None }

def get_score(g: Grid, x, y, cur_height):    
    search = [g.get(x + 1, y), g.get(x - 1, y), g.get(x, y + 1), g.get(x, y - 1)]
    search = [s for s in search if s]
    return sum(score for height, score in search if height - 1 == cur_height and score is not None)

def task1(lines):
    
    score_data = [[(None if i == "." else int(i), set()) for i in l] for l in lines]
    g = Grid(score_data)

    for x, y in g.iterate_xy():
        if g.get(x, y)[0] == 9:
            g.set(x, y, (9, {(x, y)}))

    for i in range(8, -1, -1):
        for x, y in g.iterate_xy():
            if g.get(x, y)[0] == i:
                reachable = get_reachable(g, x, y, i)
                g.set(x, y, (i, reachable))


    return sum(len(g.get(x, y)[1]) for x, y in g.iterate_xy() if g.get(x, y)[0] == 0)


def task2(lines):
    
    score_data = [[(None if i == "." else int(i), set()) for i in l] for l in lines]
    g = Grid(score_data)

    for x, y in g.iterate_xy():
        if g.get(x, y)[0] == 9:
            g.set(x, y, (9, 1))

    for i in range(8, -1, -1):
        for x, y in g.iterate_xy():
            if g.get(x, y)[0] == i:
                score = get_score(g, x, y, i)
                g.set(x, y, (i, score))

    return sum(g.get(x, y)[1] for x, y in g.iterate_xy() if g.get(x, y)[0] == 0)

if __name__ == "__main__":
    lines = get_input("10")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
