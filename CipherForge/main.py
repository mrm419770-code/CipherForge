"""
CipherForge - Classical & Modern Cryptography Suite
GUI application built using CustomTkinter with dynamic multi-theme support.
"""

import os
import sys
from tkinter import filedialog, messagebox
from typing import Dict, Optional

# Ensure workspace / package directory is on sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

import customtkinter as ctk

from ciphers import CIPHER_LIST, CIPHERS, get_cipher
from ciphers.base import BaseCipher
from ciphers.rsa import RSACipher, generate_rsa_keys
from history_manager import HistoryManager
from themes import DARK_THEME, THEME_MAP, THEME_NAMES, ThemePalette, get_theme


class RSAKeyDialog(ctk.CTkToplevel):
    """Dialog window displaying generated RSA parameters with 1-click loading."""

    def __init__(self, parent, theme: ThemePalette, on_select_key):
        super().__init__(parent)
        self.title("CipherForge - RSA Key Generator")
        self.geometry("560x520")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        self.theme = theme
        self.on_select_key = on_select_key
        self.keys_data: Dict[str, str] = {}

        self.configure(fg_color=self.theme.window_bg)
        self._build_ui()
        self._generate_new_keys()

    def _build_ui(self):
        self.grid_columnconfigure(0, weight=1)

        self.title_lbl = ctk.CTkLabel(
            self,
            text="🔑 Generated RSA Key Pair",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.theme.text_primary,
        )
        self.title_lbl.pack(pady=(15, 4))

        self.subtitle_lbl = ctk.CTkLabel(
            self,
            text="Keys generated from first principles without external crypto libraries.",
            font=ctk.CTkFont(size=12),
            text_color=self.theme.text_secondary,
        )
        self.subtitle_lbl.pack(pady=(0, 10))

        self.details_box = ctk.CTkTextbox(
            self,
            width=510,
            height=280,
            font=ctk.CTkFont(family="Consolas", size=12),
            fg_color=self.theme.input_bg,
            text_color=self.theme.input_text,
            border_color=self.theme.input_border,
            border_width=1,
        )
        self.details_box.pack(padx=20, pady=5)

        btn_frame1 = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame1.pack(pady=(8, 4))

        self.btn_use_pub = ctk.CTkButton(
            btn_frame1,
            text="Use Public Key (Encrypt)",
            command=self._use_public_key,
            fg_color=self.theme.btn_rsa_bg,
            hover_color=self.theme.btn_rsa_hover,
            text_color=self.theme.btn_rsa_text,
            font=ctk.CTkFont(weight="bold"),
            width=180,
        )
        self.btn_use_pub.pack(side="left", padx=6)

        self.btn_use_priv = ctk.CTkButton(
            btn_frame1,
            text="Use Private Key (Decrypt)",
            command=self._use_private_key,
            fg_color=self.theme.btn_decrypt_bg,
            hover_color=self.theme.btn_decrypt_hover,
            text_color=self.theme.btn_decrypt_text,
            font=ctk.CTkFont(weight="bold"),
            width=180,
        )
        self.btn_use_priv.pack(side="left", padx=6)

        btn_frame2 = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame2.pack(pady=(4, 10))

        self.btn_regen = ctk.CTkButton(
            btn_frame2,
            text="🔄 Generate New Pair",
            command=self._generate_new_keys,
            width=160,
            fg_color=self.theme.btn_utility_bg,
            hover_color=self.theme.btn_utility_hover,
            text_color=self.theme.btn_utility_text,
        )
        self.btn_regen.pack(side="left", padx=5)

        self.btn_close = ctk.CTkButton(
            btn_frame2,
            text="Close",
            command=self.destroy,
            width=100,
            fg_color=self.theme.btn_neutral_bg,
            hover_color=self.theme.btn_neutral_hover,
            text_color=self.theme.btn_neutral_text,
        )
        self.btn_close.pack(side="left", padx=5)

    def _generate_new_keys(self):
        self.keys_data = generate_rsa_keys()
        text = (
            f"Prime p:          {self.keys_data['p']}\n"
            f"Prime q:          {self.keys_data['q']}\n"
            f"Modulus n:        {self.keys_data['n']}\n"
            f"Euler's Phi:      {self.keys_data['phi']}\n"
            f"Public Exp (e):   {self.keys_data['e']}\n"
            f"Private Exp (d):  {self.keys_data['d']}\n\n"
            f"--- Ready-to-Use Key Formats ---\n"
            f"Public Key (e, n):   {self.keys_data['public_key']}\n"
            f"Private Key (d, n):  {self.keys_data['private_key']}\n"
        )
        self.details_box.configure(state="normal")
        self.details_box.delete("1.0", "end")
        self.details_box.insert("1.0", text)
        self.details_box.configure(state="disabled")

    def _use_public_key(self):
        if "public_key" in self.keys_data:
            self.on_select_key(self.keys_data["public_key"])
            self.destroy()

    def _use_private_key(self):
        if "private_key" in self.keys_data:
            self.on_select_key(self.keys_data["private_key"])
            self.destroy()


