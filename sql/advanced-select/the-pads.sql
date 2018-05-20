-- SQL > Advanced Select > The PADS
-- Query the name and abbreviated occupation for each person in OCCUPATIONS.
--
-- https://www.hackerrank.com/challenges/the-pads/problem
-- https://www.hackerrank.com/contests/simply-sql/challenges/the-pads
-- challenge id: 12889
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

select concat(name,
              concat('(',
                     concat(substr(occupation, 1, 1), ')')))
from occupations
order by name;

select concat('There are a total of ',
              concat(count(name),
                     concat(' ',
                            concat(lower(occupation), 's.'))))
from occupations group by occupation
order by count(name), occupation;

-- (skeliton_tail) ----------------------------------------------------------------------
exit;
