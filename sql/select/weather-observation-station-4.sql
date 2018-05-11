-- SQL > Basic Select > Weather Observation Station 4
-- Find the number of duplicate CITY names in STATION.
--
-- https://www.hackerrank.com/challenges/weather-observation-station-4/problem
--

select count(*)-count(distinct city) from station;
