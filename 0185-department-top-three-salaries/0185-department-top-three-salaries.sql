# Write your MySQL query statement below
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM 
    Employee e
JOIN 
    Department d ON e.departmentId = d.id
WHERE 
    e.id IN (
        SELECT 
            id 
        FROM (
            SELECT 
                id,
                DENSE_RANK() OVER (
                    PARTITION BY departmentId 
                    ORDER BY salary DESC
                ) AS rnk
            FROM 
                Employee
        ) AS ranked 
        WHERE 
            rnk <= 3
    );