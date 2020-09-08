def encrypt_transposisi(text):
    result = ""

    for i in range(3):
        j = i
        while (j < len(text)):
            result += text[j]
            j += 3

    return result

def decrypt_transposisi(text):
    result = ""

    for i in range(len(text) // 3 + 1):
        j = i
        while (j < len(text)):
            result += text[j]
            j += (len(text) // 3 + 1)

    return result

print(decrypt_transposisi(encrypt_transposisi("halohalobandun")))