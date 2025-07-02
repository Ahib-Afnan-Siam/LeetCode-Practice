# Write your MySQL query statement below
SELECT 
    id,
    CASE 
        WHEN id % 2 = 1 AND next_stu IS NOT NULL THEN next_stu
        WHEN id % 2 = 0 THEN prev_stu
        ELSE student
    END AS student
FROM (
    SELECT 
        id, 
        student,
        LEAD(student) OVER (ORDER BY id) AS next_stu,
        LAG(student) OVER (ORDER BY id) AS prev_stu
    FROM Seat
) AS t
ORDER BY id;