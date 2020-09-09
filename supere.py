import vigenere
import collections
from collections import Counter

def encrypt(plaintext, key):
    result = vigenere.encryptStandard(plaintext, key)
    result = encrypt_transposisi(result)
    
    return result

def decrypt(ciphertext, key):
    result = decrypt_transposisi(ciphertext)
    result = vigenere.decryptStandard(result, key)

    return result

def encrypt_transposisi(text):
    result = ""
    
    while (len(text) % 3 != 0):
        text += collections.Counter(text).most_common()[0][0]

    for i in range(3):
        j = i
        while (j < len(text)):
            result += text[j]
            j += 3

    return result

def decrypt_transposisi(text):
    result = ""

    for i in range(len(text) // 3):
        j = i
        while (j < len(text)):
            result += text[j]
            j += (len(text) // 3)

    return result

# print(encrypt_transposisi("jalanjalankepasar"), '\n', decrypt_transposisi(encrypt_transposisi("jalanjalankepasar")))
# print(encrypt("halohalobandung", "wow"), '\n', decrypt(encrypt("halohalobandung", "wow"), "wow"))