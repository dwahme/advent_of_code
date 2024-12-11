
UP = (0, 1)
DOWN = (0, -1)
RIGHT = (0, 1)
LEFT = (-1, 0)

CARDINAL_DIRS = [UP, DOWN, LEFT, RIGHT]

def add_tup(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

class Point:

    def __init__(self, xy):
        self.x, self.y = xy
    
    def __repr__(self):
        return f"Point({self.x}, {self.x})"

class Grid:

    def __init__(self, data, sep=","):
        self.grid = [ list(row).copy() for row in data ]
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
        return ((x, y) for y in range(len(self.grid)) for x in range(len(self.grid)))

    def get_many(self, xys):
        return [ self.get(x, y) for x, y in xys ]
    
    def map(self, f):
        return Grid([[ f(self.get(x, y)) for x in range(len(self.grid[y])) ] for y in range(len(self.grid))], sep=self.sep)
    
    def map_xy(self, f):
        return Grid([[ f(x, y) for x in range(len(self.grid[y])) ] for y in range(len(self.grid))], sep=self.sep)

if __name__ == "__main__":
    d = [ [1,2,3], [4,5,6], [7,8,9] ]
    g = Grid(d, "")
    print(g)

    d = [ "abc", "def", "ghi" ]
    g = Grid(d, ",")
    print(g)

