# ipc.py
from multiprocessing import Process, Queue
import time
import random
from logger import log_message

# Global variable for message tracking
expected_count = 0

def sender(queue, sender_id):
    for i in range(5):
        msg = f"{sender_id}-Message {i}"
        
        # Simulate random delay
        time.sleep(random.uniform(0.5, 2.5))
        
        queue.put((msg, time.time()))
        log_message(sender_id, "Receiver", msg)

def receiver(queue):
    global expected_count

    while True:
        if not queue.empty():
            msg, sent_time = queue.get()
            receive_time = time.time()

            delay = receive_time - sent_time

            # Extract message number
            try:
                msg_num = int(msg.split()[-1])
            except:
                msg_num = -1

            # Message loss detection
            if msg_num != expected_count:
                print(f"[ERROR] Message loss detected! Expected {expected_count}, got {msg_num}")

            expected_count = msg_num + 1

            log_message("Receiver", "Sender", msg, delay)

            print(f"[RECEIVED] {msg} | Delay: {delay:.4f} sec")

        time.sleep(0.5)