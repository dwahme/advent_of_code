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

    for p, dist in distances.items():
        
        for d1 in CARDINAL_DIRS:
            for d2 in CARDINAL_DIRS + [(0, 0)]:

                jump = ADD(p, d1, d2)
                new_dist = distances.get(jump, 0) + (2 if d2 != (0, 0) else 1)

                if g.get(*jump) in [".", "E"] and new_dist < dist:
                    # print(f"{p} -> {jump} ({new_dist} - {dist} = {dist - new_dist})")
                    saved[dist - new_dist] = saved.get(dist - new_dist, 0) + 1

    # pprint(saved)

    return sum(v for k, v in saved.items() if k >= 100)

def task2(g: Grid):
    return None

if __name__ == "__main__":
    lines = get_input("sample-20")
    lines = get_input("20")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    
    print(task1(g))
    print(task2(g))
