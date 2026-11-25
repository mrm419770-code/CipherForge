# CipherForge

caesar cipher
multiplicative cipher
affine cipher
playfair cipher
hill cipher
dna encryption
vigenere cipher
autokey cipher
vernam cipher
rail fence transposition cipher
block/single columnar
transposition
bouble columnar transposition
rsa

---

A clean, modular English Python desktop GUI application for classical and modern cryptography built using `customtkinter`. All 13 ciphers, modular arithmetic algorithms, matrix operations, and prime generation routines are implemented **completely from first principles** without external cryptographic libraries.

## 🎨 Theme Engine & Visual Modes
CipherForge features a modular, runtime theme engine defined in [`themes.py`](themes.py) supporting 5 distinct themes:
- **Dark Mode**: Modern slate-dark palette with blue accents and high-contrast typography.
- **Light Mode**: Crisp, clean light palette with subtle borders and clear readability.
- **Red-Orange-Blue Mode (Sunset Blaze / Cyber Flame)**: Cohesive harmony blending **Deep/Sapphire Blue** backgrounds and containers, **Vibrant Sunset Orange** highlights and secondary actions, and **Radiant Crimson Red** primary actions and active highlights.
- **Nordic Obsidian**: Sleek dark minimalist aesthetic with deep obsidian charcoal surfaces, cool slate borders, soft ice text, muted cyan-teal primary actions, and subtle steel accents.
- **Royal Champagne**: Warm luxury light aesthetic featuring warm ivory/alabaster backgrounds, champagne card surfaces, deep espresso ink typography, rich imperial emerald primary actions, and warm bronze accents.

## 🚀 Key Features
- **13 Cryptographic Algorithms**:
  1. **Caesar Cipher**: Classical additive shift modulo 26.
  2. **Multiplicative Cipher**: Monoalphabetic multiplication modulo 26 with coprime key validation.
  3. **Affine Cipher**: Linear transformation $(ax + b) \pmod{26}$.
  4. **Playfair Cipher**: 5x5 matrix digraph substitution with automatic $I/J$ merging and filler rules.
  5. **Hill Cipher (2x2)**: Invertible linear matrix transformation modulo 26 with determinant invertibility validation.
  6. **DNA Encryption**: Biological nucleotide mapping ($A, C, G, T$) with 2-bit encoding and modulo 4 arithmetic.
  7. **Vigenere Cipher**: Polyalphabetic substitution with repeating keystream.
  8. **Autokey Cipher**: Dynamic keystream extension using plaintext characters.
  9. **Vernam Cipher (XOR / OTP)**: Bitwise stream cipher with hexadecimal representation.
  10. **Rail Fence Cipher**: Multi-rail zig-zag transposition.
  11. **Single Columnar Transposition**: Irregular columnar permutation based on keyword alphabetical order.
  12. **Double Columnar Transposition**: Dual-stage columnar transposition for enhanced diffusion.
  13. **RSA Cipher**: Asymmetric public-key encryption ($c = m^e \pmod n$) with built-in key generator ($p, q, n, \phi, e, d$).

- **Modern Desktop GUI**:
  - Sidebar with dynamic algorithm auto-discovery and active state highlight.
  - **3-Option Theme Selector**: Easily toggle between **Dark**, **Light**, and **Red-Orange-Blue** at runtime.
  - Contextual Key Input with per-cipher hints and a dedicated **RSA Key Generator Dialog**.
  - Multiline Plaintext/Ciphertext workspace with **Encrypt**, **Decrypt**, **Swap**, and **Clear** controls.
  - **Tab 1 (Output & History)**: Instant copy to clipboard, live session history log, clear history, and export to `.txt`.
  - **Tab 2 (Overview & How to Solve)**: In-depth mathematical formulations, step-by-step guides, and worked examples for every algorithm.

## 📂 Project Structure
```text
CipherForge/
├── requirements.txt           # Dependencies (customtkinter>=5.2.0)
├── themes.py                  # ThemePalette definitions (Dark, Light, Red-Orange-Blue)
├── main.py                    # Modern CustomTkinter GUI application
├── history_manager.py         # Session history auditing & text file exporter
├── verify_ciphers.py          # Automated verification suite for all 13 ciphers
├── LICENSE                    # MIT License
├── README.md                  # Project documentation
└── ciphers/
    ├── __init__.py            # Dynamic cipher auto-discovery and registry
    ├── base.py                # Abstract BaseCipher + pure custom math helpers (gcd, egcd, mod_inverse, power_mod)
    ├── caesar.py              # Caesar Cipher
    ├── multiplicative.py      # Multiplicative Cipher
    ├── affine.py              # Affine Cipher
    ├── playfair.py            # Playfair Cipher
    ├── hill.py                # Hill Cipher 2x2
    ├── dna_encryption.py      # DNA Encryption
    ├── vigenere.py            # Vigenere Cipher
    ├── autokey.py             # Autokey Cipher
    ├── vernam.py              # Vernam Cipher (XOR)
    ├── rail_fence.py          # Rail Fence Transposition
    ├── single_columnar.py     # Single Columnar Transposition
    ├── double_columnar.py     # Double Columnar Transposition
    └── rsa.py                 # RSA Cipher + Key Generator
```

## 🛠️ Installation & Setup
1. Open the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the Application
Launch the GUI application directly:
```bash
python main.py
```
Or from the workspace root:
```bash
python run.py
```

## 🧪 Verification & Testing
Run the automated test suite to verify encryption, decryption, and error handling across all 13 ciphers:
```bash
python verify_ciphers.py
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
