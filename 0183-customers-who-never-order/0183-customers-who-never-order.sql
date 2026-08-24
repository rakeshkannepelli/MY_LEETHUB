# Write your MySQL query statement below
SELECT name AS Customers FROM Customers
WHERE id IN (
    SELECT id FROM Customers
    EXCEPT
    SELECT customerId FROM Orders # this getted 3 , 1 do not need to select using except remaining will select
);