import pytest
from src.domain.alphabet import EmojiAlphabet

@pytest.fixture
def basic_alphabet():
    mapping = {
        "A": "😀",
        "B": "😎",
        "1": "🔢",
    }
    return EmojiAlphabet(mapping=mapping)


def test_alphabet_maps_char_to_emoji(basic_alphabet):
    assert basic_alphabet.char_to_emoji("A") == "😀"
    assert basic_alphabet.char_to_emoji("a") == "😀"  # case-insensitive
    assert basic_alphabet.char_to_emoji("1") == "🔢"


def test_alphabet_maps_emoji_to_char(basic_alphabet):
    assert basic_alphabet.emoji_to_char("😀") == "A"





def test_unknown_char_returns_none(basic_alphabet):
    assert basic_alphabet.char_to_emoji("Z") is None


def test_unknown_emoji_returns_none(basic_alphabet):
    assert basic_alphabet.emoji_to_char("❌") is None


def test_duplicate_character_is_not_allowed():
    mapping = {
        "A": "😀",
        "a": "😎",
    }
    with pytest.raises(ValueError):
        EmojiAlphabet(mapping=mapping)


def test_duplicate_emoji_is_not_allowed():
    mapping = {
        "A": "😀",
        "B": "😀",
    }
    with pytest.raises(ValueError):
        EmojiAlphabet(mapping=mapping)
