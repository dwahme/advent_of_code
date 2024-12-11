from helpers import *
import functools

@functools.cache
def blink_recurse(stone, depth):
    if depth <= 0:
        return 1
    
    if stone == 0:
        return blink_recurse(1, depth - 1)
    
    s = str(stone)
    if len(s) % 2 == 0:
        return blink_recurse(int(s[:len(s) // 2]), depth - 1) + blink_recurse(int(s[len(s) // 2:]), depth - 1)
    
    return blink_recurse(stone * 2024, depth - 1)

def task1(stones):
    return sum(blink_recurse(stone, 25) for stone in stones)

def task2(stones):
    return sum(blink_recurse(stone, 75) for stone in stones)

if __name__ == "__main__":
    lines = get_input("sample-11-01")
    lines = get_input("sample-11-02")
    lines = get_input("11")
    lines = [l.strip() for l in lines]

    stones = [int(i) for i in lines[0].split()]
    
    print(task1(stones))
    print(task2(stones))
