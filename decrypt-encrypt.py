import base64
from cryptography.fernet import Fernet

# -------------------------------
# ENCRYPTION / DECRYPTION METHODS
# -------------------------------

# 1. Base64
def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(encoded_text):
    return base64.b64decode(encoded_text.encode()).decode()


# 2. Caesar Cipher (simple shift)
def caesar_encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)


# 3. Fernet (AES-based symmetric encryption)
def generate_fernet_key():
    """Generates and returns a new Fernet key."""
    key = Fernet.generate_key()
    print(f"[!] Save this key for decryption: {key.decode()}")
    return key

def fernet_encrypt(text, key):
    fernet = Fernet(key)
    return fernet.encrypt(text.encode()).decode()

def fernet_decrypt(token, key):
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()


# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    print("\n=== Multi Encryption/Decryption Tool ===")
    print("1. Base64")
    print("2. Caesar Cipher")
    print("3. Fernet (AES-based)")
    print("--------------------------------------")
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    method = input("Choose method (1/2/3): ").strip()
    text = input("Enter your text: ")

    if method == "1":  # Base64
        if mode == "e":
            print("\nEncrypted:", base64_encrypt(text))
        else:
            print("\nDecrypted:", base64_decrypt(text))

    elif method == "2":  # Caesar
        shift = int(input("Enter shift value (default 3): ") or 3)
        if mode == "e":
            print("\nEncrypted:", caesar_encrypt(text, shift))
        else:
            print("\nDecrypted:", caesar_decrypt(text, shift))

    elif method == "3":  # Fernet
        if mode == "e":
            key = generate_fernet_key()
            print("\nEncrypted:", fernet_encrypt(text, key))
        else:
            key = input("Enter your saved Fernet key: ").encode()
            print("\nDecrypted:", fernet_decrypt(text, key))

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

