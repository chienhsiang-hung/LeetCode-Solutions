# Write your MySQL query statement below
SELECT 
    employee_id,
    salary * IF(
        LEFT(name, 1) != 'M' AND MOD(employee_id, 2) != 0,
        1, 0
    ) AS bonus
FROM Employees
ORDER BY employee_id