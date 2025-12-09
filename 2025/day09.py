from helpers import *
from grid import *
from interval import *
from functools import cache
from itertools import combinations
import shapely

def area(p, q):
    return (abs(p[0] - q[0])+1) * (abs(p[1] - q[1])+1)

def task1(lines):
    coords = [ list(map(int, line.split(","))) for line in lines ]

    return max(area(p, q) for p, q in combinations(coords, 2))

def task2(lines):
    coords = [ tuple(map(int, line.split(","))) for line in lines ]

    s = shapely.Polygon(coords)
    
    return max((area(p, q), p, q) for p, q in combinations(coords, 2) if s.contains(shapely.box(min(p[0], q[0]), min(p[1], q[1]), max(p[0], q[0]), max(p[1], q[1]))))

if __name__ == "__main__":
    # lines = get_input("sample-09")
    lines = get_input("09")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
