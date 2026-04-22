 # main.py
from multiprocessing import Process, Queue
from ipc import sender, receiver
from debugger import analyze_logs
import time

if __name__ == "__main__":
    queue = Queue()

    senders = [
        Process(target=sender, args=(queue, "P1")),
        Process(target=sender, args=(queue, "P2")),
        Process(target=sender, args=(queue, "P3"))
    ]

    receivers = [
        Process(target=receiver, args=(queue, "R1")),
        Process(target=receiver, args=(queue, "R2"))
    ]

    for p in senders + receivers:
        p.start()

    time.sleep(12)

    for p in senders + receivers:
        p.terminate()

    analyze_logs()