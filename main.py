 # main.py
from multiprocessing import Process, Queue
from ipc import sender, receiver
from debugger import analyze_logs
import time

if __name__ == "__main__":
    queue = Queue()

    # Multiple Senders
    senders = [
        Process(target=sender, args=(queue, "P1")),
        Process(target=sender, args=(queue, "P2")),
        Process(target=sender, args=(queue, "P3"))
    ]

    # Multiple Receivers
    receivers = [
        Process(target=receiver, args=(queue, "R1")),
        Process(target=receiver, args=(queue, "R2"))
    ]

    # Start all
    for p in senders + receivers:
        p.start()

    # Let system run
    time.sleep(12)

    # Stop all
    for p in senders + receivers:
        p.terminate()

    analyze_logs()