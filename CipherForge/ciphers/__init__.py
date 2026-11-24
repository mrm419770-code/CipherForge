"""
Ciphers Package
Dynamically auto-discovers and registers every cipher module in this directory.
"""

import importlib
import inspect
import os
import pkgutil
from typing import Dict, List, Optional, Type
from ciphers.base import BaseCipher

# Preferred standard ordering of ciphers for navigation
CIPHER_ORDER = [
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


def load_ciphers() -> Dict[str, BaseCipher]:
    """
    Dynamically scans the ciphers directory, imports all cipher modules,
    and returns a dictionary mapping cipher IDs to instantiated BaseCipher objects.
    """
    ciphers: Dict[str, BaseCipher] = {}
    pkg_dir = os.path.dirname(__file__)

    for module_info in pkgutil.iter_modules([pkg_dir]):
        mod_name = module_info.name
        if mod_name in ("base", "__init__"):
            continue

        full_module_name = f"ciphers.{mod_name}"
        try:
            module = importlib.import_module(full_module_name)
        except Exception as err:
            print(f"[Warning] Failed to import cipher module {full_module_name}: {err}")
            continue

        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (
                inspect.isclass(attr)
                and issubclass(attr, BaseCipher)
                and attr is not BaseCipher
            ):
                try:
                    instance: BaseCipher = attr()
                    ciphers[instance.id] = instance
                except Exception as err:
                    print(f"[Warning] Failed to instantiate {attr_name}: {err}")

    # Reorder according to preferred CIPHER_ORDER where possible
    ordered_ciphers: Dict[str, BaseCipher] = {}
    for cid in CIPHER_ORDER:
        if cid in ciphers:
            ordered_ciphers[cid] = ciphers[cid]

    # Include any dynamically discovered ciphers not explicitly in CIPHER_ORDER
    for cid, cipher in ciphers.items():
        if cid not in ordered_ciphers:
            ordered_ciphers[cid] = cipher

    return ordered_ciphers


# Pre-loaded registry
CIPHERS: Dict[str, BaseCipher] = load_ciphers()
CIPHER_LIST: List[BaseCipher] = list(CIPHERS.values())


def get_cipher(cipher_id: str) -> Optional[BaseCipher]:
    """Retrieves a loaded cipher instance by its ID."""
    return CIPHERS.get(cipher_id)
