from helpers import *
from functools import cache
from time import time

@cache
def find_next_word(s):
    global patterns
    return (s in patterns) + sum(find_next_word(s[i:]) for i in range(1, len(s)) if s[:i] in patterns)

def task1(designs):
    return sum(find_next_word(d) > 0 for d in designs)

def task2(designs):
    return sum(find_next_word(d) for d in designs)

if __name__ == "__main__":
    lines = get_input("sample-19")
    lines = get_input("19")
    lines = [l.strip() for l in lines]

    # Make patterns a global so that we can efficiently memoize find_next_word()
    global patterns
    patterns = set([ s.strip() for s in lines[0].split(",") ])
    designs = [ l.strip() for l in lines[2:] ]

    print(task1(designs))
    print(task2(designs))
