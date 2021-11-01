-------- Create a database for the project----------

create database ems;
go

use ems;
go

------- Create structures for all tables-----------

--- create address table
create table address(
	id int primary key,
	street varchar(100) not null,
	city varchar(25) not null,
	state varchar(25) not null
);

--- create department table
create table department (
	id int primary key, 
	name varchar(50) not null,
	manager_id int not null,
	headquarter_address_id int not null,
	foreign key (headquarter_address_id) references address(id) on delete cascade on update cascade
	--foreign key (manager_id) references employee(manager_id) on delete cascade on update cascade
);

--- create employee table
create table employee(
	id int primary key ,
	name varchar(50) not null,
	age int,
	salary decimal(8,2) not null,
	department_id int not null,
	address_id int not null,
	manager_id int default null,
	foreign key (department_id) references department(id),
	foreign key (address_id) references address(id),
	foreign key (manager_id) references employee(id) 
);


-----------insert the values in tables---------------------

---insert into address table

insert into address (id,street,city,state)
	values (1,'2014 Jabberwocky Rd','South Lake','Texas'),
			(2,'147 Spadina Ave','Hobokon','New Jersery'),
			(3,'2011 Interiors Blvd','San Francisco','California'),
			(4,'560 Passaic Ave','Passaic','New Jersery');

---insert into department table

INSERT INTO department(id,name,manager_id,headquarter_address_id)
	VALUES  (01,'Administration',100,3),
			(02,'IT',103,2),
			(03,'Finance',104,1),
			(04,'Human Resources',101,1),
			(05,'Marketing',108,2),
			(06,'Sales',110,3);


---insert into employee table

insert into employee (id ,name,age,salary,department_id,address_id,manager_id)
	values (100,'Steven King', 26,80000.00,01,3,NULL),
		   (101,'Jennifer King',32,52000.00,01,2,100),
		   (102,'Bob Austin',28,40000.00,01,2,101),
		   (103,'Phoebe Khoo',24,65000.00,02,3,100),
		   (104,'Matthew Weiss',30,28000.00,03,1,100),
		   (105,'Shelli Baida',29,35000.00,02,1,104),
		   (106,'Jose Manuel Urman',40,45000.00,01,3,101),
		   (107,'Karen Colmenares',32,65000.00,03,2,103),
		   (108,'Nancy Greenberg',41,38000.00,02,2,100),
		   (109,'Den Raphaely',29,39000.00,06,1,110),
		   (110,'Shanta Vollman',37,50000.00,06,3,100),
		   (111,'John Russell',29,34000.00,03,2,103),
		   (112,'Nancie Patel',34,55000.00,03,3,104),
		   (113,'Jack Livingston',32,47000.00,05,1,108),
		   (114,'Guy Himuro', 33,39000.00,06,2,110);



--Checking the content
select * from employee;
select * from department;
select * from address;

select state,city from address group by state,city;
 --For testing purpose, if error occur--> drop table 
 drop table employee;
 drop table address;
 drop table department;

