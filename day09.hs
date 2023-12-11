main = readFile "day09.txt" >>= print . getResult . map (map solve . splitParts . parseLine) . lines
    where
        parseLine = (pure . map (read :: String -> Int)) . words
        splitParts = (++) <*> map reverse
        getResult = foldl1 (zipWith (+))
        diff = zipWith (-) <*> tail
        solve = sum . map head . takeWhile (/=[]) . iterate diff 