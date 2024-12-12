from typing import Any, Iterable, Tuple

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

def tup_op(f, tup1, tup2):
    return tuple(map(f), zip(tup1, tup2))

ADD = lambda a, b: a + b
SUB = lambda a, b: a - b
MUL = lambda a, b: a * b
DIV = lambda a, b: a / b
