# =========================
# generator.py
# =========================

import string
import secrets


def generate_password(length=12):

    if length < 8:
        length = 8
    if length > 20:
        length = 20

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password
