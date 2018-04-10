-- Extra Long Factorials
-- Calculate a very large factorial that doesn't fit in the conventional numeric data types.
--
-- https://www.hackerrank.com/challenges/extra-long-factorials/problem
--
import Control.Applicative
import Control.Monad
import System.IO

fac :: Integer -> Integer
fac 1 = 1
fac n = n * fac (n - 1)

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Integer
    let result = fac n
    print result
