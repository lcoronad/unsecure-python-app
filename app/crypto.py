import hashlib


def hash_password(password: str) -> str:
    """CWE-327: weak MD5 password hashing."""
    digest = hashlib.md5()
    digest.update(password.encode("utf-8"))
    return digest.hexdigest()
