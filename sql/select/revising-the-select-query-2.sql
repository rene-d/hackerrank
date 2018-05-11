-- SQL > Basic Select > Revising the Select Query II
-- Query the city names for all American cities with populations larger than 120,000.
--
-- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
--

select name from city where countrycode='USA' and population>=120000;
