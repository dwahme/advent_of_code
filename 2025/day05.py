from helpers import *
from grid import *
from interval import *
from functools import cache

def task1(intervals, ingredients):
    return sum(any(g in i for i in intervals) for g in ingredients)

def task2(intervals):
    return sum(len(i) for i in Interval.bulk_union(intervals))

if __name__ == "__main__":
    # lines = get_input("sample-05")
    lines = get_input("05")
    lines = [l.strip() for l in lines]

    split = lines.index("")
    intervals = [ Interval(int(l.split("-")[0]), int(l.split("-")[1]) + 1) for l in lines[:split] ]
    ingredients = [ int(l) for l in lines[split + 1:] ]
    
    print(task1(intervals, ingredients))
    print(task2(intervals))
