import tkinter as tk
from tkinter import messagebox

# Dummy credentials
VALID_USERNAME = "JAY"
VALID_PASSWORD = "1212"

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    
    if not user or not pwd:
        messagebox.showwarning("Input Error", "Please fill in all fields.")
    elif user == VALID_USERNAME and pwd == VALID_PASSWORD:
        root.destroy()
        launch_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")

def launch_dashboard():
    dash = tk.Tk()
    dash.title("Dashboard")
    tk.Label(dash, text="Welcome, JAY", font=("Arial", 20)).pack(pady=250)  
    dash.mainloop()

root = tk.Tk()
root.title("COME IN")

tk.Label(root, text="Username").grid(row=0, column=0, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, columnspan=2, pady=10)

root.mainloop()
