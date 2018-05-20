-- SQL > Advanced Select > Type of Triangle
-- Query a triangle's type based on its side lengths.
--
-- https://www.hackerrank.com/challenges/what-type-of-triangle/problem
-- https://www.hackerrank.com/contests/simply-sql/challenges/what-type-of-triangle
-- challenge id: 12887
--

SET NULL "NULL";
SET FEEDBACK OFF;
SET ECHO OFF;
SET HEADING OFF;
SET WRAP OFF;
SET LINESIZE 10000;
SET TAB OFF;
SET PAGES 0;
SET DEFINE OFF;
-- (skeliton_head) ----------------------------------------------------------------------

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/


select case when a+b<=c or b+c<=a or c+a<=b then 'Not A Triangle'
            when a=b and b=c then 'Equilateral'
            when a=b or b=c or c=a then 'Isosceles'
            else 'Scalene'
       end
from triangles;


-- (skeliton_tail) ----------------------------------------------------------------------
exit;
