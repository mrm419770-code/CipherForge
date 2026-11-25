"""
Themes Module for CipherForge
Defines cohesive, accessible color palettes for:
1. Dark Mode (Sleek Modern Slate)
2. Light Mode (Crisp Accessible Light)
3. Red-Orange-Blue Mode (Sunset Blaze / Cyber Flame)
4. Nordic Obsidian (Sleek Dark Minimalist)
5. Royal Champagne (Warm Luxury Light)
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

# 4. Nordic Obsidian (Sleek Dark Minimalist)
NORDIC_OBSIDIAN_THEME = ThemePalette(
    id="Nordic Obsidian",
    name="Nordic Obsidian",
    appearance_mode="Dark",
    window_bg="#0d1117",          # Deepest obsidian charcoal
    sidebar_bg="#161b22",         # Nordic dark slate
    card_bg="#1c2128",            # Obsidian card surface
    card_border="#30363d",        # Crisp cool slate border
    scroll_bg="#13171f",          # Deep scroll canvas
    text_primary="#f0f6fc",       # Soft off-white / ice text
    text_secondary="#8b949e",     # Cool slate secondary
    text_muted="#6e7681",         # Muted steel
    btn_encrypt_bg="#0d9488",     # Muted cyan-teal primary action
    btn_encrypt_hover="#115e59",  # Deep teal hover
    btn_encrypt_text="#ffffff",
    btn_decrypt_bg="#0284c7",     # Calm arctic cerulean secondary action
    btn_decrypt_hover="#0369a1",  # Deep cerulean hover
    btn_decrypt_text="#ffffff",
    btn_rsa_bg="#0891b2",         # Subtle cyan-slate highlight
    btn_rsa_hover="#0e7490",      # Deep cyan hover
    btn_rsa_text="#ffffff",
    btn_utility_bg="#21262d",     # Subtle steel utility
    btn_utility_hover="#30363d",  # Steel hover
    btn_utility_text="#f0f6fc",
    btn_neutral_bg="#21262d",     # Steel neutral
    btn_neutral_hover="#30363d",  # Neutral hover
    btn_neutral_text="#8b949e",
    sidebar_btn_active_bg="#0d9488",    # Teal active highlight
    sidebar_btn_active_text="#ffffff",
    sidebar_btn_inactive_text="#c9d1d9", # Ice slate text
    sidebar_btn_hover="#21262d",
    input_bg="#0d1117",           # Obsidian input surface
    input_text="#f0f6fc",
    input_border="#30363d",
    tab_bg="#1c2128",
    tab_btn_selected="#0d9488",   # Teal tab selector
    tab_btn_hover="#115e59",
    tab_text="#f0f6fc",
    badge_bg="#134e4a",           # Dark cyan-teal badge
    badge_text="#5eead4",         # Crisp light teal text
)

# 5. Royal Champagne (Warm Luxury Light)
ROYAL_CHAMPAGNE_THEME = ThemePalette(
    id="Royal Champagne",
    name="Royal Champagne",
    appearance_mode="Light",
    window_bg="#fbf8f3",          # Warm ivory / alabaster background
    sidebar_bg="#f4eee3",         # Soft warm champagne sidebar
    card_bg="#ffffff",            # Crisp alabaster card surface
    card_border="#dfd5c4",        # Refined sand/champagne hairline border
    scroll_bg="#ede3d2",          # Warm sand scroll canvas
    text_primary="#1e1b18",       # Deep espresso ink for ultra-crisp readability
    text_secondary="#685d53",     # Warm walnut / bronze secondary text
    text_muted="#8c7e72",         # Soft warm bronze muted
    btn_encrypt_bg="#0f5132",     # Rich imperial emerald primary action
    btn_encrypt_hover="#0a3622",  # Deep emerald hover
    btn_encrypt_text="#ffffff",
    btn_decrypt_bg="#9c6615",     # Rich warm bronze secondary action
    btn_decrypt_hover="#7a4f0e",  # Deep bronze hover
    btn_decrypt_text="#ffffff",
    btn_rsa_bg="#1a365d",         # Deep regal navy accent
    btn_rsa_hover="#10243e",      # Midnight navy hover
    btn_rsa_text="#ffffff",
    btn_utility_bg="#ede4d4",     # Soft champagne utility
    btn_utility_hover="#dfd5c3",  # Champagne hover
    btn_utility_text="#1e1b18",
    btn_neutral_bg="#ede4d4",     # Soft champagne neutral
    btn_neutral_hover="#dfd5c3",  # Neutral hover
    btn_neutral_text="#4a4036",
    sidebar_btn_active_bg="#0f5132",    # Rich imperial emerald active marker
    sidebar_btn_active_text="#ffffff",
    sidebar_btn_inactive_text="#3d352e", # Deep walnut inactive text
    sidebar_btn_hover="#e5dac8",
    input_bg="#ffffff",           # Pure ivory white input surface
    input_text="#1a1613",         # Deep espresso ink
    input_border="#cfc3af",       # Fine champagne border
    tab_bg="#ffffff",
    tab_btn_selected="#0f5132",   # Emerald selected tab
    tab_btn_hover="#0a3622",
    tab_text="#1e1b18",
    badge_bg="#e8decb",           # Warm champagne badge
    badge_text="#0f5132",         # Rich emerald text on champagne badge
)

# Registry of available themes
THEME_MAP: Dict[str, ThemePalette] = {
    DARK_THEME.id: DARK_THEME,
    LIGHT_THEME.id: LIGHT_THEME,
    RED_ORANGE_BLUE_THEME.id: RED_ORANGE_BLUE_THEME,
    NORDIC_OBSIDIAN_THEME.id: NORDIC_OBSIDIAN_THEME,
    ROYAL_CHAMPAGNE_THEME.id: ROYAL_CHAMPAGNE_THEME,
}

THEME_NAMES: List[str] = list(THEME_MAP.keys())


def get_theme(theme_name: str) -> ThemePalette:
    """Returns the requested ThemePalette or defaults to DARK_THEME."""
    return THEME_MAP.get(theme_name, DARK_THEME)
