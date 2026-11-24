"""
Vigenere Cipher Implementation
"""

from ciphers.base import BaseCipher, clean_alpha


class VigenereCipher(BaseCipher):
    id = "vigenere"
    name = "Vigenere Cipher"
    category = "Polyalphabetic Substitution"
    key_hint = "Enter an alphabetic keyword (e.g., 'KEY', 'LEMON', 'FORTIFICATION')."
    overview = (
        "The Vigenere Cipher was designed by Giovan Battista Bellaso in 1553 and later misattributed "
        "to Blaise de Vigenere. It was long celebrated as 'le chiffre indechiffrable' (the unbreakable cipher).\n\n"
        "Key Characteristics:\n"
        "• Uses a repeating series of Caesar shifts dictated by letters of a secret keyword.\n"
        "• Flattens single-letter frequency spikes because the same plaintext letter can encrypt "
        "to different ciphertext letters depending on its position in the text.\n"
        "• Broken in the 19th century by Friedrich Kasiski (Kasiski examination) and Charles Babbage."
    )
    how_to_solve = (
        "Mathematical Formulation:\n\n"
        "Let P = (p_0, p_1, ..., p_{n-1}) be the plaintext indices (A=0, ..., Z=25), and "
        "K = (k_0, k_1, ..., k_{m-1}) be the key letters.\n\n"
        "1. Encryption Formula:\n"
        "   c_i = (p_i + k_{i mod m}) mod 26\n\n"
        "2. Decryption Formula:\n"
        "   p_i = (c_i - k_{i mod m}) mod 26\n\n"
        "Step-by-Step Example:\n"
        "• Plaintext: 'ATTACK AT DAWN'\n"
        "• Keyword:   'LEMON' (repeated: LEMONLEMONLE)\n"
        "• A (0)  + L (11) = 11 mod 26 -> L\n"
        "• T (19) + E (4)  = 23 mod 26 -> X\n"
        "• T (19) + M (12) = 31 mod 26 = 5 -> F\n"
        "• A (0)  + O (14) = 14 mod 26 -> O\n"
        "• C (2)  + N (13) = 15 mod 26 -> P\n"
        "• K (10) + L (11) = 21 mod 26 -> V\n"
        "• Ciphertext: 'LXFOPV EF RNHR'\n\n"
        "Decryption: L (11) - L (11) = 0 -> A."
    )

    def _parse_key(self, key: str) -> str:
        clean_key = clean_alpha(key)
        if not clean_key:
            raise ValueError(
                "Vigenere key must contain at least one alphabetic letter (e.g., 'LEMON')."
            )
        return clean_key

    def encrypt(self, text: str, key: str) -> str:
        k = self._parse_key(key)
        result = []
        k_idx = 0
        m = len(k)

        for ch in text:
            if ch.isupper():
                shift = ord(k[k_idx % m]) - ord('A')
                enc = (ord(ch) - ord('A') + shift) % 26
                result.append(chr(enc + ord('A')))
                k_idx += 1
            elif ch.islower():
                shift = ord(k[k_idx % m]) - ord('A')
                enc = (ord(ch) - ord('a') + shift) % 26
                result.append(chr(enc + ord('a')))
                k_idx += 1
            else:
                result.append(ch)

        return "".join(result)

    def decrypt(self, text: str, key: str) -> str:
        k = self._parse_key(key)
        result = []
        k_idx = 0
        m = len(k)

        for ch in text:
            if ch.isupper():
                shift = ord(k[k_idx % m]) - ord('A')
                dec = (ord(ch) - ord('A') - shift) % 26
                result.append(chr(dec + ord('A')))
                k_idx += 1
            elif ch.islower():
                shift = ord(k[k_idx % m]) - ord('A')
                dec = (ord(ch) - ord('a') - shift) % 26
                result.append(chr(dec + ord('a')))
                k_idx += 1
            else:
                result.append(ch)

        return "".join(result)
