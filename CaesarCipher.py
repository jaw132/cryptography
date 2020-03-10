alphabet_size = 26


def cipher(message, offset):
    offset %= alphabet_size
    cipherList = shift(message, offset)
    return ' '.join(str(c) for c in cipherList)


def shift(plaintext, offset):
    ciphermessage = ' '
    for i in plaintext:
        i = char_shift(i, offset)
        ciphermessage += i
    return ciphermessage


def char_shift(letter, offset):
    letter = chr(ord(letter)+offset)
    if ord(letter) > ord('z'):
        letter = chr(ord(letter) - alphabet_size)
    return letter


cipher1 = cipher('hello', 5)

print(cipher1)
