-- SQL > Basic Select > Weather Observation Station 8
-- Query CITY names that start AND end with vowels.
--
-- https://www.hackerrank.com/challenges/weather-observation-station-8/problem
-- challenge id: 9343
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

select distinct city from station
where instr('aeiou', lower(substr(city, length(city), 1))) > 0
and instr('aeiou', lower(substr(city, 1, 1))) > 0;

-- (skeliton_tail) ----------------------------------------------------------------------
exit;
