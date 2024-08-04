import random
import string


def generate_random_string(length):
    """Генерирует случайную строку из латинских символов и цифр заданной длины."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def generate_username():
    random_part = generate_random_string(5)
    return f"Test-{random_part}"


def generate_email():
    random_part = generate_random_string(10)
    return f"test{random_part}@mail.coma"


def generate_password():
    return generate_random_string(7)
