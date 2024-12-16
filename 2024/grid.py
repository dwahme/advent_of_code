from helpers import *

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
UP_R = (1, 1)
UP_L = (-1, 1)
DOWN_R = (1, -1)
DOWN_L = (-1, -1)

CARDINAL_DIRS = [UP, DOWN, LEFT, RIGHT]
DIAG_DIRS = [UP_R, UP_L, DOWN_R, DOWN_L]
ALL_DIRS = CARDINAL_DIRS + DIAG_DIRS

class Grid:

    def __init__(self, data, sep=""):
        self.grid = [ list(row) for row in data ]
        self.sep = sep

    def __repr__(self):
        return "\n".join(self.sep.join(str(i) for i in col) for col in self.grid)

    def copy(self):
        return Grid([ row.copy() for row in self.grid ], sep=self.sep)
    
    def in_bounds(self, x, y):
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[y])
    
    def get(self, x, y):
        if not self.in_bounds(x, y):
            return None
        return self.grid[y][x]
    
    def set(self, x, y, val):
        if not self.in_bounds(x, y):
            return None
        self.grid[y][x] = val
        return self
    
    def iterate_xy(self):
        return ((x, y) for y in range(len(self.grid)) for x in range(len(self.grid[y])))

    def get_many(self, xys):
        return [ self.get(x, y) for x, y in xys ]
    
    def map(self, f):
        return Grid([[ f(self.get(x, y)) for x in range(len(self.grid[y])) ] for y in range(len(self.grid))], sep=self.sep)
    
    def map_xy(self, f):
        return Grid([[ f(x, y) for x in range(len(self.grid[y])) ] for y in range(len(self.grid))], sep=self.sep)

    def find(self, val):
        return [p for p in self.iterate_xy() if self.get(*p) == val]

if __name__ == "__main__":
    d = [ [1,2,3], [4,5,6], [7,8,9] ]
    g = Grid(d, "")
    print(g)

    d = [ "abc", "def", "ghi" ]
    g = Grid(d, ",")
    print(g)

