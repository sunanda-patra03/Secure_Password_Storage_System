import json
import os
from hash_utils import hash_password

USER_DB = "users.json"

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as file:
        return json.load(file)

def save_users(users):
    with open(USER_DB, "w") as file:
        json.dump(users, file, indent=4)

def register_user(username, password):
    users = load_users()

    if username in users:
        return False, "User already exists."

    hashed_password = hash_password(password)
    users[username] = hashed_password
    save_users(users)
    return True, "User registered successfully."

def login_user(username, password):
    users = load_users()

    if username not in users:
        return False, "User not found."

    hashed_password = hash_password(password)
    if users[username] == hashed_password:
        return True, "Login successful."
    else:
        return False, "Invalid password."
