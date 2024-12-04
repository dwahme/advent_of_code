
import helpers

RIGHT = [(0, 0), (1, 0), (2, 0), (3, 0)]
LEFT = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
UP = [(0, 0), (0, 1), (0, 2), (0, 3)]
DOWN = [(0, 0), (0, -1), (0, -2), (0, -3)]

def generate_directions():
    lst = [(0, 1), (1, 0), (1, 1)]
    for i in range(0,4):
        print([(x * i, y * i) for (x, y) in lst])
    for i in range(0,4):
        print([(x * -i, y * -i) for (x, y) in lst])


def look_in_direction(grid, dir, x, y):

    # print(dir)

    is_xmas = True
    for (i, j), char in zip(dir, "XMAS"):
        if (len(grid) <= y + j) or (len(grid[y + j]) <= x + i) or (y + j < 0) or (x + i < 0):
            return False
        if grid[y + j][x + i] != char:
            is_xmas = False

    return is_xmas

def task1(grid):

    lst = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    patterns = []
    for i in range(4):
        patterns += [[(x * i, y * i) for (x, y) in lst]]

    directions = []
    for i in range(4):
        directions += [[patterns[j][i] for j in range(4)]]
        directions += [[tuple(-x for x in patterns[j][i]) for j in range(4)]]

    sum = 0
    for y in range(len(grid)):
        for x in range(len(grid[int(y)])):
            for dir in directions:
                has_result = look_in_direction(grid, dir, int(x), int(y))
                sum += has_result
                # if has_result:
                #     print(x, y, dir)

    return sum

def task2(grid):

    sum = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            print(x, y)
            if grid[y][x] == "A":
                letters1 = sorted(grid[y+1][x+1] + grid[y-1][x-1])
                letters2 = sorted(grid[y+1][x-1] + grid[y-1][x+1])
                # print(x, y, letters1, letters2)

                if letters1 == letters2 and letters1 == ["M", "S"]:
                    print(x, y, letters1, letters2)
                    sum += 1
    
    return sum



if __name__ == "__main__":
    lines = helpers.get_input("04")
    lines = [l.strip() for l in lines]
    
    print(task1(lines))
    print(task2(lines))


