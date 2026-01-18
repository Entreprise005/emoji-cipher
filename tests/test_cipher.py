from src.domain.alphabet import EmojiAlphabet
from src.domain.cipher import EmojiCipher


def make_cipher():
    mapping = {
        "A": "😀",
        "B": "😎",
        "1": "🔢",
    }
    space_emoji = "⬜"
    alphabet = EmojiAlphabet(mapping=mapping, space_emoji=space_emoji)
    return EmojiCipher(alphabet=alphabet)


def test_encrypt_basic_text():
    cipher = make_cipher()
    result = cipher.encrypt("AB1")
    assert result == "😀😎🔢"


def test_encrypt_is_deterministic():
    cipher = make_cipher()
    assert cipher.encrypt("AB") == cipher.encrypt("AB")


def test_encrypt_ignores_punctuation():
    cipher = make_cipher()
    result = cipher.encrypt("A!B?")
    assert result == "😀😎"


def test_encrypt_converts_space_to_emoji():
    cipher = make_cipher()
    result = cipher.encrypt("A B")
    assert result == "😀⬜😎"


def test_encrypt_ignores_unknown_characters():
    cipher = make_cipher()
    result = cipher.encrypt("AZB")
    assert result == "😀😎"


def test_decrypt_basic_emojis():
    cipher = make_cipher()
    result = cipher.decrypt("😀😎🔢")
    assert result == "AB1"


def test_decrypt_ignores_invalid_emojis():
    cipher = make_cipher()
    result = cipher.decrypt("😀❌😎")
    assert result == "AB"


def test_round_trip_encrypt_then_decrypt():
    cipher = make_cipher()
    original = "A B1"
    encrypted = cipher.encrypt(original)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == original
