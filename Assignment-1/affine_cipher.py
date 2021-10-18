a = 7
b = 6

def encryption(message: str) -> str:
    encrypted_text = ""
    for ch in message:
        if not ch.isspace():
            encrypted_text += chr((((a * (ord(ch) - ord('a'))) + b) % 26) + ord('a'))
        else:
            encrypted_text += " "
    return encrypted_text

def decryption(message: str) -> str:
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

if __name__=='__main__':
    message = input("Enter text message to encrypt: ")
    encrypted_message = encryption(message)
    print(f"Encrypted message: {encrypted_message}")
    message = input("Enter text message to decrypt (press enter to decrypt the above result): ")
    if message:
        print(decryption(message))
    else:
        print(decryption(encrypted_message))