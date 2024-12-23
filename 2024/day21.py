from helpers import *
from grid import *
from functools import cache

def complexity(code, keys):
    return len(keys) * int(code[:-1])

@cache
def key_to_coord(key, is_numpad=False):
    if is_numpad:
        if key == "A": return (2,3)
        if key == "0": return (1,3)
        return ((int(key) + 2) % 3, 3 - ((int(key) + 2) // 3))
    else:
        if key == "^": return (1,0)
        if key == "A": return (2,0)
        if key == "<": return (0,1)
        if key == "v": return (1,1)
        if key == ">": return (2,1)

@cache
def get_dir_keys(start, end, before_char, after_char):
    return abs(start - end) * (before_char if start > end else after_char)

@cache
def is_allowed_position(x, y, is_numpad=False):
    if is_numpad:
        return 0 <= x < 3 and 0 <= y < 4 and not (x == 0 and y == 3)
    else:
        return 0 <= x < 3 and 0 <= y < 2 and not (x == 0 and y == 0)

@cache
def get_move(key, x, y):
    x += 1 if key == ">" else (-1 if key == "<" else 0)
    y += 1 if key == "v" else (-1 if key == "^" else 0)
    return x, y

@cache
def get_keypresses(cur_key, dest_key, depth, num_robots):

    is_last_robot = depth == num_robots - 1
    is_first_robot = depth == 0

    cur_x, cur_y = key_to_coord(cur_key, is_numpad=is_first_robot)
    dest_x, dest_y = key_to_coord(dest_key, is_numpad=is_first_robot)

    keys_x = get_dir_keys(cur_x, dest_x, "<", ">")
    keys_y = get_dir_keys(cur_y, dest_y, "^", "v")

    if is_last_robot or (keys_x + keys_y == ""):
        return len(keys_x + keys_y + "A")

    possible_keys = []
    for permutation in [keys_x + keys_y, keys_y + keys_x]:
        tmp_x, tmp_y = cur_x, cur_y
        presses = 0
        path_is_ok = True
        prev = "A"

        for key in permutation:
            tmp_x, tmp_y = get_move(key, tmp_x, tmp_y)
            if not is_allowed_position(tmp_x, tmp_y, is_numpad=is_first_robot):
                path_is_ok = False
                break

            presses += get_keypresses(prev, key, depth + 1, num_robots)
            prev = key
        
        if path_is_ok:
            presses += get_keypresses(permutation[-1], "A", depth + 1, num_robots)
            possible_keys.append(presses)
    
    return min(possible_keys)


def task1(codes):
    tot=0

    for code in codes:
        p_len = 0
        prev_key = "A"
        for c in code:
            presses = get_keypresses(prev_key, c, 0, 3)
            p_len += presses
            prev_key = c
        
        tot += int(code[:-1]) * p_len
        
    return tot

def task2(codes):
    tot=0

    for code in codes:
        p_len = 0
        prev_key = "A"
        for c in code:
            presses = get_keypresses(prev_key, c, 0, 26)
            p_len += presses
            prev_key = c
        
        tot += int(code[:-1]) * p_len

    return tot

if __name__ == "__main__":
    lines = get_input("sample-21")
    lines = get_input("21")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
