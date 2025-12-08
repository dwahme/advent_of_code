from helpers import *
from grid import *
from interval import *
from functools import cache
from collections import Counter

def dist(p, q):
    return sum(abs(a - b)**2 for a, b in zip(p, q))

def task1(points, distances):
    uf = UnionFind(len(points))
    [ uf.union(p, q) for _, p, q in distances[:1000] ]
    c = Counter(uf.find(i) for i in uf.parent)
    return reduce(lambda x, p: x * p[1], c.most_common(3), 1)

def task2(points, distances):
    uf = UnionFind(len(points))
    p, q = [ (p, q) for _, p, q in distances if uf.union(p, q) is not None ][-1]
    return points[p][0] * points[q][0]

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
