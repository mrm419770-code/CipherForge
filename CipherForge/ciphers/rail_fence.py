"""
Rail Fence Transposition Cipher Implementation
"""

from typing import List
from ciphers.base import BaseCipher


class RailFenceCipher(BaseCipher):
    id = "rail_fence"
    name = "Rail Fence Cipher"
    category = "Transposition Cipher"
    key_hint = "Enter an integer number of rails (depth r >= 2, e.g., 3 or 4)."
    overview = (
        "The Rail Fence Cipher (also called the Zig-Zag Cipher) is a classical transposition cipher "
        "where the characters of the plaintext are written along diagonal paths (down and up) "
        "across a specified number of 'rails', then read off row by row.\n\n"
        "Key Characteristics:\n"
        "• Pure transposition: Letter identities are preserved, only their positions are permuted.\n"
        "• The key is the depth (number of rails r >= 2).\n"
        "• Cycle length of the zig-zag is 2 * (r - 1)."
    )
    how_to_solve = (
        "Mathematical and Structural Formulation:\n\n"
        "Let r be the number of rails, and n be the length of the text.\n"
        "Cycle length T = 2 * (r - 1).\n\n"
        "1. Encryption Step:\n"
        "   - Create r empty rail rows.\n"
        "   - Place characters sequentially in a zig-zag: rail increases from 0 to r-1, "
        "then decreases from r-1 to 0.\n"
        "   - Concatenate all rows from rail 0 to rail r-1.\n\n"
        "2. Decryption Step:\n"
        "   - Mark the zig-zag matrix positions with placeholders.\n"
        "   - Fill the marked positions row by row using the ciphertext letters.\n"
        "   - Read the matrix following the original zig-zag path.\n\n"
        "Step-by-Step Example (Text: 'DEFENDTHEFLAG', Rails: 3, Cycle = 4):\n"
        "Rail 0: D . . . N . . . E . . . G  -> DNEG\n"
        "Rail 1: . E . E . D . H . F . A .  -> EEDHFA\n"
        "Rail 2: . . F . . . T . . . L . .  -> FTL\n\n"
        "Ciphertext: 'DNEGEEDHFAFTL'."
    )

    def _parse_key(self, key: str) -> int:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError("Key cannot be empty. Please enter the number of rails (e.g., 3).")
        try:
            rails = int(cleaned)
        except ValueError:
            raise ValueError(f"Invalid key '{key}'. Rails must be an integer.")
        if rails < 2:
            raise ValueError(f"Number of rails must be at least 2 (got {rails}).")
        return rails

    def encrypt(self, text: str, key: str) -> str:
        rails = self._parse_key(key)
        if not text:
            raise ValueError("Plaintext cannot be empty.")
        if rails >= len(text):
            return text

        fence: List[List[str]] = [[] for _ in range(rails)]
        rail = 0
        direction = 1

        for ch in text:
            fence[rail].append(ch)
            rail += direction
            if rail == rails - 1:
                direction = -1
            elif rail == 0:
                direction = 1

        return "".join("".join(row) for row in fence)

    def decrypt(self, text: str, key: str) -> str:
        rails = self._parse_key(key)
        if not text:
            raise ValueError("Ciphertext cannot be empty.")
        if rails >= len(text):
            return text

        # Determine rail assignment for each position in the zig-zag
        n = len(text)
        positions = []
        rail = 0
        direction = 1
        for idx in range(n):
            positions.append((rail, idx))
            rail += direction
            if rail == rails - 1:
                direction = -1
            elif rail == 0:
                direction = 1

        # Sort positions by rail, keeping original index
        sorted_indices = sorted(range(n), key=lambda i: positions[i][0])

        # Fill original characters
        result = [""] * n
        for char_idx, original_idx in enumerate(sorted_indices):
            result[original_idx] = text[char_idx]

        return "".join(result)
