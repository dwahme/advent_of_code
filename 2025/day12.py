from helpers import *
from grid import *
from interval import *
from functools import cache

def get_present_size(present):
    return sum(val == "#" for r in present for val in r)

def task1(lines):
    sizes = { i: get_present_size(lines[i*5+1:i*5+4]) for i in range(6) }
    plots = [ tuple(find_nums(l, convert_to=int)) for l in lines[30:] ]   
    return sum(sum(sizes[i] * n for i, n in enumerate(counts)) <= height * width for height, width, *counts in plots)

def task2(lines):
    return None

if __name__ == "__main__":
    # lines = get_input("sample-12")
    lines = get_input("12")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
