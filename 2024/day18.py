from helpers import *
from grid import *

def get_next_nodes_func(pre_fill, coords, bounds):

    def get_next(cur_node, path):
        next_nodes = []

        p = cur_node

        for d in CARDINAL_DIRS:
            x, y = ADD(p, d)

            if 0 <= x < bounds and 0 <= y < bounds and (x, y) not in coords[:pre_fill + len(path)]:
                next_nodes.append(((x, y), 1))

        return next_nodes

    return get_next

def get_next_nodes_func2(pre_fill, coords, bounds):

    def get_next(cur_node, path):
        next_nodes = []

        p = cur_node

        for d in CARDINAL_DIRS:
            x, y = ADD(p, d)

            if 0 <= x < bounds and 0 <= y < bounds and (x, y) not in coords[:pre_fill + 1]:
                next_nodes.append(((x, y), 1))

        return next_nodes

    return get_next

def get_goal_func(end):
    return lambda node: node == end

def task1(g_size, coords, pre_fill):

    p_len, _ = a_star((0, 0), get_goal_func((g_size - 1, g_size - 1)), get_next_nodes_func(pre_fill, coords, g_size))
    # print(p_len, path)

    return p_len

def task2(g_size, coords, pre_fill):

    lo = 0
    hi = len(coords)

    while hi - lo > 1:
        mid = (lo+hi) // 2

        p_len, path = a_star((0, 0), get_goal_func((g_size - 1, g_size - 1)), get_next_nodes_func2(mid, coords, g_size))

        if p_len == -1:
            # too high
            hi = mid
        else:
            lo = mid

    print(lo, hi)

    print(coords[lo])
    print(coords[hi])

    print(a_star((0, 0), get_goal_func((g_size - 1, g_size - 1)), get_next_nodes_func2(lo, coords, g_size))[0])
    print(a_star((0, 0), get_goal_func((g_size - 1, g_size - 1)), get_next_nodes_func2(hi, coords, g_size))[0])

    print(p_len, path)

    return ",".join(str(c) for c in coords[hi])

if __name__ == "__main__":
    lines = get_input("sample-18-01")
    lines = get_input("18")
    lines = [l.strip() for l in lines]

    coords = [ tuple(find_nums(l, int)) for l in lines ]
    # bounds = 7
    bounds = 71
    pre_fill = 1024
    
    print(task1(bounds, coords, pre_fill))
    print(task2(bounds, coords, pre_fill))
