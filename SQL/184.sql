# Write your MySQL query statement below
SELECT DISTINCT Department.name as Department, Employee.name as Employee, salary FROM Employee
LEFT JOIN Department on Department.id = Employee.departmentId
WHERE Employee.salary = (SELECT MAX(salary) FROM Employee e2 WHERE e2.departmentId = Department.id)
Order By salary 