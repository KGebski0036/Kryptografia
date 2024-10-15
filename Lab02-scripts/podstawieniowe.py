import string
import random

def get_plaintext_and_password():
    with open('plain.txt', 'r') as f:
        plaintext = f.read().strip().lower()
    try:
        with open('passwd.txt', 'r') as f:
            password = f.read().strip().lower()
    except FileNotFoundError:
        password = None
    return plaintext, password

def monoalphabetic_substitution(plaintext):
    alphabet = string.ascii_lowercase
    shuffled = ''.join(random.sample(alphabet, len(alphabet)))
    table = str.maketrans(alphabet, shuffled)
    return plaintext.translate(table)

def caesar_cipher(plaintext, shift=3):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def polyalphabetic_substitution(plaintext, key):
    alphabet = string.ascii_lowercase
    key_length = len(key)
    ciphertext = []
    for i, letter in enumerate(plaintext):
        shift = alphabet.index(key[i % key_length])
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted_alphabet)
        ciphertext.append(letter.translate(table))
    return ''.join(ciphertext)

def vigenere_cipher(plaintext, key):
    alphabet = string.ascii_lowercase
    key_length = len(key)
    ciphertext = []
    for i, letter in enumerate(plaintext):
        shift = alphabet.index(key[i % key_length])
        cipher_letter = alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
        ciphertext.append(cipher_letter)
    return ''.join(ciphertext)

def affine_cipher(plaintext, a=5, b=8):
    alphabet = string.ascii_lowercase
    m = len(alphabet)
    ciphertext = []
    for letter in plaintext:
        index = alphabet.index(letter)
        cipher_index = (a * index + b) % m
        ciphertext.append(alphabet[cipher_index])
    return ''.join(ciphertext)

def one_time_pad(plaintext, key):
    alphabet = string.ascii_lowercase
    ciphertext = []
    for p, k in zip(plaintext, key):
        cipher_index = (alphabet.index(p) + alphabet.index(k)) % len(alphabet)
        ciphertext.append(alphabet[cipher_index])
    return ''.join(ciphertext)

# Szyfr poligramowy Playfair
def playfair_cipher(plaintext, key):
    def create_playfair_matrix(key):
        alphabet = string.ascii_lowercase.replace('j', '')
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Unikalne litery w kluczu
        matrix = []
        for letter in key + alphabet:
            if letter not in matrix:
                matrix.append(letter)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def find_position(matrix, char):
        for row_idx, row in enumerate(matrix):
            if char in row:
                return row_idx, row.index(char)

    matrix = create_playfair_matrix(key)
    plaintext = plaintext.replace('j', 'i')  # Zastępujemy 'j' przez 'i'

    # Dodanie par znaków
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else 'x'
        if a == b:
            pairs.append((a, 'x'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    ciphertext = []
    for a, b in pairs:
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            ciphertext.append(matrix[row_a][(col_a + 1) % 5])
            ciphertext.append(matrix[row_b][(col_b + 1) % 5])
        elif col_a == col_b:
            ciphertext.append(matrix[(row_a + 1) % 5][col_a])
            ciphertext.append(matrix[(row_b + 1) % 5][col_b])
        else:
            ciphertext.append(matrix[row_a][col_b])
            ciphertext.append(matrix[row_b][col_a])

    return ''.join(ciphertext)

# Szyfr homofoniczny
def homophonic_cipher(plaintext):
    homophones = {
        'a': ['12', '24', '36'], 'b': ['13', '25'], 'c': ['14'], 'd': ['15'],
        'e': ['16', '26', '36'], 'f': ['17'], 'g': ['18'], 'h': ['19'],
        'i': ['21'], 'j': ['22'], 'k': ['23'], 'l': ['24'], 'm': ['25'],
        'n': ['26'], 'o': ['27'], 'p': ['28'], 'q': ['29'], 'r': ['31'],
        's': ['32'], 't': ['33'], 'u': ['34'], 'v': ['35'], 'w': ['36'],
        'x': ['37'], 'y': ['38'], 'z': ['39']
    }

    ciphertext = []
    for letter in plaintext:
        if letter in homophones:
            ciphertext.append(random.choice(homophones[letter]))
        else:
            ciphertext.append(letter)

    return ' '.join(ciphertext)

# Główna funkcja
def main():
    plaintext, password = get_plaintext_and_password()

    print("Szyfr podstawieniowy monoalfabetyczny:")
    print(monoalphabetic_substitution(plaintext))

    print("\nSzyfr monoalfabetyczny przesunięciowy:")
    print(caesar_cipher(plaintext))

    if password:
        print("\nSzyfr podstawieniowy wieloalfabetowy:")
        print(polyalphabetic_substitution(plaintext, password))

        print("\nSzyfr Vigenère'a:")
        print(vigenere_cipher(plaintext, password))

        print("\nSzyfr z kluczem jednorazowym:")
        print(one_time_pad(plaintext, password))

        print("\nSzyfr poligramowy Playfair:")
        print(playfair_cipher(plaintext, password))

    print("\nSzyfr afiniczny:")
    print(affine_cipher(plaintext))

    print("\nSzyfr homofoniczny:")
    print(homophonic_cipher(plaintext))

if __name__ == "__main__":
    main()
