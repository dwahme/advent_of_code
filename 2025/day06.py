from helpers import *
from grid import *
from interval import *
from functools import cache

def calculate(op, nums):
    match op:
        case "+": return sum(nums)
        case "*": return reduce(lambda x, y: x * y, nums, 1)
    raise ValueError(f"Invalid operator {op}")

def task1(lines):
    nums = [ find_nums(l, convert_to=int) for l in lines[:-1] ]
    ops = [ o.strip() for o in lines[-1].split(" ") if o ]

    return sum(calculate(op, (ns[i] for ns in nums)) for i, op in enumerate(ops))

def get_nums(start, stop, lines):
    nums = [ "".join(line[i] for line in lines).strip() for i in range(start, stop) ]
    return [ int(n) for n in nums if n ]

def task2(lines):
    ops = lines[-1]
    data = lines[:-1]

    op_locs = [ i for i, op in enumerate(ops) if op != " " ]
    get_stop = lambda idx: op_locs[idx + 1] if idx + 1 < len(op_locs) else len(ops)
    return sum(calculate(ops[op_pos], get_nums(op_pos, get_stop(idx), data)) for idx, op_pos in enumerate(op_locs))

if __name__ == "__main__":
    # lines = get_input("sample-06")
    lines = get_input("06")
    lines = [ l.strip("\n") for l in lines ]
    
    print(task1(lines))
    print(task2(lines))
