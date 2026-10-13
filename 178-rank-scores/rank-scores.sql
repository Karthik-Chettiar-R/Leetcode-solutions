-- Write your PostgreSQL query statement below
SELECT t1.score,(SELECT COUNT(DISTINCT t2.score) FROM scores t2 WHERE t1.score < t2.score )+1 AS rank FROM scores t1 ORDER BY t1.score DESC;   