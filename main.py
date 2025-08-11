import tkinter as tk
from gui import PyATM
from configs import load_config

if __name__ == "__main__":
    root = tk.Tk()
    app = PyATM(root)
    root.mainloop()