import helpers

def look_in_direction(grid, i, j, x, y):

    for idx, char in enumerate("XMAS"):
        if not (0 <= y + j*idx < len(grid)) or not (0 <= x + i*idx < len(grid[y + j*idx])):
            return False
        if grid[y + j*idx][x + i*idx] != char:
            return False
        
    return True

def task1(grid):

    base_dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for i, j in base_dirs:
                sum += look_in_direction(grid, i, j, x, y)
                sum += look_in_direction(grid, -i, -j, x, y)

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
