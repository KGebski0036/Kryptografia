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

def columnar_transposition_decrypt(cipher_text, key):
    numeric_key = generate_numeric_key(key)

    rows = 8
    cols = 94

    sorted_key_with_index = sorted((num, i) for i, num in enumerate(numeric_key))

    col_lengths = [len(cipher_text) // cols] * cols
    for i in range(len(cipher_text) % cols):
        col_lengths[i] += 1

    current_idx = 0
    transposed_matrix = [''] * cols
    for num, col_idx in sorted_key_with_index:
        transposed_matrix[col_idx] = cipher_text[current_idx:current_idx + col_lengths[col_idx]]
        current_idx += col_lengths[col_idx]

    decrypted_text = ''
    for row in range(rows):
        for col in range(cols):
            if row < len(transposed_matrix[col]):
                decrypted_text += transposed_matrix[col][row]

    return decrypted_text

def main():
    with open('shuffle_proprietary.txt', 'r') as f:
        cipher_text = f.read().strip()

    with open('passwd.txt', 'r') as f:
        key = f.read().strip()

    if len(key) != 94:
        print("The key must be exactly 94 characters long.")
        return

    decrypted_text = columnar_transposition_decrypt(cipher_text, key)

    print("Decrypted text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()
