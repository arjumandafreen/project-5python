import json
from hashlib import sha256
from cryptography.fernet import Fernet
import os

# Generate or load a key for encryption (keep it secret!)
KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

# Load the encryption key
KEY = load_key()
cipher = Fernet(KEY)

# Password hashing
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Encrypt and decrypt functions
def encrypt(data):
    return cipher.encrypt(data.encode()).decode()

def decrypt(encrypted_data):
    return cipher.decrypt(encrypted_data.encode()).decode()

# User storage (users.json)
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

# Encrypted data storage (data.json)
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
