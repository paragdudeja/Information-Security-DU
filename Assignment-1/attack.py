import operator

T = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def get_key(iteration: int, ch: str) -> int:
    return ord(ch) - ord(T[iteration]) 

def decryption(message,key):
    decrypted_text = ""
    for ch in message:
        decrypted_text += chr( ((ord(ch) - ord('A') - key )%26)+ord('A') ) 
    return decrypted_text

def freq_attack(message: str) -> str:
    frequency = {}
    for ch in message:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    sorted_x = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(11):
        if i == len(sorted_x):
            break
        key = get_key(i, sorted_x[i][0])
        print(key)
        print(decryption(message,key))
    

if __name__=='__main__':
    words = 'B TJNQMF NFTTBHF'.split(' ')
    for word in words:
        freq_attack(word)
