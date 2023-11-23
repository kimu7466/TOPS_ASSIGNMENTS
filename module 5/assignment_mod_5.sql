create database assignment_mod_5;
use assignment_mod_5;
create table student (rollno int auto_increment primary key, name varchar(100), branch varchar(100));

insert into student (name , branch)
value 
('jay', 'computer science'),('suhani', 'electronic and com'),('kriti', 'electronic and com');
select * from student;

CREATE TABLE exam (
    rollno INT, 
    s_code VARCHAR(100),
    mark INT,
    p_code VARCHAR(100),
    FOREIGN KEY (rollno) REFERENCES student(rollno)
);

select * from exam;

insert into exam (rollno, s_code, mark , p_code) 
values
(1,'CS11',50,'CS'),(1,'CS12',60,'CS'),
(2,'EC101',66,'EC'),(2,'EC102',70,'EC'),
(3,'EC101',45,'EC'),(3,'EC101',50,'EC');


CREATE TABLE information (
    first_name varchar(100), 
    last_name VARCHAR(100),
    address varchar(100),
    city VARCHAR(100),
    age int);
    
    insert into information (first_name, last_name, address, city, age) 
values
('mickey','mouse','123 fantasy way','anaheim',73),
('bat','man','321 cavern ave','gotham',54),
('wonder','woman','987 truth way','paradise',39),
('donald','duck','555 quack street','mallard',65),
('bugs','bunny','567 carrot street','rascal',58),
('wiley','coyote','999 acme way','canyon',61),
('cat','woman','234 purrfect street','hairball',32),
('tweety','bird','543','itotltaw',28);

select * from information;


CREATE TABLE employee (
    employee_id int,
    first_name varchar(100), 
    last_name VARCHAR(100),
    salary int,
    joining_date varchar(100),
    department VARCHAR(100));
    
     insert into employee (employee_id, first_name, last_name, salary, joining_date, department) 
values
(1,'john','abraham',1000000,'1-jan-2013 12:00:00 AM','banking'),
(2,'michael','clark',800000,'1-jan-2013 12:00:00 AM','insurance'),
(3,'roy','thomas',700000,'1-feb-2013 12:00:00 AM','banking'),
(4,'tom','jose',600000,'1-feb-2013 12:00:00 AM','insurance'),
(5,'jerry','pinto',650000,'1-feb-2013 12:00:00 AM','insurance'),
(6,'philip','mathew',750000,'1-jan-2013 12:00:00 AM','services'),
(7,'testname1','123',65000,'1-jan-2013 12:00:00 AM','services'),
(8,'testname2','lname%',600000,'1-feb-2013 12:00:00 AM','insurance');

SELECT * FROM assignment_mod_5.employee;
SELECT * FROM employee;

create table incentives(employee_ref_id int, incentive_date varchar(100),incentive_ammount int);

insert into incentives(employee_ref_id,incentive_date,incentive_ammount)
values
(1,'1-feb-2013',5000),
(2,'1-feb-2013',4000),
(3,'1-feb-2013',3000),
(1,'1-jan-2013',4500),
(2,'1-jan-2013',3500);

SELECT * FROM incentives;


SELECT first_name AS "Employee Name" FROM employee WHERE first_name = 'Tom';

SELECT first_name AS FIRST_NAME, joining_date AS "Joining Date", salary AS Salary FROM employee;

SELECT * FROM employee ORDER BY first_name ASC, salary DESC;

SELECT * FROM employee WHERE first_name LIKE '%J%';

SELECT department, MAX(salary) AS max_salary FROM employee GROUP BY department ORDER BY max_salary ASC;

SELECT e.first_name, i.incentive_ammount AS "incentive amount" FROM employee e JOIN incentives i ON e.employee_id = i.employee_ref_id WHERE i.incentive_ammount > 3000;

-- CREATE TRIGGER after_employee_insert_trigger
-- AFTER INSERT ON Employee
-- FOR EACH ROW
-- BEGIN
--     INSERT INTO view_table (column1, column2, column3)
--     VALUES (NEW.employee_id, NEW.first_name, NEW.last_name);
-- END;


-- DELIMITER2 //
-- CREATE TRIGGER after_employee_insert_trigger
-- AFTER INSERT ON Employee
-- FOR EACH ROW
-- BEGIN
--     INSERT INTO view_table (column1, column2, column3)
--     VALUES (NEW.employee_id, NEW.first_name, NEW.last_name);
-- END;
-- //
-- DELIMITER2 ;

create table SALESPERSON(Sno int primary key, Sname varchar(100),city varchar(100),comm double);

insert into SALESPERSON(Sno , Sname ,city ,comm )
values
(1001,'peel','london',.12),
(1002,'serres','san jose',.13),
(1004,'motika','london',.11),
(1007,'rafkin','barcelona',.15),
(1003,'axcelrod','new york',.1);

select * from salesperson;

create table customer(cnm int primary key, Cname varchar(100),city varchar(100),rating int, Sno int, foreign key (Sno) references salesperson (Sno));

insert into customer (cnm, Cname , city, rating, Sno)
values
(201 , 'hoffman' , 'london' , 100 , 1001 ),
(202 , 'giovanne' , 'roe' , 200 , 1003 ),
(203 , 'liu' , 'san jose' , 300 , 1002 ),
(204 , 'grass' , 'barcelona' , 100 , 1002 ),
(206 , 'clemens' , 'london' , 300 , 1007 ),
(207 , 'pereira' , 'roe' , 100 , 1004 );

select * from customer;

SELECT *
FROM customer
WHERE Sno > 1000;


SELECT Sname , city
FROM salesperson
WHERE city = 'london';

SELECT Sname , city , comm
FROM salesperson
WHERE comm > .12  ;

SELECT Sname , city
FROM salesperson
WHERE city = 'london' or city = 'barcelona';


SELECT Sname , comm
FROM salesperson
WHERE comm > .10 and comm < .12;


SELECT Cname as customer , rating
FROM customer
WHERE rating <= 100 and city = 'roe';

