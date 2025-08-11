from logic import process_transaction as process

def withdraw(atm):
    if not atm.current_pin:
        messagebox.showerror("Error", "Please authenticate first.")
        return
    atm.transaction_type = "withdraw"
    atm.screen_text.set("Enter amount to withdraw:")
    atm.process_transaction = lambda: process(atm)