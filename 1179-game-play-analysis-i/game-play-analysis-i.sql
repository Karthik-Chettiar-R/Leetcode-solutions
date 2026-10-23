-- Write your PostgreSQL query statement below
SELECT t1.player_id , t1.event_date AS first_login FROM Activity t1 WHERE t1.event_date = (
    SELECT MIN(event_date) FROM Activity WHERE t1.player_id = player_id
    
)