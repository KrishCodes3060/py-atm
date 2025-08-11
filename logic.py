import tkinter as tk
from tkinter import messagebox
import json

def authenticate_user(atm, pin):
    if pin in atm.data['users']:
        atm.current_pin = pin
        atm.current_user = atm.data['users'][pin]
        atm.entry_text = ""
        atm.screen_text.set(f"Welcome {atm.current_user['name']}")
    else:
        messagebox.showerror("Error", "Invalid PIN")
        atm.clear()

def process_transaction(atm):
    amount = atm.entry_text
    try:
        amount = float(amount)
        if atm.transaction_type == "withdraw":
            if amount > atm.current_user['balance']:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                atm.current_user['balance'] -= amount
                show_receipt(atm, "Withdraw", amount)
        elif atm.transaction_type == "deposit":
            atm.current_user['balance'] += amount
            show_receipt(atm, "Deposit", amount)

        # Update the user balance in the data dictionary
        atm.data['users'][atm.current_pin]['balance'] = atm.current_user['balance']

        # Save updated data
        save_data(atm)

        # Clear entry text and reset transaction type
        atm.clear()
        atm.transaction_type = None
    except ValueError:
        messagebox.showerror("Error", "Invalid amount")
        atm.clear()

def show_receipt(atm, transaction_type, amount):
    receipt = f"Transaction Type: {transaction_type}\n"
    receipt += f"Amount: ${amount:.2f}\n"
    receipt += f"New Balance: ${atm.current_user['balance']:.2f}\n"
    receipt += "Thank you for using PyATM!"
    messagebox.showinfo("Receipt", receipt)

def save_data(atm):
    try:
        with open('data/atm_data.json', 'w') as file:
            json.dump(atm.data, file, indent=4)
    except IOError:
        messagebox.showerror("Error", "Unable to save data.")