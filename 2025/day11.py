from helpers import *
from grid import *
from interval import *
from functools import cache

def task1(count_paths_func):
    return count_paths_func("you", "out")

def task2(count_paths_func):
    fft_to_dac = count_paths_func("svr", "fft") * count_paths_func("fft", "dac") * count_paths_func("dac", "out")
    dac_to_fft = count_paths_func("svr", "dac") * count_paths_func("dac", "fft") * count_paths_func("fft", "out")

    return fft_to_dac + dac_to_fft

if __name__ == "__main__":
    # lines = get_input("sample-11")
    lines = get_input("11")
    lines = [l.strip() for l in lines]

    dirs = { l.split(":")[0]: [c for c in l.split(":")[1].split(" ") if c] for l in lines }

    @cache
    def count_paths(cur, goal):
        return 1 if cur == goal else sum(count_paths(nxt, goal) for nxt in dirs.get(cur, []))
    
    print(task1(count_paths))
    print(task2(count_paths))
