
import Data.List

calc :: (Int, Int, Int) -> [Int] -> Maybe Int
calc (1, a, b) xs = Just $ (xs!!a) + (xs!!b)
calc (2, a, b) xs = Just $ (xs!!a) * (xs!!b)
calc _ xs = Nothing

step :: Int -> [Int] -> Int
step i xs = 
    let 
        (ys, zs) = splitAt (xs!!(i + 3)) xs
        op = xs!!i
        a = xs!!(i + 1)
        b = xs!!(i + 2)
    in 
        case calc (op, a, b) xs of
            Nothing -> (xs!!0)
            Just a -> step (i + 4) (ys ++ [a] ++ zs)

getNums :: String -> [Int]
getNums = map read . (splitOn ", ")

runProgram :: String -> String
runProgram s = show $ step 0 $ getNums s

main :: IO ()
main = interact runProgram
