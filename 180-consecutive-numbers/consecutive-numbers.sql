-- Write your PostgreSQL query statement below


SELECT DISTINCT(num) AS ConsecutiveNums FROM (

    SELECT t4.id,t4.num FROM (SELECT t2.id, t1.num FROM Logs t1 LEFT JOIN Logs t2 on t1.num=t2.num AND t1.id+1=t2.id ) t3 LEFT JOIN Logs t4 on t3.num=t4.num AND t3.id+1=t4.id


) WHERE num IS NOT NULL;