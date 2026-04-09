 # main.py
from multiprocessing import Process, Queue
from ipc import sender, receiver
from debugger import analyze_logs
import time

if __name__ == "__main__":
    queue = Queue()

    # Multiple senders
    p1 = Process(target=sender, args=(queue, "P1"))
    p2 = Process(target=sender, args=(queue, "P2"))

    # One receiver
    p3 = Process(target=receiver, args=(queue,))

    p1.start()
    p2.start()
    p3.start()

    time.sleep(10)  # let processes run

    p1.terminate()
    p2.terminate()
    p3.terminate()

    analyze_logs()