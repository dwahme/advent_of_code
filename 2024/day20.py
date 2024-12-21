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

def get_saved(distances, p1, p2):
    return distances[p2] - distances[p1] - get_dist(p1, p2) if p2 in distances else -1

def get_savings(g: Grid, jump):

    end = g.find("E")[0]
    distances = get_coord_distances(g, end)

    return sum(
        get_saved(distances, p1, ADD(p1, (i, j))) >= 100 
        for p1 in distances.keys()
        for i in range(-jump, jump + 1)
        for j in range(-(jump - abs(i)), jump - abs(i) + 1)
    )

def task1(g: Grid):
    return get_savings(g, 2)

def task2(g: Grid):
    return get_savings(g, 20)

if __name__ == "__main__":
    lines = get_input("sample-20")
    lines = get_input("20")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    
    print(task1(g))
    print(task2(g))
