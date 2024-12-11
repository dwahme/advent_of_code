from helpers import *

def blink(stone):
    if stone == 0:
        return [1]
    
    s = str(stone)
    if len(s) % 2 == 0:
        return [int(s[:len(s) // 2]), int(s[len(s) // 2:])]
    
    return [stone * 2024]

def count_stones(stone_list, prev_counts):
    stone_counts = {}
    for stone in stone_list:
        stone_counts[stone] = stone_counts.get(stone, 0) + 1 * prev_counts.get(stone, 1)

    return stone_counts

def task1(stone_counts):
    prev_counts = stone_counts

    for _ in range(25):

        stone_counts = {}
        for stone, prev_count in prev_counts.items():
            blinked = blink(stone)

            for b in blinked:
                stone_counts[b] = stone_counts.get(b, 0) + prev_count

        prev_counts = stone_counts

    return sum(val for val in stone_counts.values())

def task2(stone_counts):
    prev_counts = stone_counts

    for _ in range(75):

        stone_counts = {}
        for stone, prev_count in prev_counts.items():
            blinked = blink(stone)

            for b in blinked:
                stone_counts[b] = stone_counts.get(b, 0) + prev_count

        prev_counts = stone_counts

    return sum(val for val in stone_counts.values())

if __name__ == "__main__":
    lines = get_input("sample-11-01")
    lines = get_input("sample-11-02")
    lines = get_input("11")
    lines = [l.strip() for l in lines]
    
    stone_counts = count_stones([int(stone) for stone in lines[0].split()], {})

    print(stone_counts)
    
    print(task1(stone_counts))
    print(task2(stone_counts))
