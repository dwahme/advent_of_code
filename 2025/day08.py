from helpers import *
from grid import *
from interval import *
from functools import cache
from collections import defaultdict

def dist(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    return abs(x1 - x2)**2 + abs(y1 - y2)**2 + abs(z1 - z2)**2

def task1(points, distances):
    uf = UnionFind(len(points))

    for _, p, q in distances[:1000]:
        uf.union(p, q)

    dd = defaultdict(int)
    for i in uf.parent:
        dd[uf.find(i)] += 1

    sizes = sorted(dd.values())
    return sizes[-1] * sizes[-2] * sizes[-3]

def task2(points, distances):
    uf = UnionFind(len(points))

    connected = 0
    for _, p, q in distances:
        connected += 1 if uf.find(p) != uf.find(q) else 0
        uf.union(p, q)

        if connected == len(points) - 1:
            return points[p][0] * points[q][0]

    # we should never get here
    return None

if __name__ == "__main__":
    # lines = get_input("sample-08")
    lines = get_input("08")
    lines = [l.strip() for l in lines]

    points = [ tuple(map(int, line.split(","))) for line in lines ]
    distances = sorted(
        (dist(points[p], points[q]), p , q)
        for p in range(len(points))
        for q in range(p+1, len(points))
    )

    print(task1(points, distances))
    print(task2(points, distances))
