# list of the letters in the English alphabet order by how frequently they occur.
mostFreqLetList = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g', 'w', 'y', 'b',
                   'v', 'k', 'x', 'j', 'q', 'z']
# Function to decrypt message encoded via MonoAlphabetic substitution using frequency analysis
def decryptMono(message):
    # creating a dictionary with each letter in the message and the number of times they occur, also doing the
    # same thing for three letter words. Additionally, finding the one letter cipher text words.
    freqDict = frequencyDict(message)
    oneLetterWords, threeLetterFreq = wordAnalysis(message)
    # sorting the two dictionaries above by the frequency that the value occurs in the message
    threeLetterSort = sortDictionary(threeLetterFreq)
    sortFreqDict = sortDictionary(freqDict)

    # create map from cipher to plaintext letters
    DecryptMap = createDecryptMap(sortFreqDict, oneLetterWords, threeLetterSort, freqDict)

    # map most frequent letter in message to most frequent letter in English language
    decryptMessage = DecryptMessage(message, DecryptMap)

    return decryptMessage

# function that returns list which has been sorted by its values in descending order
def sortDictionary(dict):
    sortedList = []
    sortedTuple = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for i in range(len(sortedTuple)):
        sortedList.append(sortedTuple[i][0])
    return sortedList

# first assigns the most frequent one letter cipher text word to 'a' and the other to 'i'. Then proceeds to look at the
# top two most frequent three letter cipher words, these are more than likely 'and' and 'the', so 'n, d, t, h, e'
# will be assign to cipher letters after some checks. Finally, the remaining letters are assigned via standard
# frequency analysis
def createDecryptMap(sortedTup, oneLetter, threeWord, freqDict):
    decryptMap, j = {}, 0
    if freqDict[oneLetter[0]] > freqDict[oneLetter[1]]:
        decryptMap[oneLetter[0]] = 'a'
        decryptMap[oneLetter[1]] = 'i'
    else:
        decryptMap[oneLetter[0]] = 'i'
        decryptMap[oneLetter[1]] = 'a'
    removeListEntries(mostFreqLetList, sortedTup, ['a', 'i'], [oneLetter[0], oneLetter[1]])

    truncatedThreeLetList, andCode = [threeWord[0], threeWord[1]], ''
    for i in truncatedThreeLetList:
        if i[0] == oneLetter[0]:
            decryptMap[i[1]] = 'n'
            decryptMap[i[2]] = 'd'
            removeListEntries(mostFreqLetList, sortedTup, ['n', 'd'], [i[1], i[2]])
            andCode = i
        elif i[0] == oneLetter[1]:
            decryptMap[i[1]] = 'n'
            decryptMap[i[2]] = 'd'
            removeListEntries(mostFreqLetList, sortedTup, ['n', 'd'], [i[1], i[2]])
            andCode = i
    if andCode in truncatedThreeLetList:
        truncatedThreeLetList.remove(andCode)
    decryptMap[truncatedThreeLetList[0][0]] = 't'
    decryptMap[truncatedThreeLetList[0][1]] = 'h'
    decryptMap[truncatedThreeLetList[0][2]] = 'e'
    removeListEntries(mostFreqLetList, sortedTup, ['t', 'h', 'e'], [truncatedThreeLetList[0][0], truncatedThreeLetList[0][1], truncatedThreeLetList[0][2]])

    for i in range(len(sortedTup)):
        decryptMap[sortedTup[i][0]] = mostFreqLetList[i]
    return decryptMap

# returns the deciphered text based on the decryption map previously calculated
def DecryptMessage(message, DecryptMap):
    decryptMessage = ''
    for i in message:
        if i != ' ':
            decryptMessage += DecryptMap[i]
        else:
            decryptMessage += i
    return decryptMessage

# This creates the dictionary with all letters in the ciphertext and the number of times they appear in the message
def frequencyDict(message):
    freqDict = {}
    for i in message:
        if i != ' ':
            if i in freqDict:
                freqDict[i] += 1
            else:
                freqDict[i] = 1
    return freqDict

