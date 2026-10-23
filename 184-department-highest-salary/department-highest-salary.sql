SELECT 

    t2.name AS department ,
    t1.name AS Employee ,
    t1.salary AS salary

    FROM department t2 LEFT JOIN employee t1 
        ON t2.id = t1.departmentId

        WHERE t1.salary = (
            SELECT MAX(salary)

                FROM employee 

                WHERE t1.departmentId = departmentId
        )
        

        
