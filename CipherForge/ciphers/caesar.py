"""
Caesar Cipher Implementation
"""

from ciphers.base import BaseCipher


class CaesarCipher(BaseCipher):
    id = "caesar"
    name = "Caesar Cipher"
    category = "Monoalphabetic Substitution"
    key_hint = "Enter an integer shift k (e.g., 3, 13, -5)."
    overview = (
        "The Caesar Cipher is one of the earliest and simplest known encryption techniques. "
        "Named after Julius Caesar, who used it to protect military correspondence, it is a type of "
        "substitution cipher in which each letter in the plaintext is shifted by a fixed number of positions "
        "down the alphabet.\n\n"
        "Key Characteristics:\n"
        "• Modulo 26 arithmetic over the English alphabet (A=0, B=1, ..., Z=25).\n"
        "• Weak security: Only 25 possible keys (excluding k=0), easily broken by brute-force or frequency analysis.\n"
        "• Preserves letter casing while leaving numbers and punctuation unchanged."
    )
    how_to_solve = (
        "Mathematical Formulation:\n\n"
        "Let x be the numerical index of a letter (A=0, B=1, ..., Z=25), and k be the integer key.\n\n"
        "1. Encryption Formula:\n"
        "   E(x) = (x + k) mod 26\n\n"
        "2. Decryption Formula:\n"
        "   D(x) = (x - k) mod 26\n\n"
        "Step-by-Step Example:\n"
        "• Plaintext: 'HELLO', Key: 3\n"
        "• H (7)  -> (7 + 3) mod 26 = 10 -> K\n"
        "• E (4)  -> (4 + 3) mod 26 = 7  -> H\n"
        "• L (11) -> (11 + 3) mod 26 = 14 -> O\n"
        "• L (11) -> (11 + 3) mod 26 = 14 -> O\n"
        "• O (14) -> (14 + 3) mod 26 = 17 -> R\n"
        "• Ciphertext: 'KHOOR'\n\n"
        "Decryption reverses the shift: D(10) = (10 - 3) mod 26 = 7 -> H."
    )

    def _parse_key(self, key: str) -> int:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError("Key cannot be empty. Please provide an integer shift (e.g., 3).")
        try:
            return int(cleaned) % 26
        except ValueError:
            raise ValueError(f"Invalid Caesar key '{key}'. Key must be an integer.")

    def encrypt(self, text: str, key: str) -> str:
        k = self._parse_key(key)
        result = []
        for ch in text:
            if ch.isupper():
                result.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
            elif ch.islower():
                result.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, text: str, key: str) -> str:
        k = self._parse_key(key)
        result = []
        for ch in text:
            if ch.isupper():
                result.append(chr((ord(ch) - ord('A') - k) % 26 + ord('A')))
            elif ch.islower():
                result.append(chr((ord(ch) - ord('a') - k) % 26 + ord('a')))
            else:
                result.append(ch)
        return "".join(result)
