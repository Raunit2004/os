# ipc.py
from multiprocessing import Process, Queue
import time
from logger import log_message

def sender(queue):
    for i in range(5):
        msg = f"Message {i}"
        queue.put((msg, time.time()))
        log_message("Sender", "Receiver", msg)
        time.sleep(1)

def receiver(queue):
    while True:
        if not queue.empty():
            msg, sent_time = queue.get()
            receive_time = time.time()
            
            delay = receive_time - sent_time
            
            log_message("Receiver", "Sender", msg, delay)
            
            print(f"[RECEIVED] {msg} | Delay: {delay:.4f} sec")
        time.sleep(0.5)