"""
Multiplicative Cipher Implementation
Built completely from scratch without external cryptographic or math libraries.
"""

from ciphers.base import BaseCipher, mod_inverse, gcd


class MultiplicativeCipher(BaseCipher):
    id = "multiplicative"
    name = "Multiplicative Cipher"
    category = "Monoalphabetic Substitution"
    key_hint = "Enter an integer 'a' coprime to 26 (valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)."
    overview = (
        "The Multiplicative Cipher is a monoalphabetic substitution cipher where each character's "
        "numerical value is multiplied by a secret key 'a' modulo 26.\n\n"
        "Key Requirements:\n"
        "• The multiplier 'a' MUST be coprime to 26: gcd(a, 26) = 1.\n"
        "• Modulo 26 only has 12 valid coprime keys: {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}.\n"
        "• If 'a' is not coprime to 26, distinct letters map to the same ciphertext letter, "
        "making unique decryption impossible."
    )
    how_to_solve = (
        "Mathematical Formulation:\n\n"
        "Let x be the numerical index of a letter (A=0, B=1, ..., Z=25), and 'a' be the multiplier key.\n\n"
        "1. Encryption Formula:\n"
        "   E(x) = (a * x) mod 26\n\n"
        "2. Decryption Formula:\n"
        "   D(x) = (a^(-1) * x) mod 26\n"
        "   where a^(-1) is the modular multiplicative inverse such that (a * a^(-1)) mod 26 = 1.\n\n"
        "Coprime Inverses Modulo 26:\n"
        "• 1^(-1) = 1       • 3^(-1) = 9       • 5^(-1) = 21\n"
        "• 7^(-1) = 15      • 9^(-1) = 3       • 11^(-1) = 19\n"
        "• 15^(-1) = 7      • 17^(-1) = 23     • 19^(-1) = 11\n"
        "• 21^(-1) = 5      • 23^(-1) = 17     • 25^(-1) = 25\n\n"
        "Step-by-Step Example:\n"
        "• Plaintext: 'HELLO', Key a = 7 (a^(-1) = 15)\n"
        "• H (7)  -> (7 * 7) mod 26 = 49 mod 26 = 23 -> X\n"
        "• E (4)  -> (4 * 7) mod 26 = 28 mod 26 = 2  -> C\n"
        "• L (11) -> (11 * 7) mod 26 = 77 mod 26 = 25 -> Z\n"
        "• L (11) -> (11 * 7) mod 26 = 77 mod 26 = 25 -> Z\n"
        "• O (14) -> (14 * 7) mod 26 = 98 mod 26 = 20 -> U\n"
        "• Ciphertext: 'XCZZU'\n\n"
        "Decryption: X (23) -> (23 * 15) mod 26 = 345 mod 26 = 7 -> H."
    )

    VALID_COPRIMES = {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

    def _parse_key(self, key: str) -> int:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError(
                "Key cannot be empty. Please enter an integer coprime to 26 (e.g., 7)."
            )
        try:
            a = int(cleaned) % 26
        except ValueError:
            raise ValueError(f"Invalid key '{key}'. Multiplicative key must be an integer.")

        g = gcd(a, 26)
        if g != 1:
            coprimes_str = ", ".join(str(c) for c in sorted(self.VALID_COPRIMES))
            raise ValueError(
                f"Key {a} is not coprime to 26 (gcd={g}). "
                f"Valid coprime keys modulo 26 are: [{coprimes_str}]."
            )
        return a

    def encrypt(self, text: str, key: str) -> str:
        a = self._parse_key(key)
        result = []
        for ch in text:
            if 'A' <= ch <= 'Z':
                x = ord(ch) - ord('A')
                enc = (a * x) % 26
                result.append(chr(enc + ord('A')))
            elif 'a' <= ch <= 'z':
                x = ord(ch) - ord('a')
                enc = (a * x) % 26
                result.append(chr(enc + ord('a')))
            else:
                result.append(ch)
        return "".join(result)

    def decrypt(self, text: str, key: str) -> str:
        a = self._parse_key(key)
        a_inv = mod_inverse(a, 26)
        result = []
        for ch in text:
            if 'A' <= ch <= 'Z':
                y = ord(ch) - ord('A')
                dec = (a_inv * y) % 26
                result.append(chr(dec + ord('A')))
            elif 'a' <= ch <= 'z':
                y = ord(ch) - ord('a')
                dec = (a_inv * y) % 26
                result.append(chr(dec + ord('a')))
            else:
                result.append(ch)
        return "".join(result)
