# logger.py
import json
from datetime import datetime

def log_message(sender, receiver, message, delay=None):
    log = {
        "time": str(datetime.now()),
        "sender": sender,
        "receiver": receiver,
        "message": message,
        "delay": delay
    }

    with open("logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")