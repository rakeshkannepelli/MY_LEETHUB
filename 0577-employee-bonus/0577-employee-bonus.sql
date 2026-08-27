# Write your MySQL query statement below
SELECT name , Bonus.bonus FROM Employee
LEFT JOIN Bonus ON Bonus.empId = Employee.empId
WHERE bonus <1000 OR bonus IS NULL;