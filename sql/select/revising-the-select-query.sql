-- SQL > Basic Select > Revising the Select Query I
-- Query the data for all American cities with populations larger than 100,000.
--
-- https://www.hackerrank.com/challenges/revising-the-select-query/problem
--

select * from CITY where POPULATION>100000 and COUNTRYCODE='USA';
