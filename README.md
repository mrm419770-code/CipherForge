# CipherForge

**CipherForge** is a desktop cryptography studio built with Python and CustomTkinter. Designed for students, educators, and security enthusiasts, it provides an interactive environment to explore, execute, and understand classical and asymmetric encryption algorithms implemented completely from first principles.

---

## Highlights

- **Zero External Crypto Dependencies:** Every mathematical primitive—including modular exponentiation, Extended Euclidean GCD, modular inverses, matrix operations, and Miller-Rabin primality testing—is written from scratch in pure Python.
- **Interactive Learning Built In:** Each cipher includes a dedicated overview, mathematical formulation, and worked step-by-step example right inside the interface.
- **Modern Multi-Theme UI:** Switch seamlessly at runtime between multiple curated visual themes (including Dark, Light, vibrant blends, and minimalist palettes).
- **Session History & Verification:** Automatically records encryption/decryption operations during a session and includes a built-in verification suite (`verify_ciphers.py`) to validate round-trip accuracy across all ciphers.

---

## Implemented Ciphers

| Category | Algorithms Included |
| :--- | :--- |
| **Substitution Ciphers** | Caesar, Multiplicative, Affine, Autokey, Vigenère, Playfair |
| **Polygraphic & Stream** | Hill Cipher, Vernam (One-Time Pad), DNA Encryption |
| **Transposition Ciphers** | Rail Fence, Single Columnar, Double Columnar |
| **Asymmetric Cryptography** | RSA (with custom key generator and prime testing) |

---

## Project Architecture

```text
CipherForge/
├── run.py                  # Root convenience launcher
└── CipherForge/
    ├── main.py             # CustomTkinter GUI application & event controller
    ├── themes.py           # Color palettes and theme definitions
    ├── history_manager.py  # Session operation logging and history tracking
    ├── verify_ciphers.py   # Automated self-test script for all ciphers
    ├── requirements.txt    # UI dependency specification (customtkinter)
    └── ciphers/            # Modular cipher implementations
        ├── base.py         # BaseCipher interface & custom math utilities
        ├── caesar.py
        ├── multiplicative.py
        ├── affine.py
        ├── autokey.py
        ├── vigenere.py
        ├── playfair.py
        ├── hill.py
        ├── vernam.py
        ├── rail_fence.py
        ├── single_columnar.py
        ├── double_columnar.py
        ├── dna_encryption.py
        └── rsa.py