# src/domain/alphabet.py

class EmojiAlphabet:
    """
    Define um mapeamento reversível entre caracteres válidos e emojis.
    """

    def __init__(self, mapping: dict[str, str]):
        self._char_to_emoji = {}
        self._emoji_to_char = {}

        for char, emoji in mapping.items():
            char = char.upper()

            if char in self._char_to_emoji:
                raise ValueError(f"Duplicated character: {char}")

            if emoji in self._emoji_to_char:
                raise ValueError(f"Duplicated emoji: {emoji}")

            self._char_to_emoji[char] = emoji
            self._emoji_to_char[emoji] = char

    def has_char(self, char: str) -> bool:
        return char.upper() in self._char_to_emoji

    def has_emoji(self, emoji: str) -> bool:
        return emoji in self._emoji_to_char

    def char_to_emoji(self, char: str) -> str | None:
        return self._char_to_emoji.get(char.upper())

    def emoji_to_char(self, emoji: str) -> str | None:
        return self._emoji_to_char.get(emoji)
