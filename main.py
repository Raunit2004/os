# main.py
from multiprocessing import Process, Queue
from ipc import sender, receiver
from debugger import analyze_logs
import time

if __name__ == "__main__":
    queue = Queue()

    p1 = Process(target=sender, args=(queue,))
    p2 = Process(target=receiver, args=(queue,))

    p1.start()
    p2.start()

    time.sleep(7)  # let processes run

    p1.terminate()
    p2.terminate()

    analyze_logs()