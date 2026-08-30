# Project 1 - Personal Finance & Expense Analytics

# Project Goal: Build a Python and MySQL-based personal finance management system that allows users to record, manage, search, update, and delete income and expense transactions. 
                # The project also provides monthly financial summaries and category-based expense analysis to help users understand their spending and overall financial balance.


# Library
import mysql.connector


# Connect To MSQL 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "**********",
    database = "finance_db"
)

# Check Connections
#if mydb.is_connected():
    #print("Connected Successfully!")

# Create cursor
cursor = mydb.cursor()



# Main Menu
while True:
    print()
    print("========== PERSONAL FINANCE ==========")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Search Transactions")
    print("5. View Categories")
    print("6. Monthly Summary")
    print("7. Expense Analysis")
    print("8. Update Transaction")
    print("9. Delete Transaction")
    print("10. Exit")
    print()


    user_menu = int(input("Enter your choice: "))


    # 1. Add Income
    if user_menu == 1:

        transaction_type = input("Enter Transaction Type: ")
        amount = float(input("Enter Income Amount: "))
        category_id = int(input("Enter Category Number: "))
        description = (input("Enter Description: "))
        transaction_date = input("Enter Transaction Date: ")

        query = """ 
        INSERT INTO transactions
        (transaction_type, amount, category_id, description, transaction_date)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (transaction_type, amount, category_id, description, transaction_date)

        cursor.execute(query, values)
        mydb.commit()

        print("Income Added Successfully!")


    # 2. Add Expenses
    elif user_menu == 2:

        transaction_type = input("Enter Transaction Type: ")
        amount = float(input("Enter Expense Amount: "))
        category_id = int(input("Enter Category Number: "))
        description = input("Enter Description: ")
        transaction_date = input("Enter Transaction Date: ")

        query = """
        INSERT INTO transactions
        (transaction_type, amount, category_id, description, transaction_date)
        VALUES(%s, %s, %s, %s, %s)
        """

        values = (transaction_type, amount, category_id, description, transaction_date)

        cursor.execute(query, values)
        mydb.commit()

        print("Expense Added Successfully!")


    # 3. View Transactions
    elif user_menu == 3:

        cursor.execute("Select * From transactions")
        views = cursor.fetchall()

        if len(views) == 0:
            print("No Transactions Found.")

        else:
            print("========== ALL TRANSACTIONS ==========")
            print()

            for view in views:
                transaction_id = view[0]
                transaction_type = view[1]
                amount = view[2]
                category_id = view[3]
                description = view[4]
                transaction_date = view[5]

                print("ID:", transaction_id,"| Transaction Type:",transaction_type, "| Amount:", amount, "| Category ID:", category_id, "| Description:", description, "| Transaction Date:", transaction_date)


    # 4. Search Transactions
    elif user_menu == 4:

        search = int(input("Enter Transaction ID: "))

        query = """
        SELECT * FROM transactions
        WHERE id = %s
        """

        cursor.execute(query, (search,))
        view = cursor.fetchone()

        if view is not None:
            transaction_id = view[0]
            transaction_type = view[1]
            amount = view[2]
            category_id = view[3]
            description = view[4]
            transaction_date = view[5]

            print(
                "ID:", transaction_id,
                "| Transaction Type:", transaction_type,
                "| Amount:", amount,
                "| Category ID:", category_id,
                "| Description:", description,
                "| Transaction Date:", transaction_date
            )

        else:
            print("Error, Data Not Found!")


    # 5. View Categories
    elif user_menu == 5:

        cursor.execute("SELECT * FROM categories")
        view_categories = cursor.fetchall()

        if len(view_categories) == 0:
            print("No Categories Found.")

        else:
            print("========== CATEGORIES ==========")
            for views in view_categories:
                category_id = views[0]
                category_name = views[1]
                print("ID:", category_id, "| Category Name:", category_name)


    # 6. Monthly Summary
    elif user_menu == 6:

        month = int(input("Enter Month: "))
        year = int(input("Enter Year: "))

        # Calculate total income
        query1 = """
        SELECT SUM(amount) FROM transactions WHERE transaction_type = "Income" AND MONTH(transaction_date) = %s AND YEAR(transaction_date) = %s
        """
        cursor.execute(query1, (month, year))
        total_income = cursor.fetchone()[0]
        # If there are no income transactions
        if total_income is None:
            total_income = 0

        # Calculate total expenses
        query2 = """
        SELECT SUM(amount) FROM transactions WHERE transaction_type = "Expense" AND MONTH(transaction_date) = %s AND YEAR(transaction_date) = %s
        """
        cursor.execute(query2, (month, year))
        total_expenses = cursor.fetchone()[0]
        
        # If there are no expenses transactions
        if total_expenses is None:
            total_expenses = 0

        Balance = total_income - total_expenses

        print("========== MONTHLY SUMMARY ==========")
        print()
        print("Month:", month, year)
        print("Total Income:", total_income)
        print("Total Expenses:", total_expenses)
        print("--------------------------------")
        print("Balance:", Balance)
        print("--------------------------------")


    # 7. Expense Analysis
    elif user_menu == 7:

        query = """
        SELECT categories.category_name, SUM(transactions.amount)
        FROM transactions 
        INNER JOIN categories
        ON transactions.category_id = categories.id
        WHERE transactions.transaction_type = "Expense"
        GROUP BY categories.category_name
        """

        cursor.execute(query)
        expense_results = cursor.fetchall()
        if not expense_results:
            print("No Transactions Found.")

        else:
            print("========== EXPENSE ANALYSIS ==========")
            print()
            print("Category          Total Spent")
            print("----------------------------------")
            print()
            for total_exp in expense_results:
                category_name = total_exp[0]
                amount = total_exp[1]
                print(category_name,          amount)


    # 8. Update Transaction
    elif user_menu == 8:

        transaction_id = int(input("Enter Transaction ID: "))

        query = """
        SELECT * FROM transactions WHERE id = %s
        """

        cursor.execute(query, (transaction_id,))
        update_result = cursor.fetchone()

        if not update_result:
            print("ERROR, Data Not Found.")

        else:
            # Display existing transaction  
                transaction_id = update_result[0]
                transaction_type = update_result[1]
                amount = update_result[2]
                category_id = update_result[3]
                description = update_result[4]
                transaction_date = update_result[5]

                print(
                    "ID:", transaction_id,
                    "| Transaction Type:", transaction_type,
                    "| Amount:", amount,
                    "| Category ID:", category_id,
                    "| Description:", description,
                    "| Transaction Date:", transaction_date
                    )

                print()
                print("What do you want to update?")
                print("1 - Transaction Type")
                print("2 - Amount")
                print("3 - Category")
                print("4 - Description")
                print("5 - Transaction Date")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    column_name = "transaction_type"

                elif user_choice == 2:
                    column_name = "amount"

                elif user_choice == 3:
                    column_name = "category_id"

                elif user_choice == 4:
                    column_name = "description"

                elif user_choice == 5:
                    column_name = "transaction_date"

                else:
                    print("Invalid Choice.")
                    continue


                user_new_data = input("Enter New Data: ") 

                query = f"""
                UPDATE transactions
                SET {column_name} = %s
                WHERE id = %s
                """

                cursor.execute(query, (user_new_data, transaction_id))
                mydb.commit()

                print("Data Updated Successfully.")

    # 9 Delete Transaction
    elif user_menu == 9:

        transaction_id = int(input("Enter Transaction ID: "))

        query = """
        SELECT * FROM transactions WHERE id = %s
        """

        cursor.execute(query, (transaction_id,))
        delete_result = cursor.fetchall()
        if not delete_result:
            print("ERROR, Data Not Found.")

        else:
            for delete in delete_result:
                transaction_id = delete[0]
                transaction_type = delete[1]
                amount = delete[2]
                category_id = delete[3]
                description = delete[4]
                transaction_date = delete[5]

                print(
                    "ID:", transaction_id,
                    "| Transaction Type:", transaction_type,
                    "| Amount:", amount,
                    "| Category ID:", category_id,
                    "| Description:", description,
                    "| Transaction Date:", transaction_date
                )

                user_conformation = input("Confirmation To Delete Type (Yes/No)").lower()

                if user_conformation == "yes":
                    query = """
                    DELETE FROM transactions
                    WHERE id = %s
                    """
                    cursor.execute(query, (transaction_id, ))
                    mydb.commit()
                    
                    print("Data Deleted Succssfully.")

                else:
                    print("Request Terminated.")

    # 10 Exit
    elif user_menu == 10:

        print("Exit")
        break

    else:
        print("Invalid Menu Choice.")