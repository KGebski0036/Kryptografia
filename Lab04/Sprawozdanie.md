# Sprawozdanie
## Autor Karol Gębski 279408
## Data: 12.11.2024

## 1.
Linux, główne pliki odpowiedzialne za przechowywanie danych o użytkownikach i ich hasłach to:

- `/etc/passwd` – przechowuje podstawowe informacje o użytkownikach oraz w przypadku niezabezpieczonego u użytkownika jego hash hasła.
- `/etc/shadow` – przechowuje hasła w formie skróconej (hash).

Plik `/etc/passwd` jest ogólnie dostępny do odczytu dla wszystkich użytkowników. Plik `/etc/shadow` jest zabezpieczony i mogą go odczytać wyłącznie użytkownicy z uprawnieniami root.

W systemie Windows hasła są przechowywane w pliku SAM, który znajduje się w:
`C:\Windows\System32\config\SAM`. Plik ten jest jednak silnie chroniony i nie jest dostępny do odczytu nawet dla administratorów w standardowy sposób.

#### Format plików:

##### `/etc/passwd`
```
username:x:UID:GID:comment:home_directory:shell
```

##### `/etc/shadow`
```
username:password_hash:last_change:min_age:max_age:warn:inactive:expire
```

#### Długość hasha

Funkcja/Słowo | SHA-1 | SHA2-256 | SHA2-384 |  SHA2-512 | MD5
|---|---|---|---|---|---|
|hello|40|64|96|128|32|
|helloWorld|40|64|96|128|32|
|h|40|64|96|128|32|
|longpasswordtestexa|40|64|96|128|32|
|plik|40|64|96|128|32|

Skróty generowane przez funkcje MD5, SHA-1, SHA-256, SHA-384 i SHA-512 mają stałą długość, niezależnie od długości wejściowych danych.

Wyniki skrótów są identyczne pod względem długości i wartości dla tych samych danych wejściowych w obu systemach operacyjnych.


Zmiana jednej litery w haśle ma ogromne znaczenie w w końcowym hashu:
```bash
➜ echo -n "hello" | sha1sum
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d  -

➜ echo -n "Hello" | sha1sum
f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0  -
```

