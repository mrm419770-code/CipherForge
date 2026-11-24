"""
CipherForge Comprehensive Verification Suite
Tests all 13 ciphers for:
1. Dynamic loading
2. Encryption and Decryption round-trips
3. Edge cases and input validation
4. Error handling
5. History manager operations
"""

import sys
import os

# Set utf-8 encoding for standard output if available
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Add directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ciphers import CIPHER_LIST, CIPHERS, get_cipher
from history_manager import HistoryManager


def run_tests():
    print("=" * 65)
    print("       RUNNING CIPHERFORGE COMPREHENSIVE VERIFICATION        ")
    print("=" * 65)

    print("\n[1] Dynamic Loader Check:")
    print(f"Total discovered ciphers: {len(CIPHER_LIST)}")
    assert len(CIPHER_LIST) == 13, f"Expected 13 ciphers, found {len(CIPHER_LIST)}"

    expected_ids = [
        "caesar",
        "multiplicative",
        "affine",
        "playfair",
        "hill",
        "dna_encryption",
        "vigenere",
        "autokey",
        "vernam",
        "rail_fence",
        "single_columnar",
        "double_columnar",
        "rsa",
    ]

    for cid in expected_ids:
        cipher = get_cipher(cid)
        assert cipher is not None, f"Cipher '{cid}' was not loaded!"
        print(f"  [PASS] [{cipher.category}] {cipher.name} (id: '{cipher.id}')")

    print("\n[2] Testing Encryption & Decryption Round-Trips:")

    # 1. Caesar Cipher
    caesar = get_cipher("caesar")
    msg1 = "Hello, World! 123"
    enc1 = caesar.encrypt(msg1, "3")
    dec1 = caesar.decrypt(enc1, "3")
    assert dec1 == msg1, f"Caesar failed: {dec1} != {msg1}"
    print("  [PASS] Caesar Cipher passed round-trip.")

    # 2. Multiplicative Cipher
    mult = get_cipher("multiplicative")
    msg2 = "Attack At Dawn!"
    enc2 = mult.encrypt(msg2, "7")
    dec2 = mult.decrypt(enc2, "7")
    assert dec2 == msg2, f"Multiplicative failed: {dec2} != {msg2}"
    print("  [PASS] Multiplicative Cipher passed round-trip.")

    # 3. Affine Cipher
    affine = get_cipher("affine")
    msg3 = "Secret Affine Message!"
    enc3 = affine.encrypt(msg3, "5, 8")
    dec3 = affine.decrypt(enc3, "5, 8")
    assert dec3 == msg3, f"Affine failed: {dec3} != {msg3}"
    print("  [PASS] Affine Cipher passed round-trip.")

    # 4. Playfair Cipher
    playfair = get_cipher("playfair")
    msg4 = "INSTRUMENT"
    enc4 = playfair.encrypt(msg4, "MONARCHY")
    dec4 = playfair.decrypt(enc4, "MONARCHY")
    assert dec4 == msg4, f"Playfair failed: {dec4} != {msg4}"
    print("  [PASS] Playfair Cipher passed round-trip.")

    # 5. Hill Cipher (2x2)
    hill = get_cipher("hill")
    msg5 = "HELP"
    enc5 = hill.encrypt(msg5, "3 3 2 5")
    dec5 = hill.decrypt(enc5, "3 3 2 5")
    assert dec5 == msg5, f"Hill failed: {dec5} != {msg5}"
    print("  [PASS] Hill (2x2) Cipher passed round-trip.")

    # 6. DNA Encryption
    dna = get_cipher("dna_encryption")
    msg6 = "Top Secret 2026!"
    enc6 = dna.encrypt(msg6, "BIOKEY")
    assert all(c in "ACGT" for c in enc6), f"DNA output invalid: {enc6}"
    dec6 = dna.decrypt(enc6, "BIOKEY")
    assert dec6 == msg6, f"DNA failed: {dec6} != {msg6}"
    print("  [PASS] DNA Encryption passed round-trip.")

    # 7. Vigenere Cipher
    vig = get_cipher("vigenere")
    msg7 = "Meet me at the secret rendezvous!"
    enc7 = vig.encrypt(msg7, "LEMON")
    dec7 = vig.decrypt(enc7, "LEMON")
    assert dec7 == msg7, f"Vigenere failed: {dec7} != {msg7}"
    print("  [PASS] Vigenere Cipher passed round-trip.")

    # 8. Autokey Cipher
    auto = get_cipher("autokey")
    msg8 = "Meet me at the library tonight!"
    enc8 = auto.encrypt(msg8, "QUEEN")
    dec8 = auto.decrypt(enc8, "QUEEN")
    assert dec8 == msg8, f"Autokey failed: {dec8} != {msg8}"
    print("  [PASS] Autokey Cipher passed round-trip.")

    # 9. Vernam Cipher (XOR / OTP)
    vernam = get_cipher("vernam")
    msg9 = "Confidential Data 999"
    enc9 = vernam.encrypt(msg9, "ONE_TIME_PAD_SECRET")
    dec9 = vernam.decrypt(enc9, "ONE_TIME_PAD_SECRET")
    assert dec9 == msg9, f"Vernam failed: {dec9} != {msg9}"
    print("  [PASS] Vernam (XOR) Cipher passed round-trip.")

    # 10. Rail Fence Cipher
    rail = get_cipher("rail_fence")
    msg10 = "DEFEND THE EAST WALL"
    enc10 = rail.encrypt(msg10, "3")
    dec10 = rail.decrypt(enc10, "3")
    assert dec10 == msg10, f"Rail Fence failed: {dec10} != {msg10}"
    print("  [PASS] Rail Fence Cipher passed round-trip.")

    # 11. Single Columnar Transposition
    single = get_cipher("single_columnar")
    msg11 = "DEFEND THE EAST WALL OF THE FORTRESS"
    enc11 = single.encrypt(msg11, "ZEBRA")
    dec11 = single.decrypt(enc11, "ZEBRA")
    assert dec11 == msg11, f"Single Columnar failed: {dec11} != {msg11}"
    print("  [PASS] Single Columnar Transposition passed round-trip.")

    # 12. Double Columnar Transposition
    double = get_cipher("double_columnar")
    msg12 = "MISSION ACCOMPLISHED AT TWILIGHT"
    enc12 = double.encrypt(msg12, "ZEBRA, COBRA")
    dec12 = double.decrypt(enc12, "ZEBRA, COBRA")
    assert dec12 == msg12, f"Double Columnar failed: {dec12} != {msg12}"
    print("  [PASS] Double Columnar Transposition passed round-trip.")

    # 13. RSA Asymmetric Cipher & Key Generator
    rsa = get_cipher("rsa")
    keys = rsa.generate_keys()
    print(f"  [PASS] RSA Generated Keys: e={keys['e']}, d={keys['d']}, n={keys['n']}")
    msg13 = "Hello RSA!"
    enc13 = rsa.encrypt(msg13, keys["public_key"])
    dec13 = rsa.decrypt(enc13, keys["private_key"])
    assert dec13 == msg13, f"RSA failed: {dec13} != {msg13}"
    print("  [PASS] RSA Asymmetric Cipher passed round-trip.")

    print("\n[3] Testing Error Handling:")
    # Multiplicative with non-coprime key
    try:
        mult.encrypt("Test", "4")  # 4 is not coprime to 26
        assert False, "Should have raised ValueError for non-coprime key"
    except ValueError as e:
        print(f"  [PASS] Multiplicative validation caught: {e}")

    # Hill with non-invertible matrix
    try:
        hill.encrypt("Test", "2 4 4 8")  # det = 2*8 - 4*4 = 0
        assert False, "Should have raised ValueError for non-invertible matrix"
    except ValueError as e:
        print(f"  [PASS] Hill non-invertible validation caught: {e}")

    # Double columnar with single key
    try:
        double.encrypt("Test", "SOLOKEY")
        assert False, "Should have raised ValueError for single key"
    except ValueError as e:
        print(f"  [PASS] Double Columnar validation caught: {e}")

    print("\n[4] Testing History Manager:")
    hm = HistoryManager()
    hm.add_entry("Caesar", "ENCRYPT", "3", "HELLO", "KHOOR")
    hm.add_entry("Caesar", "DECRYPT", "3", "KHOOR", "HELLO")
    assert len(hm.get_all()) == 2
    test_export = os.path.join(os.path.dirname(__file__), "test_history_export.txt")
    hm.export_to_txt(test_export)
    assert os.path.exists(test_export)
    with open(test_export, "r", encoding="utf-8") as f:
        content = f.read()
    assert "CIPHERFORGE - OPERATION HISTORY" in content
    os.remove(test_export)
    hm.clear()
    assert hm.is_empty()
    print("  [PASS] History Manager add, export, and clear operations verified.")

    print("\n" + "=" * 65)
    print("    ALL 13 CIPHERS AND MODULES PASSED VERIFICATION CLEANLY!    ")
    print("=" * 65)


if __name__ == "__main__":
    run_tests()
