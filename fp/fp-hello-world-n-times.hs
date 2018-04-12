-- Hello World N Times
-- Print 'hello world' n times.
--
-- https://www.hackerrank.com/challenges/fp-hello-world-n-times/problem
--

import Control.Applicative
import Control.Monad
import System.IO

hello_worlds n = replicateM_ n $ putStrLn "Hello World"

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    --  Print "Hello World" on a new line 'n' times.
    hello_worlds n

getMultipleLines :: Int -> IO [String]

getMultipleLines n
    | n <= 0 = return []
    | otherwise = do
        x <- getLine
        xs <- getMultipleLines (n-1)
        let ret = (x:xs)
        return ret
