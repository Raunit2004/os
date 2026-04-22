# debugger.py
import json

THRESHOLD = 1.0  # seconds

def analyze_logs():
    print("\n--- DEBUGGER REPORT ---")

    try:
        with open("logs.json", "r") as f:
            for line in f:
                log = json.loads(line)

                if log["delay"] is not None:
                    if log["delay"] > THRESHOLD:
                        print(f"[WARNING] High delay detected: {log['delay']:.4f} sec")

    except FileNotFoundError:
        print("No logs found.")