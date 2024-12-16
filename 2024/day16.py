from helpers import *
from grid import *
from bisect import insort_left

def search(g: Grid, start, goal):
    
    insort_key = lambda tup: tup[2]
    to_visit = [(start, RIGHT, 0, [(start, RIGHT)])]

    # (pos, dir): (best_score, list of paths to pos)
    visited = {}
    min_score = None

    while to_visit:
        pos, dir, score, path = to_visit.pop(0)

        if min_score is None and pos == goal:
            min_score = score
        
        # path is too long, stop searching
        if min_score is not None and score > min_score:
            break

        new_path = path + [(pos, dir)]

        if (pos, dir) in visited:
            cur_score, cur_paths = visited[(pos, dir)]

            if score < cur_score:
                visited[(pos, dir)] = (score, [new_path])
            elif score == cur_score:
                cur_paths.append(new_path)
            else:
                continue
        else:
            visited[(pos, dir)] = (score, [new_path])
        
        # try move forward
        if g.get(*ADD(pos, dir)) != "#":
            item = (ADD(pos, dir), dir, score + 1, new_path)
            insort_left(to_visit, item, key=insort_key)

        # try turn
        turns = [RIGHT, LEFT] if dir in {UP, DOWN} else [UP, DOWN]
        for t in turns:
            item = (pos, t, score + 1000, new_path)
            insort_left(to_visit, item, key=insort_key)

    path_scores = [visited[p, d] for p, d in visited.keys() if p == goal]
    min_score = path_scores[0][0]
    paths = flatten([p for _, p in path_scores])

    return min_score, paths


def task1(g: Grid):

    pos = g.find("S")[0]
    goal = g.find("E")[0]

    return search(g, pos, goal)[0]

def task2(g: Grid):

    pos = g.find("S")[0]
    goal = g.find("E")[0]
    paths = search(g, pos, goal)[1]

    return len(set(p for path in paths for p, _ in path))

if __name__ == "__main__":
    lines = get_input("sample-16-00")
    # lines = get_input("sample-16-01")
    # lines = get_input("sample-16-02")
    lines = get_input("16")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    
    print(task1(g.copy()))
    print(task2(g.copy()))
