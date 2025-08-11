def create_button(atm, text, relx, rely, command):
    button = tk.Button(atm.root, text=text, command=command, width=15, height=2)
    button.place(relx=relx, rely=rely, anchor=tk.CENTER)

def handle_keypad(atm, num):
    if num == ' ':
        return  # Ignore space button
    atm.entry_text += num
    atm.screen_text.set(atm.entry_text)

def clear(atm):
    atm.entry_text = ""
    atm.screen_text.set(atm.entry_text)

def enter(atm):
    if not atm.current_pin:
        atm.authenticate_user(atm.entry_text)
    elif not atm.transaction_type:
        messagebox.showerror("Error", "Please select a transaction type.")
    else:
        atm.process_transaction()