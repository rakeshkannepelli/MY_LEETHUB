# Write your MySQL query statement below
SELECT DISTINCT 
    event_day AS day, 
    emp_id ,
    SUM(out_time - in_time) as total_time
FROM Employees
GROUP BY day , emp_id;

