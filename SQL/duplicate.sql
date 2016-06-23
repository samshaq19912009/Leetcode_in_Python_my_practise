# Write your MySQL query statement below
SELECT distinct t1.Email as Email From Person t1
LEFT JOIN Person t2
on t1.Email = t2.Email
where t1.Id != t2.Id


