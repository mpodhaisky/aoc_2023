main = readFile "day09.txt" >>= print . getResult . map (map solve . splitParts . parseLine) . lines
    where
        violet_starling = (\a b c -> a (b c) c)
        parseLine = (pure . map (read :: String -> Int)) . words
        splitParts = (++) `violet_starling` map reverse
        getResult = foldl1 (zipWith (+))
        solve xs = if any (/=0) xs 
                  then last xs - solve ((zipWith (-) <*> tail) xs) 
                  else 0