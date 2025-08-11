def create_screen(atm):
    atm.screen = tk.Label(atm.root, text="", font=("Courier New", 24),
                          borderwidth=2, relief="solid", width=20, height=5)
    atm.screen.place(relx=0.5, rely=0.19, anchor=tk.CENTER)
    atm.screen_text = tk.StringVar()
    atm.screen.config(textvariable=atm.screen_text)
    atm.screen.config(bg="lightgray")
    atm.screen_text.set("Enter PIN")
    atm.root.config(bg='silver')