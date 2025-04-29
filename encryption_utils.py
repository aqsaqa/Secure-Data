from cryptography.fernet import Fernet
import os

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

def encrypt_message(message: str) -> str:
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(encrypted_message: str) -> str:
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_message.encode())
    return decrypted.decode()
