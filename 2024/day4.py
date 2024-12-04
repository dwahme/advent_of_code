import helpers

def look_in_direction(grid, dir, x, y):

    for (i, j), char in zip(dir, "XMAS"):
        if not (0 <= y + j < len(grid)) or not (0 <= x + i < len(grid[y])):
            return False
        if grid[y + j][x + i] != char:
            return False

    print("found match")
    return True

def task1(grid):

    base_dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    patterns = [[(x * i, y * i) for (x, y) in base_dirs] for i in range(4)]
    directions = [[patterns[j][i] for j in range(4)] for i in range(4)]
    directions += [[tuple(-x for x in patterns[j][i]) for j in range(4)] for i in range(4)]

    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for dir in directions:
                sum += look_in_direction(grid, dir, x, y)

    return sum

def task2(grid):

    sum = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            if grid[y][x] == "A":
                letters1 = sorted(grid[y+1][x+1] + grid[y-1][x-1])
                letters2 = sorted(grid[y+1][x-1] + grid[y-1][x+1])

                if letters1 == letters2 and letters1 == ["M", "S"]:
                    sum += 1

    return sum

if __name__ == "__main__":
    lines = helpers.get_input("04")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))
