import tkinter as tk

def launch_gui():
    root = tk.Tk()
    root.title("IPC Debugger Dashboard")

    label = tk.Label(root, text="IPC Debugger Running...", font=("Arial", 14))
    label.pack(pady=20)

    root.mainloop()