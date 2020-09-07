def encrypt(plaintext, m, b):
    result = ""
    for x in plaintext:
        x_new  = ((ord(x) - 97)*m + (b % 26)) % 26
        result += chr(x_new + 97)
    return result

def decrypt(chipertext, m, b):
    result = ""
    for x in chipertext:
        x_new  = modInverse(m, 26)*((ord(x) - 97)-b) % 26
        result += chr(x_new + 97)
    return result

def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

print(encrypt('halo', 3, 1))
print(decrypt(encrypt('halo', 3, 1), 3, 1))