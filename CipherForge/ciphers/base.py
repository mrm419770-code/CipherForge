"""
BaseCipher Module
Defines the abstract base class and purely custom mathematical helper functions
for all ciphers in CipherForge, implemented completely from scratch without
external cryptographic or math libraries.
"""

from abc import ABC, abstractmethod
from typing import Tuple


def gcd(a: int, b: int) -> int:
    """
    Computes the Greatest Common Divisor of two integers a and b
    using the classical Euclidean algorithm from scratch.
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm implemented from scratch.
    Returns (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y


def mod_inverse(a: int, m: int = 26) -> int:
    """
    Computes the modular multiplicative inverse of a modulo m:
    (a * x) % m == 1.
    Raises ValueError if gcd(a, m) != 1.
    """
    a = a % m
    if a == 0:
        raise ValueError(f"Modular inverse does not exist: {a} modulo {m} is 0.")
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(
            f"Modular inverse does not exist: {a} and {m} are not coprime (gcd = {g})."
        )
    return (x % m + m) % m


def power_mod(base: int, exp: int, mod: int) -> int:
    """
    Computes (base^exp) % mod using the binary exponentiation
    (square-and-multiply) algorithm from scratch.
    """
    if mod == 1:
        return 0
    result = 1
    base = base % mod
    exp_val = exp
    while exp_val > 0:
        if exp_val % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp_val //= 2
    return result


def clean_alpha(text: str, keep_spaces: bool = False, to_upper: bool = True) -> str:
    """
    Filters text to retain only alphabetic characters (and optionally spaces)
    from scratch without regular expressions.
    """
    filtered = []
    for ch in text:
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            if to_upper:
                # Uppercase conversion from scratch
                if 'a' <= ch <= 'z':
                    filtered.append(chr(ord(ch) - 32))
                else:
                    filtered.append(ch)
            else:
                filtered.append(ch)
        elif keep_spaces and ch == ' ':
            filtered.append(ch)
    return "".join(filtered)


class BaseCipher(ABC):
    """
    Abstract base class for all cryptographic algorithms in CipherForge.
    Every algorithm is implemented completely from first principles.
    """

    id: str = "base"
    name: str = "Base Cipher"
    category: str = "General"
    key_hint: str = "Key format information"
    overview: str = "Overview of the cipher."
    how_to_solve: str = "Step-by-step mathematical guide."

    @abstractmethod
    def encrypt(self, text: str, key: str) -> str:
        """
        Encrypts plaintext using the provided key.
        Raises ValueError on invalid input or key.
        """
        pass

    @abstractmethod
    def decrypt(self, text: str, key: str) -> str:
        """
        Decrypts ciphertext using the provided key.
        Raises ValueError on invalid input or key.
        """
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id='{self.id}' name='{self.name}'>"
