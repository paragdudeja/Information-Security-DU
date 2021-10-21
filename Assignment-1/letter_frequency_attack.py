import operator


T = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'


def get_key(iteration: int, ch: str) -> int:
    """
    Returns the decrypted text decrypted using affine cipher

            Parameters:
                    iteration (int): An integer specifying the iteration number
                    ch (str): A single character

            Returns:
                    (int): An integer representing the key
    
    """
    return ord(ch) - ord(T[iteration]) 


def decryption(message: str, key: int) -> str:
    """
    Returns the decrypted text decrypted using additive cipher

            Parameters:
                    message (str): An input string
                    key (int): key for the current charcter

            Returns:
                    decrypted_text (str): affine cipher decrypted string
    
    """
    decrypted_text = ""
    for ch in message:
        if ch.isspace():
            decrypted_text += " "
        else:
            decrypted_text += chr(((ord(ch) - ord('A') - key ) % 26) + ord('A')) 
    return decrypted_text


def freq_attack(message: str):
    """
    Letter frequency attack on the decrypted message 

            Parameters:
                    message (str): An input string    
    """
    frequency = {} # Character frequency in given message

    for ch in message:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    sorted_frequency = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(11):
        if i == len(sorted_frequency):
            break
        key = get_key(i, sorted_frequency[i][0])
        print(key)
        print(decryption(message, key))
    

def main():
    message = input("Enter the encrypted message: ")
    # message = 'B TJNQMF NFTTBHF'
    freq_attack(message)

if __name__=='__main__':
    main()