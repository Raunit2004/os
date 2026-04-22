# debugger.py
import json

THRESHOLD = 1.0

suspicious_keywords = ["hack", "attack", "malware", "Suspicious"]

def analyze_logs():
    print("\n--- DEBUGGER REPORT ---")
    print("--- Threat Analysis ---")

    try:
        with open("logs.json", "r") as f:
            for line in f:
                log = json.loads(line.strip())

                if log.get("delay") is not None:
                    if log["delay"] > THRESHOLD:
                        print(f"[WARNING] High delay: {log['delay']:.4f}s")

                if "message" in log:
                    for word in suspicious_keywords:
                        if word.lower() in log["message"].lower():
                            print(f"⚠️ ALERT: Suspicious Activity Detected → {log['message']}")

    except FileNotFoundError:
        print("No logs found.")
