import time
import random
from logger import log_message

def sender(queue, sender_id):
    for i in range(5):
        msg = f"{sender_id}-Msg-{i}"
        time.sleep(1)

        queue.put((sender_id, msg, time.time()))
        log_message(sender_id, "QUEUE", msg)

        print(f"[SENT] {msg}")

def receiver(queue, receiver_id):
    while True:
        if not queue.empty():
            sender_id, msg, sent_time = queue.get()
            receive_time = time.time()

            delay = receive_time - sent_time

            log_message(sender_id, receiver_id, msg, delay)

            print(f"[RECEIVED] {msg} | Delay: {delay:.2f}")

        time.sleep(0.5)