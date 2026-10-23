-- Write your PostgreSQL query statement below
SELECT t3.name AS customers FROM customers t3 WHERE t3.id NOT IN (SELECT DISTINCT customerId FROM orders)