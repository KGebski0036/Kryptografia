def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def columnar_transposition_encrypt(plaintext, key):
    num_columns = len(key)
    num_rows = len(plaintext)
    
    table = [plaintext[i:i+num_columns] for i in range(0, len(plaintext), num_columns)]

    sorted_chars = sorted(set(key))
    
    column_order = [-1] * len(key)  # Initialize with -1 to track unassigned positions
    current_index = 0
    
    for char in sorted_chars:
        for i in range(len(key)):
            if key[i] == char and column_order[i] == -1:
                column_order[i] = current_index
                current_index += 1
    

    print(table)

    ciphertext = ''
    for col_index in column_order:
        for row in table:
            ciphertext += row[col_index]
    
    return ciphertext

def main():
    key = read_file('passwd.txt')
    plaintext = read_file('plain.txt')
    
    if len(key) != 94:
        print("Błąd: Klucz musi mieć dokładnie 94 znaki.")
        return
    
    if len(plaintext) != 94 * 8:
        print("Błąd: Tekst jawny musi mieć dokładnie 94 * 8 znaków.")
        return
    
    ciphertext = columnar_transposition_encrypt(plaintext, key)
    
    write_file('shuffle_proprietary.txt', ciphertext)
    print("Zaszyfrowano tekst i zapisano.")

if __name__ == "__main__":
    main()
