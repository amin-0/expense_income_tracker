import tkinter as tk 
from tkinter import ttk
import matplotlib.pyplot as plt


class Transaction:
    def __init__(self, transaction_type, amount, description, date):
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.date = date

class ExpensesIncomesTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expenses and Incomes Tracker")

        # Initialize variables
        self.transaction_var = tk.StringVar()
        self.total_incomes = tk.DoubleVar()
        self.total_expenses = tk.DoubleVar()
        self.total_balance = tk.DoubleVar()
        self.category = tk.StringVar()
        # self.description = tk.StringVar()
        self.categories = [
            "Salary",
            "Gift",
            "Investment",
            "Gift",
            "Food",
            "Transportation",
            "Utilities",
            "Sadaqah",
            "Others",
            "Others",]
        self.expenses =  []
        self.incomes = []
        # self.category.set(self.categories[0])

        # Create the UI
        self.create_ui()
    
    
    def create_ui(self):
        # Create and pack the title label
        title_label = ttk.Label(self.root, text="Budget Tracker", 
        font=("Arial", 16, "bold"), foreground="#d35400")
        title_label.pack(pady=10)

        # Create and pack radio buttons for transaction type
        transaction_radio_frame = ttk.Frame(self.root)
        transaction_radio_frame.pack(pady=10)


        expense_radio = ttk.Radiobutton(transaction_radio_frame, text="Expense", 
        variable=self.transaction_var, value="Expense")
        expense_radio.grid(row=0, column=0, padx=10)

        income_radio = ttk.Radiobutton(transaction_radio_frame, text="Income", 
        variable=self.transaction_var, value="Income")

        income_radio.grid(row=0, column=1, padx=10)

        # Create and pack the frame for amount and description
        entry_frame = ttk.Frame(self.root)
        entry_frame.pack(pady=10)

        # Create amount label and entry
        amount_label = ttk.Label(entry_frame, text="Amount: ", font=("Arial", 12), 
        foreground="#34495e")

        amount_label.grid(row=0,column=0, padx=5)

        self.amount_entry = ttk.Entry(entry_frame,  font=("Arial", 12))
        self.amount_entry.grid(row=0,column=1)

        # Create description label and entry
        description_label = ttk.Label(entry_frame, text="Description: ", 
        font=("Arial", 12), foreground="#34495e")

        description_label.grid(row=0,column=2, padx=5)

        self.description_entry = ttk.Combobox(
            entry_frame,
            textvariable=self.category,
            values=self.categories,
            font=("Helvetica", 12),
            width=15,
        )
        self.description_entry.grid(row=0, column=3)

        # Create date label and entry

        date_label = ttk.Label(entry_frame, text="Date:", 
        font=("Arial", 12), foreground="#34495e")

        date_label.grid(row=0,column=4, padx=5)

        self.date_entry = ttk.Entry(entry_frame,  font=("Arial", 12))
        self.date_entry.grid(row=0,column=5)

        # Create and pack the frame for Add Transaction and Show Chart button
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        # Create and pack the "Add Transaction" button
        add_button = tk.Button(button_frame, text="Add Transaction", bg="green", 
        fg="black", font=("Arial", 12, "bold"), width="22", 
        command=self.add_transaction)

        add_button.pack(pady=10)

        # Create and pack the "Show Expense Chart" button
        expense_button = tk.Button(button_frame, text="Show Expense Chart", bg="lightblue", 
        fg="black", font=("Arial", 12, "bold"), width="22", 
        command=self.show_expense_chart)

        expense_button.pack(pady=10)

         # Create and pack the "Show Income Chart" button
        income_button = tk.Button(button_frame, text="Show Income Chart", bg="cyan", 
        fg="black", font=("Arial", 12, "bold"), width="22", 
        command=self.show_income_chart)

        income_button.pack(pady=10)

        # Create and pack the frame for the lists of expenses and incomes
        listFrame = ttk.Frame(self.root)
        listFrame.pack()

        # Create Treeview with Scrollbar for expenses and incomes
        self.expenses_incomes_list = ttk.Treeview(listFrame, 
        columns=("Type", "Amount", "Description", "Date"), show="headings", height=5)

        self.expenses_incomes_list.heading("Type", text="Type")
        self.expenses_incomes_list.heading("Amount", text="Amount")
        self.expenses_incomes_list.heading("Description", text="Description")
        self.expenses_incomes_list.heading("Date", text="Date")
        self.expenses_incomes_list.pack(side="right", padx=(0, 20), fill=tk.Y)

        # Scrollbar for expenses and incomes Treeview
        scrollbar = ttk.Scrollbar(listFrame, orient="vertical", 
        command=self.expenses_incomes_list.yview)

        scrollbar.pack(side="right", padx=(20, 0), fill="y")
        self.expenses_incomes_list.config(yscrollcommand=scrollbar.set)

        # Create and pack the frame for displaying totals
        totals_frame = ttk.Frame(self.root)
        totals_frame.pack(pady=10)

        total_expenses_label = ttk.Label(totals_frame, text="Total Expenses: ", 
        font=("Arial", 12, "bold"), foreground="#e74c3c")

        total_expenses_label.grid(row=0, column=0, padx=0)

        self.total_expenses_display = ttk.Label(totals_frame,
        textvariable=self.total_expenses, font=("Arial", 12, "bold"), 
        foreground="#e74c3c")

        self.total_expenses_display.grid(row=0, column=1, padx=(0,20))

        total_incomes_label = ttk.Label(totals_frame, text="Total Incomes: ", 
        font=("Arial", 12, "bold"), foreground="#2ecc71")

        total_incomes_label.grid(row=0, column=2, padx=0)

        self.total_incomes_display = ttk.Label(totals_frame,
        textvariable=self.total_incomes, font=("Arial", 12, "bold"), 
        foreground="#2ecc71")

        self.total_incomes_display.grid(row=0, column=3, padx=(0,20))

        total_balance_label = ttk.Label(totals_frame, text="Balance: ", 
        font=("Arial", 12, "bold"), foreground="#3498db")

        total_balance_label.grid(row=0, column=4, padx=0)

        self.total_balance_display = ttk.Label(totals_frame,
        textvariable=self.total_balance, font=("Arial", 12, "bold"), 
        foreground="#3498db")

        self.total_balance_display.grid(row=0, column=5, padx=(0,20))



    def add_transaction(self):
        # Get transaction type, amount, and description from the UI
        transaction_type = self.transaction_var.get()
        amount_entry_text = self.amount_entry.get()
        category_entry_text = self.description_entry.get()
        date_text = self.date_entry.get()

        try:
            amount = float(amount_entry_text)
        except ValueError:
            self.show_error_message("Invalid amount. Please enter a numeric value.")
            return

        if not amount_entry_text or amount <= 0 :
            self.show_error_message("Amount cannot be empty or non-positive")
            return

        
        if not transaction_type :
            self.show_error_message("Please select a transaction type")
            return
        
        if not date_text :
            self.show_error_message("Please include a date")
            return


        # Create a Transaction object and update UI
        self.expenses_incomes_list.insert("","end", values=(transaction_type, 
        amount_entry_text, category_entry_text, date_text))

        if transaction_type == "Expense":
            self.total_expenses.set(self.total_expenses.get() + amount)
            self.expenses.append((amount_entry_text, category_entry_text, date_text))

        else:
            self.total_incomes.set(self.total_incomes.get() + amount)
            self.incomes.append((amount_entry_text, category_entry_text, date_text))

        self.total_balance.set(self.total_incomes.get() - self.total_expenses.get())

        # Clear entries
        self.amount_entry.delete(0, "end")
        self.description_entry.delete(0, "end")
        self.date_entry.delete(0, "end")

    def show_expense_chart(self):
        expense_category_totals = {}
        for expense, category, _ in self.expenses:
            try:
                amount = float(expense)
            except ValueError:
                continue

            expense_category_totals[category] = expense_category_totals.get(category, 0) + amount

        categories = list(expense_category_totals.keys())
        expenses = list(expense_category_totals.values())
        plt.figure(figsize=(8, 6))
        plt.pie(
            expenses, labels=categories, autopct="%1.1f%%", startangle=140, shadow=True
        )
        plt.axis("equal")
        plt.title(f"Expense Categories Distribution (NGN)")
        plt.show()
    
    def show_income_chart(self):
        income_category_totals = {}
        for income, category, _ in self.incomes:
            try:
                amount = float(income)
            except ValueError:
                continue

            income_category_totals[category] = income_category_totals.get(category, 0) + amount
            
        categories = list(income_category_totals.keys())
        incomes = list(income_category_totals.values())
        plt.figure(figsize=(8, 6))
        plt.pie(
            incomes, labels=categories, autopct="%1.1f%%", startangle=140, shadow=True
        )
        plt.axis("equal")
        plt.title(f"Incomes Categories Distribution (NGN)")
        plt.show()

    def show_error_message(self, message):
        tk.messagebox.showerror("Error", message)




if __name__ == "__main__":
    root = tk.Tk()
    app = ExpensesIncomesTracker(root)
    root.mainloop()