-- Write your PostgreSQL query statement below
SELECT 
    t2.name AS Department,
    t1.name AS Employee,
    t1.salary AS Salary

    FROM 
        department t2 JOIN employee t1
        ON
        t2.id = t1.departmentId

        WHERE t1.salary IN (
            SELECT DISTINCT salary FROM employee 
            WHERE 
            departmentId = t1.departmentId
            ORDER BY salary
            DESC
            LIMIT 3
        )


