--- Personal Finance & Expense Analytics ---

--- DATABASE --
CREATE DATABASE finance_db;

--- TABLES ---
USE finance_db;
CREATE TABLE categories(
id INT PRIMARY KEY AUTO_INCREMENT,
category_name VARCHAR(50) NOT NULL
);

CREATE TABLE transactions(
id INT PRIMARY KEY AUTO_INCREMENT,
transaction_type VARCHAR(10) NOT NULL,
amount DECIMAL (10,2) NOT NULL,
category_id INT,
description VARCHAR(20),
transaction_date DATE NOT NULL,

FOREIGN KEY (category_id)
REFERENCES categories(id)
);


--- Check Tables ---
SELECT *
FROM categories;

SELECT * 
FROM transactions;

