#The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

#Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who ear#ns more than his manager.



# Write your MySQL query statement below

SELECT t.Name AS Employee  FROM Employee t
LEFT JOIN Employee t2
ON t.ManagerId = t2.Id
WHERE t.Salary > t2.Salary



