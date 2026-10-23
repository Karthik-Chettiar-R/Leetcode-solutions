-- Write your PostgreSQL query statement below
    
    SELECT DISTINCT t1.machine_id , 
    ROUND(
    ((
    SELECT AVG(timestamp) 
    FROM activity 
        WHERE machine_id = t1.machine_id
        AND 
        activity_type='end'
        
    )
    -
    (
    SELECT AVG(timestamp) 
    FROM activity 
        WHERE machine_id = t1.machine_id
        AND 
        activity_type='start'

    ))::numeric
    ,3)
    AS
    processing_time 
    FROM
    activity t1