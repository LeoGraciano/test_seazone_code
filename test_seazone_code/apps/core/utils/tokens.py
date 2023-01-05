import random
import string
from datetime import datetime


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


def random_code_user(size=4):

    dt = datetime.now().strftime('%y%m%d')

    digits = random_digits(4)

    protocol = dt+digits

    return protocol