# function that returns a list of the one letter ciphertext words and a dictionary of the three letter words
# and how common they are.
def wordAnalysis(message):
    oneWordList, threeLetFreq = [], {}

    tempWord = ''
    for i in message:
        if i != ' ':
            tempWord += i
        else:
            if len(tempWord) == 1:
                oneWordList += tempWord
            elif len(tempWord) == 3 and tempWord in threeLetFreq:
                threeLetFreq[tempWord] += 1
            elif len(tempWord) == 3 and tempWord not in threeLetFreq:
                threeLetFreq[tempWord] = 1
            tempWord = ''
    oneWordList = list(dict.fromkeys(oneWordList))
    return oneWordList, threeLetFreq

# Clean up function to remove values from a pair of lists
def removeListEntries(list1, list2, entries1, entries2):
    for i in entries1:
        list1.remove(i)
    for i in entries2:
        list2.remove(i)

# ***********************************************************************************************************
# Example to show the decryption in action
# ***********************************************************************************************************
# A couple of quick functions to ensure the message to be encrypted only contains lowercase letters and
# perform a monoalphabetic substitution cipher.
def cleanMessage(message):
    clean = ''
    for i in message:
        if i.islower() is True or i.isupper() is True:
            clean += i.lower()
        elif i == ' ':
            clean += i
    return clean


def encrypt(message):
    encryptMap, encryptSpeech = {}, ''
    for i in range(len(mostFreqLetList)):
        encryptMap[mostFreqLetList[i]] = encryptList[i]
    for i in message:
        if i != ' ':
            encryptSpeech += encryptMap[i]
        else:
            encryptSpeech += i
    return encryptSpeech

# The message to be encrypted is an excerpt from MLK I have a dream speech
# A list of the alphabet in a random order in generated which will be used to encrypt the message
speech = cleanMessage('I say to you today, my friends, though, even though ' +
'we face the difficulties of today and tomorrow, I still have ' +
'a dream. It is a dream deeply rooted in the American ' +
'dream. I have a dream that one day this nation will rise ' +
'up, live out the true meaning of its creed: We hold these ' +
'truths to be self-evident, that all men are created equal. ' +
'I have a dream that one day on the red hills of Georgia ' +
'sons of former slaves and the sons of former slave owners ' +
'will be able to sit down together at the table of brotherhood. I have a dream that one day even the state of ' +
'Mississippi, a state sweltering with the heat of inJustice, ' +
'sweltering with the heat of oppression, will be transormed ' +
'into an oasis of freedom and justice. ' +
'I have a dream that my four little chi1dren will one day ' +
'live in a nation where they will not be judged by the color ' +
'of their skin but by the content of their character. I have ' +
'a dream. I have a dream that one day in Alabama, ' +
'with its vicious racists, with its governor having his lips ' +
'dripping with the words of interposition and nullification, ' +
'one day right there in Alabama little black boys and black ' +
'girls will he able to join hands with little white boys and ' +
'white girls as sisters and brothers.')
import random
encryptList = random.sample(mostFreqLetList, len(mostFreqLetList))

encryptedSpeech = encrypt(speech)

# Once the message has been encrypted, run the decryption algorithm to test accuracy
cipher1 = decryptMono(encryptedSpeech)
print(cipher1)

# Create a simple function to measure the accuracy based on how many letters match the original
def accuracy(originalMessage, decryptionAttempt):
    correctCounter = 0
    for i in range(len(originalMessage)):
        if originalMessage[i] == decryptionAttempt[i]:
            correctCounter += 1
    return correctCounter/len(originalMessage)

print(accuracy(speech, cipher1))
# For this particular message this decryption algo has 77% accuracy. From here the original can easily be deduced.
# to improve accuracy you can run the deciphered text through a spell checker and update the decryption map for any
# words that have strong matches.
