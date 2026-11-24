"""
Double Columnar Transposition Cipher Implementation
Built completely from scratch without external libraries.
"""

from typing import Tuple
from ciphers.base import BaseCipher
from ciphers.single_columnar import SingleColumnarCipher


class DoubleColumnarCipher(BaseCipher):
    id = "double_columnar"
    name = "Double Columnar Transposition"
    category = "Transposition Cipher"
    key_hint = "Enter two keys separated by comma or space (e.g., 'ZEBRA, COBRA' or 'KEY1 KEY2')."
    overview = (
        "Double Columnar Transposition applies the columnar transposition algorithm twice in succession, "
        "typically using two different keys of different lengths.\n\n"
        "Key Characteristics:\n"
        "• Widely regarded as one of the most secure pencil-and-paper ciphers ever devised.\n"
        "• Extensively employed during WWI and WWII (e.g., German military and SOE secret agents).\n"
        "• Severely disrupts anagramming and digram frequency analysis by creating complex cross-column permutations."
    )
    how_to_solve = (
        "Structural Formulation:\n\n"
        "Let K1 and K2 be the two secret transposition keys.\n\n"
        "1. Encryption Pipeline:\n"
        "   - Stage 1: Encrypt Plaintext P using Single Columnar Transposition with Key K1.\n"
        "              Intermediate = SingleColumnarEncrypt(P, K1)\n"
        "   - Stage 2: Encrypt Intermediate using Single Columnar Transposition with Key K2.\n"
        "              Ciphertext = SingleColumnarEncrypt(Intermediate, K2)\n\n"
        "2. Decryption Pipeline:\n"
        "   - Reverse the process in exact opposite order:\n"
        "   - Stage 1: Decrypt Ciphertext using Key K2.\n"
        "              Intermediate = SingleColumnarDecrypt(Ciphertext, K2)\n"
        "   - Stage 2: Decrypt Intermediate using Key K1.\n"
        "              Plaintext = SingleColumnarDecrypt(Intermediate, K1)\n\n"
        "Step-by-Step Example:\n"
        "• Plaintext: 'SECRET ATTACK AT DAWN'\n"
        "• Key 1: 'ZEBRA', Key 2: 'COBRA'\n"
        "• Stage 1 permutes letters into intermediate transposition.\n"
        "• Stage 2 permutes the intermediate stream again with COBRA's column ordering."
    )

    def __init__(self):
        self._single = SingleColumnarCipher()

    def _parse_keys(self, key: str) -> Tuple[str, str]:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError(
                "Key cannot be empty. Please provide two keys (e.g., 'ZEBRA, COBRA')."
            )

        # Split by comma first, then whitespace
        if "," in cleaned:
            parts = [p.strip() for p in cleaned.split(",") if p.strip()]
        else:
            parts = [p for p in cleaned.split() if p]

        if len(parts) == 1:
            raise ValueError(
                f"Double Columnar requires two distinct keys. Received only one: '{parts[0]}'. "
                "Format example: 'ZEBRA, COBRA' or 'KEY1 KEY2'."
            )

        return parts[0], parts[1]

    def encrypt(self, text: str, key: str) -> str:
        k1, k2 = self._parse_keys(key)
        intermediate = self._single.encrypt(text, k1)
        return self._single.encrypt(intermediate, k2)

    def decrypt(self, text: str, key: str) -> str:
        k1, k2 = self._parse_keys(key)
        intermediate = self._single.decrypt(text, k2)
        return self._single.decrypt(intermediate, k1)
