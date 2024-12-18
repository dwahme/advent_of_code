from helpers import *
from grid import *

def next_func(coords, size, num_corrupt):

    def get_next(cur_node):
        next_nodes = []

        for d in CARDINAL_DIRS:
            x, y = ADD(cur_node, d)

            if 0 <= x <= size and 0 <= y <= size and (x, y) not in coords[:num_corrupt + 1]:
                next_nodes.append(((x, y), 1))

        return next_nodes

    return get_next

def goal_func(end):
    return lambda node: node == end

def task1(size, coords):
    return a_star((0, 0), goal_func((size, size)), next_func(coords, size, 1024))[0]

def task2(size, coords):

    lo = 0
    hi = len(coords)

    while hi - lo > 1:
        mid = (lo+hi) // 2
        p_len, _ = a_star((0, 0), goal_func((size, size)), next_func(coords, size, mid))

        if p_len == -1:
            hi = mid
        else:
            lo = mid

    return ",".join(str(c) for c in coords[hi])

if __name__ == "__main__":
    lines = get_input("sample-18-01")
    lines = get_input("18")
    lines = [l.strip() for l in lines]

    coords = [ tuple(find_nums(l, int)) for l in lines ]
    bounds = 70
    
    print(task1(bounds, coords))
    print(task2(bounds, coords))
