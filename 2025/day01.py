from helpers import *
from grid import *
from functools import cache

def do_turns(turns):
    pos = 50
    lands_at_0 = 0
    crosses_0 = 0

    for t in turns:
        for _ in range(int(t[1:])):
            pos += 1 if t[0] == "R" else -1
            crosses_0 += 1 if pos % 100 == 0 else 0
        lands_at_0 += 1 if pos % 100 == 0 else 0

    return lands_at_0, crosses_0

def task1(lines):
    return do_turns(lines)[0]

def task2(lines):
    return do_turns(lines)[1]

if __name__ == "__main__":
    # lines = get_input("sample-01")
    lines = get_input("01")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
