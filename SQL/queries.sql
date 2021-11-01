use ems;

-- full data for each employee with address as a string, dept_name and mngr_name

select 
	em.id, em.name , em.salary, 
	a.street +'' + a.city as 'full_address',
	d.name as 'dept_name',
	mngr.name
from employee em
full join 
employee mngr
on (em.manager_id = mngr.id)
join 
department d on (em.department_id = d.id)
join 
address a on (d.headquarter_address_id = a.id);

-- 5 highest and lowest paid employee
-- for 5 highest paid employee
select  
top 5 id, name, salary
from employee
where salary <= (select max(salary) from employee) --- minimum salary is 80000
order by salary desc;

--for 5 lowest paid employee
select  
top 5 id, name, salary
from employee
where salary >= (select min(salary) from employee)  ---minimum salary is 28000
order by salary;

-- total salary for each department

select d.id, sum(e.salary) as 'Total_salary_each_dept.'
from department d
join employee e
on (d.id= e.department_id)
group by d.id
order by 'Total_salary_each_dept.'desc;

--Each employee that lives in a given state 
select e.name,a.state 
from employee e
join address a
on (a.id = e.address_id)
where a.state = 'Texas';

--import data from emp.csv file
select * from emp;