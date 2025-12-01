from helpers import *
from grid import *
from functools import cache

def task1(lines):
    net = 50
    at_0 = 0

    for l in lines:
        dir = 1 if l[0] == "R" else -1
        steps = int(l[1:])

        lands_at_0 = (net + dir * steps) % 100 == 0
        if lands_at_0:
            at_0 += 1
            
        net += dir * steps
        
    return at_0

def task2(lines):
    net = 50
    at_0 = 0

    for l in lines:
        dir = 1 if l[0] == "R" else -1
        steps = int(l[1:])

        for _ in range(steps):
            net += dir
            at_0 += net % 100 == 0
        
    return at_0

if __name__ == "__main__":
    # lines = get_input("sample-01")
    lines = get_input("01")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
