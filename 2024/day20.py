from helpers import *
from grid import *

def get_coord_distances(g: Grid, end):

    to_visit = [(end, 0)]
    visited = set()
    distances = {}

    while to_visit:
        p, dist = to_visit.pop(0)

        visited.add(p)

        distances[p] = dist

        for d in CARDINAL_DIRS:
            nxt = ADD(p, d)

            if g.get(*nxt) != "#" and nxt not in visited:
                to_visit.append((nxt, dist + 1))
    
    return distances

def get_dist(a, b):
    ax, ay = a
    bx, by = b
    return abs(bx - ax) + abs(by - ay)

def task1(g: Grid):

    saved = {}

    end = g.find("E")[0]

    distances = get_coord_distances(g, end)

    checked = set()

    to_jump = list(distances.items())

    for i, tup1 in enumerate(to_jump):
        p1, d1 = to_jump[i]

        for p2, d2 in to_jump[i + 1:]:
            savings = d2 - d1 - get_dist(p1, p2)

            if savings > 0 and get_dist(p1, p2) <= 2:
                saved[savings] = saved.get(savings, 0) + 1

    return sum(v for k, v in saved.items() if k >= 100)

def task2(g: Grid):

    saved = {}

    end = g.find("E")[0]

    distances = get_coord_distances(g, end)

    checked = set()

    to_jump = list(distances.items())

    for i, tup1 in enumerate(to_jump):
        p1, d1 = to_jump[i]

        for p2, d2 in to_jump[i + 1:]:
            savings = d2 - d1 - get_dist(p1, p2)

            if savings > 0 and get_dist(p1, p2) <= 20:
                saved[savings] = saved.get(savings, 0) + 1

    return sum(v for k, v in saved.items() if k >= 100)

if __name__ == "__main__":
    lines = get_input("sample-20")
    lines = get_input("20")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    
    print(task1(g))
    print(task2(g))
