import tkinter as tk

def create_screen(atm):
    atm.screen = tk.Label(atm.root, text="", font=("Courier New", 24),
                          borderwidth=2, relief="solid", width=20, height=5)
    atm.screen.place(relx=0.5, rely=0.19, anchor=tk.CENTER)
    atm.screen_text = tk.StringVar()
    atm.screen.config(textvariable=atm.screen_text)
    atm.screen.config(bg="lightgray")
    atm.screen_text.set("Enter PIN")
    atm.root.config(bg='silver')

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

def create_button(atm, text, relx, rely, command):
    button = tk.Button(atm.root, text=text, command=command, width=15, height=2)
    button.place(relx=relx, rely=rely, anchor=tk.CENTER)