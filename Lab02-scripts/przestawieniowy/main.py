def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def generate_numeric_key(key):
    key_list = list(key)
    key_with_index = sorted((char, i) for i, char in enumerate(key_list))

    numeric_key = [0] * len(key)
    last_char = None
    last_num = 0
    for i, (char, original_idx) in enumerate(key_with_index):
        if char == last_char:
            last_num += 1
        else:
            last_num = i + 1
        numeric_key[original_idx] = last_num
        last_char = char

    return numeric_key

def columnar_transposition_encrypt(plain_text, key):
    numeric_key = generate_numeric_key(key)

    cols = 94
    matrix = [plain_text[i:i+cols] for i in range(0, len(plain_text), cols)]

    transposed_matrix = [''] * cols
    sorted_key_with_index = sorted((num, i) for i, num in enumerate(numeric_key))

    for new_col_idx, (num, original_col_idx) in enumerate(sorted_key_with_index):
        for row in matrix:
            transposed_matrix[new_col_idx] += row[original_col_idx]

    cipher_text = ''.join(transposed_matrix)

    return cipher_text

def main():
    key = read_file('passwd.txt')
    plaintext = read_file('plain.txt')

    if len(key) != 94:
        print("Błąd: Klucz musi mieć dokładnie 94 znaki.")
        return

    if len(plaintext) != 94 * 8:
        print("Błąd: Tekst jawny musi mieć dokładnie 94 * 8 znaków.")
        return

    cipher_text = columnar_transposition_encrypt(plaintext, key)

    write_file('shuffle_proprietary.txt', cipher_text)
    print("Zaszyfrowano tekst i zapisano.")

if __name__ == "__main__":
    main()
