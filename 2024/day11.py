from helpers import *

def blink(stone):
    if stone == 0:
        return [1]
    
    s = str(stone)
    if len(s) % 2 == 0:
        return [int(s[:len(s) // 2]), int(s[len(s) // 2:])]
    
    return [stone * 2024]

def count_stones(stones, iterations):
    prev_counts = { stone: stones.count(stone) for stone in set(stones) }

    for _ in range(iterations):

        stone_counts = {}
        for stone, prev_count in prev_counts.items():
            blinked = blink(stone)

            for b in blinked:
                stone_counts[b] = stone_counts.get(b, 0) + prev_count

        prev_counts = stone_counts

    return sum(val for val in stone_counts.values())

def task1(stones):
    return count_stones(stones, 25)

def task2(stones):
    return count_stones(stones, 75)

if __name__ == "__main__":
    lines = get_input("sample-11-01")
    lines = get_input("sample-11-02")
    lines = get_input("11")
    lines = [l.strip() for l in lines]

    stones = [int(i) for i in lines[0].split()]
    
    print(task1(stones))
    print(task2(stones))
