import tkinter as tk
from tkinter import messagebox
from utils import load_data, save_data
from auth import authenticate_user
from transaction import process_transaction, check_balance, cancel_transaction, go_back, show_instructions
from widget import create_screen, create_keypad, create_button

class PyATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("1280x800")

        # Load user data
        self.data = load_data()
        if self.data is None:
            self.root.quit()

        # Initialize variables
        self.current_pin = None
        self.current_user = None
        self.transaction_type = None
        self.entry_text = ""  # Initialize entry_text here
        self.screen_text = tk.StringVar()

        # Create GUI elements
        self.create_widgets()

        # Set initial screen text and background color
        self.screen_text.set("Enter PIN")
        self.screen.config(bg="lightgray")
        
        # Set root background color
        self.root.config(bg='silver')

    def create_widgets(self):
        create_screen(self)
        create_keypad(self)
        
        create_button(self, "Withdraw", 0.12, 0.4, self.withdraw)
        create_button(self, "Deposit", 0.12, 0.5, self.deposit)
        create_button(self, "Check Balance", 0.12, 0.6, self.check_balance)
        create_button(self, "Cancel Transaction", 0.88, 0.4, self.cancel_transaction)
        create_button(self, "Go Back", 0.88, 0.5, self.go_back)
        create_button(self, "Instructions", 0.88, 0.6, self.show_instructions)

    def handle_keypad(self, num):
        if num == ' ':
            return  # Ignore space button
        self.entry_text += num
        self.screen_text.set(self.entry_text)

    def clear(self):
        self.entry_text = ""
        self.screen_text.set(self.entry_text)

    def enter(self):
        if not self.current_pin:
            self.authenticate_user()
        elif not self.transaction_type:
            messagebox.showerror("Error", "Please select a transaction type.")
        else:
            self.process_transaction()

    def authenticate_user(self):
        pin = self.entry_text
        if pin in self.data['users']:
            self.current_pin = pin
            self.current_user = self.data['users'][pin]
            self.entry_text = ""
            self.screen_text.set(f"Welcome {self.current_user['name']}")
        else:
            messagebox.showerror("Error", "Invalid PIN")
            self.clear()

    def withdraw(self):
        if not self.current_pin:
            messagebox.showerror("Error", "Please authenticate first.")
            return
        self.transaction_type = "withdraw"
        self.screen_text.set("Enter amount to withdraw:")
        self.screen.config(font=("Courier New", 17, "bold"),
                           borderwidth=2, relief="solid", width=28, height=7)

    def deposit(self):
        if not self.current_pin:
            messagebox.showerror("Error", "Please authenticate first.")
            return
        self.transaction_type = "deposit"
        self.screen_text.set("Enter amount to deposit:")
        self.screen.config(font=("Courier New", 17, "bold"),
                           borderwidth=2, relief="solid", width=28, height=7)

    def check_balance(self):
        if not self.current_pin:
            messagebox.showerror("Error", "Please authenticate first.")
            return
        self.screen_text.set(f"Balance: ${self.current_user['balance']}")

    def process_transaction(self):
        amount = self.entry_text
        try:
            amount = float(amount)
            if self.transaction_type == "withdraw":
                if amount > self.current_user['balance']:
                    messagebox.showerror("Error", "Insufficient funds")
                else:
                    self.current_user['balance'] -= amount
                    self.show_receipt("Withdraw", amount)
            elif self.transaction_type == "deposit":
                self.current_user['balance'] += amount
                self.show_receipt("Deposit", amount)

            # Save updated data
            save_data(self.data)

            # Clear entry text and reset transaction type
            self.clear()
            self.transaction_type = None
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            self.clear()

    def show_receipt(self, transaction_type, amount):
        receipt = f"Transaction Type: {transaction_type}\n"
        receipt += f"Amount: ${amount:.2f}\n"
        receipt += f"New Balance: ${self.current_user['balance']:.2f}\n"
        receipt += "Thank you for using our ATM!"
        messagebox.showinfo("Receipt", receipt)

    def cancel_transaction(self):
        self.current_pin = None
        self.current_user = None
        self.transaction_type = None
        self.screen_text.set("Transaction canceled")
        self.clear()

    def go_back(self):
        self.current_pin = None
        self.transaction_type = None
        self.screen_text.set("Go back to main menu")
        self.clear()

    def show_instructions(self):
        instructions = (
            "Instructions:\n"
            "1. Enter PIN to log in.\n"
            "2. Select a transaction type (Deposit/Withdraw/Check Balance).\n"
            "3. Enter the amount and press Enter.\n"
            "4. Use Clear to reset or Cancel to abort."
        )
        messagebox.showinfo("Instructions", instructions)