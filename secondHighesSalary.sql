# Write your MySQL query statement below
SELECT MAX(Salary) as SecondHighestSalary from Employee
where Salary not in (SELECT MAX(Salary) from Employee)