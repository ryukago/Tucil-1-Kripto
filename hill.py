import numpy as np

def encrypt(plaintext, matrix):
    result = ""
    m = len(matrix)
    matrix = toIntMatrix(matrix)

    for adds in range(len(plaintext) % m + 1):
        plaintext += 'z'

    plaintext_matrix = textToMatrix(plaintext, m)

    for chunk in plaintext_matrix:
        # print('chunk', chunk)
        temp_matrix = np.matmul(matrix, chunk)
        # print('temp_matrix', temp_matrix)
        for character in temp_matrix:
            # print('character', character % 26)
            result += chr(character % 26 + 97)
    
    return result

def decrypt(chipertext, matrix):
    result = ""
    return result

def toIntMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    
    return matrix

def textToMatrix(text, m):
    text_matrix = []
    size = m
    for i in range(len(text) // m):
        text_matrix.append([])
        for j in range(m):
            text_matrix[i].append((ord(text[m * i + j]) - 97) % 26)
    return(text_matrix)

# matrix = [[1, 2], [3, 4]]
# print(encrypt("halo", len(matrix), matrix))