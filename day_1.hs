
getFuel :: Int -> Int
getFuel x = div x 3 - 2

getTotalFuel :: [Int] -> Int
getTotalFuel = sum . map getFuel

getNums :: String -> [Int]
getNums = map read . lines

linesToFuel :: String -> String
linesToFuel = show . getTotalFuel . getNums

main :: IO ()
main = interact linesToFuel
