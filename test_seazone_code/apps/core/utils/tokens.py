import hashlib
import random
import string


# simples gerador de key
def random_digits(size=8):
    chars = string.digits
    return ''.join(random.choice(chars) for x in range(size))


def random_letters(size=8):
    chars = string.digits
    return ''.join(random.choice(chars) for x in range(size))


def random_key(size=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for x in range(size))
