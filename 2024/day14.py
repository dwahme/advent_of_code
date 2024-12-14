from helpers import *
from collections import Counter

def pos(p, v, steps, bound):
    return (p + v * steps) % bound

def quadrant(p, grid):
    return p > (grid // 2)

def task1(data, grid_x, grid_y):
    new_positions = [ (pos(px, vx, 100, grid_x), pos(py, vy, 100, grid_y)) for (px, py, vx, vy) in data ]

    new_positions = [ (x, y) for x, y in new_positions if x != grid_x // 2 and y != grid_y // 2]
    quadrants = [ (quadrant(x, grid_x), quadrant(y, grid_y)) for x, y in new_positions]

    a = 1
    for v in Counter(quadrants).values():
        a *= v

    return a

def task2(data, grid_x, grid_y):

    for i in range(100000):
        new_positions = [ (pos(px, vx, i, grid_x), pos(py, vy, i, grid_y)) for (px, py, vx, vy) in data ]

        if len(set(new_positions)) == len(new_positions):
            return i

    return None

if __name__ == "__main__":
    lines = get_input("14")
    lines = [l.strip() for l in lines]

    data = [ tuple(find_nums(l, int)) for l in lines ]
    
    print(task1(data, 101, 103))
    print(task2(data, 101, 103))
