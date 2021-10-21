k = 3

def encrypt(message):
    """
    Returns the encrypted text encrypted using additive cipher

            Parameters:
                    message (str): An input string

            Returns:
                    encrypted_text (str): additive cipher encrypted string
    
    """
    encrypted_text = ""
    for ch in message:
        if not ch.isspace():
            encrypted_text += chr( ((ord(ch) - ord('a') + k )%26)+ord('a') ) 
        else:
            encrypted_text += " "
    return encrypted_text
    

def decrypt(message):
    """
    Returns the decrypted text decrypted using additive cipher

            Parameters:
                    message (str): An input string

            Returns:
                    decrypted_text (str): additive cipher decrypted string
    
    """
    decrypted_text = ""
    for ch in message:
        if not ch.isspace():
            decrypted_text += chr( ((ord(ch) - ord('a') - k )%26)+ord('a') ) 
        else:
            decrypted_text += " "

    return decrypted_text


def main():
    message = input("Enter text message to encrypt: ")
    encrypted_message = encrypt(message)
    print(f"Encrypted message: {encrypted_message}")
    message = input("Enter text message to decrypt (press enter to decrypt the above result): ")
    if message:
        print(decrypt(message))
    else:
        print(decrypt(encrypted_message))
    
if __name__ == "__main__":
    main()