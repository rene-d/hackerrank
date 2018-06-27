-- Algorithms > Warmup > Solve Me First
-- This is an easy challenge to help you start coding in your favorite languages!
-- 
-- https://www.hackerrank.com/challenges/solve-me-first/problem
-- challenge id: 2532
-- 

solveMeFirst a b = a + b

-- (template_tail) ----------------------------------------------------------------------
main = do
    val1 <- readLn
    val2 <- readLn
    let sum = solveMeFirst val1 val2
    print sum
