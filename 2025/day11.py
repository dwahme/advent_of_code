from helpers import *
from grid import *
from interval import *
from functools import cache

def task1(lines):
    d = { l.split(":")[0]: [c for c in l.split(":")[1].split(" ") if c] for l in lines }
    
    goal_func = lambda x: x == "out"
    next_func = lambda cur: [ (nxt, 0) for nxt in d[cur] ] if cur != "out" else []
    _, paths = a_star("you", goal_func, next_func, allow_multipath=True)

    return len(paths)

def task2(lines):
    d = { l.split(":")[0]: [c for c in l.split(":")[1].split(" ") if c] for l in lines }
    
    @cache
    def count_paths(cur, goal):
        return 1 if cur == goal else sum([ count_paths(nxt, goal) for nxt in d.get(cur, []) ])
    
    fft_to_dac = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")
    dac_to_fft = count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")

    return fft_to_dac + dac_to_fft

if __name__ == "__main__":
    # lines = get_input("sample-11")
    lines = get_input("11")
    lines = [l.strip() for l in lines]
    
    # print(task1(lines))
    print(task2(lines))
