alphabet_size = 26

# The vigenere cipher works by performing a different Caesar shift cipher on each letter in the message,
# based on a code word provided.
# For simplicity the message has to consist of only lowercase letters.

# main function to encrypt message, logic deferred
def VigenereCipher(message, codeWord):
    encryptionList = codeWordToShiftList(codeWord)
    cipherText = vigEncrypt(message, encryptionList)
    return ''.join(i for i in cipherText)

# function works out what shift is to be implemented and calls shift function
def vigEncrypt(message, shiftList):
    counter, loopLen = 0, len(shiftList)
    cipherText = []
    for i in message:
        encLetter = char_shift(i, shiftList[counter])
        cipherText += encLetter
        counter = (counter + 1) % loopLen
    return cipherText

# this function calculates the shift that should be performed on each letter based on the code word
# and returns a list with the values.
def codeWordToShiftList(codeWord):
    shiftList = []
    for i in codeWord:
        shiftList.append(int(ord(i.lower())) - 97)
    return shiftList

# function to shift letter by given amount
def char_shift(letter, offset):
    letter = chr(ord(letter) + offset)
    if ord(letter) > ord('z'):
        letter = chr(ord(letter) - alphabet_size)
    return letter

