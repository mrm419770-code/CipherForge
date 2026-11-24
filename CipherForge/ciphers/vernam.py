"""
Vernam Cipher (XOR / One-Time Pad) Implementation
"""

from ciphers.base import BaseCipher


class VernamCipher(BaseCipher):
    id = "vernam"
    name = "Vernam Cipher (XOR / OTP)"
    category = "Stream / Information-Theoretic Cipher"
    key_hint = "Enter a secret key string (e.g., 'SUPERSECRETKEY99'). Produces Hex output."
    overview = (
        "Invented by Gilbert Vernam in 1917 and mathematically proven by Claude Shannon in 1949, "
        "the Vernam Cipher operates on bitwise XOR (Exclusive OR) between plaintext and key bits.\n\n"
        "Key Characteristics:\n"
        "• When the key is truly random, as long as the message, and never reused, it is a One-Time Pad (OTP) "
        "and achieves PERFECT SECRECY (unconditionally secure against any computational power).\n"
        "• Self-reciprocal operation: (A XOR B) XOR B = A.\n"
        "• Ciphertext is represented in Hexadecimal format to preserve non-printable binary bytes safely."
    )
    how_to_solve = (
        "Mathematical Formulation:\n\n"
        "1. Bitwise XOR Truth Table:\n"
        "   0 XOR 0 = 0\n"
        "   0 XOR 1 = 1\n"
        "   1 XOR 0 = 1\n"
        "   1 XOR 1 = 0\n\n"
        "2. Encryption:\n"
        "   Convert plaintext characters and key to bytes.\n"
        "   C_i = P_i XOR K_{i mod |K|}\n"
        "   Format output as a hexadecimal string.\n\n"
        "3. Decryption:\n"
        "   Convert hex string back into bytes.\n"
        "   P_i = C_i XOR K_{i mod |K|}\n"
        "   Decode bytes back to original UTF-8 text.\n\n"
        "Step-by-Step Example:\n"
        "• Plaintext byte: 'H' = 0x48 = 01001000_2\n"
        "• Key byte:       'K' = 0x4B = 01001011_2\n"
        "• Cipher byte:    0x48 XOR 0x4B = 0x03 = 00000011_2\n"
        "• Decryption:     0x03 XOR 0x4B = 0x48 ('H')."
    )

    def encrypt(self, text: str, key: str) -> str:
        if not text:
            raise ValueError("Plaintext cannot be empty.")
        if not key:
            raise ValueError("Key cannot be empty. Please enter a secret key string.")

        p_bytes = text.encode("utf-8")
        k_bytes = key.encode("utf-8")

        c_bytes = bytearray(len(p_bytes))
        for i in range(len(p_bytes)):
            c_bytes[i] = p_bytes[i] ^ k_bytes[i % len(k_bytes)]

        return c_bytes.hex()

    def decrypt(self, text: str, key: str) -> str:
        cleaned = text.strip()
        if not cleaned:
            raise ValueError("Ciphertext cannot be empty.")
        if not key:
            raise ValueError("Key cannot be empty. Please enter a secret key string.")

        # Attempt to decode hex
        try:
            c_bytes = bytes.fromhex(cleaned)
        except ValueError:
            raise ValueError(
                "Invalid Vernam ciphertext. Expected a valid hexadecimal string "
                "(e.g., '1c040d1f...')."
            )

        k_bytes = key.encode("utf-8")
        p_bytes = bytearray(len(c_bytes))
        for i in range(len(c_bytes)):
            p_bytes[i] = c_bytes[i] ^ k_bytes[i % len(k_bytes)]

        try:
            return p_bytes.decode("utf-8")
        except UnicodeDecodeError:
            return p_bytes.decode("latin-1")
