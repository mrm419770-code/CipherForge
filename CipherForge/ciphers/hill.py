"""
Hill Cipher (2x2) Implementation
Built completely from scratch without external cryptographic, linear algebra, or math libraries.
"""

from typing import Tuple
from ciphers.base import BaseCipher, clean_alpha, mod_inverse, gcd


class HillCipher(BaseCipher):
    id = "hill"
    name = "Hill Cipher (2x2)"
    category = "Polygraphic Substitution"
    key_hint = "Enter 4 integers 'a b c d' or a 4-letter word (e.g., '3 3 2 5', 'HILL', 'GYBN')."
    overview = (
        "The Hill Cipher was invented by Lester S. Hill in 1929. It is the first polygraphic cipher "
        "based on linear algebra and modular arithmetic.\n\n"
        "Key Characteristics:\n"
        "• Encrypts blocks of n letters using an n x n invertible matrix modulo 26 (here n=2).\n"
        "• The matrix determinant MUST be coprime to 26: gcd(det(K), 26) = 1.\n"
        "• Highly resistant to single-letter frequency analysis because it disguises letter frequencies "
        "across multi-character vectors."
    )
    how_to_solve = (
        "Mathematical Formulation (2x2):\n\n"
        "Let the key matrix be K = [[a, b], [c, d]].\n"
        "1. Determinant:\n"
        "   det(K) = (a*d - b*c) mod 26\n"
        "   Condition: gcd(det(K), 26) must equal 1.\n\n"
        "2. Encryption of vector P = [p1, p2]^T:\n"
        "   C = K * P mod 26\n"
        "   c1 = (a*p1 + b*p2) mod 26\n"
        "   c2 = (c*p1 + d*p2) mod 26\n\n"
        "3. Decryption:\n"
        "   P = K^(-1) * C mod 26\n"
        "   K^(-1) = det^(-1) * [[d, -b], [-c, a]] mod 26\n\n"
        "Step-by-Step Example:\n"
        "• Key matrix K = [[3, 3], [2, 5]]\n"
        "• det(K) = (3*5 - 3*2) mod 26 = 9 mod 26. Since gcd(9, 26) = 1, det^(-1) = 3.\n"
        "• K^(-1) = 3 * [[5, -3], [-2, 3]] mod 26 = [[15, 17], [20, 9]] mod 26.\n"
        "• Plaintext 'HELP':\n"
        "  - 'HE' = [7, 4]^T -> C1 = (3*7 + 3*4) mod 26 = 33 mod 26 = 7 (H)\n"
        "                       C2 = (2*7 + 5*4) mod 26 = 34 mod 26 = 8 (I) -> 'HI'\n"
        "  - 'LP' = [11, 15]^T -> C1 = (3*11 + 3*15) mod 26 = 78 mod 26 = 0 (A)\n"
        "                         C2 = (2*11 + 5*15) mod 26 = 97 mod 26 = 19 (T) -> 'AT'\n"
        "• Ciphertext: 'HIAT'."
    )

    def _parse_key(self, key: str) -> Tuple[int, int, int, int]:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError(
                "Key cannot be empty. Enter 4 integers or a 4-letter word (e.g., '3 3 2 5' or 'GYBN')."
            )

        # Check if 4 alphabetic letters
        alpha_only = clean_alpha(cleaned)
        has_digits = any('0' <= ch <= '9' for ch in cleaned)
        if len(alpha_only) == 4 and not has_digits:
            nums = [ord(c) - ord('A') for c in alpha_only]
            a, b, c, d = nums[0], nums[1], nums[2], nums[3]
        else:
            # Parse numbers manually
            raw_parts = cleaned.replace(",", " ").split()
            parts = [p for p in raw_parts if p]
            if len(parts) != 4:
                raise ValueError(
                    f"Hill (2x2) key requires 4 values (a, b, c, d). Received: '{key}'. "
                    "Example: '3, 3, 2, 5' or '3 3 2 5' or 'GYBN'."
                )
            try:
                a, b, c, d = (int(p) % 26 for p in parts)
            except ValueError:
                raise ValueError(f"Invalid integer values in Hill key: '{key}'.")

        det = (a * d - b * c) % 26
        g = gcd(det, 26)
        if g != 1:
            raise ValueError(
                f"Matrix [[{a}, {b}], [{c}, {d}]] is not invertible modulo 26: "
                f"det(K) = {det}, gcd({det}, 26) = {g} != 1. "
                "Please choose a key whose determinant is coprime to 26."
            )

        return a, b, c, d

    def encrypt(self, text: str, key: str) -> str:
        a, b, c, d = self._parse_key(key)
        cleaned = clean_alpha(text)
        if not cleaned:
            raise ValueError("Plaintext must contain at least one alphabetic character.")

        if len(cleaned) % 2 != 0:
            cleaned += "X"

        result = []
        for i in range(0, len(cleaned), 2):
            p1 = ord(cleaned[i]) - ord('A')
            p2 = ord(cleaned[i + 1]) - ord('A')
            c1 = (a * p1 + b * p2) % 26
            c2 = (c * p1 + d * p2) % 26
            result.append(chr(c1 + ord('A')))
            result.append(chr(c2 + ord('A')))

        return "".join(result)

    def decrypt(self, text: str, key: str) -> str:
        a, b, c, d = self._parse_key(key)
        cleaned = clean_alpha(text)
        if not cleaned:
            raise ValueError("Ciphertext must contain at least one alphabetic character.")
        if len(cleaned) % 2 != 0:
            raise ValueError("Hill (2x2) ciphertext length must be an even number.")

        det = (a * d - b * c) % 26
        det_inv = mod_inverse(det, 26)

        # Adjugate matrix: [[d, -b], [-c, a]]
        inv_a = (det_inv * d) % 26
        inv_b = (det_inv * (-b)) % 26
        inv_c = (det_inv * (-c)) % 26
        inv_d = (det_inv * a) % 26

        result = []
        for i in range(0, len(cleaned), 2):
            c1 = ord(cleaned[i]) - ord('A')
            c2 = ord(cleaned[i + 1]) - ord('A')
            p1 = (inv_a * c1 + inv_b * c2) % 26
            p2 = (inv_c * c1 + inv_d * c2) % 26
            result.append(chr(p1 + ord('A')))
            result.append(chr(p2 + ord('A')))

        return "".join(result)
