from helpers import *
from grid import *
from interval import *
from functools import cache
import re

def parse_input(line):
    expected_states = tuple(i == "#" for i in line.split(" ")[0][1:-1])
    buttons = tuple(tuple(find_nums(b, int)) for b in line.split(" ")[1:-1])
    joltages = tuple(find_nums(line.split(" ")[-1]))
    return expected_states, buttons, joltages

def min_presses(expected_states, buttons):

    goal = lambda x: x == expected_states
    press = lambda state: [(tuple(not v if idx in b else v for idx, v in enumerate(state)), 1) for b in buttons]
    return a_star(tuple(False for _ in expected_states), goal, press)[0]

def task1(lines):
    data = [ parse_input(l) for l in lines ]

    return sum(min_presses(expected_states, buttons) for expected_states, buttons, _ in data)

def press_joltage_func(buttons, expected_joltages):
    def press(joltages):
        ret = []
        for b in buttons:
            new_joltage = tuple(j + (1 if idx in b else 0) for idx, j in enumerate(joltages))
            score = 1
            if all(a <= e for e, a in zip(expected_joltages, joltages)):
                ret.append((new_joltage, score))

        return ret
    return press

def min_presses_j(expected_joltages, buttons):

    goal = lambda x: x == expected_joltages
    return a_star(tuple(0 for _ in expected_joltages), goal, press_joltage_func(buttons, expected_joltages))[0]

def task2(lines):
    # TODO- this is way too slow and will not finish computing
    data = [ parse_input(l) for l in lines ]
    return sum(min_presses_j(joltages, buttons) for _, buttons, joltages in data)

if __name__ == "__main__":
    # lines = get_input("sample-10")
    lines = get_input("10")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
