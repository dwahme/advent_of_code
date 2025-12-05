from typing import List
from numbers import Number

class Interval():

    # lower bound is inclusive while upper bound is exclusive
    def __init__(self, lo: Number, hi: Number) -> None:
        self.lo = lo
        self.hi = hi
        self.range = range(lo, hi)
    
    def __repr__(self):
        return f"Interval({self.lo}, {self.hi})"
    
    def __contains__(self, value) -> bool:
        return value in self.range

    def __eq__(self, other: "Interval") -> bool:
        return self.range == other.range

    def __lt__(self, other: "Interval") -> bool:
        return self.lo < other.lo if self.lo != other.lo else self.hi < other.hi
    
    def __iter__(self) -> Number:
        return self.range.__iter__()
    
    def __len__(self) -> int:
        return len(self.range)
    
    def has_overlap(self, other: "Interval") -> bool:
        return range(max(self.lo, other.lo), min(self.hi, other.hi)) or None

    def union(self, other: "Interval"):
        if not self.has_overlap(other):
            return None
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))

    def bulk_union(ranges: List["Interval"]) -> List["Interval"]:
        result = []
        rs = sorted(ranges)

        for r in rs:
            if result and r.has_overlap(result[-1]):
                result[-1] = result[-1].union(r)
            else:
                result.append(r)

        return result

    def intersect(self, other: "Interval") -> "Interval":
        if not self.has_overlap(other):
            return False
        return Interval(max(self.lo, other.lo), min(self.hi, other.hi))
