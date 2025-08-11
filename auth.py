def authenticate_user(atm, pin):
    if pin in atm.data['users']:
        atm.current_pin = pin
        atm.current_user = atm.data['users'][pin]
        atm.entry_text = ""
        atm.screen_text.set(f"Welcome {atm.current_user['name']}")
    else:
        messagebox.showerror("Error", "Invalid PIN")
        atm.clear()