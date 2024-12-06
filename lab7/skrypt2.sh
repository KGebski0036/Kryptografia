#!/bin/bash

# Funkcja do analizy rozkładu znaków
analyze_file() {
    local file=$1
    local output=$2
    echo "Analiza pliku $file"
    cat $file | base64 | tr -d '\n' | fold -w1 | sort | uniq -c | awk '{print $2, $1}' > $output &
}

# Analiza plików
echo "Rozpoczynanie analizy statystycznej..."
mkdir -p analiza

for file in duzy_plik.txt aes_ecb.txt aes_cbc.txt des_ecb.txt des_cbc.txt zaszyfrowany_rsa.bin; do
    analyze_file $file "analiza/${file%.txt}_analiza.txt"
done

echo "Analiza zakończona. Wyniki zapisane w katalogu analiza."

