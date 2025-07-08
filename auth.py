
import time
import json
import os

CREDENTIALS = {"username": "admin", "password": "admin"}
LOCK_FILE = "login_lock.json"

def is_locked():
    if os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, "r") as file:
            data = json.load(file)
        if time.time() < data.get("unlock_time", 0):
            return True
        else:
            os.remove(LOCK_FILE)
    return False

def login():
    if is_locked():
        print("Too many failed attempts. Try again later.")
        return False

    attempts = 0
    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")

        if username == CREDENTIALS["username"] and password == CREDENTIALS["password"]:
            print("Login successful!")
            return True
        else:
            attempts += 1
            print(f"Invalid credentials. Attempts left: {3 - attempts}")

    
    with open(LOCK_FILE, "w") as file:
        json.dump({"unlock_time": time.time() + 300}, file)
    print("Too many failed attempts. You are locked out for 5 minutes.")
    return 