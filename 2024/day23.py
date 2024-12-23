from helpers import *
from grid import *
from functools import cache
import networkx as nx

def task1(network):
    return sum(len(c) == 3 and any(n.startswith("t") for n in c) for c in nx.enumerate_all_cliques(network))

def task2(network):
    best = max((c for c in nx.enumerate_all_cliques(network)), key=len)
    return ",".join(sorted(best))

if __name__ == "__main__":
    lines = get_input("sample-23")
    lines = get_input("23")
    lines = [l.strip() for l in lines]

    connections = [tuple(s.split("-")) for s in lines]
    network = nx.Graph()
    for e in connections:
        g.add_edge(*e)

    print(task1(network))
    print(task2(network))
