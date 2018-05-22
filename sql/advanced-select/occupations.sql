-- SQL > Advanced Select > Occupations
-- Pivot the Occupation column so the Name of each person in OCCUPATIONS is displayed underneath their respective Occupation.
--
-- https://www.hackerrank.com/challenges/occupations/problem
-- https://www.hackerrank.com/contests/simply-sql/challenges/occupations
-- challenge id: 12890
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

-- solution Oracle

SELECT Doctor, Professor, Singer, Actor
FROM (SELECT ROW_NUMBER() OVER (PARTITION BY occupation ORDER BY name) as rn, name, occupation
      FROM occupations)
PIVOT (MAX(name) FOR OCCUPATION IN ('Doctor' as Doctor,
                                    'Professor' as Professor,
                                    'Singer' as Singer,
                                    'Actor' as Actor))
ORDER BY rn;

-- (skeliton_tail) ----------------------------------------------------------------------
exit;
