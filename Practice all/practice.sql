create database if not exists deligent_pra;
use deligent_pra ;
select database();

create  table department(
department_id int  unique primary key auto_increment,
department_name varchar(50)NOT NULL unique 
);

create table employee (
emp_id int unique primary key auto_increment,
emp_name varchar(50) NOT NULL ,
email  varchar(50) unique  ,
phonenumber int unique NOT NULL,
salary decimal(10,2) NOT NULL,
age int ,
department_id INT,
manager_id INT,
hire_date DATE,
foreign key (department_id)
REFERENCES department(department_id)
);
ALTER TABLE employee
MODIFY phonenumber VARCHAR(15) NOT NULL UNIQUE;

insert into department (department_name)
values
('IT'),
('HR'),
('Finance'),
('Marketing');

INSERT INTO employee
    (emp_name, email, phonenumber, salary, age,
     department_id, manager_id, hire_date)
VALUES
    ('Aman', 'aman@example.com', 9876500001, 60000, 28, 1, NULL, '2024-01-15'),
    ('Riya', 'riya@example.com', 9876500002, 40000, 25, 2, NULL, '2023-06-10'),
    ('Karan', 'karan@example.com', 9876500003, 80000, 32, 1, 1, '2022-03-20'),
    ('Neha', 'neha@example.com', 9876500004, 50000, 27, 2, 2, '2024-08-01'),
    ('Raj', 'raj@example.com', 9876500005, 70000, 30, 1, 1, '2021-11-05'),
    ('Priya', 'priya@example.com', 9876500006, 90000, 35, 3, NULL, '2020-07-12'),
    ('Vikram', 'vikram@example.com', 9876500007, 55000, 29, 3, 6, '2023-02-18'),
    ('Sara', 'sara@example.com', 9876500008, 45000, 24, 4, NULL, '2024-05-25');

SELECT * FROM department;
select * from employee;
show tables ;

DESCRIBE employee;

select emp_id, emp_name,  salary , age  ,department_id from employee 
where salary>=55000 and age<30
group by department
ORDER BY salary asc;

select emp_id, emp_name,  salary , age from employee 
where emp_name like 's%';


select count(emp_id) as totalemp, AVG(salary) as avg_salary, Max(salary) as high_sal, AVG(age) as avg_age from employee ;

select emp_id, emp_name,  salary , age  ,department_id from employee 
where department_id <> 1;

SELECT emp_name, manager_id
FROM employee
WHERE manager_id IS not  NULL;

SELECT DISTINCT age
FROM employee
ORDER BY age ASC;

select emp_name as en, salary as sl from employee;
SELECT
    emp_name,
    salary AS curr_sal,
    salary * 12 AS anual_sal
FROM employee;


SELECT
    emp_name,
    salary,
    CASE
        WHEN salary >= 70000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_level
FROM employee;

select emp_name , salary , age ,
case
when age < 25 then 'young'
when age between 25 and 30  then 'adult'
when age > 30 then 'senior'
else 'not defined'
end as age_category 
from employee;

SELECT COUNT(*), COUNT(email)
FROM employee;

SELECT department_id, AVG(salary) AS average_salary
FROM employee
GROUP BY department_id;

select department_id , count(*) as total_emp from employee
group by department_id;
#agreggate 
select department_id , sum(salary) as total_sal, avg(salary)as avg_sal,MAX(salary) AS highest_salary from employee 
group by department_id; 
## inner join 
select d.department_id , d.department_name , e.emp_name,e.salary
from employee as e 
inner join department as d 
on  d.department_id  = e.department_id
order by d.department_id asc  ;
## inner join
SELECT e.emp_name, d.department_name
FROM employee e
INNER JOIN department d
    ON e.department_id = d.department_id
WHERE d.department_name = 'IT';
## left join 
SELECT e.emp_name, d.department_name
FROM employee e
LEFT JOIN department d
    ON e.department_id = d.department_id;
    
## left join
SELECT e.emp_name, d.department_name
FROM employee e
LEFT JOIN department d
    ON e.department_id = d.department_id
where d.department_id is null;
## right join 
SELECT e.emp_name,
       d.department_name
FROM employee e
RIGHT JOIN department d
    ON e.department_id = d.department_id;

## full outer join
    SELECT e.emp_name, d.department_name
FROM employee e
LEFT JOIN departments d
    ON e.department_id = d.department_id

UNION ALL

SELECT e.emp_name, d.department_name
FROM employee e
RIGHT JOIN departments d
    ON e.department_id = d.department_id
WHERE e.emp_id IS NULL;

##subquery (corelated)

select e.emp_name, e.salary,e.department_id
from employee e 
where e.salary>(
select avg(salary)
from employee e2
where e2.department_id = e.department_id);

## subquery(in)
select emp_name , salary , age , email , phonenumber , department_id
from employee 
where department_id  in (
select department_id
from department
where department_name in ('HR','FINANCE'));



SELECT MAX(salary) AS second_highest_salary
FROM employee
WHERE salary < (
    SELECT MAX(salary)
    FROM employee
);