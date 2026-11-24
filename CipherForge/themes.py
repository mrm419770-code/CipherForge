"""
Themes Module for CipherForge
Defines cohesive, accessible color palettes for Dark, Light, and Red-Orange-Blue
(Sunset Blaze / Cyber Flame) visual modes.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class ThemePalette:
    """Defines color styling specifications for all UI components."""

    id: str
    name: str
    appearance_mode: str  # "Dark" or "Light" (CustomTkinter core mode)

    # Window & Containers
    window_bg: str
    sidebar_bg: str
    card_bg: str
    card_border: str
    scroll_bg: str

    # Typography
    text_primary: str
    text_secondary: str
    text_muted: str

    # Primary Action (Encrypt / High-emphasis)
    btn_encrypt_bg: str
    btn_encrypt_hover: str
    btn_encrypt_text: str

    # Secondary Action (Decrypt / Medium-emphasis)
    btn_decrypt_bg: str
    btn_decrypt_hover: str
    btn_decrypt_text: str

    # Tertiary / Accent Action (RSA Generator / Highlight)
    btn_rsa_bg: str
    btn_rsa_hover: str
    btn_rsa_text: str

    # Functional Utilities (Swap / Copy / Save History)
    btn_utility_bg: str
    btn_utility_hover: str
    btn_utility_text: str

    # Neutral Controls (Clear Buttons)
    btn_neutral_bg: str
    btn_neutral_hover: str
    btn_neutral_text: str

    # Sidebar Navigation Buttons
    sidebar_btn_active_bg: str
    sidebar_btn_active_text: str
    sidebar_btn_inactive_text: str
    sidebar_btn_hover: str

    # Text Inputs & Outputs
    input_bg: str
    input_text: str
    input_border: str

    # Tabview Styling
    tab_bg: str
    tab_btn_selected: str
    tab_btn_hover: str
    tab_text: str

    # Category Badge
    badge_bg: str
    badge_text: str


# 1. Sleek Modern Dark Palette
DARK_THEME = ThemePalette(
    id="Dark",
    name="Dark",
    appearance_mode="Dark",
    window_bg="#121212",
    sidebar_bg="#1e1e1e",
    card_bg="#252525",
    card_border="#383838",
    scroll_bg="#181818",
    text_primary="#ffffff",
    text_secondary="#b0b0b0",
    text_muted="#757575",
    btn_encrypt_bg="#1f538d",
    btn_encrypt_hover="#14375e",
    btn_encrypt_text="#ffffff",
    btn_decrypt_bg="#2b7a4b",
    btn_decrypt_hover="#1d5232",
    btn_decrypt_text="#ffffff",
    btn_rsa_bg="#27568b",
    btn_rsa_hover="#193b61",
    btn_rsa_text="#ffffff",
    btn_utility_bg="#383838",
    btn_utility_hover="#484848",
    btn_utility_text="#ffffff",
    btn_neutral_bg="#424242",
    btn_neutral_hover="#525252",
    btn_neutral_text="#e0e0e0",
    sidebar_btn_active_bg="#1f538d",
    sidebar_btn_active_text="#ffffff",
    sidebar_btn_inactive_text="#b8b8b8",
    sidebar_btn_hover="#2c2c2c",
    input_bg="#181818",
    input_text="#f5f5f5",
    input_border="#3a3a3a",
    tab_bg="#252525",
    tab_btn_selected="#1f538d",
    tab_btn_hover="#14375e",
    tab_text="#ffffff",
    badge_bg="#333333",
    badge_text="#8ab4f8",
)

# 2. Crisp Accessible Light Palette
LIGHT_THEME = ThemePalette(
    id="Light",
    name="Light",
    appearance_mode="Light",
    window_bg="#f4f5f8",
    sidebar_bg="#eaecf2",
    card_bg="#ffffff",
    card_border="#d2d6e0",
    scroll_bg="#e2e5ee",
    text_primary="#1a1c23",
    text_secondary="#4b5563",
    text_muted="#6b7280",
    btn_encrypt_bg="#2563eb",
    btn_encrypt_hover="#1d4ed8",
    btn_encrypt_text="#ffffff",
    btn_decrypt_bg="#16a34a",
    btn_decrypt_hover="#15803d",
    btn_decrypt_text="#ffffff",
    btn_rsa_bg="#0284c7",
    btn_rsa_hover="#0369a1",
    btn_rsa_text="#ffffff",
    btn_utility_bg="#e2e8f0",
    btn_utility_hover="#cbd5e1",
    btn_utility_text="#1e293b",
    btn_neutral_bg="#e2e8f0",
    btn_neutral_hover="#cbd5e1",
    btn_neutral_text="#334155",
    sidebar_btn_active_bg="#2563eb",
    sidebar_btn_active_text="#ffffff",
    sidebar_btn_inactive_text="#374151",
    sidebar_btn_hover="#dbe0eb",
    input_bg="#ffffff",
    input_text="#111827",
    input_border="#cbd5e1",
    tab_bg="#ffffff",
    tab_btn_selected="#2563eb",
    tab_btn_hover="#1d4ed8",
    tab_text="#1f2937",
    badge_bg="#e0e7ff",
    badge_text="#3730a3",
)

# 3. Sunset Blaze / Cyber Flame Palette (Red, Orange, and Blue)
RED_ORANGE_BLUE_THEME = ThemePalette(
    id="Red-Orange-Blue",
    name="Red-Orange-Blue",
    appearance_mode="Dark",
    window_bg="#080e1e",          # Deep obsidian blue
    sidebar_bg="#0a1936",         # Midnight cobalt blue
    card_bg="#0e234c",            # Luminous navy blue card surface
    card_border="#1d3d75",        # Subtle indigo boundary
    scroll_bg="#07142d",          # Deep midnight scroll container
    text_primary="#ffffff",       # Crisp white typography
    text_secondary="#ff9e00",     # Radiant sunset orange
    text_muted="#70b8ff",         # Luminous electric cyan/sky
    btn_encrypt_bg="#d90429",     # Fiery Crimson RED primary action
    btn_encrypt_hover="#ef233c",  # Vivid red hover
    btn_encrypt_text="#ffffff",
    btn_decrypt_bg="#f77f00",     # Warm Sunset ORANGE secondary action
    btn_decrypt_hover="#ff9e00",  # Vivid amber hover
    btn_decrypt_text="#ffffff",
    btn_rsa_bg="#0077b6",         # Vibrant Cobalt/Ocean BLUE highlight
    btn_rsa_hover="#0096c7",      # Sky blue hover
    btn_rsa_text="#ffffff",
    btn_utility_bg="#1d3d75",     # Deep blue utility background
    btn_utility_hover="#27529b",  # Mid-blue utility hover
    btn_utility_text="#ffffff",
    btn_neutral_bg="#19335f",     # Deep navy neutral
    btn_neutral_hover="#244983",  # Navy hover
    btn_neutral_text="#e2e8f0",
    sidebar_btn_active_bg="#d90429",    # Red active marker in sidebar
    sidebar_btn_active_text="#ffffff",
    sidebar_btn_inactive_text="#90caf9", # Soft ice blue
    sidebar_btn_hover="#142c5b",
    input_bg="#061229",           # Dark navy text field
    input_text="#ffffff",
    input_border="#1e4585",
    tab_bg="#0e234c",
    tab_btn_selected="#d90429",   # Fiery red active tab
    tab_btn_hover="#ef233c",
    tab_text="#ffffff",
    badge_bg="#ff7b00",           # High-visibility orange badge
    badge_text="#071329",         # Deep navy text on orange
)

# Registry of available themes
THEME_MAP: Dict[str, ThemePalette] = {
    DARK_THEME.id: DARK_THEME,
    LIGHT_THEME.id: LIGHT_THEME,
    RED_ORANGE_BLUE_THEME.id: RED_ORANGE_BLUE_THEME,
}

THEME_NAMES: List[str] = list(THEME_MAP.keys())


def get_theme(theme_name: str) -> ThemePalette:
    """Returns the requested ThemePalette or defaults to DARK_THEME."""
    return THEME_MAP.get(theme_name, DARK_THEME)
