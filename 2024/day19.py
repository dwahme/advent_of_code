from helpers import *
from functools import cache

@cache
def find_next_word(s, patterns):
    return (s in patterns) + sum(find_next_word(s[i:], patterns) for i in range(1, len(s)) if s[:i] in patterns)

def task1(designs, patterns):
    return sum(find_next_word(d, patterns) > 0 for d in designs)

def task2(designs, patterns):
    return sum(find_next_word(d, patterns) for d in designs)

if __name__ == "__main__":
    lines = get_input("sample-19")
    lines = get_input("19")
    lines = [l.strip() for l in lines]

    patterns = tuple([ s.strip() for s in lines[0].split(",") ])
    designs = [ l.strip() for l in lines[2:] ]

    print(task1(designs, patterns))
    print(task2(designs, patterns))
