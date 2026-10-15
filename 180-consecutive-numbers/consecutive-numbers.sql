-- Write your PostgreSQL query statement below


SELECT DISTINCT(t1.num ) AS consecutiveNums FROM (
Logs t1 JOIN Logs t2 ON t1.id+1=t2.id AND t1.num=t2.num 
JOIN
Logs t3 ON t2.id+1=t3.id AND t2.num=t3.num )
WHERE t1.num IS NOT NULL ;