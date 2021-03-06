a = 7
b = 6

def encrypt(message: str) -> str:
    """
    Returns the encrypted text encrypted using affine cipher

            Parameters:
                    message (str): An input string

            Returns:
                    encrypted_text (str): affine cipher encrypted string
    
    """
    encrypted_text = ""
    for ch in message:
        if not ch.isspace():
            encrypted_text += chr((((a * (ord(ch) - ord('a'))) + b) % 26) + ord('a'))
        else:
            encrypted_text += " "
    return encrypted_text


def decrypt(message: str) -> str:
    """
    Returns the decrypted text decrypted using affine cipher

            Parameters:
                    message (str): An input string

            Returns:
                    decrypted_text (str): affine cipher decrypted string
    
    """
    decrypted_text = ""
    multi_inverse = 0

    for i in range(26):
        if (a*i)%26 == 1:
            multi_inverse = i

    for ch in message:
        if not ch.isspace():
            decrypted_text += chr((multi_inverse * ((ord(ch) - ord('a') - b)))%26 + ord('a'))
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


if __name__=='__main__':
    main()