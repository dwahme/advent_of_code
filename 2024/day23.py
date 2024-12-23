from helpers import *
from grid import *
from functools import cache
import networkx as nx

def task1(connections):

    g = nx.Graph()
    for e in connections:
        g.add_edge(*e)
    
    return sum(len(c) == 3 and any(n.startswith("t") for n in c) for c in nx.enumerate_all_cliques(g))

def task2(connections):

    g = nx.Graph()
    for e in connections:
        g.add_edge(*e)
    
    best = max((c for c in nx.enumerate_all_cliques(g)), key=len)
    
    return ",".join(sorted(best))

if __name__ == "__main__":
    lines = get_input("sample-23")
    lines = get_input("23")
    lines = [l.strip() for l in lines]

    connections = [tuple(s.split("-")) for s in lines]

    print(task1(connections))
    print(task2(connections))
