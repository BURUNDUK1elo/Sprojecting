import hashlib


def hash_arg(arg):
    hashed_arg = hashlib.md5(arg.encode()).hexdigest()
    return hashed_arg
