import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt

# MySQL Database Connection for Finance Manager
db = mysql.connector.connect(
    host="localhost",
    user="root",    # Replace with your MySQL username
    password="334229",  # Replace with your MySQL password
    database="finance_manager"
)

cursor = db.cursor()

# Finance Manager Functions
def add_transaction(category, amount):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO transactions (date, category, amount) VALUES (%s, %s, %s)"
    values = (date, category, amount)
    cursor.execute(query, values)
    db.commit()
    print("Transaction added successfully.")

def view_transactions():
    query = "SELECT * FROM transactions"
    cursor.execute(query)
    rows = cursor.fetchall()
    if not rows:
        print("No transactions available.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Category: {row[2]}, Amount: {row[3]}")

def erase_transaction(transaction_id):
    query = "DELETE FROM transactions WHERE id = %s"
    cursor.execute(query, (transaction_id,))
    db.commit()
    
    if cursor.rowcount > 0:
        print(f"Transaction with ID {transaction_id} has been deleted.")
    else:
        print(f"No transaction found with ID {transaction_id}.")

def erase_all_transactions():
    query = "TRUNCATE TABLE transactions"
    cursor.execute(query)
    db.commit()
    print("All transactions have been deleted.")

# Monthly summary by category
def monthly_summary():
    query = "SELECT category, SUM(amount) FROM transactions GROUP BY category"
    cursor.execute(query)
    summary = cursor.fetchall()
    
    if not summary:
        print("No transactions available for summary.")
    else:
        print("Monthly Summary by Category:")
        for category, total in summary:
            print(f"{category}: {total}")

# Spending chart (pie chart)
def spending_chart():
    query = "SELECT category, SUM(amount) FROM transactions GROUP BY category"
    cursor.execute(query)
    data = cursor.fetchall()
    
    if not data:
        print("No transactions available for chart.")
    else:
        categories = [row[0] for row in data]
        amounts = [row[1] for row in data]
        
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title("Spending by Category")
        plt.show()

# Main Finance Manager loop
def finance_manager():
    while True:
        print("\n--- Finance Manager ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Erase Transaction ID")
        print("4. Erase All Transactions")
        print("5. Monthly Summary")
        print("6. Spending Chart")
        print("7. Exit Finance Manager")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter category (e.g., Food, Rent): ")
            amount = float(input("Enter amount: "))
            add_transaction(category, amount)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            transaction_id = int(input("Enter the ID of the transaction to delete: "))
            erase_transaction(transaction_id)
        elif choice == '4':
            erase_all_transactions()
        elif choice == '5':
            monthly_summary()
        elif choice == '6':
            spending_chart()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")
