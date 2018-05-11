-- SQL > Basic Select > Weather Observation Station 3
-- Query a list of unique CITY names with even ID numbers.
--
-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem
--

select distinct city from station where mod(id, 2) = 0;
