"""
CipherForge Root Runner
Convenience launcher to run CipherForge directly from the workspace root.
"""

import os
import sys

# Add inner CipherForge directory to sys.path
PROJECT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "CipherForge")
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from main import main

if __name__ == "__main__":
    main()
