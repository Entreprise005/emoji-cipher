# src/domain/cipher.py

from .alphabet import EmojiAlphabet

class EmojiCipher:
    """
    Aplica as regras de criptografia e descriptografia
    usando um EmojiAlphabet.
    """

    def __init__(self, alphabet: EmojiAlphabet):
        self._alphabet = alphabet

    def encrypt(self, text: str) -> str:
        result = []

        for char in text:
            emoji = self._alphabet.char_to_emoji(char)
            if emoji:
                result.append(emoji)
            # pontuação e caracteres desconhecidos são ignorados

        return "".join(result)

    def decrypt(self, emojis: str) -> str:
        result = []

        for emoji in emojis:
            char = self._alphabet.emoji_to_char(emoji)
            if char:
                result.append(char)
            # emojis inválidos são ignorados

        return "".join(result)
