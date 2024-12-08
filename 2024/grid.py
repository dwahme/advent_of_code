
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
    
    def _max_x(self):
        return len(self.grid[0]) - 1
    
    def _max_y(self):
        return len(self.grid) - 1
    
    def get(self, x, y, dx=0, dy=0):
        if not (0 <= y + dy <= self._max_y()) or not (0 <= x + dx <= self._max_x()):
            return None
        return self.grid[y + dy][x + dx]

    def set(self, val, x, y, dx=0, dy=0):
        if not (0 <= y + dy <= self._max_y()) or not (0 <= x + dx <= self._max_x()):
            return None
        
        self.grid[y + dy][x + dx] = val
        return self
    
    def check(self, expected, x, y, dx=0, dy=0):
        return self.get(x, y, dx, dy) == expected
    
    # def get_many(self, x, y, dxs, dys):
    #     if len(dxs) != len(dys):
    #         return None
    #     return [self.get(x, y, dxs[i], dys[i]) for i in len(dxs)]
    
    def get_p(self, point, d_point=Point((0, 0))):
        return self.get(point.x, point.y, d_point.x, d_point.y)
    
    # def get_p_many(self, point, d_points=[]):
    #     return [self.get(point.x, point.y, d_point.x, d_point.y) for d_point in d_points]

    def find_string_in_grid(grid: list[list[str]], string: str, x: int, y: int, dx: int, dy: int, allow_backwards=False):
        
        str_end = len(string) - 1
        if not (0 <= y + dy*str_end < len(grid)) or not (0 <= x + dx*str_end < len(grid[y + dy*str_end])):
            return False

        s = "".join([grid[y + dy*idx][x + dx*idx] for idx in range(len(string))])
        return s == string or (allow_backwards and s[::-1] == string)

    def find_items_in_grid(self, origin_point, d_points, possible_items):
        found = [ self.get_p(origin_point, d_point) for d_point in d_points ]
        return found in possible_items
    
    def map(self, f):
        for row in self.grid:
            for elem in row:
                f(elem)
        return self

if __name__ == "__main__":
    d = [ [1,2,3], [4,5,6], [7,8,9] ]
    g = Grid(d, "")
    print(g)

    d = [ "abc", "def", "ghi" ]
    g = Grid(d, ",")
    print(g)

