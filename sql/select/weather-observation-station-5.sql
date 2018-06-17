-- SQL > Basic Select > Weather Observation Station 5
-- Write a query to print the shortest and longest length city name along with the length of the city names.
--
-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem
-- challenge id: 9340
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

-- Oracle:
select city,length(city) from (select city from station order by length(city) asc,city) where rownum=1;
select city,length(city) from (select city from station order by length(city) desc,city) where rownum=1;


-- MySQL:
-- select city,length(city) from station order by length(city) asc,city limit 1;
-- select city,length(city) from station order by length(city) desc,city limit 1;


-- (skeliton_tail) ----------------------------------------------------------------------
exit;
