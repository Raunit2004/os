from multiprocessing import Process, Queue
from ipc import sender, receiver
import time
import os

if __name__ == "__main__":
    # Clear previous logs
    open("logs.json", "w").close()
    print("Cleared logs.json, starting fresh IPC simulation...")

    queue = Queue()

    # Create processes: 2 senders, 1 receiver
    s1 = Process(target=sender, args=(queue, "P1"))
    s2 = Process(target=sender, args=(queue, "P2"))
    r1 = Process(target=receiver, args=(queue, "R1"))

    # Start processes
    s1.start()
    s2.start()
    r1.start()

    # Let them run longer for more logs
    time.sleep(15)

    # Stop processes
    s1.terminate()
    s2.terminate()
    r1.terminate()
    s1.join()
    s2.join()
    r1.join()

    print("Multi-sender IPC simulation finished. Check dashboard: http://127.0.0.1:5001")

