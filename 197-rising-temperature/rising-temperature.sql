-- Write your PostgreSQL query statement below
SELECT t1.id FROM Weather t1 WHERE t1.temperature > (SELECT temperature FROM weather where t1.recordDate = recordDate+1) 