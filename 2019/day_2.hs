

calc :: (Int, Int, Int) -> [Int] -> Maybe Int
calc (1, a, b) xs = Just $ (xs!!a) + (xs!!b)
calc (2, a, b) xs = Just $ (xs!!a) * (xs!!b)
calc _ _ = Nothing

step :: Int -> [Int] -> [Int]
step i xs = 
    let 
        (ys, _:zs) = splitAt (xs!!(i + 3)) xs
        op = xs!!i
        a = xs!!(i + 1)
        b = xs!!(i + 2)
    in 
        case calc (op, a, b) xs of
            Just x -> step (i + 4) (ys ++ [x] ++ zs)
            Nothing -> xs

commaToSpace :: String -> String
commaToSpace s = [if c == ',' then ' ' else c | c <- s]

getNums :: String -> [Int]
getNums = map read . words . commaToSpace

findNounVerb :: [Int] -> [Int]
findNounVerb (x:a:b:xs) = 
    if head (step 0 (x:a:b:xs)) == 19690720
    then x:a:b:xs
    else if a == 99
        then findNounVerb $ x:0:(b + 1):xs
        else findNounVerb $ x:(a + 1):b:xs
findNounVerb _ = [-1]

runProgram :: String -> String
runProgram s = show $ findNounVerb $ getNums s

main :: IO ()
main = interact runProgram
