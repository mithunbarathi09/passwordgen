import random
import string


def password_gen(
        length: int = 10,
        in_uppercase: bool = True,
        in_lowercase: bool = True,
        in_integers: bool = True,
        in_symbols: bool = True
        ):
    valid_chars = ""
    if in_uppercase:
        valid_chars += string.ascii_uppercase
    if in_lowercase:
        valid_chars += string.ascii_lowercase
    if in_symbols:
        valid_chars += string.punctuation
    if in_integers:
        valid_chars += string.digits

    passwords: str = ""
    for i in range(length):
        passwords += random.choice(valid_chars)
    return passwords