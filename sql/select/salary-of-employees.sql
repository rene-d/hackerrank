-- SQL > Basic Select > Employee Salaries
-- Print the names of employees who earn more than $2000 per month and have worked at the company for less than 10 months.
--
-- https://www.hackerrank.com/challenges/salary-of-employees/problem
-- https://www.hackerrank.com/contests/simply-sql-the-sequel/challenges/salary-of-employees
-- challenge id: 19630
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


select name from employee
where salary > 2000 and months < 10;


-- (skeliton_tail) ----------------------------------------------------------------------
exit;
