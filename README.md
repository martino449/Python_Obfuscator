# Python_Obfuscator
### Simple Python Code Obfuscator 🧑‍💻🔒

**Overview:**
This Python program obfuscates Python code by encrypting it with AES (Advanced Encryption Standard) and provides a mechanism to decrypt and execute the obfuscated code at runtime. The obfuscation process includes generating a random AES key, encrypting the code, and embedding the decryption logic within the obfuscated script.

**Features:**
1. **Generate AES Key:** Creates a random 256-bit AES key for encryption.
2. **Encrypt Code:** Encrypts the provided code using AES in CBC mode, ensuring the code is padded to fit the AES block size.
3. **Create Obfuscated Script:** Generates an obfuscated script that includes the decryption logic for the encrypted code.
4. **Read/Write Files:** Functions to read code from a file and write the obfuscated code to a new file.
5. **Command-Line Interface (CLI):** A simple CLI menu for user interaction.

**How to Use:**

1. **Obfuscate a Python File:**
   - Save your Python code to a file.
   - Run the program and select option `1` from the CLI menu.
   - Provide the path to the file containing the Python code you want to obfuscate.
   - The program will generate an obfuscated script with the encrypted code and write it to a new file.

2. **Execute Obfuscated Script:**
   - Select option `2` from the CLI menu to execute the obfuscated script.
   - The program will decrypt and execute the obfuscated code dynamically at runtime.

3. **Exit:**
   - Select option `3` to exit the program.

**CLI Menu:**

1. **Obfuscate a Python file:** Encrypts and obfuscates the specified Python file.
2. **Execute obfuscated script:** Decrypts and runs the obfuscated script.
3. **Exit:** Closes the program.

**Example Usage:**

1. **Obfuscate a File:**
   - Place your code in `example_code.py`.
   - Run the obfuscator script and choose option `1`.
   - Provide `example_code.py` as input.
   - The obfuscated code will be saved to `obfuscated_script.py`.

2. **Execute Obfuscated Script:**
   - Run the obfuscator script and choose option `2`.
   - Provide `obfuscated_script.py` as input.
   - The obfuscated code will be executed after decryption.

This tool is intended for educational and experimental purposes and is not recommended for securing sensitive code in production environments.
