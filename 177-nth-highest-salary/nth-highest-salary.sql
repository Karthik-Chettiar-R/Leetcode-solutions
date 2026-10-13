CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
IF N<1 THEN RETURN;
END IF;


  RETURN QUERY (
    
    -- Write your PostgreSQL query statement below.
    SELECT DISTINCT t1.salary  FROM employee t1 ORDER BY t1.salary DESC OFFSET N-1 LIMIT 1      
  );
END;
$$ LANGUAGE plpgsql;