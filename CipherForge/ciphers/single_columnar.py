"""
Single Columnar Transposition Cipher Implementation
Built completely from scratch without external libraries.
"""

from typing import List
from ciphers.base import BaseCipher, clean_alpha


class SingleColumnarCipher(BaseCipher):
    id = "single_columnar"
    name = "Single Columnar Transposition"
    category = "Transposition Cipher"
    key_hint = "Enter a keyword (e.g., 'ZEBRA', 'GERMAN') or numeric order (e.g., '3 1 4 2')."
    overview = (
        "Single Columnar Transposition is a classical transposition cipher where the message "
        "is written out in rows of a fixed width (determined by the key length) and then read out column "
        "by column in the alphabetical order of the key.\n\n"
        "Key Characteristics:\n"
        "• Permutes character locations without altering their identity.\n"
        "• Supports irregular transposition (natural lengths without padding artifacts).\n"
        "• The column reading order is determined by sorting the letters or numbers of the key."
    )
    how_to_solve = (
        "Structural Formulation:\n\n"
        "Let k be the key length, and n be the message length.\n"
        "1. Key Ordering:\n"
        "   - Sort key letters alphabetically, noting their original column indices.\n"
        "   - Example: 'ZEBRA' -> Alphabetical: A (col 4), B (col 2), E (col 1), R (col 3), Z (col 0).\n\n"
        "2. Encryption Step:\n"
        "   - Write plaintext row-by-row into a grid of width k.\n"
        "   - Read off columns completely in the determined alphabetical order.\n\n"
        "3. Decryption Step:\n"
        "   - Compute the height of each column:\n"
        "     Base rows = floor(n / k), remainder = n mod k.\n"
        "     Columns with index < remainder have height (base rows + 1); others have base rows.\n"
        "   - Reconstruct each column in alphabetical order, then read row by row."
    )

    def _parse_key_order(self, key: str) -> List[int]:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError(
                "Key cannot be empty. Please enter a keyword (e.g., 'ZEBRA') or numbers (e.g., '3 1 4 2')."
            )

        # Check if numbers separated by spaces or commas
        raw_parts = cleaned.replace(",", " ").split()
        if len(raw_parts) > 1 and all(p.isdigit() for p in raw_parts):
            num_vals = [int(p) for p in raw_parts]
            # Custom sort indices based on value
            indexed_nums = list(enumerate(num_vals))
            indexed_nums.sort(key=lambda pair: pair[1])
            return [idx for idx, _ in indexed_nums]

        # Alphabetic keyword
        alpha_key = clean_alpha(cleaned)
        if not alpha_key:
            raise ValueError("Keyword must contain at least one valid character.")

        # Alphabetical sort with stable original index
        indexed = list(enumerate(alpha_key))
        indexed.sort(key=lambda pair: pair[1])
        return [idx for idx, _ in indexed]

    def encrypt(self, text: str, key: str) -> str:
        col_order = self._parse_key_order(key)
        k = len(col_order)
        if not text:
            raise ValueError("Plaintext cannot be empty.")

        # Distribute characters into columns
        cols: List[List[str]] = [[] for _ in range(k)]
        for i, ch in enumerate(text):
            cols[i % k].append(ch)

        # Read columns in sorted key order
        result = []
        for col_idx in col_order:
            result.append("".join(cols[col_idx]))

        return "".join(result)

    def decrypt(self, text: str, key: str) -> str:
        col_order = self._parse_key_order(key)
        k = len(col_order)
        n = len(text)
        if not text:
            raise ValueError("Ciphertext cannot be empty.")

        # Calculate heights for each column 0..k-1
        base_rows = n // k
        rem = n % k
        col_lengths = [base_rows + (1 if c < rem else 0) for c in range(k)]

        # Extract text into sorted column order
        cols: List[List[str]] = [[] for _ in range(k)]
        text_idx = 0
        for col_idx in col_order:
            length = col_lengths[col_idx]
            cols[col_idx] = list(text[text_idx : text_idx + length])
            text_idx += length

        # Read row by row using integer division for ceiling: (n + k - 1) // k
        num_rows = (n + k - 1) // k if k > 0 else 0
        result = []
        for r in range(num_rows):
            for c in range(k):
                if r < len(cols[c]):
                    result.append(cols[c][r])

        return "".join(result)
