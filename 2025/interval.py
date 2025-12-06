from functools import reduce
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
    
    def overlaps(self, other: "Interval") -> bool:
        return bool(range(max(self.lo, other.lo), min(self.hi, other.hi)))

    def union(self, other: "Interval"):
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi)) if self.overlaps(other) else None 

    def bulk_union(ranges: List["Interval"]) -> List["Interval"]:
        f = lambda rs, r: rs[:-1] + [rs[-1].union(r)] if rs and r.overlaps(rs[-1]) else rs + [r]
        return reduce(f, sorted(ranges), [])

    def intersect(self, other: "Interval") -> "Interval":
        return Interval(max(self.lo, other.lo), min(self.hi, other.hi)) if self.overlaps(other) else None
