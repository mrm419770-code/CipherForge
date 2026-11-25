"""
RSA Asymmetric Cipher & Key Generator Implementation
Built completely from scratch without external cryptographic, number-theoretic, or math libraries.
All modular exponentiation, GCD, and inverses are custom-implemented from first principles.
"""

import time
from typing import Dict, Tuple
from ciphers.base import BaseCipher, mod_inverse, gcd, power_mod


def _pseudo_rand(seed_val: int) -> Tuple[int, int]:
    """Linear Congruential Generator for deterministic pseudo-randomness."""
    a = 1664525
    c = 1013904223
    m = 2**32
    new_seed = (a * seed_val + c) % m
    return new_seed, new_seed


def is_prime(n: int) -> bool:
    """
    Miller-Rabin primality test implemented from scratch.
    Deterministic for integers up to 3.3 * 10^14 using small prime bases.
    """
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Deterministic testing bases for small integers
    bases = [2, 3, 5, 7, 11, 13, 17]
    for a in bases:
        if a >= n:
            continue
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(r - 1):
            x = power_mod(x, 2, n)
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True


def generate_prime(min_val: int = 1000, max_val: int = 5000, seed: int = 0) -> Tuple[int, int]:
    """
    Finds a prime number within the specified range from scratch.
    Returns (prime, new_seed).
    """
    if seed == 0:
        seed = int(time.time() * 1000) % 1000000007

    candidate = min_val + (seed % (max_val - min_val))
    if candidate % 2 == 0:
        candidate += 1

    while True:
        seed, _ = _pseudo_rand(seed)
        if is_prime(candidate):
            return candidate, seed
        candidate += 2
        if candidate > max_val:
            candidate = min_val + 1


def generate_rsa_keys() -> Dict[str, str]:
    """
    Generates a functional sample RSA public/private key pair from scratch.
    Returns a dictionary with formatted string representations.
    """
    seed = int(time.time() * 1000) % 1000000007
    p, seed = generate_prime(1009, 4999, seed)
    q, seed = generate_prime(5003, 8999, seed + 1337)
    while p == q:
        q, seed = generate_prime(5003, 8999, seed + 999)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Standard public exponents
    candidates = [65537, 17, 7, 5, 3]
    e = 65537
    for cand in candidates:
        if cand < phi and gcd(cand, phi) == 1:
            e = cand
            break
    else:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)

    return {
        "p": str(p),
        "q": str(q),
        "n": str(n),
        "phi": str(phi),
        "e": str(e),
        "d": str(d),
        "public_key": f"{e}, {n}",
        "private_key": f"{d}, {n}",
    }


class RSACipher(BaseCipher):
    id = "rsa"
    name = "RSA Cipher"
    category = "Asymmetric / Public-Key Cryptography"
    key_hint = "Public Key: 'e, n' for Encrypt | Private Key: 'd, n' for Decrypt (or click 'Generate RSA Keys')."
    overview = (
        "Invented in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman, RSA is the cornerstone of "
        "modern public-key asymmetric cryptography.\n\n"
        "Key Principles:\n"
        "• Two mathematically linked keys: a Public Key (e, n) shared openly for encryption, and a "
        "Private Key (d, n) kept secret for decryption.\n"
        "• Security rests on the computational hardness of factoring large semiprimes (n = p * q).\n"
        "• In this educational engine, text characters are represented as integers and encrypted "
        "into numerical ciphertext sequences."
    )
    how_to_solve = (
        "Mathematical Formulation:\n\n"
        "1. Key Generation:\n"
        "   - Select two distinct primes p and q.\n"
        "   - Modulus n = p * q\n"
        "   - Euler's totient phi(n) = (p - 1) * (q - 1)\n"
        "   - Choose public exponent e coprime to phi(n): gcd(e, phi(n)) = 1.\n"
        "   - Compute private exponent d = e^(-1) mod phi(n).\n\n"
        "2. Encryption (using Public Key (e, n)):\n"
        "   c = (m^e) mod n\n"
        "   where m is the character code (m < n).\n\n"
        "3. Decryption (using Private Key (d, n)):\n"
        "   m = (c^d) mod n\n"
        "   By Euler's Totient Theorem, (m^e)^d = m^(e*d) = m^(1 + k*phi(n)) = m mod n.\n\n"
        "Step-by-Step Small Example:\n"
        "• p = 61, q = 53 -> n = 3233, phi(n) = 3120\n"
        "• Choose e = 17 -> d = 17^(-1) mod 3120 = 2753\n"
        "• Message 'A' (ASCII 65):\n"
        "  c = 65^17 mod 3233 = 2790\n"
        "• Decryption:\n"
        "  m = 2790^2753 mod 3233 = 65 -> 'A'."
    )

    def _parse_key_pair(self, key: str) -> Tuple[int, int]:
        cleaned = key.strip()
        if not cleaned:
            raise ValueError(
                "Key cannot be empty. Please enter 'exponent, modulus' (e.g., '65537, 3233')."
            )
        raw_parts = cleaned.replace(",", " ").split()
        parts = [p for p in raw_parts if p]
        if len(parts) != 2:
            raise ValueError(
                f"RSA key requires two integers (exponent, modulus). Received: '{key}'. "
                "Format: 'e, n' or 'd, n'."
            )
        try:
            exp = int(parts[0])
            mod = int(parts[1])
        except ValueError:
            raise ValueError(f"RSA key components must be valid integers: '{key}'.")
        if mod < 2:
            raise ValueError(f"RSA modulus n must be greater than 1 (got {mod}).")
        return exp, mod


    def encrypt(self, text: str, key: str) -> str:
        e, n = self._parse_key_pair(key)
        if not text:
            raise ValueError("Plaintext cannot be empty.")

        cipher_nums = []
        for ch in text:
            m = ord(ch)
            if m >= n:
                raise ValueError(
                    f"Character '{ch}' (code {m}) exceeds RSA modulus n={n}. "
                    "Please generate a key with a larger modulus."
                )
            c = power_mod(m, e, n)
            cipher_nums.append(str(c))
        return " ".join(cipher_nums)

    def decrypt(self, text: str, key: str) -> str:
        d, n = self._parse_key_pair(key)
        cleaned = text.strip()
        if not cleaned:
            raise ValueError("Ciphertext cannot be empty.")

        parts = cleaned.replace(",", " ").split()
        plain_chars = []
        for p in parts:
            if not p:
                continue
            try:
                c = int(p)
            except ValueError:
                raise ValueError(
                    f"Invalid encrypted token '{p}'. RSA ciphertext must be space-separated integers."
                )
            m = power_mod(c, d, n)
            plain_chars.append(chr(m))

        return "".join(plain_chars)

    def generate_keys(self) -> Dict[str, str]:
        """Expose key generator utility on the cipher instance."""
        return generate_rsa_keys()
