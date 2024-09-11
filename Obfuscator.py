from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import base64

# Function to generate a random AES key
def generate_key():
    return os.urandom(32)  # 256-bit key

# Function to encrypt code using AES
def encrypt_code(code, key):
    # Initialize cipher for AES encryption in CBC mode with a random IV
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Pad the code to ensure it's a multiple of AES block size (128 bits)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(code.encode('utf-8')) + padder.finalize()
    
    # Encrypt the padded data
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    # Return the encrypted data, encoded in Base64 along with the IV
    return base64.b64encode(iv + encrypted_data).decode('utf-8')

# Function to create an obfuscated script with AES-encrypted code
def obfuscate_code_with_aes(code):
    key = generate_key()  # Generate a random AES key
    encrypted_code = encrypt_code(code, key)  # Encrypt the original code
    
    # Convert the key to Base64 for storage in the deobfuscator
    encoded_key = base64.b64encode(key).decode('utf-8')
    
    # Deobfuscation code that will decrypt and execute the original code at runtime
    deobfuscator = f"""
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# AES decryption function
def decrypt_code(encrypted_code, key):
    encrypted_data = base64.b64decode(encrypted_code)
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_code = unpadder.update(decrypted_padded) + unpadder.finalize()
    
    return decrypted_code.decode('utf-8')

# Decode the key and encrypted code
encoded_key = "{encoded_key}"
encrypted_code = "{encrypted_code}"

# Decrypt and execute the original code
key = base64.b64decode(encoded_key)
exec(decrypt_code(encrypted_code, key))
"""
    return deobfuscator

# Function to read a file and return its content
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# Function to write the obfuscated code to a new file
def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

# Function to display the CLI menu
def display_menu():
    print("\nSimple Python Code Obfuscator 🧑‍💻🔒")
    print("1. Obfuscate a Python file")
    print("2. Execute obfuscated script")
    print("3. Exit")
    return input("\
