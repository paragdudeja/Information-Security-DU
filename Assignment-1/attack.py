import operator

T = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def get_key(iteration: int, ch: str) -> int:
    T[iteration] - ord(ch)


def encrypt(message: str) -> str:
    frequency = {}
    for ch in message:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    sorted_x = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    
    key = ord(sorted_x[0]) - ord('E')
    for i in range(11):
        key = get_key(i, sorted_x[i])

if __name__=='__main__':
    encrypt('hello world')