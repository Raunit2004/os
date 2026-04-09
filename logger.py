import datetime

def log_message(sender, receiver, message, delay=None):
    with open("logs.txt", "a") as f:
        if delay is None:
            f.write(f"{datetime.datetime.now()} | {sender} -> {receiver} : {message}\n")
        else:
            f.write(f"{datetime.datetime.now()} | {sender} -> {receiver} : {message} | Delay: {delay:.4f} sec\n")

def log(sender, receiver, message):
    return log_message(sender, receiver, message)