from typing import List
from numbers import Number

class Range():

    # lower bound is inclusive while upper bound is exclusive
    def __init__(self, lo: Number, hi: Number) -> None:
        self.lo = lo
        self.hi = hi
        self.range = range(lo, hi)
    
    def __repr__(self):
        return f"Range({self.lo}, {self.hi})"
    
    def __contains__(self, value) -> bool:
        return value in self.range

    def __eq__(self, other: "Range") -> bool:
        return self.range == other.range

    def __lt__(self, other: "Range") -> bool:
        return self.lo < other.lo if self.lo != other.lo else self.hi < other.hi
    
    def __iter__(self) -> Number:
        return self.range.__iter__()
    
    def __len__(self) -> int:
        return len(self.range)
    
    def has_overlap(self, other: "Range") -> bool:
        return range(max(self.lo, other.lo), min(self.hi, other.hi)) or None

    def merge(self, other: "Range"):
        if not self.has_overlap(other):
            return None
        return Range(min(self.lo, other.lo), max(self.hi, other.hi))

    def merge_all(ranges: List["Range"]) -> List["Range"]:
        result = []
        rs = sorted(ranges)

        for r in rs:
            if result and r.has_overlap(result[-1]):
                result[-1] = result[-1].merge(r)
            else:
                result.append(r)

        return result
