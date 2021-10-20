import numpy as np
def det_inverse(input):
    possible_inverses = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    if input not in possible_inverses:
        raise Exception(f"inverse for determinant {input} does not exist. There are only 12 possibilties for the determinant: 1,3,5,7,9,11,15,17,19,21,23,25.")

    for inverse in range(1, 27):
        check = (input * inverse) % 26
        if (check == 1):
            return inverse

def get_matrix_inverse(m):

    determinant = (m[0][0]*m[1][1]-m[0][1]*m[1][0]) % 26
    
    # determinant should be between 0 - 26
    if(determinant < 0):
        determinant = 26 + determinant
    

    det_inv = det_inverse(determinant)

    # for 2x2 matrix the elements other than diagonal matrix becomes negative, so keep its value in between 0 - 26
    m[0][1] = 26 - m[0][1] 
    m[1][0] = 26 - m[1][0] 


    return [[(m[1][1] * det_inv) % 26, (m[0][1] * det_inv) % 26],
            [(m[1][0] * det_inv) % 26, (m[0][0] * det_inv) % 26]] 

def prepare_key_matrix(key):
    keyMatrix = [[0] * 2 for i in range(2)]
    idx = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = (ord(key[idx]) - ord('A')) % 26
            idx += 1
    return keyMatrix

def prepare_inverse_key_matrix(key):
    key_matrix = prepare_key_matrix(key)
    inverse_key_matrix = get_matrix_inverse(key_matrix)
    return inverse_key_matrix

def prepare_message_vector(message):
    message_vector = []
    i = 0
    for k in range(int(len(message)/2)):
        l = []
        for j in range(2):
            l.append((ord(message[i]) - ord('a')) % 26)
            i = i + 1
        message_vector.append(l)
    return message_vector

def prepapre_cipher_vector(key_matrix,message_vector):
    cipher_matrix = []
    for v in message_vector:
        cipher_matrix.append(np.dot(key_matrix,v))
    return cipher_matrix

def prepare_cipher_text_from_matrix(cipher_matrix):
    cipher_text = ""
    for vector in cipher_matrix:
        for ele in vector:
            cipher_text += chr(ele%26 + ord('a'))
    return cipher_text

def hill_cipher(key,message):
    key_matrix =  prepare_key_matrix(key)
    message_vector = prepare_message_vector(message)
    cipher_vector = prepapre_cipher_vector(key_matrix,message_vector)
    cipher_text = prepare_cipher_text_from_matrix(cipher_vector)
    return cipher_text

def hill_ciper_inverse(key,message):
    key_matrix =  prepare_inverse_key_matrix(key)
    message_vector = prepare_message_vector(message)
    cipher_vector = prepapre_cipher_vector(key_matrix,message_vector)
    cipher_text = prepare_cipher_text_from_matrix(cipher_vector)
    return cipher_text

def main():
    key = "HILL"
    message = input("Enter text message to encrypt: ")
    if(len(message)%2 == 1):
        message += ' '
    cipher_text = hill_cipher(key,message)
    print("Cipher text is ::",cipher_text)
    message = input("Enter text message to decrypt (press enter to decrypt the above result): ")
    if message:
        print(hill_ciper_inverse(key,message))
    else:
        print(hill_ciper_inverse(key,cipher_text))
    
if __name__ == "__main__":
    main()