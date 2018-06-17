-- SQL > Basic Select > Higher Than 75 Marks
-- Query the names of students scoring higher than 75 Marks. Sort the output by the LAST three characters of each name.
--
-- https://www.hackerrank.com/challenges/more-than-75-marks/problem
-- https://www.hackerrank.com/contests/simply-sql/challenges/more-than-75-marks
-- challenge id: 12965
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

select name from students
where marks>75
order by lower(substr(name, length(name)-2, 3)), id;

-- (skeliton_tail) ----------------------------------------------------------------------
exit;
