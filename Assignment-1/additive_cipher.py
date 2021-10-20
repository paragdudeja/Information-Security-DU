k = 3
def encryption(message):
    encrypted_text = ""
    for ch in message:
        if not ch.isspace():
            encrypted_text += chr( ((ord(ch) - ord('a') + k )%26)+ord('a') ) 
        else:
            encrypted_text += " "
    return encrypted_text
    
def decryption(message):
    decrypted_text = ""
    for ch in message:
        if not ch.isspace():
            decrypted_text += chr( ((ord(ch) - ord('a') - k )%26)+ord('a') ) 
        else:
            decrypted_text += " "

    return decrypted_text

def main():
    message = input("Enter text message to encrypt: ")
    encrypted_message = encryption(message)
    print(f"Encrypted message: {encrypted_message}")
    message = input("Enter text message to decrypt (press enter to decrypt the above result): ")
    if message:
        print(decryption(message))
    else:
        print(decryption(encrypted_message))
    
if __name__ == "__main__":
    main()