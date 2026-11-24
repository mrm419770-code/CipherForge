"""
History Manager Module
Tracks encryption and decryption operations with timestamps, algorithm names,
modes, keys, and inputs/outputs. Supports clearing and exporting to .txt files.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class HistoryEntry:
    timestamp: str
    cipher_name: str
    mode: str  # "ENCRYPT" or "DECRYPT"
    key: str
    input_text: str
    output_text: str

    def to_formatted_block(self) -> str:
        border = "=" * 60
        return (
            f"{border}\n"
            f"Timestamp : {self.timestamp}\n"
            f"Algorithm : {self.cipher_name}\n"
            f"Operation : {self.mode}\n"
            f"Key       : {self.key}\n"
            f"Input     : {self.input_text}\n"
            f"Output    : {self.output_text}\n"
        )


class HistoryManager:
    """Manages an in-memory audit log of cryptographic operations."""

    def __init__(self):
        self._entries: List[HistoryEntry] = []

    def add_entry(
        self,
        cipher_name: str,
        mode: str,
        key: str,
        input_text: str,
        output_text: str,
    ) -> HistoryEntry:
        """Records a new cryptographic operation."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = HistoryEntry(
            timestamp=now,
            cipher_name=cipher_name,
            mode=mode.upper(),
            key=key,
            input_text=input_text,
            output_text=output_text,
        )
        self._entries.append(entry)
        return entry

    def get_all(self) -> List[HistoryEntry]:
        """Returns a copy of all recorded history entries."""
        return list(self._entries)

    def clear(self) -> None:
        """Clears all history entries."""
        self._entries.clear()

    def is_empty(self) -> bool:
        """Checks if the history log is empty."""
        return len(self._entries) == 0

    def to_formatted_text(self) -> str:
        """Renders all history entries into a human-readable text document."""
        if not self._entries:
            return "No cryptographic operations recorded yet."

        header = (
            "============================================================\n"
            "              CIPHERFORGE - OPERATION HISTORY               \n"
            "============================================================\n\n"
        )
        blocks = [entry.to_formatted_block() for entry in self._entries]
        return header + "\n".join(blocks)

    def export_to_txt(self, filepath: str) -> None:
        """Exports the formatted history log to a specified .txt file path."""
        content = self.to_formatted_text()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
