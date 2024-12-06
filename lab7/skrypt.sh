#!/bin/bash

# Klucze szyfrowania
AES_KEY="0123456789ABCDEF0123456789ABCDEF"  # 32 znaki (256-bitowy klucz)
DES_KEY="0123456789ABCDEF"                 # 16 znaków (64-bitowy klucz)

# IV dla trybu CBC
IV="0000000000000000"

# Szyfrowanie DES i AES w trybach ECB oraz CBC
echo "Szyfrowanie plików..."
openssl enc -aes-128-ecb -e -in duzy_plik.txt -out aes_ecb.txt -K $AES_KEY -nosalt
openssl enc -aes-128-cbc -e -in duzy_plik.txt -out aes_cbc.txt -K $AES_KEY -iv $IV -nosalt

openssl enc -des-ecb -e -in duzy_plik.txt -out des_ecb.txt -K $DES_KEY -nosalt -provider legacy -provider default
openssl enc -des-cbc -e -in duzy_plik.txt -out des_cbc.txt -K $DES_KEY -iv $IV -nosalt -provider legacy -provider default

# RSA: najpierw szyfrujemy plik AES
#
# Generowanie kluczy RSA (klucz 4096-bitowy)
if [ ! -f rsa_private.pem ] || [ ! -f rsa_public.pem ]; then
  echo "Generowanie kluczy RSA..."
  openssl genrsa -out rsa_private.pem 4096
  openssl rsa -in rsa_private.pem -out rsa_public.pem -pubout
  echo "Klucze RSA wygenerowane."
fi

# Parametry
INPUT_FILE="duzy_plik.txt"
ENCRYPTED_FILE="zaszyfrowany_rsa.bin"
TEMP_DIR="temp_rsa"
BLOCK_SIZE=200  # Maksymalny rozmiar bloku dla 4096-bitowego klucza RSA z paddingiem PKCS#1

# Przygotowanie katalogu tymczasowego
mkdir -p $TEMP_DIR
rm -f $TEMP_DIR/*

# Podział pliku na fragmenty
echo "Dzielimy plik wejściowy na fragmenty..."
split -b $BLOCK_SIZE -d $INPUT_FILE $TEMP_DIR/block_


i=0
files=$(ls $TEMP_DIR -l | wc -l); 
# Szyfrowanie fragmentów
echo "Szyfrowanie fragmentów RSA..."
for block in $TEMP_DIR/block_*; do
  echo $i "/" $files
  i=$(($i + 1));  
  openssl pkeyutl -encrypt -inkey rsa_public.pem -pubin -in $block -out ${block}.enc &
done

sleep 5

# Łączenie zaszyfrowanych fragmentów
echo "Łączenie zaszyfrowanych fragmentów w jeden plik..."
cat $TEMP_DIR/*.enc > $ENCRYPTED_FILE

echo "Szyfrowanie zakończone. Zaszyfrowany plik zapisano jako $ENCRYPTED_FILE."

# Usuwanie katalogu tymczasowego
rm -r $TEMP_DIR

echo "Szyfrowanie zakończone."

