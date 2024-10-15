import math

# Pobranie tekstu do zaszyfrowania z pliku
def get_plaintext():
    with open('plain.txt', 'r') as f:
        return f.read().strip().replace(" ", "").lower()

# Szyfr przestawieniowy okresowo permutacyjny
def periodic_permutation_cipher(plaintext, key):
    key_length = len(key)
    ciphertext = [''] * key_length
    for i, char in enumerate(plaintext):
        ciphertext[i % key_length] += char
    return ''.join(ciphertext)

# Szyfr macierzowy płotkowy (Rail Fence)
def rail_fence_cipher(plaintext, num_rails):
    rail = [''] * num_rails
    direction_down = False
    row = 0
    for char in plaintext:
        rail[row] += char
        if row == 0 or row == num_rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)

# Szyfr macierzowy spiralny
def spiral_cipher(plaintext, rows, cols):
    matrix = [[''] * cols for _ in range(rows)]
    direction = 'right'
    row, col = 0, 0
    for char in plaintext:
        matrix[row][col] = char
        if direction == 'right':
            if col + 1 < cols and matrix[row][col + 1] == '':
                col += 1
            else:
                direction = 'down'
                row += 1
        elif direction == 'down':
            if row + 1 < rows and matrix[row + 1][col] == '':
                row += 1
            else:
                direction = 'left'
                col -= 1
        elif direction == 'left':
            if col - 1 >= 0 and matrix[row][col - 1] == '':
                col -= 1
            else:
                direction = 'up'
                row -= 1
        elif direction == 'up':
            if row - 1 >= 0 and matrix[row - 1][col] == '':
                row -= 1
            else:
                direction = 'right'
                col += 1

    return ''.join(''.join(row) for row in matrix)

# Szyfr macierzowy kolumnowy
def columnar_transposition_cipher(plaintext, key):
    key_length = len(key)
    columns = [''] * key_length
    for i, char in enumerate(plaintext):
        columns[i % key_length] += char

    # Posortowanie kolumn według kolejności klucza
    sorted_columns = [x for _, x in sorted(zip(key, columns))]
    return ''.join(sorted_columns)

# Główna funkcja
def main():
    plaintext = get_plaintext()

    print("Szyfr przestawieniowy okresowo permutacyjny:")
    key = "312"  # Przykładowy klucz
    print(periodic_permutation_cipher(plaintext, key))

    print("\nSzyfr macierzowy płotkowy (Rail Fence):")
    num_rails = 3
    print(rail_fence_cipher(plaintext, num_rails))

    print("\nSzyfr macierzowy spiralny:")
    rows, cols = 4, 4  # Rozmiar macierzy
    print(spiral_cipher(plaintext, rows, cols))

    print("\nSzyfr macierzowy kolumnowy:")
    column_key = "3142"  # Przykładowy klucz
    print(columnar_transposition_cipher(plaintext, column_key))

if __name__ == "__main__":
    main()
