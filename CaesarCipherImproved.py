# Set alphabet size
alphabet_size = 26

# Function that takes two inputs from user, the plaintext message and the shift to apply, and return the
# encrypted message.
def cipher():
    print('Enter message to be encrypted')
    plaintext = input()
    plaintext = clean(plaintext)
    if plaintext == 'Error':
        return 'Invalid character in message string'

    print('Enter Shift value')
    # Ensures the offset input is an integer
    try:
        offset = int(input())
    except ValueError:
        return 'Invalid offset input, offset must be an integer'

    # Use modulo arithmetic to standardise large offset inputs
    offset %= alphabet_size
    cipherList = shift(plaintext, offset)
    return ' '.join(str(c) for c in cipherList)

# Function to perform the shift on the plaintext, calls to char_shift
def shift(plaintext, offset):
    ciphermessage = []
    for i in plaintext:
        if i != ' ':
            i = char_shift(i, offset)
        ciphermessage += i
    return ciphermessage

# Function to shift a character by the specified offset
def char_shift(letter, offset):
    letter = chr(ord(letter) + offset)
    if ord(letter) > ord('z'):
        letter = chr(ord(letter) - alphabet_size)
    if ord(letter) < ord('a'):
        letter = chr(ord(letter) + alphabet_size)
    return letter

# function to ensure the message only contains letters and converts capitals to lowercase
def clean(plaintext):
    cleantext = ' '
    for i in plaintext:
        if 65 <= ord(i) <= 90:
            cleantext += i.lower()
        elif 97 <= ord(i) <= 122 or ord(i) == 32:
            cleantext += i
        else:
            return 'Error'
    return cleantext


cipher1 = cipher()
print(cipher1)