class CipherForgeApp(ctk.CTk):
    """Main Application Window for CipherForge with Dynamic Theme Engine."""

    def __init__(self):
        super().__init__()
        self.title("CipherForge - Classical & Modern Cryptography Suite")
        self.geometry("1180x820")
        self.minsize(980, 700)

        self.current_theme: ThemePalette = DARK_THEME
        ctk.set_appearance_mode(self.current_theme.appearance_mode)
        ctk.set_default_color_theme("blue")

        self.history_mgr = HistoryManager()
        self.current_cipher: BaseCipher = CIPHER_LIST[0] if CIPHER_LIST else None
        self.sidebar_buttons: Dict[str, ctk.CTkButton] = {}

        self._build_layout()
        self._apply_theme(self.current_theme.id)
        if self.current_cipher:
            self._select_cipher(self.current_cipher.id)

    def _build_layout(self):
        # Grid setup: sidebar (col 0), content (col 1)
        self.grid_columnconfigure(0, weight=0, minsize=260)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # -----------------------------
        # 1. SIDEBAR
        # -----------------------------
        self.sidebar_frame = ctk.CTkFrame(self, width=260, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(2, weight=1)

        # Brand header
        self.brand_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="⚡ CipherForge",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.brand_label.grid(row=0, column=0, padx=20, pady=(20, 2), sticky="w")

        self.brand_sub = ctk.CTkLabel(
            self.sidebar_frame,
            text="Cryptography Suite & Solvers",
            font=ctk.CTkFont(size=12),
        )
        self.brand_sub.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="w")

        # Scrollable cipher list
        self.ciphers_scroll = ctk.CTkScrollableFrame(self.sidebar_frame, label_text="Algorithms")
        self.ciphers_scroll.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

        for cipher in CIPHER_LIST:
            btn = ctk.CTkButton(
                self.ciphers_scroll,
                text=cipher.name,
                anchor="w",
                font=ctk.CTkFont(size=13),
                fg_color="transparent",
                command=lambda cid=cipher.id: self._select_cipher(cid),
            )
            btn.pack(fill="x", padx=5, pady=2)
            self.sidebar_buttons[cipher.id] = btn

        # Theme selector container
        self.theme_frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.theme_frame.grid(row=3, column=0, padx=15, pady=(10, 15), sticky="ew")

        self.theme_lbl = ctk.CTkLabel(
            self.theme_frame,
            text="Theme / Color Mode:",
            font=ctk.CTkFont(size=11, weight="bold"),
            anchor="w",
        )
        self.theme_lbl.pack(fill="x", pady=(0, 4))

        self.theme_selector = ctk.CTkOptionMenu(
            self.theme_frame,
            values=THEME_NAMES,
            command=self._on_theme_changed,
            font=ctk.CTkFont(size=12, weight="bold"),
            dropdown_font=ctk.CTkFont(size=12),
        )
        self.theme_selector.set(self.current_theme.id)
        self.theme_selector.pack(fill="x")

        # -----------------------------
        # 2. MAIN CONTENT AREA
        # -----------------------------
        self.content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=15)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(3, weight=1)

        # Header: Selected Cipher info
        header_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        self.lbl_cipher_title = ctk.CTkLabel(
            header_frame,
            text="Cipher Name",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self.lbl_cipher_title.pack(side="left", padx=(0, 10))

        self.lbl_cipher_category = ctk.CTkLabel(
            header_frame,
            text="Category",
            font=ctk.CTkFont(size=12, weight="bold"),
            corner_radius=6,
            padx=10,
            pady=3,
        )
        self.lbl_cipher_category.pack(side="left")

        # Key Input Section
        self.key_frame = ctk.CTkFrame(self.content_frame, border_width=1)
        self.key_frame.grid(row=1, column=0, sticky="ew", pady=5)
        self.key_frame.grid_columnconfigure(1, weight=1)

        self.lbl_key = ctk.CTkLabel(self.key_frame, text="Secret Key:", font=ctk.CTkFont(weight="bold"))
        self.lbl_key.grid(row=0, column=0, padx=12, pady=(10, 2), sticky="w")

        self.entry_key = ctk.CTkEntry(self.key_frame, placeholder_text="Enter secret key...", border_width=1)
        self.entry_key.grid(row=0, column=1, padx=(0, 10), pady=(10, 2), sticky="ew")

        self.btn_rsa_gen = ctk.CTkButton(
            self.key_frame,
            text="🔑 Generate RSA Keys",
            width=160,
            command=self._open_rsa_generator,
            font=ctk.CTkFont(weight="bold"),
        )
        self.btn_rsa_gen.grid(row=0, column=2, padx=(0, 12), pady=(10, 2), sticky="e")

        self.lbl_key_hint = ctk.CTkLabel(
            self.key_frame,
            text="Key format hint goes here.",
            font=ctk.CTkFont(size=11),
        )
        self.lbl_key_hint.grid(row=1, column=1, padx=(0, 10), pady=(0, 8), sticky="w")

        # Input Text Section
        self.input_container = ctk.CTkFrame(self.content_frame, border_width=1)
        self.input_container.grid(row=2, column=0, sticky="ew", pady=5)
        self.input_container.grid_columnconfigure(0, weight=1)

        input_header = ctk.CTkFrame(self.input_container, fg_color="transparent")
        input_header.pack(fill="x", padx=12, pady=(8, 2))

        self.lbl_input = ctk.CTkLabel(input_header, text="Input Text (Plaintext or Ciphertext):", font=ctk.CTkFont(weight="bold"))
        self.lbl_input.pack(side="left")

        self.txt_input = ctk.CTkTextbox(
            self.input_container,
            height=90,
            font=ctk.CTkFont(family="Consolas", size=13),
            border_width=1,
        )
        self.txt_input.pack(fill="x", padx=12, pady=5)

        # Operations row
        ops_frame = ctk.CTkFrame(self.input_container, fg_color="transparent")
        ops_frame.pack(fill="x", padx=12, pady=(4, 10))

        self.btn_encrypt = ctk.CTkButton(
            ops_frame,
            text="🔒 Encrypt",
            command=self._on_encrypt,
            font=ctk.CTkFont(weight="bold"),
            width=125,
        )
        self.btn_encrypt.pack(side="left", padx=(0, 10))

        self.btn_decrypt = ctk.CTkButton(
            ops_frame,
            text="🔓 Decrypt",
            command=self._on_decrypt,
            font=ctk.CTkFont(weight="bold"),
            width=125,
        )
        self.btn_decrypt.pack(side="left", padx=(0, 10))

        self.btn_swap = ctk.CTkButton(
            ops_frame,
            text="🔄 Swap In/Out",
            command=self._swap_input_output,
            font=ctk.CTkFont(weight="bold"),
            width=125,
        )
        self.btn_swap.pack(side="left", padx=(0, 10))

        self.btn_clear_input = ctk.CTkButton(
            ops_frame,
            text="🧹 Clear Input",
            command=self._clear_input,
            width=105,
        )
        self.btn_clear_input.pack(side="right")

        # Tabs Section (Output & History vs Overview & How to Solve)
        self.tabview = ctk.CTkTabview(self.content_frame)
        self.tabview.grid(row=3, column=0, sticky="nsew", pady=(5, 0))

        self.tab_output = self.tabview.add("Output & History")
        self.tab_info = self.tabview.add("Overview & How to Solve")

        self._build_tab_output()
        self._build_tab_info()

        # Status notification banner at bottom
        self.lbl_status = ctk.CTkLabel(
            self.content_frame,
            text="Ready.",
            font=ctk.CTkFont(size=12),
            anchor="w",
        )
        self.lbl_status.grid(row=4, column=0, sticky="ew", pady=(5, 0))

    def _build_tab_output(self):
        self.tab_output.grid_columnconfigure(0, weight=1)
        self.tab_output.grid_columnconfigure(1, weight=1)
        self.tab_output.grid_rowconfigure(1, weight=1)

        # Output column (left)
        out_header = ctk.CTkFrame(self.tab_output, fg_color="transparent")
        out_header.grid(row=0, column=0, sticky="ew", padx=5, pady=(5, 2))

        self.lbl_out = ctk.CTkLabel(out_header, text="Operation Result:", font=ctk.CTkFont(weight="bold"))
        self.lbl_out.pack(side="left")

        self.btn_copy = ctk.CTkButton(
            out_header,
            text="📋 Copy Output",
            command=self._copy_output,
            width=115,
            height=26,
            font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.btn_copy.pack(side="right")

        self.txt_output = ctk.CTkTextbox(
            self.tab_output,
            font=ctk.CTkFont(family="Consolas", size=13),
            border_width=1,
        )
        self.txt_output.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        # History column (right)
        hist_header = ctk.CTkFrame(self.tab_output, fg_color="transparent")
        hist_header.grid(row=0, column=1, sticky="ew", padx=5, pady=(5, 2))

        self.lbl_hist = ctk.CTkLabel(hist_header, text="Operation History:", font=ctk.CTkFont(weight="bold"))
        self.lbl_hist.pack(side="left")

        self.btn_save_hist = ctk.CTkButton(
            hist_header,
            text="💾 Save (.txt)",
            command=self._save_history,
            width=95,
            height=26,
            font=ctk.CTkFont(size=12, weight="bold"),
        )
        self.btn_save_hist.pack(side="right", padx=(5, 0))

        self.btn_clear_hist = ctk.CTkButton(
            hist_header,
            text="🗑️ Clear",
            command=self._clear_history,
            width=75,
            height=26,
            font=ctk.CTkFont(size=12),
        )
        self.btn_clear_hist.pack(side="right")

        self.txt_history = ctk.CTkTextbox(
            self.tab_output,
            font=ctk.CTkFont(family="Consolas", size=11),
            border_width=1,
        )
        self.txt_history.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self._refresh_history_view()

    def _build_tab_info(self):
        self.tab_info.grid_columnconfigure(0, weight=1)
        self.tab_info.grid_rowconfigure(0, weight=1)

        self.txt_info = ctk.CTkTextbox(
            self.tab_info,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            wrap="word",
            border_width=1,
        )
        self.txt_info.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def _apply_theme(self, theme_name: str):
        """Dynamically applies the chosen theme palette across all window components."""
        theme = get_theme(theme_name)
        self.current_theme = theme
        ctk.set_appearance_mode(theme.appearance_mode)

        # 1. Main Window & Top Container
        self.configure(fg_color=theme.window_bg)

        # 2. Sidebar & Navigation
        self.sidebar_frame.configure(fg_color=theme.sidebar_bg)
        self.brand_label.configure(text_color=theme.text_primary)
        self.brand_sub.configure(text_color=theme.text_secondary)
        self.ciphers_scroll.configure(
            fg_color=theme.scroll_bg,
            label_text_color=theme.text_secondary,
        )
        self.theme_lbl.configure(text_color=theme.text_secondary)
        self.theme_selector.configure(
            fg_color=theme.btn_neutral_bg,
            button_color=theme.btn_rsa_bg,
            button_hover_color=theme.btn_rsa_hover,
            text_color=theme.text_primary,
            dropdown_fg_color=theme.card_bg,
            dropdown_text_color=theme.text_primary,
            dropdown_hover_color=theme.sidebar_btn_hover,
        )
        self.theme_selector.set(theme.id)

        # Update sidebar buttons
        current_id = self.current_cipher.id if self.current_cipher else None
        for cid, btn in self.sidebar_buttons.items():
            if cid == current_id:
                btn.configure(
                    fg_color=theme.sidebar_btn_active_bg,
                    text_color=theme.sidebar_btn_active_text,
                    hover_color=theme.btn_encrypt_hover,
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=theme.sidebar_btn_inactive_text,
                    hover_color=theme.sidebar_btn_hover,
                )

        # 3. Header
        self.lbl_cipher_title.configure(text_color=theme.text_primary)
        self.lbl_cipher_category.configure(
            fg_color=theme.badge_bg,
            text_color=theme.badge_text,
        )

        # 4. Key Input Section
        self.key_frame.configure(
            fg_color=theme.card_bg,
            border_color=theme.card_border,
        )
        self.lbl_key.configure(text_color=theme.text_primary)
        self.entry_key.configure(
            fg_color=theme.input_bg,
            text_color=theme.input_text,
            border_color=theme.input_border,
        )
        self.btn_rsa_gen.configure(
            fg_color=theme.btn_rsa_bg,
            hover_color=theme.btn_rsa_hover,
            text_color=theme.btn_rsa_text,
        )
        self.lbl_key_hint.configure(text_color=theme.text_muted)

        # 5. Input Container & Action Buttons
        self.input_container.configure(
            fg_color=theme.card_bg,
            border_color=theme.card_border,
        )
        self.lbl_input.configure(text_color=theme.text_primary)
        self.txt_input.configure(
            fg_color=theme.input_bg,
            text_color=theme.input_text,
            border_color=theme.input_border,
        )
        self.btn_encrypt.configure(
            fg_color=theme.btn_encrypt_bg,
            hover_color=theme.btn_encrypt_hover,
            text_color=theme.btn_encrypt_text,
        )
        self.btn_decrypt.configure(
            fg_color=theme.btn_decrypt_bg,
            hover_color=theme.btn_decrypt_hover,
            text_color=theme.btn_decrypt_text,
        )
        self.btn_swap.configure(
            fg_color=theme.btn_utility_bg,
            hover_color=theme.btn_utility_hover,
            text_color=theme.btn_utility_text,
        )
        self.btn_clear_input.configure(
            fg_color=theme.btn_neutral_bg,
            hover_color=theme.btn_neutral_hover,
            text_color=theme.btn_neutral_text,
        )

        # 6. Tabview
        self.tabview.configure(
            fg_color=theme.card_bg,
            segmented_button_fg_color=theme.sidebar_bg,
            segmented_button_selected_color=theme.tab_btn_selected,
            segmented_button_selected_hover_color=theme.tab_btn_hover,
            text_color=theme.tab_text,
        )

        # 7. Output & History Widgets
        self.lbl_out.configure(text_color=theme.text_primary)
        self.btn_copy.configure(
            fg_color=theme.btn_utility_bg,
            hover_color=theme.btn_utility_hover,
            text_color=theme.btn_utility_text,
        )
        out_content = self.txt_output.get("1.0", "end-1c")
        is_err = out_content.startswith("Encryption Error:") or out_content.startswith("Decryption Error:")
        self.txt_output.configure(
            fg_color=theme.input_bg,
            text_color="#ef4444" if is_err else theme.input_text,
            border_color=theme.input_border,
        )

        self.lbl_hist.configure(text_color=theme.text_primary)
        self.btn_save_hist.configure(
            fg_color=theme.btn_utility_bg,
            hover_color=theme.btn_utility_hover,
            text_color=theme.btn_utility_text,
        )
        self.btn_clear_hist.configure(
            fg_color=theme.btn_neutral_bg,
            hover_color=theme.btn_neutral_hover,
            text_color=theme.btn_neutral_text,
        )
        self.txt_history.configure(
            fg_color=theme.input_bg,
            text_color=theme.input_text,
            border_color=theme.input_border,
        )

        # 8. Info Tab
        self.txt_info.configure(
            fg_color=theme.input_bg,
            text_color=theme.input_text,
            border_color=theme.input_border,
        )

        # 9. Status Banner
        self.lbl_status.configure(text_color=theme.text_muted)

    def _on_theme_changed(self, theme_name: str):
        self._apply_theme(theme_name)
        self._set_status(f"Theme switched to: {theme_name}")

    def _select_cipher(self, cipher_id: str):
        cipher = get_cipher(cipher_id)
        if not cipher:
            return

        self.current_cipher = cipher

        # Update sidebar active button colors based on active theme
        for cid, btn in self.sidebar_buttons.items():
            if cid == cipher_id:
                btn.configure(
                    fg_color=self.current_theme.sidebar_btn_active_bg,
                    text_color=self.current_theme.sidebar_btn_active_text,
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=self.current_theme.sidebar_btn_inactive_text,
                )

        # Update header and hints
        self.lbl_cipher_title.configure(text=cipher.name)
        self.lbl_cipher_category.configure(text=cipher.category)
        self.lbl_key_hint.configure(text=f"Hint: {cipher.key_hint}")

        # Show RSA Key Generator button only when RSA is active
        if cipher.id == "rsa":
            self.btn_rsa_gen.grid()
        else:
            self.btn_rsa_gen.grid_remove()

        # Update Overview & How to Solve tab
        self._refresh_info_tab()
        self._set_status(f"Selected: {cipher.name}")

    def _refresh_info_tab(self):
        if not self.current_cipher:
            return

        content = (
            f"=== {self.current_cipher.name.upper()} ===\n"
            f"Category: {self.current_cipher.category}\n\n"
            f"--- ALGORITHM OVERVIEW ---\n"
            f"{self.current_cipher.overview}\n\n"
            f"--- KEY REQUIREMENTS ---\n"
            f"{self.current_cipher.key_hint}\n\n"
            f"--- HOW TO SOLVE & MATHEMATICAL GUIDE ---\n"
            f"{self.current_cipher.how_to_solve}\n"
        )
        self.txt_info.configure(state="normal")
        self.txt_info.delete("1.0", "end")
        self.txt_info.insert("1.0", content)
        self.txt_info.configure(state="disabled")

    def _on_encrypt(self):
        if not self.current_cipher:
            return

        text = self.txt_input.get("1.0", "end-1c")
        key = self.entry_key.get()

        try:
            output = self.current_cipher.encrypt(text, key)
            self._set_output(output)
            self.history_mgr.add_entry(
                cipher_name=self.current_cipher.name,
                mode="ENCRYPT",
                key=key,
                input_text=text,
                output_text=output,
            )
            self._refresh_history_view()
            self._set_status(f"Encryption successful using {self.current_cipher.name}.")
        except Exception as ex:
            err_msg = f"Encryption Error: {str(ex)}"
            self._set_output(err_msg, is_error=True)
            self._set_status(err_msg, is_error=True)

    def _on_decrypt(self):
        if not self.current_cipher:
            return

        text = self.txt_input.get("1.0", "end-1c")
        key = self.entry_key.get()

        try:
            output = self.current_cipher.decrypt(text, key)
            self._set_output(output)
            self.history_mgr.add_entry(
                cipher_name=self.current_cipher.name,
                mode="DECRYPT",
                key=key,
                input_text=text,
                output_text=output,
            )
            self._refresh_history_view()
            self._set_status(f"Decryption successful using {self.current_cipher.name}.")
        except Exception as ex:
            err_msg = f"Decryption Error: {str(ex)}"
            self._set_output(err_msg, is_error=True)
            self._set_status(err_msg, is_error=True)

    def _set_output(self, text: str, is_error: bool = False):
        self.txt_output.configure(state="normal")
        self.txt_output.delete("1.0", "end")
        self.txt_output.insert("1.0", text)
        self.txt_output.configure(
            text_color="#ef4444" if is_error else self.current_theme.input_text
        )

    def _set_status(self, text: str, is_error: bool = False):
        self.lbl_status.configure(
            text=text,
            text_color="#ef4444" if is_error else self.current_theme.text_muted,
        )

    def _swap_input_output(self):
        out_text = self.txt_output.get("1.0", "end-1c")
        if not out_text or out_text.startswith("Encryption Error:") or out_text.startswith("Decryption Error:"):
            return

        self.txt_input.delete("1.0", "end")
        self.txt_input.insert("1.0", out_text)
        self._set_output("")
        self._set_status("Output swapped into Input box.")

    def _clear_input(self):
        self.txt_input.delete("1.0", "end")
        self._set_status("Input cleared.")

    def _copy_output(self):
        output = self.txt_output.get("1.0", "end-1c")
        if output:
            self.clipboard_clear()
            self.clipboard_append(output)
            self._set_status("Output copied to clipboard.")
        else:
            self._set_status("Nothing to copy.")

    def _refresh_history_view(self):
        content = self.history_mgr.to_formatted_text()
        self.txt_history.configure(state="normal")
        self.txt_history.delete("1.0", "end")
        self.txt_history.insert("1.0", content)
        self.txt_history.configure(state="disabled")

    def _clear_history(self):
        if self.history_mgr.is_empty():
            self._set_status("History is already empty.")
            return

        if messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all operation history?"):
            self.history_mgr.clear()
            self._refresh_history_view()
            self._set_status("Operation history cleared.")

    def _save_history(self):
        if self.history_mgr.is_empty():
            messagebox.showinfo("Export History", "No history entries to export.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files (*.txt)", "*.txt"), ("All Files (*.*)", "*.*")],
            title="Save History Log",
            initialfile="cipherforge_history.txt",
        )
        if file_path:
            try:
                self.history_mgr.export_to_txt(file_path)
                messagebox.showinfo("Export Successful", f"History saved successfully to:\n{file_path}")
                self._set_status(f"History exported to {os.path.basename(file_path)}")
            except Exception as ex:
                messagebox.showerror("Export Failed", f"Failed to save history: {ex}")
                self._set_status("Failed to save history.", is_error=True)

    def _open_rsa_generator(self):
        def on_key_selected(key_str: str):
            self.entry_key.delete(0, "end")
            self.entry_key.insert(0, key_str)
            self._set_status(f"RSA key loaded into key field: {key_str}")

        RSAKeyDialog(self, theme=self.current_theme, on_select_key=on_key_selected)


def main():
    app = CipherForgeApp()
    app.mainloop()


if __name__ == "__main__":
    main()
