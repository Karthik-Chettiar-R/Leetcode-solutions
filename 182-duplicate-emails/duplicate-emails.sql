-- Write your PostgreSQL query statement below

SELECT DISTINCT t1.email FROM person t1 JOIN person t2 ON t1.email = t2.email AND t1.id != t2.id
