
getFuel :: Int -> Int
getFuel x = max 0 $ div x 3 - 2

getRecursiveFuel :: Int -> Int
getRecursiveFuel 0 = 0
getRecursiveFuel x = getFuel x + getRecursiveFuel (getFuel x)

getTotalFuel :: [Int] -> Int
getTotalFuel = sum . map getRecursiveFuel

getNums :: String -> [Int]
getNums = map read . lines

linesToFuel :: String -> String
linesToFuel = show . getTotalFuel . getNums

main :: IO ()
main = interact linesToFuel
