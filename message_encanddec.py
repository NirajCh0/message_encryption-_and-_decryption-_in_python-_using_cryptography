from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Generate a new encryption key and save it to a file.
    """
    key = Fernet.generate_key()
    key_file_path = os.path.join(os.path.expanduser("~"), "encryption_key.txt")
    with open(key_file_path, "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated successfully.")

def load_key():
    """
    Load the encryption key from the file.
    """
    key_file_path = os.path.join(os.path.expanduser("~"), "encryption_key.txt")
    try:
        with open(key_file_path, "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        print("Encryption key not found. Please generate a key first.")
        return None

def encrypt_message(message, key):
    """
    Encrypt the message using the provided key.
    """
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Decrypt the encrypted message using the provided key.
    """
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    print("Welcome to the Message Encryption and Decryption Tool!")

    # Check if encryption key exists
    key = load_key()
    if key is None:
        choice = input("No encryption key found. Generate a new key (y/n)? ").lower()
        if choice == "y":
            generate_key()
            key = load_key()
        else:
            print("Exiting.")
            return

    while True:
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Generate a new key")
        print("4. Exit")

        option = input("\nEnter your choice (1/2/3/4): ")

        if option == "1":
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print("Encrypted message:", encrypted_message.decode())

        elif option == "2":
            encrypted_message = input("Enter the encrypted message: ")
            decrypted_message = decrypt_message(encrypted_message.encode(), key)
            print("Decrypted message:", decrypted_message)

        elif option == "3":
            choice = input("Are you sure you want to generate a new key? This will overwrite the existing key (y/n): ").lower()
            if choice == "y":
                generate_key()
                key = load_key()
                print("New encryption key generated successfully.")
            else:
                print("Key generation canceled.")

        elif option == "4":
            print("Exiting.")
            break

        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
