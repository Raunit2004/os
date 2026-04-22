import tkinter as tk
from tkinter import scrolledtext, messagebox
import json

def launch_gui():
    root = tk.Tk()
    root.title("IPC Debugger GUI")
    root.geometry("800x600")

    tk.Label(root, text="IPC Debugger Logs Viewer", font=("Arial", 16)).pack(pady=10)

    # Load logs button
    def load_logs():
        try:
            text_area.delete(1.0, tk.END)
            with open("logs.json", "r") as f:
                for line_num, line in enumerate(f, 1):
                    try:
                        log = json.loads(line.strip())
                        formatted = f"[{line_num}] {log['time']} | {log['sender']} -> {log['receiver']} | {log['message']} | Delay: {log.get('delay', 'N/A'):.4f}\n"
                    except:
                        formatted = f"[{line_num}] Invalid: {line.strip()}\n"
                    text_area.insert(tk.END, formatted)
            text_area.see(tk.END)
        except FileNotFoundError:
            messagebox.showinfo("Info", "No logs.json found. Run python main.py first.")

    tk.Button(root, text="Load Logs", command=load_logs, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)

    # Analyze button
    from debugger import analyze_logs_json
    def show_analysis():
        try:
            analysis = analyze_logs_json()
            msg = f"Summary: {analysis['summary']['total_logs']} logs, {analysis['summary']['high_delays']} high delays, {analysis['summary']['suspicious_alerts']} alerts"
            messagebox.showinfo("Analysis", msg)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(root, text="Run Analysis", command=show_analysis, font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=5)

    # Scrolled text
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25, font=("Consolas", 10))
    text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    root.mainloop()

