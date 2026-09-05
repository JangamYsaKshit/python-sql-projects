# 💰 Personal Finance & Expense Analytics

A Python and MySQL-based personal finance management system for recording, managing, and analyzing income and expense transactions.

## 📌 Project Overview

Personal Finance & Expense Analytics is a console-based application built with **Python** and **MySQL**.

The application allows users to manage financial transactions and perform basic financial analysis through a simple menu-driven interface. It demonstrates how Python can interact with a relational database to perform **CRUD operations, SQL aggregations, joins, filtering, and transaction analysis**.

This project was built as part of my journey toward becoming a **Data Scientist / Machine Learning Engineer**, with a focus on strengthening my Python, SQL, database, and data-analysis skills.

---

## 🎯 Project Goals

The main goals of this project are to:

- Practice connecting Python applications with MySQL databases
- Understand relational database design
- Implement CRUD operations using Python and SQL
- Work with SQL filtering, aggregation, and grouping
- Use `INNER JOIN` to combine related tables
- Build monthly financial summaries
- Analyze expenses by category
- Practice writing structured and readable Python code
- Develop real-world problem-solving skills

---

## 🚀 Features

### 1. Add Income

Allows users to record income transactions including:

- Transaction type
- Amount
- Category
- Description
- Transaction date

### 2. Add Expense

Allows users to record expense transactions using the same transaction structure.

### 3. View Transactions

Displays all stored financial transactions from the MySQL database.

### 4. Search Transactions

Allows users to search for a specific transaction using its unique transaction ID.

### 5. View Categories

Displays all available transaction categories stored in the database.

### 6. Monthly Summary

Generates a financial summary for a selected month and year.

The application calculates:

- Total income
- Total expenses
- Remaining balance

**Balance = Total Income − Total Expenses**

### 7. Expense Analysis

Analyzes expenses by category using SQL aggregation.

For example:

```text
Category       Total Spent
--------------------------
Food           250.50
Transport      120.00
Shopping       300.75
