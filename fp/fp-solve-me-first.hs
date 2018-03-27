-- Solve Me First FP
-- This is a special challenge to make you familiar with IO.
-- 
-- https://www.hackerrank.com/challenges/fp-solve-me-first/problem
-- 

solveMeFirst a b = a + b

-- (template_tail) ----------------------------------------------------------------------
main = do
    val1 <- readLn
    val2 <- readLn
    let sum = solveMeFirst val1 val2
    print sum
