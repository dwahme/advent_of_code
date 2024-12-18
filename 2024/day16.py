from helpers import *
from grid import *

def get_next_nodes_func(g: Grid):

    def get_next(cur_node, _):
        next_nodes = []

        p, d = cur_node

        if g.get(*ADD(p, d)) != "#":
            next_nodes.append(((ADD(p, d), d), 1))

        turns = [RIGHT, LEFT] if d in {UP, DOWN} else [UP, DOWN]
        for t in turns:
            next_nodes.append(((p, t), 1000))
        
        return next_nodes

    return get_next

def get_goal_func(end):
    return lambda node: node[0] == end

def task1(g: Grid):

    pos = g.find("S")[0]
    goal = g.find("E")[0]

    return a_star((pos, RIGHT), get_goal_func(goal), get_next_nodes_func(g))[0]

def task2(g: Grid):

    pos = g.find("S")[0]
    goal = g.find("E")[0]
    paths = a_star((pos, RIGHT), get_goal_func(goal), get_next_nodes_func(g), allow_multipath=True)[1]

    return len(set(p for path in paths for p, _ in path))

if __name__ == "__main__":
    lines = get_input("sample-16-00")
    # lines = get_input("sample-16-01")
    # lines = get_input("sample-16-02")
    lines = get_input("16")
    lines = [l.strip() for l in lines]

    g = Grid(lines)
    
    print(task1(g.copy()))
    print(task2(g.copy()))
