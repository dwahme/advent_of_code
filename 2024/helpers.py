from typing import Any, Iterable, Tuple
from numbers import Number
import re

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

def ADD(tup1: Tuple[Number, Number], tup2: Tuple[Number, Number]):
    return (tup1[0] + tup2[0], tup1[1] + tup2[1])

def find_nums(s: str, convert_to=float):
    return [ convert_to(x) for x in re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+', s)]
