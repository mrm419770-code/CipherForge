"""
Affine Cipher Implementation
Built completely from scratch without external cryptographic or math libraries.
"""

from typing import Tuple
from ciphers.base import BaseCipher, mod_inverse, gcd


class AffineCipher(BaseCipher):
    id = "affine"
    name = "Affine Cipher"
    category = "Monoalphabetic Substitution"
    key_hint = "Enter two numbers 'a, b' where gcd(a, 26) = 1 (e.g., '5, 8' or '7, 3')."
    overview = (
        "The Affine Cipher combines multiplicative and additive (Caesar) ciphers into a single linear "
        "transformation over the integers modulo 26.\n\n"
        "Key Structure:\n"
        "• Key is a pair of integers (a, b).\n"
        "• Multiplier 'a' must be coprime to 26: gcd(a, 26) = 1 (12 possible values).\n"
        "• Shift 'b' can be any integer from 0 to 25.\n"
        "• Total keyspace = 12 * 26 = 312 keys."
    )
    how_to_solve = (
        "Mathematical Formulation:\n\n"
        "Let x be the numerical index of a letter (A=0, ..., Z=25).\n\n"
        "1. Encryption Formula:\n"
        "   E(x) = (a * x + b) mod 26\n\n"
        "2. Decryption Formula:\n"
        "   D(x) = a^(-1) * (x - b) mod 26\n"
        "   where a^(-1) is the modular multiplicative inverse of 'a' modulo 26.\n\n"
        "Step-by-Step Example:\n"
        "• Plaintext: 'AFFINE', Key: a = 5, b = 8 (a^(-1) = 21)\n"
        "• A (0) -> (5*0 + 8) mod 26 = 8 -> I\n"
        "• F (5) -> (5*5 + 8) mod 26 = 33 mod 26 = 7 -> H\n"
        "• F (5) -> H\n"
        "• I (8) -> (5*8 + 8) mod 26 = 48 mod 26 = 22 -> W\n"
        "• N (13) -> (5*13 + 8) mod 26 = 73 mod 26 = 21 -> V\n"
        "• E (4) -> (5*4 + 8) mod 26 = 28 mod 26 = 2 -> C\n"
        "• Ciphertext: 'IHHWVC'\n\n"
        "Decryption: I (8) -> 21 * (8 - 8) mod 26 = 0 -> A."
    )

    def _parse_key(self, key: str) -> Tuple[int, int]:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError("Key cannot be empty. Enter two integers 'a, b' (e.g., '5, 8').")

        # Split on commas and spaces manually without regex
        raw_parts = cleaned.replace(",", " ").split()
        parts = [p for p in raw_parts if p]
        if len(parts) != 2:
            raise ValueError(
                f"Affine key requires two integers (a, b). Received: '{key}'. Example: '5, 8'."
            )

        try:
            a = int(parts[0]) % 26
            b = int(parts[1]) % 26
        except ValueError:
            raise ValueError(
                f"Invalid key components '{parts}'. Both 'a' and 'b' must be integers."
            )

        g = gcd(a, 26)
        if g != 1:
            raise ValueError(
                f"Multiplier 'a' = {a} is not coprime to 26 (gcd={g}). "
                "Valid values for 'a' modulo 26: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25."
            )

        return a, b

    def encrypt(self, text: str, key: str) -> str:
        a, b = self._parse_key(key)
        result = []
        for ch in text:
            if 'A' <= ch <= 'Z':
                x = ord(ch) - ord('A')
                enc = (a * x + b) % 26
                result.append(chr(enc + ord('A')))
            elif 'a' <= ch <= 'z':
                x = ord(ch) - ord('a')
                enc = (a * x + b) % 26
                result.append(chr(enc + ord('a')))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, text: str, key: str) -> str:
        a, b = self._parse_key(key)
        a_inv = mod_inverse(a, 26)
        result = []
        for ch in text:
            if 'A' <= ch <= 'Z':
                y = ord(ch) - ord('A')
                dec = (a_inv * (y - b)) % 26
                result.append(chr(dec + ord('A')))
            elif 'a' <= ch <= 'z':
                y = ord(ch) - ord('a')
                dec = (a_inv * (y - b)) % 26
                result.append(chr(dec + ord('a')))
            else:
                result.append(ch)
        return "".join(result)
