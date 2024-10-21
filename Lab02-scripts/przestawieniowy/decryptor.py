def read_file(filename):
    """Funkcja do odczytu pliku i zwracania jego zawartości jako tekst."""
    with open(filename, 'r') as file:
        return file.read().strip()

def columnar_transposition_decrypt(ciphertext, key):
    """Funkcja do dekodowania za pomocą szyfru przestawieniowego kolumnowego."""
    num_columns = len(key)  # 94 kolumn
    num_rows = len(ciphertext) // num_columns  # 8 wierszy
    
    # Stwórz pustą tabelę (wiersze x kolumny)
    table = [''] * num_rows
    
    # Posortuj klucz, aby uzyskać kolejność kolumn w szyfrowanym tekście
    sorted_key = sorted(list(key))
    
    # Mapa kolumn: znajdź indeksy kolumn według posortowanego klucza
    column_order = [key.index(col) for col in sorted_key]
    
    # Zapełnij kolumny w tabeli zgodnie z kolejnością kolumn w szyfrowanym tekście
    col_len = num_rows
    index = 0
    columns = [''] * num_columns
    for col_index in column_order:
        columns[col_index] = ciphertext[index:index + col_len]
        index += col_len
    
    # Odtwórz oryginalny tekst z tabeli, czytając wierszami
    plaintext = ''
    for i in range(num_rows):
        for col in columns:
            plaintext += col[i]
    
    return plaintext

def main():
    # Odczytaj klucz i zaszyfrowany tekst z plików
    key = read_file('passwd.txt')
    ciphertext = read_file('shuffle_proprietary.txt')
    
    # Sprawdź, czy długości klucza i tekstu są odpowiednie
    if len(key) != 94:
        print("Błąd: Klucz musi mieć dokładnie 94 znaki.")
        return
    
    if len(ciphertext) != 94 * 8:
        print("Błąd: Zaszyfrowany tekst musi mieć dokładnie 94 * 8 znaków.")
        return
    
    # Odszyfruj za pomocą szyfru przestawieniowego kolumnowego
    plaintext = columnar_transposition_decrypt(ciphertext, key)
    
    # Wypisz odszyfrowany tekst
    print("Odszyfrowany tekst:")
    print(plaintext)

# Uruchom skrypt
if __name__ == "__main__":
    main()
