from src.domain.alphabet import EmojiAlphabet
from src.domain.cipher import EmojiCipher

DEFAULT_MAPPING = {
    'A': '🍎', 'B': '🍌', 'C': '🐱', 'D': '🐶', 'E': '🐘',
    'F': '🐸', 'G': '🦒', 'H': '🐹', 'I': '🍦', 'J': '🐆',
    'K': '🥝', 'L': '🦁', 'M': '🐒', 'N': '🥜', 'O': '🐙',
    'P': '🐧', 'Q': '👑', 'R': '🐰', 'S': '🐍', 'T': '🐢',
    'U': '🦄', 'V': '🌋', 'W': '🐳', 'X': '❌', 'Y': '🧘',
    'Z': '🦓',
    '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
    '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣'
}

alphabet = EmojiAlphabet(DEFAULT_MAPPING)
cipher = EmojiCipher(alphabet)

def encrypt_text(text: str) -> str:
    return cipher.encrypt(text)

def decrypt_emojis(emojis: str) -> str:
    return cipher.decrypt(emojis)
