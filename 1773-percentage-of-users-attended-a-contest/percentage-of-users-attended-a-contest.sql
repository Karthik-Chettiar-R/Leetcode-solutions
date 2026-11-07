-- Write your PostgreSQL query statement below

SELECT t.contest_id,ROUND(COUNT(t.contest_id::numeric) * 100.0 /(SELECT COUNT(*) FROM USERS),2) AS percentage FROM register t GROUP BY t.contest_id ORDER BY percentage DESC,t.contest_id;
 