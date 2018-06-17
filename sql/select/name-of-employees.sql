-- SQL > Basic Select > Employee Names
-- Print employee names.
--
-- https://www.hackerrank.com/challenges/name-of-employees/problem
-- https://www.hackerrank.com/contests/simply-sql-the-sequel/challenges/name-of-employees
-- challenge id: 19629
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

select name from employee order by name;

-- (skeliton_tail) ----------------------------------------------------------------------
exit;
