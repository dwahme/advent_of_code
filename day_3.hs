
data Line = Ln (Int, Int) (Int, Int)
    deriving (Show, Eq)

data Instr = Ins Char Int
    deriving (Show, Eq)

pointCmp :: (Int, Int) -> (Int, Int) -> Bool
pointCmp (x0, y0) (x1, y1) = x0 + y0 < x1 + y1

makeMove :: [Line] -> Instr -> [Line]
makeMove ((Ln p1 (x0, y0)):ls) (Ins 'D' i) = 
    Ln (x0, y0) (x0, (y0 - i)) : Ln p1 (x0, y0) : ls
makeMove ((Ln p1 (x0, y0)):ls) (Ins 'U' i) = 
    Ln (x0, y0) (x0, (y0 + i)) : Ln p1 (x0, y0) : ls
makeMove ((Ln p1 (x0, y0)):ls) (Ins 'L' i) = 
    Ln (x0, y0) ((x0 - i), y0) : Ln p1 (x0, y0) : ls
makeMove ((Ln p1 (x0, y0)):ls) (Ins 'R' i) = 
    Ln (x0, y0) ((x0 + i), y0) : Ln p1 (Pt x0 y0) : ls
makeMove g _ = g

findIntersection :: Line -> Line -> Maybe (Int, Int)
findIntersection (Ln (x0, y0) (x1, y1)) (Ln (i0, j0) (i1, j1))
    | x0 == x1 && j0 == j1 = 
        -- l0 vertical, l1 horizontal
        if i0 <= x0 && x0 <= i1 && y0 <= j0 && j0 <= y1
        then Just (x0, j0)
        else Nothing
    | i0 == i1 && y0 == y1 = 
        -- l0 horizontal, l1 vertical
        if x0 <= i0 && i0 <= x1 && j0 <= y0 && y0 <= j1
        then Just (i0, y0)
        else Nothing
    | otherwise = Nothing

getIntersections :: [Line] -> [(Int, Int)]
getIntersections (l0:l1:ls) = 
    mapMaybe (map (findIntersection l0)) ls

commaToSpace :: String -> String
commaToSpace s = [if c == ',' then ' ' else c | c <- s]

readInstr :: String -> Instr
readInstr (c:i) = Ins c (read i)

getInstr :: String -> [(Char, Int)]
getInstr = map read . words . commaToSpace

main :: IO ()
main = interact id
