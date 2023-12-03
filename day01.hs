import Data.Char (isDigit)
import Control.Monad

main = readFile "day01.txt" >>= print . sum . map (read . (liftM2 (++) (pure . head) (pure . last)) .filter isDigit) . lines