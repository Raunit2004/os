 # ipc.py
from multiprocessing import Queue
import time
import random
from logger import log_message

def sender(queue, sender_id):
    for i in range(5):
        msg = f"{sender_id}-Msg-{i}"
        
        time.sleep(random.uniform(0.5, 2.0))
        
        queue.put((sender_id, msg, time.time()))
        log_message(sender_id, "QUEUE", msg)

        print(f"[SENT] {msg}")

def receiver(queue, receiver_id):
    last_received = {}

    while True:
        if not queue.empty():
            sender_id, msg, sent_time = queue.get()
            receive_time = time.time()

            delay = receive_time - sent_time

            msg_num = int(msg.split("-")[-1])

            # Message loss detection
            if sender_id in last_received:
                if msg_num != last_received[sender_id] + 1:
                    print(f"[ERROR] {receiver_id}: Message loss from {sender_id}")

            last_received[sender_id] = msg_num

            log_message(sender_id, receiver_id, msg, delay)

            print(f"[{receiver_id}] {msg} from {sender_id} | Delay: {delay:.4f}s")

        time.sleep(0.3)