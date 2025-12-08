from helpers import *
from grid import *
from interval import *
from functools import cache
from itertools import combinations
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        self.parent[self.find(p)] = self.find(q)

def dist(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    return abs(x1 - x2)**2 + abs(y1 - y2)**2 + abs(z1 - z2)**2

def task1(lines):
    points = { tuple(map(int, line.split(","))): idx for idx, line in enumerate(lines) }
    distances = [ (dist(p, q), p , q) for p, q in combinations(points, 2) ]

    uf = UnionFind(len(points))
    for _, p, q in sorted(distances)[:1000]:
        uf.union(points[p], points[q])

    dd = defaultdict(int)
    for i in uf.parent:
        dd[uf.find(i)] += 1
    sizes = sorted(dd.values())

    return sizes[-1] * sizes[-2] * sizes[-3]

def task2(lines):
    points = { tuple(map(int, line.split(","))): idx for idx, line in enumerate(lines) }
    distances = [ (dist(p, q), p , q) for p, q in combinations(points.keys(), 2) ]

    uf = UnionFind(len(points))

    connected = 0
    for _, p, q in sorted(distances):
        connected += uf.find(points[p]) != uf.find(points[q])
        uf.union(points[p], points[q])

        if connected == len(points) - 1:
            return p[0] * q[0]

    # we should never get here
    return None

if __name__ == "__main__":
    # lines = get_input("sample-08")
    lines = get_input("08")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
