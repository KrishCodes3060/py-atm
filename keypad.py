def create_keypad(atm):
    atm.keypad_frame = tk.Frame(atm.root)
    atm.keypad_frame.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    atm.keypad = [
        '1', '2', '3',
        '4', '5', '6',
        '7', '8', '9',
        '–', '0', '+'
    ]

    for i, num in enumerate(atm.keypad):
        button = tk.Button(atm.keypad_frame, text=num, width=5, height=2, command=lambda n=num: atm.handle_keypad(n))
        button.grid(row=i//3, column=i%3)

    atm.enter_button = tk.Button(atm.keypad_frame, text="Enter", width=5, height=2, command=atm.enter)
    atm.enter_button.grid(row=4, column=0)

    atm.clear_button = tk.Button(atm.keypad_frame, text="Clear", width=5, height=2, command=atm.clear)
    atm.clear_button.grid(row=4, column=1)

    atm.cancel_button = tk.Button(atm.keypad_frame, text="Cancel", width=5, height=2, command=atm.clear)
    atm.cancel_button.grid(row=4, column=2)