# Caesar program for web-caesar assignment

import string
from helpers import alphabet_position, rotate_char

def rotate_string(text, rot):
    """Encrypts submitted text by rotating characters by factor of rot"""
    encrypted = []
    for char in text:
        if char not in string.ascii_letters:
            encrypted.append(char)
        else:    
            encrypted.append(rotate_char(char, rot))

    return "".join(encrypted)    

def main():
    """Runs Caesar.py program"""
    message = input("Enter your message:\n")
    rotation = input("Rotate by:\n")
    secret = encrypt(message, rotation)
    print(secret)


if __name__ == "__main__":
    main() 