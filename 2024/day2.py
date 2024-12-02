
import helpers

def is_safe_report(lst):
    diffs = [lst[i] - lst[i + 1] for i in range(len(lst) - 1)]
    
    all_pos = all([i > 0 for i in diffs])
    all_neg = all([i < 0 for i in diffs])
    all_in_range = all([1 <= abs(i) and abs(i) <= 3 for i in diffs])

    return (all_pos or all_neg) and all_in_range

def try_safe_variations(lst):
    variations = [lst[:i] + lst[i + 1:] for i in range(len(lst))]
    return any([is_safe_report(v) for v in variations])

def count_safe_reports(lines):
    safe_reports = [l for l in lines if is_safe_report(l)]
    return len(safe_reports)

def count_safe_variations(lines):
    safe_reports = [l for l in lines if try_safe_variations(l)]
    return len(safe_reports)

if __name__ == "__main__":
    lines = helpers.get_input("02")

    lines = [[int(i) for i in l.split()] for l in lines]

    helpers.call_and_print(count_safe_reports, lines)
    helpers.call_and_print(count_safe_variations, lines)
