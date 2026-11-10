"""VELOCITY INDONESIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY INDONESIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "INDONESIAN"
HANDLE = "@velocityindonesian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "id",
    "name": "Indonesian",
    "native_name": "Bahasa Indonesia",
    "history_key": "indonesian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "id-ID-ArdiNeural",
    "native_fallback_voice": "id-ID-GadisNeural",
    "native_engine": "edge",
    "native_lang_code": "id",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "BAHASA INDONESIA",
    "translit_label": "SAY IT LIKE",
    "greeting": "Halo!",
    "encouragement": "Luar biasa!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Salam", "hand", "#1CB0F6"),
    ("Basic Phrases", "Frasa Dasar", "chat", "#58CC02"),
    ("Common Expressions", "Ekspresi Umum", "chat", "#1CB0F6"),
    ("Travel", "Perjalanan", "plane", "#1CB0F6"),
    ("Restaurant", "Restoran", "fork", "#FF7A00"),
    ("Shopping", "Belanja", "bag", "#E056A0"),
    ("Emergency", "Darurat", "siren", "#FF4B4B"),
    ("Family Terms", "Istilah Keluarga", "heart", "#E056A0"),
    ("Numbers", "Angka", "hash", "#A560E8"),
    ("Time", "Waktu", "clock", "#00A889"),
    ("Motivation", "Motivasi", "rocket", "#A560E8"),
    ("Love", "Cinta", "heart", "#FF4B4B"),
    ("Success", "Sukses", "trophy", "#F5A700"),
    ("Wisdom", "Kebijaksanaan", "book", "#A560E8"),
    ("Happiness", "Kebahagiaan", "smile", "#F5A700"),
    ("Self Improvement", "Perbaikan Diri", "leaf", "#58CC02"),
    ("Gratitude", "Rasa Syukur", "heart", "#FF7A00"),
    ("Friendship", "Persahabatan", "users", "#00A889"),
    ("Hope", "Harapan", "sun", "#FF7A00"),
    ("Creativity", "Kreativitas", "palette", "#E056A0"),
    ("Inner Peace", "Kedamaian Batin", "lotus", "#00A889"),
    ("Confidence", "Percaya Diri", "shield", "#1CB0F6"),
    ("Perseverance", "Ketekunan", "mountain", "#FF7A00"),
    ("Inspiration", "Inspirasi", "sparkles", "#A560E8"),
    ("Positive Life", "Hidup Positif", "sun", "#58CC02"),
    ("Courage", "Keberanian", "shield", "#FF4B4B"),
    ("Kindness", "Kebaikan", "heart", "#E056A0"),
    ("Patience", "Kesabaran", "hourglass", "#00A889"),
    ("Forgiveness", "Pengampunan", "hands", "#FF7A00"),
    ("Strength", "Kekuatan", "dumbbell", "#FF4B4B"),
    ("Joy", "Sukacita", "smile", "#F5A700"),
    ("Balance", "Keseimbangan", "scale", "#00A889"),
    ("Growth", "Pertumbuhan", "sprout", "#58CC02"),
    ("Purpose", "Tujuan", "target", "#A560E8"),
    ("Mindfulness", "Perhatian Penuh", "lotus", "#00A889"),
    ("Daily Routine", "Rutinitas Harian", "calendar", "#1CB0F6"),
    ("Weather", "Cuaca", "cloud", "#1CB0F6"),
    ("Feelings", "Perasaan", "smile", "#E056A0"),
    ("Food", "Makanan", "fork", "#FF7A00"),
    ("Health", "Kesehatan", "heart", "#58CC02"),
    ("Work", "Pekerjaan", "briefcase", "#1CB0F6"),
    ("Technology", "Teknologi", "chip", "#A560E8"),
    ("Nature", "Alam", "leaf", "#58CC02"),
    ("Animals", "Binatang", "paw", "#FF7A00"),
    ("Colors", "Warna", "palette", "#E056A0"),
    ("Directions", "Arah", "compass", "#1CB0F6"),
    ("Body Parts", "Bagian Tubuh", "hand", "#00A889"),
    ("Clothes", "Pakaian", "shirt", "#E056A0"),
    ("Music", "Musik", "music", "#A560E8"),
    ("Sports", "Olahraga", "ball", "#FF7A00"),
    ("Holidays", "Hari Libur", "gift", "#FF4B4B"),
    ("Education", "Pendidikan", "book", "#1CB0F6"),
    ("Culture", "Budaya", "globe", "#00A889"),
    ("Finance", "Keuangan", "coin", "#58CC02"),
    ("Relationships", "Hubungan", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnindonesian",
    "#indonesianlessons",
    "#indonesianforbeginners",
    "#languagelearning",
    "#indonesianvocabulary",
    "#velocityindonesian",
    "#dailyindonesian",
    "#indonesian",
    "#learnlanguages",
    "#speakindonesian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
