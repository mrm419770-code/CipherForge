"""
Autokey Cipher Implementation
"""

from typing import List
from ciphers.base import BaseCipher, clean_alpha


class AutokeyCipher(BaseCipher):
    id = "autokey"
    name = "Autokey Cipher"
    category = "Polyalphabetic Substitution"
    key_hint = "Enter an alphabetic primer keyword (e.g., 'QUEEN', 'CIPHER')."
    overview = (
        "The Autokey Cipher was invented by Blaise de Vigenere in 1586. Unlike the periodic "
        "Vigenere cipher, the Autokey cipher avoids periodic repetitions by appending the message itself "
        "to the secret primer key to form the keystream.\n\n"
        "Key Characteristics:\n"
        "• Eliminates the periodic key repetition exploited by the Kasiski examination.\n"
        "• The keystream is formed by: Primer Key + Plaintext.\n"
        "• In decryption, each recovered plaintext letter feeds into the keystream to unlock subsequent letters."
    )
    how_to_solve = (
        "Mathematical Formulation:\n\n"
        "Let K = (k_0, ..., k_{m-1}) be the initial primer key of length m.\n\n"
        "1. Encryption:\n"
        "   Keystream S begins with K: S = (k_0, ..., k_{m-1}, p_0, p_1, p_2, ...)\n"
        "   c_i = (p_i + S_i) mod 26\n\n"
        "2. Decryption:\n"
        "   For i = 0 to m-1:\n"
        "     p_i = (c_i - k_i) mod 26\n"
        "   For i >= m:\n"
        "     p_i = (c_i - p_{i - m}) mod 26\n\n"
        "Step-by-Step Example:\n"
        "• Plaintext: 'ATTACK AT DAWN'\n"
        "• Primer Key: 'QUEEN' (m = 5)\n"
        "• Keystream:  Q U E E N A T T A C K A T\n"
        "• A (0)  + Q (16) = 16 -> Q\n"
        "• T (19) + U (20) = 39 mod 26 = 13 -> N\n"
        "• T (19) + E (4)  = 23 -> X\n"
        "• A (0)  + E (4)  = 4  -> E\n"
        "• C (2)  + N (13) = 15 -> P\n"
        "• K (10) + A (0)  = 10 -> K (Plaintext 'A' shifted K)\n"
        "• Ciphertext: 'QNXEPK TR DTCI'."
    )

    def _parse_key(self, key: str) -> str:
        clean_key = clean_alpha(key)
        if not clean_key:
            raise ValueError(
                "Autokey primer key must contain at least one alphabetic letter (e.g., 'QUEEN')."
            )
        return clean_key

    def encrypt(self, text: str, key: str) -> str:
        primer = self._parse_key(key)
        # Extract all alpha characters from plaintext to form the keystream extension
        plain_alpha = clean_alpha(text)
        keystream_alpha = primer + plain_alpha

        result = []
        k_idx = 0
        for ch in text:
            if ch.isupper():
                shift = ord(keystream_alpha[k_idx]) - ord('A')
                enc = (ord(ch) - ord('A') + shift) % 26
                result.append(chr(enc + ord('A')))
                k_idx += 1
            elif ch.islower():
                shift = ord(keystream_alpha[k_idx]) - ord('A')
                enc = (ord(ch) - ord('a') + shift) % 26
                result.append(chr(enc + ord('a')))
                k_idx += 1
            else:
                result.append(ch)

        return "".join(result)

    def decrypt(self, text: str, key: str) -> str:
        primer = self._parse_key(key)
        keystream: List[str] = list(primer)

        result = []
        k_idx = 0
        for ch in text:
            if ch.isalpha():
                shift = ord(keystream[k_idx]) - ord('A')
                is_upper = ch.isupper()
                base = ord('A') if is_upper else ord('a')
                dec_val = (ord(ch) - base - shift) % 26
                dec_char = chr(dec_val + base)
                result.append(dec_char)

                # Feed recovered plaintext letter into keystream
                keystream.append(chr(dec_val + ord('A')))
                k_idx += 1
            else:
                result.append(ch)

        return "".join(result)
