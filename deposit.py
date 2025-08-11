from logic import process_transaction as process

def deposit(atm):
    if not atm.current_pin:
        messagebox.showerror("Error", "Please authenticate first.")
        return
    atm.transaction_type = "deposit"
    atm.screen_text.set("Enter amount to deposit:")
    atm.process_transaction = lambda: process(atm)