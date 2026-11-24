"""
DNA Encryption Implementation
"""

from typing import List
from ciphers.base import BaseCipher


class DNAEncryptionCipher(BaseCipher):
    id = "dna_encryption"
    name = "DNA Encryption"
    category = "Bio-inspired Cryptography"
    key_hint = "Enter a secret key phrase or DNA sequence (e.g., 'BIOKEY', 'ACGTTAGC')."
    overview = (
        "DNA Cryptography is an emerging branch of cryptography inspired by molecular biology. "
        "It harnesses the information-carrying capability of the four DNA nucleotide bases: "
        "Adenine (A), Cytosine (C), Guanine (G), and Thymine (T).\n\n"
        "Key Characteristics:\n"
        "• Each byte of data (8 bits) is represented by 4 DNA nucleotides using 2-bit binary encoding:\n"
        "  - A = 00 (0)\n"
        "  - C = 01 (1)\n"
        "  - G = 10 (2)\n"
        "  - T = 11 (3)\n"
        "• Modulo 4 algebraic addition between plaintext DNA bases and a repeating key DNA stream.\n"
        "• Produces genuine biological DNA sequence representations (e.g., 'CGATCGTAGC')."
    )
    how_to_solve = (
        "Mathematical and Biological Formulation:\n\n"
        "1. Binary to DNA Mapping (Rule: A=00, C=01, G=10, T=11):\n"
        "   Each character is converted to its 8-bit ASCII representation, "
        "then split into four 2-bit pairs.\n"
        "   Example: 'M' = ASCII 77 = 01001101_2\n"
        "   - 01 -> C\n"
        "   - 00 -> A\n"
        "   - 11 -> T\n"
        "   - 01 -> C\n"
        "   DNA representation: 'CATC'.\n\n"
        "2. Key DNA Stream:\n"
        "   The secret key is likewise converted to DNA nucleotides (or used directly if already DNA) "
        "and repeated to match the plaintext DNA length.\n\n"
        "3. DNA Addition Modulo 4:\n"
        "   Values: A=0, C=1, G=2, T=3.\n"
        "   - Encryption: C_i = (P_i + K_i) mod 4\n"
        "   - Decryption: P_i = (C_i - K_i) mod 4\n\n"
        "4. Nucleotide to Text Reconstruction:\n"
        "   Every 4 decrypted DNA bases are mapped back to 2-bit numbers, concatenated into an 8-bit "
        "byte, and decoded into ASCII characters."
    )

    BASE_TO_INT = {"A": 0, "C": 1, "G": 2, "T": 3}
    INT_TO_BASE = {0: "A", 1: "C", 2: "G", 3: "T"}

    def _text_to_dna(self, text: str) -> List[str]:
        dna_bases = []
        for ch in text:
            val = ord(ch)
            if val > 255:
                # UTF-8 byte encoding
                byte_vals = ch.encode('utf-8')
            else:
                byte_vals = [val]
            for b in byte_vals:
                # 4 pairs of 2 bits (bits 7-6, 5-4, 3-2, 1-0)
                dna_bases.append(self.INT_TO_BASE[(b >> 6) & 0b11])
                dna_bases.append(self.INT_TO_BASE[(b >> 4) & 0b11])
                dna_bases.append(self.INT_TO_BASE[(b >> 2) & 0b11])
                dna_bases.append(self.INT_TO_BASE[b & 0b11])
        return dna_bases

    def _dna_to_text(self, dna_bases: List[str]) -> str:
        if len(dna_bases) % 4 != 0:
            raise ValueError(
                f"DNA sequence length ({len(dna_bases)}) must be a multiple of 4 (4 bases per byte)."
            )

        byte_array = bytearray()
        for i in range(0, len(dna_bases), 4):
            b0 = self.BASE_TO_INT[dna_bases[i]]
            b1 = self.BASE_TO_INT[dna_bases[i + 1]]
            b2 = self.BASE_TO_INT[dna_bases[i + 2]]
            b3 = self.BASE_TO_INT[dna_bases[i + 3]]
            byte_val = (b0 << 6) | (b1 << 4) | (b2 << 2) | b3
            byte_array.append(byte_val)

        try:
            return byte_array.decode('utf-8')
        except UnicodeDecodeError:
            return byte_array.decode('latin-1')

    def _get_key_dna(self, key: str) -> List[str]:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError("Key cannot be empty. Please enter a key string or DNA sequence.")

        upper = cleaned.upper()
        if all(ch in "ACGT" for ch in upper):
            return list(upper)
        return self._text_to_dna(cleaned)

    def encrypt(self, text: str, key: str) -> str:
        if not text:
            raise ValueError("Plaintext cannot be empty.")

        p_dna = self._text_to_dna(text)
        k_dna = self._get_key_dna(key)

        c_dna = []
        for i, p_base in enumerate(p_dna):
            k_base = k_dna[i % len(k_dna)]
            p_val = self.BASE_TO_INT[p_base]
            k_val = self.BASE_TO_INT[k_base]
            c_val = (p_val + k_val) % 4
            c_dna.append(self.INT_TO_BASE[c_val])

        return "".join(c_dna)

    def decrypt(self, text: str, key: str) -> str:
        cleaned = "".join(text.split()).upper()
        if not cleaned:
            raise ValueError("Ciphertext cannot be empty.")

        for ch in cleaned:
            if ch not in self.BASE_TO_INT:
                raise ValueError(
                    f"Invalid DNA base '{ch}'. DNA ciphertext must contain only A, C, G, and T."
                )

        k_dna = self._get_key_dna(key)

        p_dna = []
        for i, c_base in enumerate(cleaned):
            k_base = k_dna[i % len(k_dna)]
            c_val = self.BASE_TO_INT[c_base]
            k_val = self.BASE_TO_INT[k_base]
            p_val = (c_val - k_val + 4) % 4
            p_dna.append(self.INT_TO_BASE[p_val])

        return self._dna_to_text(p_dna)
