from utils import save_data

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

        # Save updated data
        save_data(atm.data)

        # Clear entry text and reset transaction type
        atm.clear()
        atm.transaction_type = None
    except ValueError:
        messagebox.showerror("Error", "Invalid amount")
        atm.clear()

def check_balance(atm):
    if not atm.current_pin:
        messagebox.showerror("Error", "Please authenticate first.")
        return
    atm.screen_text.set(f"Balance: ${atm.current_user['balance']}")

def cancel_transaction(atm):
    atm.current_pin = None
    atm.current_user = None
    atm.transaction_type = None
    atm.screen_text.set("Transaction canceled")
    atm.clear()

def go_back(atm):
    atm.current_pin = None
    atm.transaction_type = None
    atm.screen_text.set("Go back to main menu")
    atm.clear()

def show_instructions(atm):
    instructions = (
        "Instructions:\n"
        "1. Enter PIN to log in.\n"
        "2. Select a transaction type (Deposit/Withdraw/Check Balance).\n"
        "3. Enter the amount and press Enter.\n"
        "4. Use Clear to reset or Cancel to abort."
    )
    messagebox.showinfo("Instructions", instructions)

def show_receipt(atm, transaction_type, amount):
    receipt = f"Transaction Type: {transaction_type}\n"
    receipt += f"Amount: ${amount:.2f}\n"
    receipt += f"New Balance: ${atm.current_user['balance']:.2f}\n"
    receipt += "Thank you for using our ATM!"
    messagebox.showinfo("Receipt", receipt)