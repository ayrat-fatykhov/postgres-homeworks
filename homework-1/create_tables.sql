-- SQL-команды для создания таблиц
CREATE TABLE employees (
employee_id int PRIMARY KEY,
first_name varchar(100) NOT NULL,
last_name varchar(100) NOT NULL,
title varchar(255) NOT NULL,
birth_date varchar(100) NOT NULL,
notes text
);

CREATE TABLE customers_v2 (
customer_id varchar(5) PRIMARY KEY,
company_name varchar(100) NOT NULL,
contact_name varchar(100) NOT NULL
);

CREATE TABLE orders (
order_id int PRIMARY KEY,
customer_id varchar(5) REFERENCES customers_v2(customer_id) NOT NULL,
employee_id int REFERENCES employees(employee_id) NOT NULL,
order_date varchar(100) NOT NULL,
ship_city varchar(100) NOT NULL
);
