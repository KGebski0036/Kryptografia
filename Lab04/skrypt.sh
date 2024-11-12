#!/bin/bash

# Skonfiguruj zmienne
HASH_TYPE_SHA1=100   # Typ skrótu dla SHA-1 w HashCat
HASH_TYPE_SHA512=1700 # Typ skrótu dla SHA-512 w HashCat
CHARSET_LOWER="abcdefghijklmnopqrstuvwxyz" # Tylko małe litery
CHARSET_ALL="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~\`-!@#$%^&*()_+:\"<>?/[]" # Dowolne znaki klawiatury
RESULT_FILE="hashcat_test_results.txt" # Plik wyników
MAX_TIME=1200 # Maksymalny czas w sekundach (20 minut)

# Wyczyść plik wyników
echo "Testy HashCat - Czas łamania haseł" > $RESULT_FILE
echo "Długość | SHA-1 (s) | SHA-512 (s)" >> $RESULT_FILE
echo "----------------------------------" >> $RESULT_FILE

# Funkcja do generowania skrótu dla danego hasła
generate_hash() {
    local password=$1
    local hash_type=$2
    if [ "$hash_type" == "sha1" ]; then
        echo -n "$password" | sha1sum | awk '{print $1}'
    elif [ "$hash_type" == "sha512" ]; then
        echo -n "$password" | sha512sum | awk '{print $1}'
    fi
}

# Testowanie łamania hasła w HashCat
test_cracking() {
    local hash=$1
    local hash_type=$2
    local length=$3
    local charset=$4

    # Zapisz hash do pliku
    echo "$hash" > temp_hash.txt

    # Ustaw maskę na podstawie długości
    local mask=$(printf '?l%.0s' $(seq 1 $length)) # np. dla 3-znakowego hasła: ?l?l?l

    # Uruchom HashCat z limitem czasu
    local start_time=$(date +%s)
    hashcat -m $hash_type -a 3 temp_hash.txt "$mask" --increment --increment-min=$length --increment-max=$length --force --quiet
    local exit_status=$?
    local end_time=$(date +%s)
    local elapsed=$(( end_time - start_time ))

    # Sprawdź, czy czas łamania przekroczył limit lub czy hash został złamany
    if [[ $elapsed -ge $MAX_TIME ]] || [[ $exit_status -ne 0 ]]; then
        elapsed=">20m" # jeśli przekroczono limit
    fi
    rm -f temp_hash.txt
    echo $elapsed
}

# Pętla testująca hasła o różnych długościach
for length in {1..10}; do
    # Generuj hasło z samymi małymi literami o długości $length
    password=$(head /dev/urandom | tr -dc $CHARSET_LOWER | head -c $length)

    # Generuj skróty SHA-1 i SHA-512 dla hasła
    sha1_hash=$(generate_hash "$password" "sha1")
    sha512_hash=$(generate_hash "$password" "sha512")

    # Testuj łamanie skrótu SHA-1
    sha1_time=$(test_cracking "$sha1_hash" $HASH_TYPE_SHA1 $length "$CHARSET_LOWER")

    # Testuj łamanie skrótu SHA-512
    sha512_time=$(test_cracking "$sha512_hash" $HASH_TYPE_SHA512 $length "$CHARSET_LOWER")

    # Zapisz wyniki do pliku
    echo "$length        | $sha1_time      | $sha512_time" >> $RESULT_FILE

    # Zakończ, jeśli czas łamania przekracza 20 minut
    if [[ "$sha1_time" == ">20m" && "$sha512_time" == ">20m" ]]; then
        break
    fi
done

echo "Testy zakończone. Wyniki zapisano w $RESULT_FILE."
