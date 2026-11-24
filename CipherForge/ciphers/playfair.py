"""
Playfair Cipher Implementation
"""

from typing import List, Tuple
from ciphers.base import BaseCipher, clean_alpha


class PlayfairCipher(BaseCipher):
    id = "playfair"
    name = "Playfair Cipher"
    category = "Polygraphic Substitution"
    key_hint = "Enter a keyword or phrase (e.g., 'MONARCHY', 'SECRET KEY')."
    overview = (
        "The Playfair Cipher was invented by Charles Wheatstone in 1854 and promoted by Lord Playfair. "
        "It was the first practical digraph substitution cipher, encrypting pairs of letters instead of "
        "single letters.\n\n"
        "Key Characteristics:\n"
        "• Uses a 5x5 matrix populated with a secret keyword followed by the remaining alphabet letters.\n"
        "• 'I' and 'J' are combined into a single cell to fit 25 letters.\n"
        "• Significantly harder to break than monoalphabetic ciphers because letter frequency analysis "
        "must be performed on 600+ digraphs rather than 26 single letters."
    )
    how_to_solve = (
        "Matrix Construction:\n"
        "1. Write keyword without duplicate letters, treating J as I.\n"
        "2. Fill remaining cells with unused letters A-Z (excluding J).\n\n"
        "Digraph Preparation:\n"
        "• Break plaintext into pairs of letters.\n"
        "• If both letters in a pair are identical, insert 'X' between them (e.g., 'EE' -> 'EX EG').\n"
        "• If the total count is odd, append 'X' (or 'Z' if the last letter is X).\n\n"
        "Encryption Rules for Digraph (A, B):\n"
        "1. Same Row: Replace each letter with the letter to its immediate right (wrapping around).\n"
        "2. Same Column: Replace each letter with the letter immediately below it (wrapping around).\n"
        "3. Rectangle: Form a rectangle where A and B are opposite corners. Replace each letter with "
        "the letter in its own row and the other letter's column.\n\n"
        "Decryption Rules:\n"
        "• Same Row: Shift LEFT.\n"
        "• Same Column: Shift UP.\n"
        "• Rectangle: Swap columns (same as encryption).\n\n"
        "Example (Key 'MONARCHY', Matrix 5x5):\n"
        "M O N A R\n"
        "C H Y B D\n"
        "E F G I K\n"
        "L P Q S T\n"
        "U V W X Z\n"
        "• Plaintext pair 'TH' forms rectangle -> Encrypts to 'PD'."
    )

    def _build_matrix(self, key: str) -> Tuple[List[List[str]], dict]:
        clean_key = clean_alpha(key).replace("J", "I")
        if not clean_key:
            raise ValueError("Playfair key must contain at least one alphabetic character.")

        matrix_chars: List[str] = []
        seen = set()

        for ch in clean_key:
            if ch not in seen:
                seen.add(ch)
                matrix_chars.append(ch)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: J omitted
        for ch in alphabet:
            if ch not in seen:
                seen.add(ch)
                matrix_chars.append(ch)

        matrix = [matrix_chars[i * 5 : (i + 1) * 5] for i in range(5)]
        pos_map = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
        return matrix, pos_map

    def _prepare_plaintext(self, text: str) -> List[Tuple[str, str]]:
        cleaned = clean_alpha(text).replace("J", "I")
        if not cleaned:
            raise ValueError("Plaintext must contain at least one alphabetic letter.")

        pairs: List[Tuple[str, str]] = []
        i = 0
        n = len(cleaned)
        while i < n:
            a = cleaned[i]
            if i + 1 < n:
                b = cleaned[i + 1]
                if a == b:
                    filler = "Q" if a == "X" else "X"
                    pairs.append((a, filler))
                    i += 1
                else:
                    pairs.append((a, b))
                    i += 2
            else:
                filler = "Z" if a == "X" else "X"
                pairs.append((a, filler))
                i += 1
        return pairs

    def encrypt(self, text: str, key: str) -> str:
        matrix, pos_map = self._build_matrix(key)
        pairs = self._prepare_plaintext(text)

        cipher_chars = []
        for a, b in pairs:
            r1, c1 = pos_map[a]
            r2, c2 = pos_map[b]

            if r1 == r2:
                cipher_chars.append(matrix[r1][(c1 + 1) % 5])
                cipher_chars.append(matrix[r2][(c2 + 1) % 5])
            elif c1 == c2:
                cipher_chars.append(matrix[(r1 + 1) % 5][c1])
                cipher_chars.append(matrix[(r2 + 1) % 5][c2])
            else:
                cipher_chars.append(matrix[r1][c2])
                cipher_chars.append(matrix[r2][c1])

        return "".join(cipher_chars)

    def decrypt(self, text: str, key: str) -> str:
        matrix, pos_map = self._build_matrix(key)
        cleaned = clean_alpha(text).replace("J", "I")
        if not cleaned:
            raise ValueError("Ciphertext must contain at least one alphabetic letter.")
        if len(cleaned) % 2 != 0:
            raise ValueError("Playfair ciphertext must have an even length.")

        plain_chars = []
        for i in range(0, len(cleaned), 2):
            a, b = cleaned[i], cleaned[i + 1]
            r1, c1 = pos_map[a]
            r2, c2 = pos_map[b]

            if r1 == r2:
                plain_chars.append(matrix[r1][(c1 - 1) % 5])
                plain_chars.append(matrix[r2][(c2 - 1) % 5])
            elif c1 == c2:
                plain_chars.append(matrix[(r1 - 1) % 5][c1])
                plain_chars.append(matrix[(r2 - 1) % 5][c2])
            else:
                plain_chars.append(matrix[r1][c2])
                plain_chars.append(matrix[r2][c1])

        return "".join(plain_chars)
