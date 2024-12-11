
from helpers import *

def is_safe_report(lst):
    diffs = [lst[i] - lst[i + 1] for i in range(len(lst) - 1)]
    return all([1 <= i <= 3 for i in diffs]) or all([-3 <= i <= -1 for i in diffs])

def try_safe_variations(lst):
    variations = [lst[:i] + lst[i + 1:] for i in range(len(lst))]
    return any([is_safe_report(v) for v in variations])

def count_safe_reports(lines):
    return len([l for l in lines if is_safe_report(l)])

def count_safe_variations(lines):
    return len([l for l in lines if try_safe_variations(l)])

if __name__ == "__main__":
    lines = get_input("02")

    lines = [[int(i) for i in l.split()] for l in lines]

    call_and_print(count_safe_reports, lines)
    call_and_print(count_safe_variations, lines)
