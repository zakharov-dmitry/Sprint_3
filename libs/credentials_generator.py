import random
import string


def generate_random_name():
    first_name = ''.join(random.choices((string.ascii_letters + "_"), k=10))
    second_name = ''.join(random.choices((string.ascii_letters + "_"), k=10))
    return first_name + ' ' + second_name


def generate_random_password(length=6):
    possible_chars = string.ascii_letters + string.digits + "!#$%&"
    return ''.join(random.choices(possible_chars, k=length))


def generate_random_mail():
    username = ''.join(random.choices((string.ascii_lowercase + "_"), k=10))
    domain = ''.join(random.choices((string.ascii_lowercase + "-"), k=10))
    ext = ''.join(random.choices((string.ascii_lowercase + "-"), k=3))
    return username + "@" + domain + '.' + ext


class Credential:
    def __init__(self):
        self.name = generate_random_name()
        self.password = generate_random_password()
        self.mail = generate_random_mail()
        self.short_password = generate_random_password(length=5)




