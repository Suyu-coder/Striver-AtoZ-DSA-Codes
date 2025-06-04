
-- second Highest Salary 
select MAX(salary) AS secondHighestSalary 
From employee
where salary < (select Max(salary) from Employee)

-- second highest salary using DENSE_RANK
select salary 
from (
	select salart , DENSE_RANK() over(Order BY Salary DESC) as rnk
	from employee 
	) as ranked
where rnk = 2

-- -- second highest salary using OFFSET and limit 
select Distinct salary 
from employee
Order BY salary DESC
LIMIT 1 OFFSET 1;

-- top 3 earner from each department 
select * from 
(
	select *, DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) as rnk
	from employee
) as ranked 
where rnk <= 3 

-- count duplicate in the table
select column_name , COUNT(*) as count 
from table_name 
group BY column_name 
HAVING COUNT(*) > 1

-- convert row level data into column level data 
select * from (
	select department , month, salary
	from salaries 
) src 
PIVOT (
sum(salary) for month IN ([JAN],[FEB],[MAR])
) as pvt 

-- find employee earning morethan their manager 
select e.employee_id , e.salary 
from employee e 
JOIN employee m ON e.manager_id = m.employee_id 
where e.salary > m.salary 

-- cumulative sum of column 
select employee_id , deopartment, salary 
	sum(salary) over(PARTiTION BY  department Order BY employee_id) as cululative_salary
from employee

--Nth higest Salary 
select distinct salary 
from (
	select salary . DENSE_RANK() OVER (ORDER BY salary DESC) as rnk 
	from employee
	) as ranked 
where rank = N 

-- Employee who joined in last 6 month 
select * from employee
where joining_date > = DATEADD(MONTH , -6, GETDATE())

-- Department wise higest salary 
select department , MAX(salary) as max_salary
from employee 
Group By department 

-- Remove duplicate rows 
delete from employee
where id not in (
	select MIN(id)
	from employee 
	group by name , salary , department 
)
