import re
from collections import Counter

# Define the alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ#'
alphabet_size = len(alphabet)

# Given ciphertext
ciphertext = 'ERIPHEMJEHIPHZMMDMDHEQHGBPPHERMHWAVGEQFABGRVHP#OKMWEHTQAHIEHWQZEBIZPHBHDMPWAIGEIQZHQTHBHWAVGEQFABGRVHEBPYHTQAHERMHFAQ#GHWRBAXIM'

# Keyword to search for
keyword = 'CRYPTOGRAPHY'

def find_possible_positions(ciphertext, keyword):
    positions = []
    for i in range(len(ciphertext) - len(keyword) + 1):
        mapping = {}
        reverse_mapping = {}
        conflict = False
        for j in range(len(keyword)):
            c_char = ciphertext[i + j]
            p_char = keyword[j]
            # Check for conflicting mappings
            if c_char in mapping:
                if mapping[c_char] != p_char:
                    conflict = True
                    break
            if p_char in reverse_mapping:
                if reverse_mapping[p_char] != c_char:
                    conflict = True
                    break
            mapping[c_char] = p_char
            reverse_mapping[p_char] = c_char
        if not conflict:
            positions.append((i, mapping))
    return positions

def expand_mapping(mapping, ciphertext, plaintext_alphabet):
    # Initialize the mapping with the known substitutions
    cipher_to_plain = mapping.copy()
    plain_to_cipher = {v: k for k, v in mapping.items()}

    # Frequency analysis on the remaining letters
    cipher_remaining = [c for c in ciphertext if c not in cipher_to_plain]
    plain_remaining = [c for c in plaintext_alphabet if c not in plain_to_cipher]

    cipher_freq = Counter(cipher_remaining)
    plain_freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ#'

    # Sort the remaining plaintext letters by frequency order
    plain_remaining_sorted = [c for c in plain_freq_order if c in plain_remaining]

    # Map the most frequent ciphertext letters to the most frequent plaintext letters
    cipher_freq_sorted = [item[0] for item in cipher_freq.most_common()]
    for c_ciph, c_plain in zip(cipher_freq_sorted, plain_remaining_sorted):
        cipher_to_plain[c_ciph] = c_plain
        plain_to_cipher[c_plain] = c_ciph

    return cipher_to_plain

def decrypt(ciphertext, cipher_to_plain):
    decrypted = ''
    for c in ciphertext:
        if c in cipher_to_plain:
            decrypted += cipher_to_plain[c]
        else:
            decrypted += '?'
    return decrypted

# Main function
def main():
    possible_positions = find_possible_positions(ciphertext, keyword)
    if not possible_positions:
        print("No possible positions found for the keyword.")
        return

    plaintext_alphabet = list(alphabet)
    for pos, mapping in possible_positions:
        print(f"Trying position {pos} with initial mapping {mapping}")
        # Expand the mapping
        cipher_to_plain = expand_mapping(mapping, ciphertext, plaintext_alphabet)
        # Decrypt the ciphertext
        decrypted_text = decrypt(ciphertext, cipher_to_plain)
        # Check if the keyword is in the decrypted text
        if keyword in decrypted_text:
            print(f"Decrypted text:\n{decrypted_text}\n")
            # Optionally, you can break here if you find a plausible decryption
            # break
    else:
        print("No valid decryption found containing the keyword.")

if __name__ == "__main__":
    main()
