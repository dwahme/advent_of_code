from typing import Any, Iterable, Tuple
from numbers import Number
import re
from bisect import insort_left

def _reduce_list(arg):
    if type(arg) == list and len(arg) > 2:
        return [_reduce_list(a) for a in arg[:2]] + ["..."]

    return arg

def _get_str_arg(arg):
    return str(_reduce_list(arg)).replace("'...'", "...")

def call_and_print(fn, *args):
    str_args = ", ".join(_get_str_arg(arg) for arg in args)

    result = fn(*args)

    print(f"{fn.__name__}({str_args}) = {result}")
    return result

def get_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return lines

def get_input(file_code):
    return get_lines(f"inputs\{file_code}.in")

def flatten(nested_list: Iterable[Iterable[Any]]):
    return [x for xs in nested_list for x in xs]

def ADD(*tups: Tuple[Number, Number]):
    return (sum(a for a, _ in tups), sum(b for _, b in tups))

def SCALE(tup: Tuple[Number, Number], scale: Number):
    return (tup[0] * scale, tup[1]  * scale)

def find_nums(s: str, convert_to=float):
    return [ convert_to(x) for x in re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+', s)]

def a_star(start, goal_func, get_next_nodes_func, allow_multipath=False):
    """
    a* algorithm (or djikstra, depending on get_next_nodes_func)

    start: the node to start at
    goal_func: a function that returns whether a node is the goal. Can be "lamda x: x == goal"
    get_next_nodes_func: a function that returns the next nodes to try and their additional cost
        - if next_score contains a heuristic, this is a*, otherwise, djikstra
        - can just be "lambda cur_node: [(next_node, next_score), ...]"
    allow_multipath: whether or not we want to allow multiple shortest paths to the goal
    """

    to_visit = [(start, 0, [start])]

    visited = {}
    min_score = None

    while to_visit:
        node, score, path = to_visit.pop(0)

        # path is too long, stop searching
        if min_score is not None and score > min_score:
            break

        if goal_func(node) and (min_score is None or score < min_score):
            min_score = score

        if node in visited:
            # we have multiple shortest paths to this node
            if allow_multipath and score == visited[node][0]:
                visited[node][1].append(path)

            # this path is not the best path to the node, no need to continue
            else:
                continue
        else:
            # This is the first time we've seen this node, assume it's best path
            visited[node] = (score, [path])
        
        for new_node, add_score in get_next_nodes_func(node):
            item = (new_node, score + add_score, path + [new_node])
            insort_left(to_visit, item, key=lambda tup: tup[1])
    
    path_scores = [path_score for node, path_score in visited.items() if goal_func(node)]
    if not path_scores:
        return -1, None

    min_score = path_scores[0][0]
    paths = flatten([p for _, p in path_scores])

    return min_score, paths
