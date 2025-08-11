import json
from tkinter import messagebox

def load_data():
    try:
        with open('data/atm_data.json', 'r') as file:
            data = json.load(file)
        if 'users' not in data:
            raise KeyError("Missing 'users' key in data file.")
        return data
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found.")
        return None
    except KeyError as e:
        messagebox.showerror("Error", str(e))
        return None
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Data file is not a valid JSON.")
        return None

def save_data(data):
    try:
        with open('data/atm_data.json', 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        messagebox.showerror("Error", "Unable to save data.")