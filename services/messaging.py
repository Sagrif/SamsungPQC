from utils.encryption import encrypt_message
import json, os
import uuid

DATA_PATH = "data/messages.json"

def send_secure_message(to, msg):
    encrypted = encrypt_message(msg)
    message_obj = {
        "id": str(uuid.uuid4()),
        "to": to,
        "msg": encrypted
    }

    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)

    with open(DATA_PATH, "r+") as f:
        messages = json.load(f)
        messages.append(message_obj)
        f.seek(0)
        json.dump(messages, f, indent=2)

def get_messages():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def delete_all_messages():
    with open(DATA_PATH, "w") as f:
        json.dump([], f)
