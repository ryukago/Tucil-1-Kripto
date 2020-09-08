import random
import string

# Repeat the keyword until equal length with plaintext
def repeatKey(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return(''.join(key))

# Add plaintext to key until equal length with plaintext
def autoKey(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(plaintext[i])
    return(''.join(key))

def generateTable(seed):
    table = []
    for i in range(26):
        order = list(string.ascii_lowercase)
        random.Random(i+seed).shuffle(order)
        table.append(order)
    return table
    
# MAIN FUNCTIONS

# Standard Vigenere Cipher
def encryptStandard(plaintext, key):
    key = repeatKey(plaintext, key)
    ciphertext = []
    for i in range(len(plaintext)): 
        x = ((ord(plaintext[i]) - ord('a') + ord(key[i])- ord('a')) % 26) + ord('a') 
        ciphertext.append(chr(x)) 
    return("" . join(ciphertext))

def decryptStandard(ciphertext, key):
    key = repeatKey(ciphertext, key)
    plaintext = [] 
    for i in range(len(ciphertext)): 
        x = ((ord(ciphertext[i]) - ord(key[i])) % 26) + ord('a') 
        plaintext.append(chr(x)) 
    return("" . join(plaintext))

# Extended Vigenere Cipher
def encryptExtended(plaintext, key):
    key = repeatKey(plaintext, key)
    ciphertext = []
    for i in range(len(plaintext)): 
        x = ord(plaintext[i]) + ord(key[i]) % 256
        ciphertext.append(chr(x)) 
    return("" . join(ciphertext))

def decryptExtended(ciphertext, key):
    key = repeatKey(ciphertext, key)
    plaintext = [] 
    for i in range(len(ciphertext)): 
        x = ord(ciphertext[i]) - ord(key[i]) % 256 
        plaintext.append(chr(x)) 
    return("" . join(plaintext))

# Auto-Key Vigenere Cyper
def encryptAutoKey(plaintext, key):
    key = autoKey(plaintext, key)
    ciphertext = []
    for i in range(len(plaintext)): 
        x = ((ord(plaintext[i]) - ord('a') + ord(key[i])- ord('a')) % 26) + ord('a') 
        ciphertext.append(chr(x)) 
    return("" . join(ciphertext))

def decryptAutoKey(ciphertext, key):
    plaintext = [] 
    for i in range(len(key)): 
        x = ((ord(ciphertext[i]) - ord(key[i])) % 26) + ord('a') 
        plaintext.append(chr(x))
    for i in range(len(key), len(ciphertext)):
        x = ((ord(ciphertext[i]) - ord(plaintext[i-len(key)])) % 26) + ord('a')
        plaintext.append(chr(x))
    return("" . join(plaintext))

# Full Vigenere Cipher
def encryptFull(plaintext, key, seed):
    if (not key.isalpha()):
        return('Error: Key can only be alphabetic')
    else:
        key = repeatKey(plaintext, key)
        table = generateTable(seed)
        ciphertext = []
        for x in range(len(plaintext)):
            i = ord(key[x]) - ord('a')
            j = ord(plaintext[x]) - ord('a')
            ciphertext.append(table[i][j])
        return("" . join(ciphertext))

def decryptFull(ciphertext, key, seed):
    if (not key.isalpha()):
        return('Error: Key can only be alphabetic')
    else:
        key = repeatKey(ciphertext, key)
        table = generateTable(seed)
        plaintext = []
        for x in range(len(ciphertext)):
            i = ord(key[x]) - ord('a')
            j = table[i].index(ciphertext[x])
            plaintext.append(chr(j + ord('a')))
        return("" . join(plaintext))

'''
key = 'hehehe'
plaintext = 'inicontohsebuahkalimat'
ciphertext = encryptFull(plaintext, key, 1)
deciphered_text = decryptFull(ciphertext, key, 1)
print("encrypted text:", ciphertext)
print("decrypted text:", deciphered_text)
'''