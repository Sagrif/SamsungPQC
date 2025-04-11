from utils.encryption import encrypt_message
import json, os

DATA_PATH = "data/messages.json"

def send_secure_message(to, msg):
    encrypted = encrypt_message(msg)
    message_obj = {"to": to, "msg": encrypted}
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)
    with open(DATA_PATH, "r+") as f:
        messages = json.load(f)
        messages.append(message_obj)
        f.seek(0)
        json.dump(messages, f, indent=2)
