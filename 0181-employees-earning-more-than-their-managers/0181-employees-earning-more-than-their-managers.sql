SELECT a.name as Employee
FROM Employee a JOIN Employee b
ON a.managerId = b.id
where a.salary>b.salary;
