from helpers import *
from grid import *

def bfs(g: Grid, start, goal):
    
    to_visit = [(start, RIGHT, 0)]

    visited = set()
    

    while to_visit:

        pos, dir, score = to_visit.pop(0)
        # print(f"checking {pos}, {dir}, {score}")

        if (pos, dir) in visited:
            continue

        visited.add((pos, dir))

        if pos == goal:
            return score
        
        # try move forward
        if g.get(*ADD(pos, dir)) != "#":
            to_visit.append((ADD(pos, dir), dir, score + 1))

        # try turn
        turns = [RIGHT, LEFT] if dir in {UP, DOWN} else [UP, DOWN]
        for t in turns:
            to_visit.append((pos, t, score + 1000))

        to_visit = sorted(to_visit, key=lambda tup: tup[2])

def super_bfs(g: Grid, start, goal):
    
    to_visit = [(start, RIGHT, 0, [(start, RIGHT)])]

    # (pos, dir): (best_score, list of paths)
    visited = {}

    min_score = None

    while to_visit:

        pos, dir, score, path = to_visit.pop(0)

        if (pos, dir) in visited:
            if score < visited[(pos, dir)][0]:
                visited[(pos, dir)] = (score, [path + [(pos, dir)]])
            elif score == visited[(pos, dir)][0]:
                visited[(pos, dir)] = (score, visited[(pos, dir)][1] + [path + [(pos, dir)]])
            else:
                continue
        else:
            visited[(pos, dir)] = (score, [path + [(pos, dir)]])
        
        # try move forward
        if g.get(*ADD(pos, dir)) != "#":
            to_visit.append((ADD(pos, dir), dir, score + 1, path + [(pos, dir)]))

        # try turn
        turns = [RIGHT, LEFT] if dir in {UP, DOWN} else [UP, DOWN]
        for t in turns:
            to_visit.append((pos, t, score + 1000, path + [(pos, dir)]))

        to_visit = sorted(to_visit, key=lambda tup: tup[2])
    


    paths = [visited[p, d] for p, d in visited.keys() if p == goal]
    for p in paths:
        print(p)
    min_score = min(s for s, _ in paths)
    best_paths = [p for s, p in paths if s == min_score]

    return best_paths


def task1(g: Grid):

    pos = g.find("S")[0]
    goal = g.find("E")[0]

    return bfs(g, pos, goal)

def task2(g: Grid):

    pos = g.find("S")[0]
    goal = g.find("E")[0]

    paths = super_bfs(g, pos, goal)

    print(paths)

    for path in paths[0]:
        print(path)
        for p, d in path:
            g.set(*p, "O")

    print(g)

    # print(flatten(paths))
    return sum(g.get(*p) == "O" for p in g.iterate_xy())

if __name__ == "__main__":
    lines = get_input("sample-16-00")
    lines = get_input("sample-16-01")
    lines = get_input("sample-16-02")
    lines = get_input("16")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    print(g)
    
    # print(task1(g))
    print(task2(g))
