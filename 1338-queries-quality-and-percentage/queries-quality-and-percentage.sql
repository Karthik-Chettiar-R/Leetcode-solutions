-- Write your PostgreSQL query statement below

SELECT t1.query_name,

COALESCE(ROUND(SUM(t1.rating * 1.0 / t1.position)/COUNT(t1.rating) ,2),0)
AS quality
, COALESCE(ROUND(((SELECT COUNT(rating) FROM Queries WHERE rating<3 AND query_name=t1.query_name GROUP BY query_name)*100.0/COUNT(t1.query_name)),2),0)
 AS poor_query_percentage
  FROM Queries t1
   GROUP BY
    t1.query_name