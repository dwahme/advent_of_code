from helpers import *
from grid import *
from interval import *
from functools import cache

def task1(lines):
    nums = [ [int(n.strip()) for n in ns.split(" ") if n.strip() ] for ns in lines[:-1] ]
    ops = [ o.strip() for o in lines[-1].split(" ") if o.strip()]

    total = 0

    for i, op in enumerate(ops):
        match op:
            case "+":
                total += sum(ns[i] for ns in nums)
            case "*":
                total += reduce(lambda x, y: x * y, (ns[i] for ns in nums), 1)

    return total

def get_nums(start, stop, lines):
    nums = []

    for i in range(start, stop):
        n = ""
        for line in lines:
            n += line[i] if line[i] != " " else ""
        if n:
            nums.append(int(n))

    return nums

def task2(lines):
    total = 0
    ops = lines[-1]
    data = lines[:-1]

    op_indices = [(i, op) for i, op in enumerate(ops) if op != " "]
    for idx, op_data in enumerate(op_indices):
        i, op = op_data
        next_i, _ = op_indices[idx + 1] if idx + 1 < len(op_indices) else (len(ops), None)

        nums = get_nums(i, next_i, data)

        match op:
            case "+":
                total += sum(nums)
            case "*":
                total += reduce(lambda x, y: x * y, nums, 1)

    return total

if __name__ == "__main__":
    # lines = get_input("sample-06")
    lines = get_input("06")
    lines = [l.strip("\n") for l in lines]
    
    print(task1(lines))
    print(task2(lines))
