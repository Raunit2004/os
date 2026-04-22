# analyzer.py - DEPRECATED (merged into debugger.py)
# Legacy code for threat analysis on logs.txt (old format).
# Use dashboard /analyze or python debugger.py instead.

# def analyze():
#     print("\n--- Threat Analysis ---")
#     suspicious_keywords = ["hack", "attack", "malware", "Suspicious"]
# 
#     try:
#         with open("logs.txt", "r") as f:
#             logs = f.readlines()
#
#         for line in logs:
#             for word in suspicious_keywords:
#                 if word.lower() in line.lower():
#                     print("⚠️ ALERT: Suspicious Activity Detected →", line.strip())
#     except FileNotFoundError:
#         print("No logs found yet.")

